"""Detect primary language of each document using langdetect.

Reads first 3000 chars of each .md file and classifies the language.
Updates documents.language.
"""

import io
import sqlite3
import sys
from pathlib import Path

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')

from langdetect import detect, LangDetectException

CORPUS_ROOT = Path(__file__).resolve().parent.parent
DB_PATH = CORPUS_ROOT / "db" / "renmagic.db"


def detect_lang(md_path: str) -> str | None:
    path = Path(md_path)
    if not path.exists():
        return None
    try:
        text = path.read_text(encoding="utf-8", errors="replace")[:3000]
        # Strip markdown formatting
        text = text.replace("#", "").replace("*", "").replace("---", "")
        if len(text.strip()) < 50:
            return None
        return detect(text)
    except LangDetectException:
        return None
    except Exception:
        return None


def main():
    conn = sqlite3.connect(str(DB_PATH))
    rows = conn.execute(
        "SELECT id, md_path FROM documents WHERE language IS NULL AND md_path IS NOT NULL"
    ).fetchall()

    detected = 0
    langs = {}
    for doc_id, md_path in rows:
        lang = detect_lang(md_path)
        if lang:
            conn.execute("UPDATE documents SET language=?, updated_at=datetime('now') WHERE id=?",
                        (lang, doc_id))
            detected += 1
            langs[lang] = langs.get(lang, 0) + 1

    conn.commit()
    print(f"=== LANGUAGE DETECTION ===")
    print(f"Documents checked: {len(rows)}")
    print(f"Detected: {detected}")
    for lang, count in sorted(langs.items(), key=lambda x: -x[1]):
        print(f"  {lang}: {count}")
    conn.close()


if __name__ == "__main__":
    main()
