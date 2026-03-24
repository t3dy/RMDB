"""Convert PDF files to markdown using PyMuPDF.

Extracts text with heading detection based on font size heuristics.
Produces one .md file per PDF in the md/ output directory.
Idempotent: skips if .md exists and source file is older.
"""

import json
import sys
import os
import datetime
from pathlib import Path

import fitz  # PyMuPDF

# Fix Windows console encoding
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')


CORPUS_ROOT = Path(__file__).resolve().parent.parent
MD_ROOT = CORPUS_ROOT / "md"
MANIFEST_PATH = CORPUS_ROOT / "data" / "conversion_manifest.json"

# Quality thresholds
QUALITY_GOOD = 0.8
QUALITY_PARTIAL = 0.3


def get_quality_flag(score: float, total_chars: int) -> str:
    if total_chars == 0:
        return "EMPTY"
    if score < QUALITY_PARTIAL:
        return "SCANNED"
    if score < QUALITY_GOOD:
        return "PARTIAL"
    return "GOOD"


def extract_page_text_with_headings(page: fitz.Page) -> str:
    """Extract text from a page, detecting headings via font size."""
    blocks = page.get_text("dict", flags=fitz.TEXT_PRESERVE_WHITESPACE)["blocks"]

    body_sizes = []
    for block in blocks:
        if block.get("type") != 0:  # text blocks only
            continue
        for line in block.get("lines", []):
            for span in line.get("spans", []):
                if span["text"].strip():
                    body_sizes.append(span["size"])

    if not body_sizes:
        return page.get_text("text")

    mean_size = sum(body_sizes) / len(body_sizes)
    h1_threshold = mean_size * 1.5
    h2_threshold = mean_size * 1.2

    lines_out = []
    for block in blocks:
        if block.get("type") != 0:
            continue
        for line in block.get("lines", []):
            line_text = ""
            max_size = 0
            for span in line.get("spans", []):
                text = span["text"]
                if text.strip():
                    max_size = max(max_size, span["size"])
                line_text += text

            line_text = line_text.strip()
            if not line_text:
                continue

            if max_size >= h1_threshold and len(line_text) < 200:
                lines_out.append(f"\n# {line_text}\n")
            elif max_size >= h2_threshold and len(line_text) < 200:
                lines_out.append(f"\n## {line_text}\n")
            else:
                lines_out.append(line_text)

    return "\n".join(lines_out)


def convert_pdf(source_path: Path, md_path: Path) -> dict:
    """Convert a single PDF to markdown. Returns manifest entry."""
    md_path.parent.mkdir(parents=True, exist_ok=True)

    entry = {
        "source_path": str(source_path),
        "md_path": str(md_path),
        "format": "PDF",
        "pages": 0,
        "chars": 0,
        "quality_score": 0.0,
        "quality_flag": "EMPTY",
        "timestamp": datetime.datetime.now().isoformat(),
    }

    try:
        doc = fitz.open(str(source_path))
    except Exception as e:
        entry["quality_flag"] = "EMPTY"
        entry["error"] = str(e)
        md_path.write_text(f"<!-- CONVERSION ERROR: {e} -->\n", encoding="utf-8")
        return entry

    entry["pages"] = len(doc)
    pages_text = []
    non_empty_pages = 0

    for page in doc:
        try:
            text = extract_page_text_with_headings(page)
        except Exception:
            text = page.get_text("text")

        if text.strip():
            non_empty_pages += 1
        pages_text.append(text)

    doc.close()

    full_text = "\n\n---\n\n".join(pages_text)
    total_chars = len(full_text.strip())

    entry["chars"] = total_chars
    entry["quality_score"] = round(non_empty_pages / max(entry["pages"], 1), 3)
    entry["quality_flag"] = get_quality_flag(entry["quality_score"], total_chars)

    # Write markdown
    title = source_path.stem
    header = f"# {title}\n\n"
    if entry["quality_flag"] == "SCANNED":
        header += "<!-- SCANNED: OCR needed -->\n\n"
    elif entry["quality_flag"] == "EMPTY":
        header += "<!-- EMPTY: No text extracted -->\n\n"

    md_path.write_text(header + full_text, encoding="utf-8")
    return entry


def convert_folder(folder: Path, target_folder: str = None) -> list:
    """Convert all PDFs in a folder. Returns list of manifest entries."""
    entries = []
    pdfs = sorted(folder.glob("*.pdf"))

    if not pdfs:
        return entries

    for pdf_path in pdfs:
        # Determine output path
        rel = pdf_path.relative_to(CORPUS_ROOT)
        md_rel = Path("md") / rel.with_suffix(".md")
        md_path = CORPUS_ROOT / md_rel

        # Idempotent: skip if md exists and is newer
        if md_path.exists() and md_path.stat().st_mtime > pdf_path.stat().st_mtime:
            print(f"  SKIP (cached): {pdf_path.name}")
            # Still register in manifest if not already there
            entries.append({
                "source_path": str(pdf_path),
                "md_path": str(md_path),
                "format": "PDF",
                "pages": 0,
                "chars": len(md_path.read_text(encoding="utf-8", errors="replace")),
                "quality_score": 1.0,
                "quality_flag": "GOOD",
                "timestamp": datetime.datetime.fromtimestamp(md_path.stat().st_mtime).isoformat(),
                "cached": True,
            })
            continue

        print(f"  Converting: {pdf_path.name}")
        entry = convert_pdf(pdf_path, md_path)
        entries.append(entry)
        flag = entry["quality_flag"]
        print(f"    -> {entry['pages']} pages, {entry['chars']} chars, {flag}")

    return entries


def main():
    """Convert PDFs in specified folder or all folders."""
    if len(sys.argv) > 1:
        folder_name = sys.argv[1]
        folder = CORPUS_ROOT / folder_name
        if not folder.is_dir():
            print(f"ERROR: {folder} is not a directory")
            sys.exit(1)
        folders = [folder]
    else:
        # All folders + root
        folders = [CORPUS_ROOT]
        folders += sorted([d for d in CORPUS_ROOT.iterdir()
                          if d.is_dir() and d.name not in
                          {"md", "db", "scripts", "docs", "site", "data",
                           "staging", "templates", "agile", ".claude", ".git",
                           "__pycache__"}])

    all_entries = []
    for folder in folders:
        label = folder.name if folder != CORPUS_ROOT else "(root)"
        print(f"\n[{label}]")
        entries = convert_folder(folder)
        all_entries.extend(entries)

    # Merge with existing manifest
    MANIFEST_PATH.parent.mkdir(parents=True, exist_ok=True)
    existing = []
    if MANIFEST_PATH.exists():
        existing = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))

    # Update existing entries by source_path
    existing_map = {e["source_path"]: e for e in existing}
    for entry in all_entries:
        existing_map[entry["source_path"]] = entry

    merged = sorted(existing_map.values(), key=lambda e: e["source_path"])
    MANIFEST_PATH.write_text(json.dumps(merged, indent=2, ensure_ascii=False), encoding="utf-8")

    # Summary
    flags = {}
    for e in all_entries:
        flags[e["quality_flag"]] = flags.get(e["quality_flag"], 0) + 1
    print(f"\n=== CONVERSION SUMMARY ===")
    print(f"Converted: {len(all_entries)} PDFs")
    for flag, count in sorted(flags.items()):
        print(f"  {flag}: {count}")


if __name__ == "__main__":
    main()
