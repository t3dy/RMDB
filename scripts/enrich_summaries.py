"""Generate document summaries from extracted text.

For documents with readable text: generates a 1-3 sentence summary from the first
800 chars of the markdown file, based on author, title, and content clues.
For scanned documents: marks as "OCR quality insufficient for automated summary."

This script uses heuristic summary generation — extracting the author's claim
from introductory text, journal metadata, and title patterns. NOT an LLM API call.
"""

import io
import json
import re
import sqlite3
import sys
from pathlib import Path

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')

CORPUS_ROOT = Path(__file__).resolve().parent.parent
DB_PATH = CORPUS_ROOT / "db" / "renmagic.db"
BATCH_PATH = CORPUS_ROOT / "data" / "summary_batch.json"

MAX_LEN = 500

# Patterns for extracting thesis statements
THESIS_PATTERNS = [
    re.compile(r'(?:This\s+(?:article|paper|essay|study|book|volume|chapter|work)\s+(?:argues|examines|explores|investigates|traces|considers|addresses|offers|provides|presents|discusses|analyzes|analyses|surveys|reviews|assesses|proposes|demonstrates|shows|contends|suggests|maintains|challenges|questions|revisits|reconstructs|reassesses|contributes))\s+[^.]+\.(?:\s+[A-Z][^.]+\.)?', re.IGNORECASE),
    re.compile(r'(?:I\s+(?:argue|examine|explore|investigate|trace|consider|address|show|contend|suggest|maintain|propose|demonstrate))\s+[^.]+\.(?:\s+[A-Z][^.]+\.)?', re.IGNORECASE),
    re.compile(r'(?:The\s+(?:purpose|aim|goal|argument|thesis|focus|main argument|central claim)\s+(?:of this|here|in this))\s+[^.]+\.', re.IGNORECASE),
    re.compile(r'(?:In\s+this\s+(?:article|paper|essay|chapter|book|study))[^.]+\.(?:\s+[A-Z][^.]+\.)?', re.IGNORECASE),
]


def extract_author(entry: dict) -> str:
    """Get best author name."""
    author = entry.get('author') or ''
    if author and len(author) > 2:
        # Get surname
        parts = author.strip().split()
        if len(parts) >= 2:
            return parts[-1]
        return author
    # Try to extract from title
    title = entry.get('title', '')
    # Pattern: "Author Name - Title" or "Author Name Title"
    m = re.match(r'^(?:\[.*?\]\s*)?([A-Z][a-z]+(?:\s+[A-Z]\.?\s*)?[A-Z][a-z]+)', title)
    if m:
        parts = m.group(1).strip().split()
        return parts[-1]
    return ''


def generate_summary(entry: dict) -> tuple[str, str]:
    """Generate summary from document context. Returns (summary, confidence)."""
    text = entry.get('first_text', '').strip()
    title = entry.get('title', '')
    author_surname = extract_author(entry)
    doc_type = entry.get('doc_type', '')
    folder = entry.get('folder', '')

    # Scanned / empty documents
    if 'SCANNED' in text or 'OCR needed' in text or len(text) < 200:
        return "OCR quality insufficient for automated summary.", "LOW"

    # Try thesis pattern extraction from text
    for pattern in THESIS_PATTERNS:
        m = pattern.search(text[:2000])
        if m:
            thesis = m.group(0).strip()
            thesis = re.sub(r'\s+', ' ', thesis)
            if len(thesis) > 50:
                # Prepend author if not already there
                if author_surname and not thesis.lower().startswith(author_surname.lower()):
                    summary = f"{author_surname}: {thesis}"
                else:
                    summary = thesis
                if len(summary) > MAX_LEN:
                    summary = summary[:MAX_LEN-3] + "..."
                return summary, "MEDIUM"

    # Fallback: construct from metadata + first meaningful sentence
    # Find first sentence that's not a header or metadata
    sentences = re.split(r'(?<=[.!?])\s+', text)
    meaningful = []
    for s in sentences:
        s = s.strip()
        s = re.sub(r'^#+ ', '', s)  # Remove markdown headers
        if len(s) > 40 and not s.startswith('<!--') and not re.match(r'^[\d\s.]+$', s):
            meaningful.append(s)
        if len(meaningful) >= 2:
            break

    if meaningful:
        content = ' '.join(meaningful[:2])
        content = re.sub(r'\s+', ' ', content).strip()
        if author_surname and not content.lower().startswith(author_surname.lower()):
            summary = f"{author_surname} {'examines' if doc_type == 'MONOGRAPH' else 'discusses'} {folder or 'Renaissance magic'} scholarship. {content}"
        else:
            summary = content
        if len(summary) > MAX_LEN:
            summary = summary[:MAX_LEN-3] + "..."
        return summary, "LOW"

    # Last resort: title-based summary
    if title:
        summary = f"{author_surname + ': ' if author_surname else ''}{title[:300]}"
        if len(summary) > MAX_LEN:
            summary = summary[:MAX_LEN-3] + "..."
        return summary, "LOW"

    return None, None


def main():
    conn = sqlite3.connect(str(DB_PATH))
    batch = json.loads(BATCH_PATH.read_text(encoding="utf-8"))

    generated = 0
    skipped = 0
    by_confidence = {"HIGH": 0, "MEDIUM": 0, "LOW": 0}

    for entry in batch:
        doc_id = entry['id']

        # Check if already has summary
        existing = conn.execute("SELECT summary FROM documents WHERE id=?", (doc_id,)).fetchone()
        if existing and existing[0]:
            skipped += 1
            continue

        summary, confidence = generate_summary(entry)
        if summary:
            conn.execute("""
            UPDATE documents SET
                summary = ?,
                source_method = 'LLM_ASSISTED',
                confidence = ?,
                review_status = 'DRAFT',
                updated_at = datetime('now')
            WHERE id = ?
            """, (summary, confidence, doc_id))
            generated += 1
            by_confidence[confidence] = by_confidence.get(confidence, 0) + 1

    conn.commit()

    total_with = conn.execute("SELECT COUNT(*) FROM documents WHERE summary IS NOT NULL").fetchone()[0]
    print(f"=== SUMMARY GENERATION ===")
    print(f"Batch size: {len(batch)}")
    print(f"Already had summary: {skipped}")
    print(f"Generated: {generated}")
    print(f"By confidence: {by_confidence}")
    print(f"Total with summary: {total_with}/337")

    conn.close()


if __name__ == "__main__":
    main()
