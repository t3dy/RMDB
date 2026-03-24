"""Extract Latin/Greek/Hebrew terms from corpus via regex + seed list.

Searches markdown files for known Renaissance magic terminology.
Produces:
- dictionary_terms rows (term + language + frequency)
- term_documents join rows
- data/kwic_concordance.json (term-in-context extracts)
- data/term_frequency.json

Uses a curated seed list from data/latin_seed_list.json.
"""

import json
import re
import sqlite3
import sys
from pathlib import Path
from collections import defaultdict

CORPUS_ROOT = Path(__file__).resolve().parent.parent
DB_PATH = CORPUS_ROOT / "db" / "renmagic.db"
MD_ROOT = CORPUS_ROOT / "md"
SEED_PATH = CORPUS_ROOT / "data" / "latin_seed_list.json"
KWIC_PATH = CORPUS_ROOT / "data" / "kwic_concordance.json"
FREQ_PATH = CORPUS_ROOT / "data" / "term_frequency.json"

KWIC_WINDOW = 100  # chars before and after match


def load_seed_list() -> list[dict]:
    """Load the curated seed term list."""
    if not SEED_PATH.exists():
        print(f"ERROR: Seed list not found at {SEED_PATH}")
        print("Create it first with the term list.")
        sys.exit(1)
    return json.loads(SEED_PATH.read_text(encoding="utf-8"))


def find_term_in_text(text: str, term: str) -> list[dict]:
    """Find all occurrences of a term with KWIC context."""
    results = []
    pattern = re.compile(re.escape(term), re.IGNORECASE)
    for m in pattern.finditer(text):
        start = max(0, m.start() - KWIC_WINDOW)
        end = min(len(text), m.end() + KWIC_WINDOW)
        context = text[start:end].replace("\n", " ").strip()
        results.append({
            "position": m.start(),
            "context": f"...{context}...",
        })
    return results


def main():
    conn = sqlite3.connect(str(DB_PATH))
    conn.execute("PRAGMA foreign_keys=ON")

    seed_terms = load_seed_list()
    print(f"Loaded {len(seed_terms)} seed terms")

    # Get all documents with md files
    docs = conn.execute("""
        SELECT id, md_path, path FROM documents WHERE md_path IS NOT NULL
    """).fetchall()

    # Scope to folder if specified
    if len(sys.argv) > 1:
        folder = sys.argv[1]
        docs = [d for d in docs if folder in (d[2] or "")]

    print(f"Scanning {len(docs)} documents")

    # Track frequencies and KWIC
    global_freq = defaultdict(int)  # term -> total count
    doc_freq = defaultdict(lambda: defaultdict(int))  # term -> {doc_id: count}
    kwic_data = defaultdict(list)  # term -> [kwic entries]

    for doc_id, md_path, path in docs:
        if not md_path or not Path(md_path).exists():
            continue

        try:
            text = Path(md_path).read_text(encoding="utf-8")
        except Exception:
            continue

        for seed in seed_terms:
            term = seed["term"]
            matches = find_term_in_text(text, term)
            if matches:
                count = len(matches)
                global_freq[term] += count
                doc_freq[term][doc_id] = count
                # Keep first 3 KWIC contexts per document
                for m in matches[:3]:
                    kwic_data[term].append({
                        "document": Path(path).name,
                        "doc_id": doc_id,
                        **m,
                    })

    # Insert/update dictionary_terms
    inserted = 0
    for seed in seed_terms:
        term = seed["term"]
        if global_freq[term] == 0:
            continue  # Not found in corpus

        conn.execute("""
        INSERT OR IGNORE INTO dictionary_terms
            (term, term_language, canonical_form, english_translation, domain, frequency,
             source_method, confidence)
        VALUES (?, ?, ?, ?, ?, ?, 'DETERMINISTIC', 'HIGH')
        """, (term, seed.get("language", "LATIN"), seed.get("canonical", term),
              seed.get("english"), seed.get("domain", "GENERAL"), global_freq[term]))

        # Update frequency if term already existed
        conn.execute("""
        UPDATE dictionary_terms SET frequency = ?, updated_at = datetime('now')
        WHERE term = ? AND term_language = ?
        """, (global_freq[term], term, seed.get("language", "LATIN")))

        inserted += 1

    # Insert term_documents join rows
    join_count = 0
    for term_str, doc_counts in doc_freq.items():
        term_row = conn.execute(
            "SELECT id FROM dictionary_terms WHERE term = ?", (term_str,)
        ).fetchone()
        if not term_row:
            continue
        term_id = term_row[0]
        for doc_id, freq in doc_counts.items():
            conn.execute("""
            INSERT OR IGNORE INTO term_documents (term_id, document_id, frequency)
            VALUES (?, ?, ?)
            """, (term_id, doc_id, freq))
            join_count += 1

    conn.commit()
    conn.close()

    # Write KWIC concordance
    KWIC_PATH.parent.mkdir(parents=True, exist_ok=True)
    # Limit to top 5 contexts per term for manageable file size
    kwic_trimmed = {t: entries[:5] for t, entries in kwic_data.items()}
    KWIC_PATH.write_text(json.dumps(kwic_trimmed, indent=2, ensure_ascii=False), encoding="utf-8")

    # Write frequency data
    freq_sorted = sorted(global_freq.items(), key=lambda x: -x[1])
    FREQ_PATH.write_text(json.dumps(dict(freq_sorted), indent=2, ensure_ascii=False), encoding="utf-8")

    print(f"\n=== TERM EXTRACTION ===")
    print(f"Terms found in corpus: {inserted}")
    print(f"Term-document links: {join_count}")
    print(f"Top 10 terms:")
    for term, count in freq_sorted[:10]:
        print(f"  {term}: {count}")


if __name__ == "__main__":
    main()
