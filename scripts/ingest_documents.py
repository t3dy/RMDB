"""Ingest document metadata into the documents table.

Sources:
1. Filename parsing (author, title, year, journal, DOI) via regex
2. PDF internal metadata via PyMuPDF
3. Conversion manifest (pages, chars, quality_flag)
4. Folder name -> figure mapping

Idempotent: uses INSERT OR IGNORE + UPDATE for existing rows.
"""

import json
import re
import sqlite3
import sys
import html
from pathlib import Path

import fitz  # PyMuPDF

CORPUS_ROOT = Path(__file__).resolve().parent.parent
DB_PATH = CORPUS_ROOT / "db" / "renmagic.db"
MANIFEST_PATH = CORPUS_ROOT / "data" / "conversion_manifest.json"

# Folders that are NOT corpus content
SKIP_DIRS = {"md", "db", "scripts", "docs", "site", "data", "staging",
             "templates", "agile", ".claude", ".git", "__pycache__"}

# Skip these file types
SKIP_EXTENSIONS = {".gif", ".jpg", ".jpeg", ".png", ".css", ".js", ".json",
                   ".crdownload", ".db", ".sqlite"}

# Folder -> primary figure mapping
FOLDER_FIGURE_MAP = {
    "Agrippa": "Agrippa",
    "Bruno Lull": "Bruno",  # Primary figure; Llull secondary
    "Christian Cabalah": None,  # tradition, not a figure
    "Copenhaver": "Copenhaver",
    "Dee": "Dee",
    "FM Van Helmont": "Van Helmont",
    "Ficino": "Ficino",
    "Fludd": "Fludd",
    "Kircher": "Kircher",
    "Pico": "Pico",
    "Reuchlin": "Reuchlin",
    "Vittoria Perrone Compagni": "Perrone Compagni",
    "Zika": "Zika",
    "bohme": "Bohme",
    "trithemius": "Trithemius",
}


def decode_filename(name: str) -> str:
    """Clean HTML entities and encoding artifacts from filenames."""
    name = name.replace("&_039_", "'")
    name = name.replace("&amp_", "&")
    name = name.replace("&quot_", '"')
    name = name.replace("_", " ")
    name = html.unescape(name)
    return name.strip()


def parse_year(text: str) -> int | None:
    """Extract a plausible publication year."""
    matches = re.findall(r'\b(1[4-9]\d{2}|20[0-2]\d)\b', text)
    if matches:
        # Prefer years in publishing range (1900-2026)
        publishing = [int(y) for y in matches if 1800 <= int(y) <= 2026]
        if publishing:
            return max(publishing)  # most recent = likely pub date
        return int(matches[0])
    return None


def parse_author(filename: str) -> str | None:
    """Extract author from filename heuristics."""
    name = decode_filename(filename)

    # Pattern: "Author Name - Title"
    m = re.match(r'^([A-Z][a-zA-Z\s\.]+?)\s*[-_]\s', name)
    if m:
        author = m.group(1).strip()
        if len(author.split()) <= 5:
            return author

    # Pattern: "Firstname Lastname Title..."
    # Look for 2-4 capitalized words before a longer title-like phrase
    m = re.match(r'^((?:[A-Z][a-z]+\s+){1,3}[A-Z][a-z]+)\s+[A-Z]', name)
    if m:
        author = m.group(1).strip()
        if len(author.split()) <= 4:
            return author

    return None


def detect_format(path: Path) -> str:
    ext = path.suffix.lower()
    fmt_map = {".pdf": "PDF", ".epub": "EPUB", ".html": "HTML",
               ".htm": "HTML", ".chm": "OTHER"}
    return fmt_map.get(ext, "OTHER")


def get_pdf_metadata(path: Path) -> dict:
    """Extract metadata from PDF internals."""
    meta = {}
    try:
        doc = fitz.open(str(path))
        pdf_meta = doc.metadata
        if pdf_meta.get("title"):
            meta["title"] = pdf_meta["title"]
        if pdf_meta.get("author"):
            meta["author"] = pdf_meta["author"]
        meta["pages"] = len(doc)
        doc.close()
    except Exception:
        pass
    return meta


def ingest_folder(conn: sqlite3.Connection, folder: Path, folder_figure: str | None):
    """Ingest all documents from a folder."""
    files = []
    for f in sorted(folder.iterdir()):
        if f.is_dir():
            continue
        if f.suffix.lower() in SKIP_EXTENSIONS:
            continue
        if f.suffix.lower() in (".pdf", ".epub", ".html", ".htm", ".chm"):
            files.append(f)

    for filepath in files:
        rel_path = str(filepath.relative_to(CORPUS_ROOT))
        fmt = detect_format(filepath)
        clean_name = decode_filename(filepath.stem)
        year = parse_year(filepath.name)
        author = parse_author(filepath.stem)

        # PDF internal metadata
        pdf_meta = {}
        if fmt == "PDF":
            pdf_meta = get_pdf_metadata(filepath)

        title = pdf_meta.get("title") or clean_name
        if not author and pdf_meta.get("author"):
            author = pdf_meta["author"]
        pages = pdf_meta.get("pages", 0)

        # Check manifest for quality data
        md_rel = str((Path("md") / filepath.relative_to(CORPUS_ROOT)).with_suffix(".md"))
        md_path = str(CORPUS_ROOT / md_rel)

        conn.execute("""
        INSERT OR IGNORE INTO documents
            (path, md_path, title, title_from_filename, author_from_filename,
             year, format, folder_figure, pages, source_method, confidence)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, 'DETERMINISTIC', 'HIGH')
        """, (rel_path, md_path, title, clean_name, author,
              year, fmt, folder_figure, pages))

        # Update fields that may have been NULL on first insert
        conn.execute("""
        UPDATE documents SET
            title = COALESCE(title, ?),
            author_from_filename = COALESCE(author_from_filename, ?),
            year = COALESCE(year, ?),
            pages = COALESCE(pages, ?),
            updated_at = datetime('now')
        WHERE path = ?
        """, (title, author, year, pages, rel_path))

    return len(files)


def apply_manifest(conn: sqlite3.Connection):
    """Update documents with conversion manifest data."""
    if not MANIFEST_PATH.exists():
        print("No conversion manifest found, skipping quality data.")
        return

    manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    for entry in manifest:
        source_path = entry["source_path"]
        # Normalize path separators
        rel = str(Path(source_path).relative_to(CORPUS_ROOT)).replace("\\", "/")
        # Try both forward and back slash versions
        conn.execute("""
        UPDATE documents SET
            chars = ?,
            quality_flag = ?,
            updated_at = datetime('now')
        WHERE path = ? OR path = ?
        """, (entry.get("chars", 0), entry.get("quality_flag", "UNKNOWN"),
              rel, rel.replace("/", "\\")))


def main():
    if not DB_PATH.exists():
        print("ERROR: Database not found. Run init_db.py first.")
        sys.exit(1)

    conn = sqlite3.connect(str(DB_PATH))
    conn.execute("PRAGMA foreign_keys=ON")
    total = 0

    # Determine scope
    if len(sys.argv) > 1:
        folder_name = sys.argv[1]
        folder = CORPUS_ROOT / folder_name
        figure = FOLDER_FIGURE_MAP.get(folder_name)
        print(f"[{folder_name}] (figure: {figure})")
        count = ingest_folder(conn, folder, figure)
        total += count
    else:
        # Root level files
        print("[(root)]")
        count = ingest_folder(conn, CORPUS_ROOT, None)
        total += count

        # All subject folders
        for d in sorted(CORPUS_ROOT.iterdir()):
            if d.is_dir() and d.name not in SKIP_DIRS:
                figure = FOLDER_FIGURE_MAP.get(d.name)
                print(f"[{d.name}] (figure: {figure})")
                count = ingest_folder(conn, d, figure)
                total += count

    # Apply manifest data
    apply_manifest(conn)

    conn.commit()

    # Summary
    row_count = conn.execute("SELECT COUNT(*) FROM documents").fetchone()[0]
    with_year = conn.execute("SELECT COUNT(*) FROM documents WHERE year IS NOT NULL").fetchone()[0]
    with_author = conn.execute("SELECT COUNT(*) FROM documents WHERE author_from_filename IS NOT NULL").fetchone()[0]
    conn.close()

    print(f"\n=== INGESTION SUMMARY ===")
    print(f"Files processed: {total}")
    print(f"Documents in DB: {row_count}")
    print(f"With year: {with_year}")
    print(f"With author: {with_author}")


if __name__ == "__main__":
    main()
