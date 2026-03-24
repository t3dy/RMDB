"""Build FTS5 full-text search index from markdown files.

Populates the documents_fts virtual table with title, summary, and full_text
from the converted markdown files.
"""

import io
import sqlite3
import sys
from pathlib import Path

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')

CORPUS_ROOT = Path(__file__).resolve().parent.parent
DB_PATH = CORPUS_ROOT / "db" / "renmagic.db"


def main():
    conn = sqlite3.connect(str(DB_PATH))

    # Clear existing FTS data
    conn.execute("DELETE FROM documents_fts")

    rows = conn.execute("SELECT id, title, summary, path FROM documents").fetchall()
    indexed = 0

    for doc_id, title, summary, path in rows:
        # Read full text from md file
        md_path = CORPUS_ROOT / "md" / Path(path).with_suffix(".md")
        full_text = ""
        if md_path.exists():
            try:
                full_text = md_path.read_text(encoding="utf-8", errors="replace")
            except Exception:
                pass

        if not full_text and not title and not summary:
            continue

        conn.execute("""
        INSERT INTO documents_fts (rowid, title, summary, full_text)
        VALUES (?, ?, ?, ?)
        """, (doc_id, title or "", summary or "", full_text))
        indexed += 1

    conn.commit()

    # Test query
    test_results = conn.execute("""
    SELECT COUNT(*) FROM documents_fts WHERE documents_fts MATCH 'prima materia'
    """).fetchone()[0]

    print(f"=== FTS5 INDEX ===")
    print(f"Documents indexed: {indexed}")
    print(f"Test query 'prima materia': {test_results} hits")

    conn.close()


if __name__ == "__main__":
    main()
