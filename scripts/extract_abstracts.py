"""Extract abstracts from markdown files using regex patterns.

Looks for common academic abstract markers:
- "Abstract" / "ABSTRACT" / "Summary" headers
- First substantial paragraph if no explicit abstract found

Updates documents.summary for matches.
"""

import re
import sqlite3
import sys
from pathlib import Path

CORPUS_ROOT = Path(__file__).resolve().parent.parent
DB_PATH = CORPUS_ROOT / "db" / "renmagic.db"
MD_ROOT = CORPUS_ROOT / "md"

# Patterns for abstract detection
ABSTRACT_PATTERNS = [
    # Explicit "Abstract" header followed by text
    re.compile(r'(?:^|\n)\s*#*\s*(?:Abstract|ABSTRACT|Summary|SUMMARY)\s*\n+(.*?)(?:\n\s*#|\n\s*(?:Keywords|KEYWORDS|Introduction|INTRODUCTION|1\.))', re.DOTALL | re.IGNORECASE),
    # "Abstract." or "Abstract:" inline
    re.compile(r'(?:Abstract|ABSTRACT|Summary)[.:]\s*(.*?)(?:\n\s*\n|\n\s*(?:Keywords|Introduction|1\.))', re.DOTALL | re.IGNORECASE),
    # "Abstract" as a standalone word followed by a paragraph
    re.compile(r'\bAbstract\b\s*\n+(.*?)(?:\n\s*\n\s*\n)', re.DOTALL | re.IGNORECASE),
]

MAX_SUMMARY_LEN = 500


def clean_abstract(text: str) -> str:
    """Clean extracted abstract text."""
    text = re.sub(r'\s+', ' ', text).strip()
    # Remove markdown formatting
    text = re.sub(r'[#*_`]', '', text)
    # Truncate to max length at sentence boundary
    if len(text) > MAX_SUMMARY_LEN:
        truncated = text[:MAX_SUMMARY_LEN]
        last_period = truncated.rfind('.')
        if last_period > MAX_SUMMARY_LEN // 2:
            text = truncated[:last_period + 1]
        else:
            text = truncated.rstrip() + "..."
    return text


def extract_abstract(md_path: str) -> str | None:
    """Try to extract an abstract from a markdown file."""
    path = Path(md_path)
    if not path.exists():
        return None

    # Read first 10000 chars (abstracts are near the top)
    try:
        text = path.read_text(encoding="utf-8")[:10000]
    except Exception:
        return None

    for pattern in ABSTRACT_PATTERNS:
        m = pattern.search(text)
        if m:
            abstract = clean_abstract(m.group(1))
            if len(abstract) > 50:  # Must be substantial
                return abstract

    return None


def main():
    conn = sqlite3.connect(str(DB_PATH))

    # Get documents without summaries
    if len(sys.argv) > 1:
        folder = sys.argv[1]
        rows = conn.execute(
            "SELECT id, md_path, path FROM documents WHERE folder_figure = ? AND summary IS NULL",
            (FOLDER_FIGURE_MAP.get(folder, folder),)
        ).fetchall()
    else:
        rows = conn.execute(
            "SELECT id, md_path, path FROM documents WHERE summary IS NULL"
        ).fetchall()

    extracted = 0
    for doc_id, md_path, path in rows:
        if not md_path:
            continue
        abstract = extract_abstract(md_path)
        if abstract:
            conn.execute("""
            UPDATE documents SET
                summary = ?,
                source_method = 'DETERMINISTIC',
                updated_at = datetime('now')
            WHERE id = ?
            """, (abstract, doc_id))
            extracted += 1
            print(f"  EXTRACTED: {Path(path).name[:60]}... ({len(abstract)} chars)")

    conn.commit()
    total = len(rows)
    print(f"\n=== ABSTRACT EXTRACTION ===")
    print(f"Documents checked: {total}")
    print(f"Abstracts extracted: {extracted}")
    print(f"Hit rate: {extracted/max(total,1)*100:.0f}%")
    conn.close()


# Reuse the folder map from ingest
FOLDER_FIGURE_MAP = {
    "Agrippa": "Agrippa", "Bruno Lull": "Bruno", "Copenhaver": "Copenhaver",
    "Dee": "Dee", "FM Van Helmont": "Van Helmont", "Ficino": "Ficino",
    "Fludd": "Fludd", "Kircher": "Kircher", "Pico": "Pico",
    "Reuchlin": "Reuchlin", "Vittoria Perrone Compagni": "Perrone Compagni",
    "Zika": "Zika", "bohme": "Bohme", "trithemius": "Trithemius",
}

if __name__ == "__main__":
    main()
