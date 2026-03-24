"""Curate generic terms — flag overly common Latin words for deprioritization.

Terms with frequency >5000 AND domain=PHILOSOPHICAL are flagged as LOW priority.
These are standard Latin philosophical vocabulary, not Renaissance-magic-specific.
"""

import io
import sqlite3
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

from pathlib import Path
CORPUS_ROOT = Path(__file__).resolve().parent.parent
DB_PATH = CORPUS_ROOT / "db" / "renmagic.db"

GENERIC_THRESHOLD = 5000


def main():
    conn = sqlite3.connect(str(DB_PATH))

    # Find generic terms
    generics = conn.execute("""
        SELECT id, term, frequency, domain FROM dictionary_terms
        WHERE frequency > ? AND domain = 'PHILOSOPHICAL'
        ORDER BY frequency DESC
    """, (GENERIC_THRESHOLD,)).fetchall()

    # Flag them with a note in definition_brief
    flagged = 0
    for term_id, term, freq, domain in generics:
        conn.execute("""
        UPDATE dictionary_terms SET
            confidence = 'LOW',
            definition_brief = '[GENERIC: standard Latin, define in magic-specific context only]',
            updated_at = datetime('now')
        WHERE id = ?
        """, (term_id,))
        flagged += 1
        print(f"  FLAGGED: {term} (freq={freq:,})")

    conn.commit()

    remaining = conn.execute("""
        SELECT COUNT(*) FROM dictionary_terms WHERE confidence != 'LOW' OR confidence IS NULL
    """).fetchone()[0]
    total = conn.execute("SELECT COUNT(*) FROM dictionary_terms").fetchone()[0]

    print(f"\n=== TERM CURATION ===")
    print(f"Generic terms flagged: {flagged}")
    print(f"Priority terms remaining: {remaining}/{total}")

    conn.close()


if __name__ == "__main__":
    main()
