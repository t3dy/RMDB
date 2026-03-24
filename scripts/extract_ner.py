"""NER extraction using spaCy on markdown files.

Extracts PERSON, GPE (geopolitical entities), DATE, and ORG entities.
Stores results in data/ner_report.json.
Seeds figures table with most-frequent PERSON entities.
"""

import json
import sqlite3
import sys
from pathlib import Path
from collections import defaultdict, Counter

import spacy

CORPUS_ROOT = Path(__file__).resolve().parent.parent
DB_PATH = CORPUS_ROOT / "db" / "renmagic.db"
MD_ROOT = CORPUS_ROOT / "md"
NER_PATH = CORPUS_ROOT / "data" / "ner_report.json"

# How much text to process per document (first N chars)
TEXT_LIMIT = 5000

# NER entity types we care about
ENTITY_TYPES = {"PERSON", "GPE", "DATE", "ORG", "WORK_OF_ART"}

# Known false positives to filter
STOP_ENTITIES = {
    "renaissance", "medieval", "christian", "jewish", "islamic",
    "european", "western", "ancient", "modern", "latin", "greek",
    "hebrew", "arabic", "english", "german", "italian", "french",
    # Publisher/metadata noise discovered in Lampton analysis
    "vol", "iss", "ed", "eds", "trans", "rev", "ibid", "op", "cit",
    "koninklijke brill nv", "brill", "routledge", "cambridge",
    "oxford", "yale", "princeton", "chicago", "harvard",
    "university press", "press", "library", "journal",
    "milton park", "abingdon", "new york", "london",
    "i. title", "p. cm", "isbn", "doi",
    "monas hieroglyphica", "de occulta philosophia",  # titles, not people
    "steganographia", "picatrix", "enneads", "timaeus",
}


def clean_entity(text: str) -> str:
    """Normalize entity text."""
    text = text.strip().strip("'\".,;:()")
    return text


def main():
    print("Loading spaCy model...")
    nlp = spacy.load("en_core_web_sm")

    conn = sqlite3.connect(str(DB_PATH))

    # Get documents
    docs = conn.execute("""
        SELECT id, md_path, path, folder_figure FROM documents WHERE md_path IS NOT NULL
    """).fetchall()

    if len(sys.argv) > 1:
        folder = sys.argv[1]
        docs = [d for d in docs if folder in (d[2] or "")]

    print(f"Processing {len(docs)} documents")

    all_persons = Counter()  # global person frequency
    ner_report = {}

    for doc_id, md_path, path, folder_figure in docs:
        if not md_path or not Path(md_path).exists():
            continue

        try:
            text = Path(md_path).read_text(encoding="utf-8")[:TEXT_LIMIT]
        except Exception:
            continue

        doc_nlp = nlp(text)

        entities = defaultdict(list)
        for ent in doc_nlp.ents:
            if ent.label_ not in ENTITY_TYPES:
                continue
            cleaned = clean_entity(ent.text)
            if len(cleaned) < 2 or cleaned.lower() in STOP_ENTITIES:
                continue
            entities[ent.label_].append(cleaned)

        # Count persons globally
        for person in entities.get("PERSON", []):
            all_persons[person] += 1

        # Store per-document report (top 20 entities per type)
        doc_report = {}
        for etype, elist in entities.items():
            counted = Counter(elist).most_common(20)
            doc_report[etype] = [{"entity": e, "count": c} for e, c in counted]

        if doc_report:
            ner_report[str(doc_id)] = {
                "path": path,
                "entities": doc_report,
            }

    # Write NER report
    NER_PATH.parent.mkdir(parents=True, exist_ok=True)
    NER_PATH.write_text(json.dumps(ner_report, indent=2, ensure_ascii=False), encoding="utf-8")

    # Seed figures from top persons (frequency >= 3)
    seeded = 0
    for person, count in all_persons.most_common(50):
        if count < 2:
            break
        # Skip very short or generic names
        if len(person.split()) < 2:
            continue
        conn.execute("""
        INSERT OR IGNORE INTO figures (name, figure_type, source_method, confidence)
        VALUES (?, 'HISTORICAL', 'DETERMINISTIC', 'MEDIUM')
        """, (person,))
        if conn.execute("SELECT changes()").fetchone()[0] > 0:
            seeded += 1

    conn.commit()

    # Summary
    total_persons = len(all_persons)
    total_docs_with_ner = len(ner_report)

    print(f"\n=== NER EXTRACTION ===")
    print(f"Documents processed: {len(docs)}")
    print(f"Documents with entities: {total_docs_with_ner}")
    print(f"Unique persons found: {total_persons}")
    print(f"Figures seeded: {seeded}")
    print(f"\nTop 15 persons:")
    for person, count in all_persons.most_common(15):
        print(f"  {person}: {count}")

    conn.close()


if __name__ == "__main__":
    main()
