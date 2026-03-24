"""Convert EPUB files to markdown using ebooklib + BeautifulSoup.

Preserves internal heading hierarchy from XHTML chapter structure.
Idempotent: skips if .md exists and source file is older.
"""

import json
import sys
import datetime
from pathlib import Path

import ebooklib
from ebooklib import epub
from bs4 import BeautifulSoup
import html2text
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')


CORPUS_ROOT = Path(__file__).resolve().parent.parent
MD_ROOT = CORPUS_ROOT / "md"
MANIFEST_PATH = CORPUS_ROOT / "data" / "conversion_manifest.json"


def convert_epub(source_path: Path, md_path: Path) -> dict:
    """Convert a single EPUB to markdown."""
    md_path.parent.mkdir(parents=True, exist_ok=True)

    entry = {
        "source_path": str(source_path),
        "md_path": str(md_path),
        "format": "EPUB",
        "pages": 0,
        "chars": 0,
        "quality_score": 0.0,
        "quality_flag": "EMPTY",
        "timestamp": datetime.datetime.now().isoformat(),
    }

    try:
        book = epub.read_epub(str(source_path), options={"ignore_ncx": True})
    except Exception as e:
        entry["error"] = str(e)
        md_path.write_text(f"<!-- CONVERSION ERROR: {e} -->\n", encoding="utf-8")
        return entry

    h = html2text.HTML2Text()
    h.body_width = 0  # no wrapping
    h.unicode_snob = True

    chapters = []
    items = list(book.get_items_of_type(ebooklib.ITEM_DOCUMENT))
    entry["pages"] = len(items)
    non_empty = 0

    for item in items:
        content = item.get_content().decode("utf-8", errors="replace")
        soup = BeautifulSoup(content, "html.parser")

        # Remove scripts, styles
        for tag in soup(["script", "style"]):
            tag.decompose()

        md_text = h.handle(str(soup))
        if md_text.strip():
            non_empty += 1
            chapters.append(md_text.strip())

    full_text = "\n\n---\n\n".join(chapters)
    total_chars = len(full_text)

    entry["chars"] = total_chars
    entry["quality_score"] = round(non_empty / max(entry["pages"], 1), 3)

    if total_chars == 0:
        entry["quality_flag"] = "EMPTY"
    elif entry["quality_score"] < 0.3:
        entry["quality_flag"] = "PARTIAL"
    else:
        entry["quality_flag"] = "GOOD"

    title = source_path.stem
    md_path.write_text(f"# {title}\n\n{full_text}", encoding="utf-8")
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
        epubs = sorted(folder.glob("*.epub"))
        if not epubs:
            continue
        label = folder.name if folder != CORPUS_ROOT else "(root)"
        print(f"\n[{label}]")
        for epub_path in epubs:
            rel = epub_path.relative_to(CORPUS_ROOT)
            md_path = CORPUS_ROOT / "md" / rel.with_suffix(".md")

            if md_path.exists() and md_path.stat().st_mtime > epub_path.stat().st_mtime:
                print(f"  SKIP (cached): {epub_path.name}")
                continue

            print(f"  Converting: {epub_path.name}")
            entry = convert_epub(epub_path, md_path)
            all_entries.append(entry)
            print(f"    -> {entry['pages']} chapters, {entry['chars']} chars, {entry['quality_flag']}")

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

    print(f"\n=== EPUB CONVERSION SUMMARY ===")
    print(f"Converted: {len(all_entries)} EPUBs")


if __name__ == "__main__":
    main()
