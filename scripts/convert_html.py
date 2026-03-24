"""Convert HTML/HTM files to markdown using html2text.

Handles Dee folder HTML files with companion _files/ directories.
Idempotent: skips if .md exists and source file is older.
"""

import json
import sys
import datetime
from pathlib import Path

import html2text
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')


CORPUS_ROOT = Path(__file__).resolve().parent.parent
MANIFEST_PATH = CORPUS_ROOT / "data" / "conversion_manifest.json"


def convert_html_file(source_path: Path, md_path: Path) -> dict:
    """Convert a single HTML file to markdown."""
    md_path.parent.mkdir(parents=True, exist_ok=True)

    entry = {
        "source_path": str(source_path),
        "md_path": str(md_path),
        "format": "HTML",
        "pages": 1,
        "chars": 0,
        "quality_score": 0.0,
        "quality_flag": "EMPTY",
        "timestamp": datetime.datetime.now().isoformat(),
    }

    try:
        # Try UTF-8 first, fall back to latin-1
        try:
            content = source_path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            content = source_path.read_text(encoding="latin-1")
    except Exception as e:
        entry["error"] = str(e)
        md_path.write_text(f"<!-- CONVERSION ERROR: {e} -->\n", encoding="utf-8")
        return entry

    h = html2text.HTML2Text()
    h.body_width = 0
    h.unicode_snob = True
    h.images_to_alt = True  # Replace images with alt text
    h.ignore_links = False

    md_text = h.handle(content)
    total_chars = len(md_text.strip())

    entry["chars"] = total_chars
    entry["quality_score"] = 1.0 if total_chars > 100 else 0.0
    entry["quality_flag"] = "GOOD" if total_chars > 100 else "EMPTY"

    title = source_path.stem
    md_path.write_text(f"# {title}\n\n{md_text}", encoding="utf-8")
    return entry


def main():
    if len(sys.argv) > 1:
        folder = CORPUS_ROOT / sys.argv[1]
        folders = [folder]
    else:
        folders = [CORPUS_ROOT]
        folders += sorted([d for d in CORPUS_ROOT.iterdir()
                          if d.is_dir() and d.name not in
                          {"md", "db", "scripts", "docs", "site", "data",
                           "staging", "templates", "agile", ".claude", ".git",
                           "__pycache__"}])

    all_entries = []
    for folder in folders:
        htmls = sorted(list(folder.glob("*.html")) + list(folder.glob("*.htm")))
        if not htmls:
            continue
        label = folder.name if folder != CORPUS_ROOT else "(root)"
        print(f"\n[{label}]")
        for html_path in htmls:
            rel = html_path.relative_to(CORPUS_ROOT)
            md_path = CORPUS_ROOT / "md" / rel.with_suffix(".md")

            if md_path.exists() and md_path.stat().st_mtime > html_path.stat().st_mtime:
                print(f"  SKIP (cached): {html_path.name}")
                continue

            print(f"  Converting: {html_path.name}")
            entry = convert_html_file(html_path, md_path)
            all_entries.append(entry)
            print(f"    -> {entry['chars']} chars, {entry['quality_flag']}")

    # Merge manifest
    MANIFEST_PATH.parent.mkdir(parents=True, exist_ok=True)
    existing = []
    if MANIFEST_PATH.exists():
        existing = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    existing_map = {e["source_path"]: e for e in existing}
    for entry in all_entries:
        existing_map[entry["source_path"]] = entry
    merged = sorted(existing_map.values(), key=lambda e: e["source_path"])
    MANIFEST_PATH.write_text(json.dumps(merged, indent=2, ensure_ascii=False), encoding="utf-8")

    print(f"\n=== HTML CONVERSION SUMMARY ===")
    print(f"Converted: {len(all_entries)} HTML files")


if __name__ == "__main__":
    main()
