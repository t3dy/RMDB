"""Enhanced heuristic classification (v2) for remaining 99 ambiguous documents.

Additional signals beyond v1:
1. File size (<1MB = article, >10MB = monograph)
2. First-line patterns in .md files (journal headers, chapter markers)
3. PDF page count refinements (mid-range disambiguation)
4. Known publisher patterns
"""

import io
import re
import sqlite3
import sys
from pathlib import Path

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')

CORPUS_ROOT = Path(__file__).resolve().parent.parent
DB_PATH = CORPUS_ROOT / "db" / "renmagic.db"

# First-line patterns that indicate document type
CHAPTER_PATTERNS = [
    re.compile(r'^#*\s*Chapter\s+\d', re.IGNORECASE),
    re.compile(r'^#*\s*Part\s+[IVX\d]', re.IGNORECASE),
    re.compile(r'^\d+\.\s+[A-Z]'),  # "1. Introduction" style
]

JOURNAL_FIRST_LINE = [
    re.compile(r'(?:published|accepted|received)\s+\d', re.IGNORECASE),
    re.compile(r'doi[:\s]', re.IGNORECASE),
    re.compile(r'volume\s+\d+', re.IGNORECASE),
    re.compile(r'pp\.\s*\d+', re.IGNORECASE),
]

EDITED_PATTERNS = [
    re.compile(r'\bedited\s+by\b', re.IGNORECASE),
    re.compile(r'\beds?\.\b.*\beds?\.\b', re.IGNORECASE),  # multiple "ed." markers
]


def classify_v2(path: str, pages: int, chars: int, md_path: str) -> str | None:
    """Enhanced classification using file size + first-line analysis."""
    source = CORPUS_ROOT / path
    name_lower = path.lower()

    # File size heuristic
    file_size = 0
    if source.exists():
        file_size = source.stat().st_size

    # Read first 2000 chars of md for pattern detection
    first_text = ""
    md_file = CORPUS_ROOT / "md" / Path(path).with_suffix(".md")
    if md_file.exists():
        try:
            first_text = md_file.read_text(encoding="utf-8", errors="replace")[:2000]
        except Exception:
            pass

    # File size signals
    if file_size > 0:
        if file_size < 500_000 and pages and pages < 30:  # <500KB and <30 pages
            return "ARTICLE"
        if file_size > 15_000_000:  # >15MB
            return "MONOGRAPH"

    # First-line chapter detection → CHAPTER
    for pat in CHAPTER_PATTERNS:
        if pat.search(first_text[:500]):
            return "CHAPTER"

    # First-line journal detection → ARTICLE
    journal_score = 0
    for pat in JOURNAL_FIRST_LINE:
        if pat.search(first_text[:1000]):
            journal_score += 1
    if journal_score >= 2:
        return "ARTICLE"

    # Edited volume detection
    for pat in EDITED_PATTERNS:
        if pat.search(name_lower):
            return "ANTHOLOGY"

    # Refined page count heuristics for mid-range
    if pages:
        if 30 <= pages <= 60 and journal_score >= 1:
            return "ARTICLE"
        if 60 < pages <= 150:
            # Could be either — check for dissertation markers
            if "diss" in name_lower or "thesis" in name_lower:
                return "DISSERTATION"
            # Default to CHAPTER if part of an edited volume name pattern
            if any(kw in name_lower for kw in ["studies in", "essays in", "companion to"]):
                return "CHAPTER"
            return "MONOGRAPH"  # Lean monograph for 60-150 page works
        if pages > 150:
            return "MONOGRAPH"

    # File size fallback
    if file_size > 5_000_000:  # >5MB
        return "MONOGRAPH"
    if file_size < 2_000_000 and file_size > 0:  # <2MB
        return "ARTICLE"

    return None


def main():
    conn = sqlite3.connect(str(DB_PATH))

    rows = conn.execute("""
        SELECT id, path, pages, chars FROM documents WHERE doc_type IS NULL
    """).fetchall()

    classified = 0
    type_counts = {}
    for doc_id, path, pages, chars in rows:
        md_path = str(CORPUS_ROOT / "md" / Path(path).with_suffix(".md"))
        doc_type = classify_v2(path, pages, chars, md_path)
        if doc_type:
            conn.execute("UPDATE documents SET doc_type=?, updated_at=datetime('now') WHERE id=?",
                        (doc_type, doc_id))
            classified += 1
            type_counts[doc_type] = type_counts.get(doc_type, 0) + 1

    conn.commit()

    remaining = conn.execute("SELECT COUNT(*) FROM documents WHERE doc_type IS NULL").fetchone()[0]
    total_classified = conn.execute("SELECT COUNT(*) FROM documents WHERE doc_type IS NOT NULL").fetchone()[0]

    print(f"=== ENHANCED CLASSIFICATION v2 ===")
    print(f"Previously unclassified: {len(rows)}")
    print(f"Newly classified: {classified}")
    for dtype, count in sorted(type_counts.items()):
        print(f"  {dtype}: {count}")
    print(f"Still unclassified: {remaining}")
    print(f"Total classified: {total_classified}/337 ({total_classified/337*100:.0f}%)")

    conn.close()


if __name__ == "__main__":
    main()
