"""Classify document types using heuristics (no LLM).

Rules:
- "Review by_" or "review of" in filename -> REVIEW
- Journal name patterns (vol/iss) -> ARTICLE
- Page count > 200 -> MONOGRAPH
- Page count < 40 with journal pattern -> ARTICLE
- Known primary source authors -> PRIMARY_SOURCE
- "dissertation" in filename -> DISSERTATION
- "edited by" or "anthology" -> ANTHOLOGY

Updates documents.doc_type for matches. Leaves NULL for ambiguous cases (LLM in v2).
"""

import re
import sqlite3
import sys
from pathlib import Path

CORPUS_ROOT = Path(__file__).resolve().parent.parent
DB_PATH = CORPUS_ROOT / "db" / "renmagic.db"

# Journal indicators
JOURNAL_PATTERNS = [
    re.compile(r'\bvol\s+\d+\s+iss\s+\d+\b', re.IGNORECASE),
    re.compile(r'\b(?:Renaissance Quarterly|Sixteenth Century Journal|Ambix|Isis|Speculum|Aries)\b', re.IGNORECASE),
    re.compile(r'\bJournal\s+of\s+(?:the\s+)?(?:History|Warburg|Philosophy|Religion)\b', re.IGNORECASE),
    re.compile(r'\b10\.\d{4,}/', re.IGNORECASE),  # DOI
    re.compile(r'\blibgen\s*li\b', re.IGNORECASE),
]

# Primary source indicators
PRIMARY_AUTHORS = {
    "agrippa", "ficino", "dee", "pico", "bruno", "fludd",
    "trithemius", "reuchlin", "kircher", "bohme", "boehme",
    "paracelsus", "lull", "llull",
}

REVIEW_PATTERNS = [
    re.compile(r'\bReview\s+by[_\s]', re.IGNORECASE),
    re.compile(r'\bReview\s+of\b', re.IGNORECASE),
    re.compile(r'\bBook\s+Review\b', re.IGNORECASE),
]


def classify(path: str, title: str, author: str, pages: int, folder: str) -> str | None:
    """Classify a document by heuristic rules. Returns doc_type or None."""
    name = (path or "").lower()
    title_lower = (title or "").lower()
    author_lower = (author or "").lower()

    # Review detection
    for pat in REVIEW_PATTERNS:
        if pat.search(name) or pat.search(title_lower):
            return "REVIEW"

    # Dissertation
    if "dissertation" in name or "dissertation" in title_lower:
        return "DISSERTATION"

    # Anthology
    if "anthology" in name or "edited by" in name:
        return "ANTHOLOGY"

    # Journal article (strong signal)
    journal_score = 0
    for pat in JOURNAL_PATTERNS:
        if pat.search(name):
            journal_score += 1

    if journal_score >= 2:
        return "ARTICLE"

    # Primary source: if the file IS by a historical magician
    for primary in PRIMARY_AUTHORS:
        if primary in name[:50] and pages and pages < 500:
            # Check if it's the actual text vs scholarship about them
            if any(kw in name for kw in ["three books", "de occulta", "monas", "mysteriorum",
                                          "heptaplus", "oration", "de arte", "steganographia",
                                          "de vanitate", "on the christian religion"]):
                return "PRIMARY_SOURCE"

    # Page-count heuristics
    if pages:
        if pages > 250 and journal_score == 0:
            return "MONOGRAPH"
        if pages < 40 and journal_score >= 1:
            return "ARTICLE"

    # Single journal indicator + short = probably article
    if journal_score >= 1 and pages and pages < 60:
        return "ARTICLE"

    # Longer works without journal indicators = likely monograph
    if pages and pages > 150 and journal_score == 0:
        return "MONOGRAPH"

    return None  # Ambiguous — leave for LLM in v2


def main():
    conn = sqlite3.connect(str(DB_PATH))

    rows = conn.execute("""
        SELECT id, path, title, author_from_filename, pages, folder_figure
        FROM documents WHERE doc_type IS NULL
    """).fetchall()

    classified = 0
    type_counts = {}
    for doc_id, path, title, author, pages, folder in rows:
        doc_type = classify(path, title, author, pages, folder)
        if doc_type:
            conn.execute("""
            UPDATE documents SET
                doc_type = ?,
                updated_at = datetime('now')
            WHERE id = ?
            """, (doc_type, doc_id))
            classified += 1
            type_counts[doc_type] = type_counts.get(doc_type, 0) + 1

    conn.commit()
    print(f"\n=== HEURISTIC CLASSIFICATION ===")
    print(f"Documents checked: {len(rows)}")
    print(f"Classified: {classified}")
    print(f"Ambiguous (left NULL): {len(rows) - classified}")
    for dtype, count in sorted(type_counts.items()):
        print(f"  {dtype}: {count}")
    conn.close()


if __name__ == "__main__":
    main()
