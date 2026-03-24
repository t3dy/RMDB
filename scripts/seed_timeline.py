"""Seed timeline events from figure dates + curated milestones.

Sources:
1. Figure birth/death dates -> BIOGRAPHY events
2. Known publication dates from curated list -> PUBLICATION events
3. Key historical milestones -> TRIAL, POLITICAL, etc.

All deterministic. No LLM.
"""

import io
import sqlite3
import sys
from pathlib import Path

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

CORPUS_ROOT = Path(__file__).resolve().parent.parent
DB_PATH = CORPUS_ROOT / "db" / "renmagic.db"

# Curated milestone events (drawn from corpus knowledge)
MILESTONES = [
    (1460, None, "PUBLICATION", "Ficino begins translating Corpus Hermeticum",
     "At the request of Cosimo de' Medici, Marsilio Ficino begins translating the Greek Hermetica into Latin, prioritizing it over his Plato translations."),
    (1463, None, "PUBLICATION", "Ficino completes Pimander translation",
     "Ficino's Latin translation of the Corpus Hermeticum circulates in manuscript, establishing Hermes Trismegistus as a prisca theologia authority."),
    (1486, None, "PUBLICATION", "Pico's 900 Theses",
     "Giovanni Pico della Mirandola publishes his 900 Conclusiones, proposing a syncretic unity of Kabbalah, Hermeticism, and Christian theology."),
    (1487, None, "TRIAL", "Papal condemnation of Pico's Theses",
     "Pope Innocent VIII condemns 13 of Pico's 900 theses as heretical. Pico flees to France and is briefly imprisoned."),
    (1489, None, "PUBLICATION", "Ficino's De Vita",
     "Ficino publishes Three Books on Life, integrating Neoplatonic philosophy with astrological medicine and natural magic."),
    (1494, None, "PUBLICATION", "Reuchlin's De Verbo Mirifico",
     "Johannes Reuchlin publishes On the Wonder-Working Word, the first systematic Christian Kabbalistic treatise."),
    (1510, None, "PUBLICATION", "Agrippa's De Occulta Philosophia (first draft)",
     "Agrippa circulates the manuscript of De Occulta Philosophia, synthesizing natural, celestial, and ceremonial magic."),
    (1516, None, "PUBLICATION", "Trithemius' Polygraphia published posthumously",
     "Trithemius' cryptographic treatise is published after his death, becoming a landmark in both cryptography and angel magic."),
    (1517, None, "PUBLICATION", "Reuchlin's De Arte Cabalistica",
     "Reuchlin publishes On the Art of Kabbalah, the most sophisticated Christian Kabbalistic work of the Renaissance."),
    (1531, 1533, "PUBLICATION", "Agrippa's De Occulta Philosophia published",
     "The three books of De Occulta Philosophia are published in Cologne, becoming the foundational Renaissance synthesis of magical philosophy."),
    (1564, None, "PUBLICATION", "Dee's Monas Hieroglyphica",
     "John Dee publishes the Monas Hieroglyphica in Antwerp, proposing a unified hieroglyphic symbol encoding cosmic knowledge."),
    (1583, 1589, "BIOGRAPHY", "Dee's angelic conversations in Prague and Krakow",
     "Dee and Edward Kelley conduct scrying sessions across Central Europe, producing the Enochian angel language system."),
    (1584, None, "PUBLICATION", "Bruno's De la Causa and Cena de le Ceneri",
     "Giordano Bruno publishes his Italian dialogues in London, arguing for an infinite universe and Hermetic cosmology."),
    (1600, None, "TRIAL", "Bruno burned at the stake in Rome",
     "The Roman Inquisition executes Giordano Bruno for heresy at the Campo de' Fiori, making him a martyr for free thought."),
    (1614, None, "PUBLICATION", "Fama Fraternitatis (Rosicrucian manifesto)",
     "The first Rosicrucian manifesto appears, claiming a secret brotherhood founded on Hermetic and Paracelsian principles."),
    (1617, None, "PUBLICATION", "Fludd's Utriusque Cosmi Historia",
     "Robert Fludd publishes his encyclopedic History of the Two Worlds, featuring elaborate cosmological diagrams integrating Hermetic philosophy."),
    (1652, None, "PUBLICATION", "Casaubon publishes A True and Faithful Relation",
     "Meric Casaubon publishes Dee's angelic diaries, framing them as evidence of demonic deception rather than genuine revelation."),
    (1964, None, "SCHOLARSHIP", "Yates publishes Giordano Bruno and the Hermetic Tradition",
     "Frances Yates' landmark study proposes that Hermeticism was a driving force behind the Scientific Revolution, launching the 'Yates thesis' debate."),
]


def main():
    conn = sqlite3.connect(str(DB_PATH))
    conn.execute("PRAGMA foreign_keys=ON")

    seeded = 0

    # 1. Figure birth/death events (only for major figures with dates)
    figures = conn.execute("""
        SELECT id, name, birth_year, death_year, figure_type FROM figures
        WHERE birth_year IS NOT NULL AND figure_type = 'HISTORICAL'
        AND birth_year > 0
    """).fetchall()

    for fig_id, name, birth, death, ftype in figures:
        # Birth
        if birth and birth > 100:  # Skip ancient figures for timeline clarity
            conn.execute("""
            INSERT OR IGNORE INTO timeline_events (year, event_type, title, source_method, confidence)
            VALUES (?, 'BIOGRAPHY', ?, 'SEED_DATA', 'HIGH')
            """, (birth, f"Birth of {name}"))

            # Link to figure
            ev = conn.execute("SELECT id FROM timeline_events WHERE year=? AND title=?",
                            (birth, f"Birth of {name}")).fetchone()
            if ev:
                conn.execute("INSERT OR IGNORE INTO event_figures (event_id, figure_id) VALUES (?,?)",
                            (ev[0], fig_id))
                seeded += 1

        # Death
        if death and death > 100:
            conn.execute("""
            INSERT OR IGNORE INTO timeline_events (year, event_type, title, source_method, confidence)
            VALUES (?, 'BIOGRAPHY', ?, 'SEED_DATA', 'HIGH')
            """, (death, f"Death of {name}"))

            ev = conn.execute("SELECT id FROM timeline_events WHERE year=? AND title=?",
                            (death, f"Death of {name}")).fetchone()
            if ev:
                conn.execute("INSERT OR IGNORE INTO event_figures (event_id, figure_id) VALUES (?,?)",
                            (ev[0], fig_id))
                seeded += 1

    # 2. Curated milestones
    for year, year_end, etype, title, desc in MILESTONES:
        conn.execute("""
        INSERT OR IGNORE INTO timeline_events (year, year_end, event_type, title, description,
                                               source_method, confidence)
        VALUES (?, ?, ?, ?, ?, 'SEED_DATA', 'HIGH')
        """, (year, year_end, etype, title, desc))
        seeded += 1

    conn.commit()

    total = conn.execute("SELECT COUNT(*) FROM timeline_events").fetchone()[0]
    with_desc = conn.execute("SELECT COUNT(*) FROM timeline_events WHERE description IS NOT NULL").fetchone()[0]
    links = conn.execute("SELECT COUNT(*) FROM event_figures").fetchone()[0]

    print(f"=== TIMELINE SEEDING ===")
    print(f"Events seeded: {seeded}")
    print(f"Total events: {total}")
    print(f"With descriptions: {with_desc}")
    print(f"Event-figure links: {links}")

    conn.close()


if __name__ == "__main__":
    main()
