"""Seed figures table from curated JSON + folder mapping.

Sources:
1. data/figures_seed.json (29 curated figures with biographical data)
2. Folder mapping for document_figures join table
3. Era assignments from seed data

Idempotent: INSERT OR IGNORE + UPDATE.
"""

import io
import json
import sqlite3
import sys
from pathlib import Path

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')

CORPUS_ROOT = Path(__file__).resolve().parent.parent
DB_PATH = CORPUS_ROOT / "db" / "renmagic.db"
SEED_PATH = CORPUS_ROOT / "data" / "figures_seed.json"

# Folder figure mapping (folder_figure value -> figure names)
FOLDER_TO_FIGURES = {
    "Dee": ["John Dee"],
    "Pico": ["Giovanni Pico della Mirandola"],
    "Bruno": ["Giordano Bruno", "Ramon Llull"],
    "Agrippa": ["Heinrich Cornelius Agrippa"],
    "Ficino": ["Marsilio Ficino"],
    "Copenhaver": ["Brian P. Copenhaver"],
    "Reuchlin": ["Johannes Reuchlin"],
    "Fludd": ["Robert Fludd"],
    "Kircher": ["Athanasius Kircher"],
    "Bohme": ["Jacob Boehme"],
    "Trithemius": ["Johannes Trithemius"],
    "Zika": ["Charles Zika"],
    "Perrone Compagni": ["Vittoria Perrone Compagni"],
    "Van Helmont": ["Francis Mercury van Helmont"],
}


def main():
    conn = sqlite3.connect(str(DB_PATH))
    conn.execute("PRAGMA foreign_keys=ON")

    figures = json.loads(SEED_PATH.read_text(encoding="utf-8"))
    seeded = 0

    for fig in figures:
        name = fig["name"]
        conn.execute("""
        INSERT INTO figures (name, figure_type, birth_year, death_year, nationality,
                            significance, source_method, review_status, confidence)
        VALUES (?, ?, ?, ?, ?, ?, 'SEED_DATA', 'DRAFT', 'HIGH')
        ON CONFLICT(name) DO UPDATE SET
            figure_type = excluded.figure_type,
            birth_year = COALESCE(excluded.birth_year, figures.birth_year),
            death_year = COALESCE(excluded.death_year, figures.death_year),
            nationality = COALESCE(excluded.nationality, figures.nationality),
            significance = COALESCE(excluded.significance, figures.significance),
            source_method = 'SEED_DATA',
            updated_at = datetime('now')
        """, (name, fig["type"], fig.get("birth"), fig.get("death"),
              fig.get("nat"), fig.get("sig")))
        seeded += 1

        # Era assignments
        fig_id = conn.execute("SELECT id FROM figures WHERE name=?", (name,)).fetchone()[0]
        for era, role in fig.get("eras", []):
            conn.execute("""
            INSERT OR IGNORE INTO era_assignments (entity_type, entity_id, era, era_role)
            VALUES ('FIGURE', ?, ?, ?)
            """, (fig_id, era, role))

    # Populate document_figures from folder mapping
    join_count = 0
    for folder_fig, figure_names in FOLDER_TO_FIGURES.items():
        docs = conn.execute(
            "SELECT id FROM documents WHERE folder_figure=?", (folder_fig,)
        ).fetchall()
        for fig_name in figure_names:
            fig_row = conn.execute("SELECT id FROM figures WHERE name=?", (fig_name,)).fetchone()
            if not fig_row:
                continue
            for (doc_id,) in docs:
                conn.execute("""
                INSERT OR IGNORE INTO document_figures (document_id, figure_id, relationship, source_method)
                VALUES (?, ?, 'SUBJECT', 'DETERMINISTIC')
                """, (doc_id, fig_row[0]))
                join_count += 1

    conn.commit()

    # Summary
    total = conn.execute("SELECT COUNT(*) FROM figures").fetchone()[0]
    hist = conn.execute("SELECT COUNT(*) FROM figures WHERE figure_type='HISTORICAL'").fetchone()[0]
    scholar = conn.execute("SELECT COUNT(*) FROM figures WHERE figure_type='SCHOLAR'").fetchone()[0]
    with_birth = conn.execute("SELECT COUNT(*) FROM figures WHERE birth_year IS NOT NULL").fetchone()[0]
    era_count = conn.execute("SELECT COUNT(*) FROM era_assignments WHERE entity_type='FIGURE'").fetchone()[0]
    df_count = conn.execute("SELECT COUNT(*) FROM document_figures").fetchone()[0]

    print(f"=== FIGURE SEEDING ===")
    print(f"Figures seeded: {seeded} ({hist} historical, {scholar} scholars)")
    print(f"With birth year: {with_birth}")
    print(f"Era assignments: {era_count}")
    print(f"Document-figure links: {df_count}")

    # Show sample
    print(f"\nSample figures:")
    for row in conn.execute("SELECT name, birth_year, death_year, nationality, figure_type FROM figures ORDER BY birth_year LIMIT 10").fetchall():
        print(f"  {row[0]} ({row[1]}-{row[2]}) [{row[3]}] {row[4]}")

    conn.close()


if __name__ == "__main__":
    main()
