"""Seed the texts table (primary sources referenced in scholarship).

Sources:
1. Documents with doc_type='PRIMARY_SOURCE' -> they ARE primary texts
2. High-frequency title terms in dictionary_terms (corpus hermeticum, de occulta philosophia, etc.)
3. Known authorship from figures table

All deterministic. No LLM.
"""

import io
import sqlite3
import sys
from pathlib import Path

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

CORPUS_ROOT = Path(__file__).resolve().parent.parent
DB_PATH = CORPUS_ROOT / "db" / "renmagic.db"

# Curated primary sources with metadata (drawn from corpus evidence)
PRIMARY_SOURCES = [
    {"title": "Corpus Hermeticum", "title_latin": "Corpus Hermeticum", "author": "Hermes Trismegistus",
     "era": "ANCIENT", "tradition": "Hermetic", "language": "Greek", "date": "2nd-3rd century CE"},
    {"title": "Asclepius", "title_latin": "Asclepius", "author": "Hermes Trismegistus",
     "era": "ANCIENT", "tradition": "Hermetic", "language": "Latin", "date": "3rd century CE"},
    {"title": "Pimander", "title_latin": "Pimander", "author": "Hermes Trismegistus",
     "era": "ANCIENT", "tradition": "Hermetic", "language": "Greek", "date": "2nd century CE"},
    {"title": "Timaeus", "title_latin": "Timaeus", "author": "Plato",
     "era": "ANCIENT", "tradition": "Neoplatonic", "language": "Greek", "date": "c. 360 BCE"},
    {"title": "Enneads", "title_latin": "Enneades", "author": "Plotinus",
     "era": "ANCIENT", "tradition": "Neoplatonic", "language": "Greek", "date": "c. 270 CE"},
    {"title": "De Mysteriis", "title_latin": "De Mysteriis Aegyptiorum", "author": "Iamblichus",
     "era": "ANCIENT", "tradition": "Neoplatonic", "language": "Greek", "date": "c. 300 CE"},
    {"title": "Elements of Theology", "title_latin": "Elementatio Theologica", "author": "Proclus",
     "era": "ANCIENT", "tradition": "Neoplatonic", "language": "Greek", "date": "c. 460 CE"},
    {"title": "De Radiis Stellarum", "title_latin": "De Radiis Stellarum", "author": "Al-Kindi",
     "era": "MEDIEVAL", "tradition": "Astrological", "language": "Arabic", "date": "9th century"},
    {"title": "Picatrix", "title_latin": "Picatrix (Ghayat al-Hikam)", "author": "Anonymous",
     "era": "MEDIEVAL", "tradition": "Magical", "language": "Arabic", "date": "10th-11th century"},
    {"title": "Sefer Yetzirah", "title_latin": None, "author": "Anonymous",
     "era": "ANCIENT", "tradition": "Kabbalistic", "language": "Hebrew", "date": "3rd-6th century CE"},
    {"title": "Zohar", "title_latin": None, "author": "Moses de Leon (attributed)",
     "era": "MEDIEVAL", "tradition": "Kabbalistic", "language": "Aramaic/Hebrew", "date": "c. 1280"},
    {"title": "Ars Magna", "title_latin": "Ars Magna", "author": "Ramon Llull",
     "era": "MEDIEVAL", "tradition": "Magical", "language": "Latin", "date": "1305"},
    {"title": "Speculum Astronomiae", "title_latin": "Speculum Astronomiae", "author": "Albertus Magnus",
     "era": "MEDIEVAL", "tradition": "Astrological", "language": "Latin", "date": "c. 1260"},
    {"title": "Theologia Platonica", "title_latin": "Theologia Platonica", "author": "Marsilio Ficino",
     "era": "RENAISSANCE", "tradition": "Neoplatonic", "language": "Latin", "date": "1482"},
    {"title": "De Vita (Three Books on Life)", "title_latin": "De Vita Libri Tres", "author": "Marsilio Ficino",
     "era": "RENAISSANCE", "tradition": "Hermetic", "language": "Latin", "date": "1489"},
    {"title": "Oration on the Dignity of Man", "title_latin": "Oratio de Hominis Dignitate", "author": "Giovanni Pico della Mirandola",
     "era": "RENAISSANCE", "tradition": "Kabbalistic", "language": "Latin", "date": "1486"},
    {"title": "900 Conclusions", "title_latin": "Conclusiones Nongentae", "author": "Giovanni Pico della Mirandola",
     "era": "RENAISSANCE", "tradition": "Kabbalistic", "language": "Latin", "date": "1486"},
    {"title": "Heptaplus", "title_latin": "Heptaplus", "author": "Giovanni Pico della Mirandola",
     "era": "RENAISSANCE", "tradition": "Kabbalistic", "language": "Latin", "date": "1489"},
    {"title": "De Verbo Mirifico", "title_latin": "De Verbo Mirifico", "author": "Johannes Reuchlin",
     "era": "RENAISSANCE", "tradition": "Kabbalistic", "language": "Latin", "date": "1494"},
    {"title": "De Arte Cabalistica", "title_latin": "De Arte Cabalistica", "author": "Johannes Reuchlin",
     "era": "RENAISSANCE", "tradition": "Kabbalistic", "language": "Latin", "date": "1517"},
    {"title": "De Occulta Philosophia", "title_latin": "De Occulta Philosophia Libri Tres", "author": "Heinrich Cornelius Agrippa",
     "era": "RENAISSANCE", "tradition": "Magical", "language": "Latin", "date": "1531-1533"},
    {"title": "De Vanitate Scientiarum", "title_latin": "De Incertitudine et Vanitate Scientiarum", "author": "Heinrich Cornelius Agrippa",
     "era": "RENAISSANCE", "tradition": "Magical", "language": "Latin", "date": "1530"},
    {"title": "Steganographia", "title_latin": "Steganographia", "author": "Johannes Trithemius",
     "era": "RENAISSANCE", "tradition": "Magical", "language": "Latin", "date": "c. 1499 (pub. 1606)"},
    {"title": "Polygraphia", "title_latin": "Polygraphia", "author": "Johannes Trithemius",
     "era": "RENAISSANCE", "tradition": "Magical", "language": "Latin", "date": "1518"},
    {"title": "Monas Hieroglyphica", "title_latin": "Monas Hieroglyphica", "author": "John Dee",
     "era": "RENAISSANCE", "tradition": "Hermetic", "language": "Latin", "date": "1564"},
    {"title": "Five Books of Mystery", "title_latin": "Mysteriorum Libri Quinque", "author": "John Dee",
     "era": "RENAISSANCE", "tradition": "Enochian", "language": "Latin/English", "date": "1581-1583"},
    {"title": "A True and Faithful Relation", "title_latin": None, "author": "John Dee (ed. Meric Casaubon)",
     "era": "RENAISSANCE", "tradition": "Enochian", "language": "English/Latin", "date": "1659 (composed 1581-1589)"},
    {"title": "De la Causa, Principio et Uno", "title_latin": "De la Causa, Principio et Uno", "author": "Giordano Bruno",
     "era": "RENAISSANCE", "tradition": "Hermetic", "language": "Italian", "date": "1584"},
    {"title": "De Umbris Idearum", "title_latin": "De Umbris Idearum", "author": "Giordano Bruno",
     "era": "RENAISSANCE", "tradition": "Magical", "language": "Latin", "date": "1582"},
    {"title": "Utriusque Cosmi Historia", "title_latin": "Utriusque Cosmi Historia", "author": "Robert Fludd",
     "era": "RENAISSANCE", "tradition": "Hermetic", "language": "Latin", "date": "1617-1621"},
    {"title": "Aurora", "title_latin": "Aurora", "author": "Jacob Boehme",
     "era": "EARLY_MODERN", "tradition": "Theological", "language": "German", "date": "1612"},
    {"title": "Ars Notoria", "title_latin": "Ars Notoria", "author": "Anonymous",
     "era": "MEDIEVAL", "tradition": "Magical", "language": "Latin", "date": "13th century"},
]


def main():
    conn = sqlite3.connect(str(DB_PATH))
    conn.execute("PRAGMA foreign_keys=ON")

    seeded = 0
    linked = 0

    for src in PRIMARY_SOURCES:
        # Find author figure
        author_id = None
        if src["author"] and src["author"] not in ("Anonymous", "Unknown"):
            # Try exact match first, then partial
            row = conn.execute("SELECT id FROM figures WHERE name=?", (src["author"],)).fetchone()
            if not row:
                row = conn.execute("SELECT id FROM figures WHERE name LIKE ?",
                                  (f"%{src['author'].split()[-1]}%",)).fetchone()
            if row:
                author_id = row[0]

        # Find corpus document if this text IS in the corpus
        corpus_doc_id = None
        title_lower = src["title"].lower()
        for row in conn.execute("SELECT id, title FROM documents WHERE is_primary_source=1 OR doc_type='PRIMARY_SOURCE'"):
            if title_lower in (row[1] or "").lower():
                corpus_doc_id = row[0]
                break

        conn.execute("""
        INSERT OR IGNORE INTO texts
            (title, title_latin, author_figure_id, corpus_document_id,
             era, tradition, language, date_composed,
             source_method, confidence)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, 'SEED_DATA', 'HIGH')
        """, (src["title"], src.get("title_latin"), author_id, corpus_doc_id,
              src.get("era"), src.get("tradition"), src.get("language"), src.get("date")))
        seeded += 1

        # Era assignment for text
        text_row = conn.execute("SELECT id FROM texts WHERE title=?", (src["title"],)).fetchone()
        if text_row and src.get("era"):
            conn.execute("""
            INSERT OR IGNORE INTO era_assignments (entity_type, entity_id, era, era_role)
            VALUES ('TEXT', ?, ?, 'COMPOSED_IN')
            """, (text_row[0], src["era"]))

        # Figure-text link
        if text_row and author_id:
            conn.execute("""
            INSERT OR IGNORE INTO figure_texts (figure_id, text_id, relationship)
            VALUES (?, ?, 'AUTHORED')
            """, (author_id, text_row[0]))
            linked += 1

    conn.commit()

    total = conn.execute("SELECT COUNT(*) FROM texts").fetchone()[0]
    with_author = conn.execute("SELECT COUNT(*) FROM texts WHERE author_figure_id IS NOT NULL").fetchone()[0]
    ft_links = conn.execute("SELECT COUNT(*) FROM figure_texts").fetchone()[0]
    era_links = conn.execute("SELECT COUNT(*) FROM era_assignments WHERE entity_type='TEXT'").fetchone()[0]

    print(f"=== PRIMARY SOURCE SEEDING ===")
    print(f"Texts seeded: {seeded}")
    print(f"Total in DB: {total}")
    print(f"With author link: {with_author}")
    print(f"Figure-text links: {ft_links}")
    print(f"Era assignments (texts): {era_links}")

    conn.close()


if __name__ == "__main__":
    main()
