"""Detect potential duplicate documents using fuzzy string matching.

Compares normalized titles using rapidfuzz. Flags pairs with similarity > 85%.
Also detects cross-format pairs (.pdf + .epub of same work).
Outputs data/duplicates.json.
"""

import io
import json
import sqlite3
import sys
from pathlib import Path

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')

from rapidfuzz import fuzz

CORPUS_ROOT = Path(__file__).resolve().parent.parent
DB_PATH = CORPUS_ROOT / "db" / "renmagic.db"
DUPES_PATH = CORPUS_ROOT / "data" / "duplicates.json"

THRESHOLD = 85


def normalize_title(title: str) -> str:
    """Normalize title for comparison."""
    if not title:
        return ""
    t = title.lower().strip()
    # Remove common suffixes
    for suffix in ["libgen li", "libgen.li", ".pdf", ".epub"]:
        t = t.replace(suffix, "")
    # Remove punctuation
    t = "".join(c for c in t if c.isalnum() or c.isspace())
    # Collapse whitespace
    t = " ".join(t.split())
    return t


def main():
    conn = sqlite3.connect(str(DB_PATH))
    rows = conn.execute("SELECT id, title, path, format FROM documents").fetchall()

    # Normalize all titles
    docs = []
    for doc_id, title, path, fmt in rows:
        norm = normalize_title(title or Path(path).stem)
        docs.append({"id": doc_id, "title": title, "norm": norm, "path": path, "format": fmt})

    # Find duplicates (O(n^2) but n is small ~350)
    duplicates = []
    seen = set()
    group_id = 1

    for i, a in enumerate(docs):
        for j, b in enumerate(docs):
            if j <= i:
                continue
            if (a["id"], b["id"]) in seen:
                continue

            score = fuzz.ratio(a["norm"], b["norm"])
            if score >= THRESHOLD:
                seen.add((a["id"], b["id"]))
                duplicates.append({
                    "group_id": group_id,
                    "doc_a": {"id": a["id"], "title": a["title"], "path": a["path"], "format": a["format"]},
                    "doc_b": {"id": b["id"], "title": b["title"], "path": b["path"], "format": b["format"]},
                    "similarity": score,
                    "cross_format": a["format"] != b["format"],
                })

                # Update duplicate_group_id in DB
                conn.execute("UPDATE documents SET duplicate_group_id=? WHERE id=?", (group_id, a["id"]))
                conn.execute("UPDATE documents SET duplicate_group_id=? WHERE id=?", (group_id, b["id"]))
                group_id += 1

    conn.commit()
    conn.close()

    DUPES_PATH.parent.mkdir(parents=True, exist_ok=True)
    DUPES_PATH.write_text(json.dumps(duplicates, indent=2, ensure_ascii=False), encoding="utf-8")

    print(f"=== DUPLICATE DETECTION ===")
    print(f"Documents compared: {len(docs)}")
    print(f"Duplicate pairs found: {len(duplicates)}")
    cross = sum(1 for d in duplicates if d["cross_format"])
    print(f"Cross-format pairs: {cross}")
    for d in duplicates[:10]:
        print(f"  [{d['similarity']}%] {Path(d['doc_a']['path']).name[:50]} <-> {Path(d['doc_b']['path']).name[:50]}")


if __name__ == "__main__":
    main()
