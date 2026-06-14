#!/usr/bin/env python3
"""
Ontology remediation derived from TEXTS_CATALOG.md (Part 6).
Idempotent: safe to re-run.
  1. Insert 6 missing HISTORICAL figures (essays exist, no DB row).
  2. Relink orphaned texts to their authors.
All new/changed rows tagged source_method='LLM_ASSISTED', review_status='DRAFT'.
"""
import sqlite3, io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

con = sqlite3.connect('db/renmagic.db')
c = con.cursor()

NEW_FIGURES = [
    # name, latin, birth, death, nationality, primary_tradition
    ("Thomas Aquinas", "Thomas Aquinas", 1225, 1274, "Italian", "Scholasticism"),
    ("Porphyry", "Porphyrius", 234, 305, "Phoenician", "Neoplatonism"),
    ("Giovan Battista Della Porta", "Iohannes Baptista Porta", 1535, 1615, "Italian", "Natural Magic"),
    ("Avicenna", "Avicenna (Ibn Sina)", 980, 1037, "Persian", "Islamic Philosophy"),
    ("Reginald Scot", "Reginaldus Scotus", 1538, 1599, "English", "Witchcraft Skepticism"),
    ("Johann Weyer", "Ioannes Wierus", 1515, 1588, "Dutch", "Medical Demonology"),
]

inserted = 0
for name, latin, by, dy, nat, trad in NEW_FIGURES:
    c.execute("SELECT id FROM figures WHERE name=?", (name,))
    if c.fetchone():
        print(f"  exists, skip: {name}")
        continue
    c.execute("""
        INSERT INTO figures (name, name_latin, figure_type, birth_year, death_year,
            nationality, primary_tradition, source_method, review_status, confidence,
            created_at, updated_at)
        VALUES (?,?,'HISTORICAL',?,?,?,?,'LLM_ASSISTED','DRAFT','MEDIUM',
            datetime('now'), datetime('now'))
    """, (name, latin, by, dy, nat, trad))
    inserted += 1
    print(f"  inserted figure: {name} (id={c.lastrowid})")

# Relink orphaned texts: (text_title, author_name)
RELINKS = [
    ("Opus Majus", "Roger Bacon"),
    ("De Docta Ignorantia", "Nicholas of Cusa"),
    ("Ars Magna", "Ramon Llull"),
]
relinked = 0
for title, author in RELINKS:
    c.execute("SELECT id FROM figures WHERE name=?", (author,))
    frow = c.fetchone()
    if not frow:
        print(f"  WARN: author not found for relink: {author}")
        continue
    fid = frow[0]
    c.execute("SELECT id, author_figure_id FROM texts WHERE title=?", (title,))
    trow = c.fetchone()
    if not trow:
        print(f"  WARN: text not found: {title}")
        continue
    if trow[1] == fid:
        print(f"  already linked: {title} -> {author}")
        continue
    c.execute("UPDATE texts SET author_figure_id=?, updated_at=datetime('now') WHERE id=?", (fid, trow[0]))
    relinked += 1
    print(f"  relinked text: {title} -> {author} (figure {fid})")

con.commit()

c.execute("SELECT COUNT(*) FROM figures WHERE figure_type='HISTORICAL'")
hist = c.fetchone()[0]
c.execute("SELECT COUNT(*) FROM texts WHERE author_figure_id IS NOT NULL")
attributed = c.fetchone()[0]
print(f"\nDONE. inserted {inserted} figures, relinked {relinked} texts.")
print(f"  HISTORICAL figures now: {hist}")
print(f"  texts with an author now: {attributed}/36")
con.close()
