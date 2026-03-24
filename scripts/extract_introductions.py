"""Extract introductory paragraphs from monographs and long documents.

Looks for headings like "Introduction", "Preface", "Chapter 1" and grabs
the first substantial paragraph after them. Updates documents.summary.
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

MAX_SUMMARY_LEN = 500

INTRO_PATTERNS = [
    re.compile(r'(?:^|\n)\s*#*\s*(?:Introduction|INTRODUCTION)\s*\n+(.*?)(?:\n\s*#|\n\s*\n\s*\n)', re.DOTALL | re.IGNORECASE),
    re.compile(r'(?:^|\n)\s*#*\s*(?:Preface|PREFACE)\s*\n+(.*?)(?:\n\s*#|\n\s*\n\s*\n)', re.DOTALL | re.IGNORECASE),
    re.compile(r'(?:^|\n)\s*#*\s*(?:Chapter\s+(?:1|One|I)\b)[^\n]*\n+(.*?)(?:\n\s*#|\n\s*\n\s*\n)', re.DOTALL | re.IGNORECASE),
    re.compile(r'(?:^|\n)\s*#*\s*(?:Foreword|FOREWORD)\s*\n+(.*?)(?:\n\s*#|\n\s*\n\s*\n)', re.DOTALL | re.IGNORECASE),
    # "This book/study/volume argues/examines/explores"
    re.compile(r'((?:This\s+(?:book|study|volume|work|essay|article)\s+(?:argues|examines|explores|investigates|traces|considers|addresses|offers|provides|presents))[^.]+\.(?:\s+[A-Z][^.]+\.){0,2})', re.DOTALL),
]


def clean_intro(text: str) -> str:
    text = re.sub(r'\s+', ' ', text).strip()
    text = re.sub(r'[#*_`]', '', text)
    if len(text) > MAX_SUMMARY_LEN:
        truncated = text[:MAX_SUMMARY_LEN]
        last_period = truncated.rfind('.')
        if last_period > MAX_SUMMARY_LEN // 2:
            text = truncated[:last_period + 1]
        else:
            text = truncated.rstrip() + "..."
    return text


def extract_intro(md_path: Path) -> str | None:
    if not md_path.exists():
        return None
    try:
        text = md_path.read_text(encoding="utf-8", errors="replace")[:30000]
    except Exception:
        return None

    for pattern in INTRO_PATTERNS:
        m = pattern.search(text)
        if m:
            intro = clean_intro(m.group(1) if m.lastindex else m.group(0))
            if len(intro) > 80:
                return intro
    return None


def main():
    conn = sqlite3.connect(str(DB_PATH))

    rows = conn.execute("""
        SELECT id, path FROM documents WHERE summary IS NULL
    """).fetchall()

    extracted = 0
    for doc_id, path in rows:
        md_path = CORPUS_ROOT / "md" / Path(path).with_suffix(".md")
        intro = extract_intro(md_path)
        if intro:
            conn.execute("UPDATE documents SET summary=?, updated_at=datetime('now') WHERE id=?",
                        (intro, doc_id))
            extracted += 1

    conn.commit()
    total_with = conn.execute("SELECT COUNT(*) FROM documents WHERE summary IS NOT NULL").fetchone()[0]
    print(f"=== INTRODUCTION EXTRACTION ===")
    print(f"Documents checked: {len(rows)}")
    print(f"Introductions extracted: {extracted}")
    print(f"Total with summary: {total_with}/337")
    conn.close()


if __name__ == "__main__":
    main()
