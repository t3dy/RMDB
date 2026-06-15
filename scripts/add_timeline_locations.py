"""Add geographic location data to all 135 timeline events.

Adds location_name, latitude, longitude columns and populates them.
Run: python scripts/add_timeline_locations.py
Idempotent.
"""

import io
import sqlite3
import sys
from pathlib import Path

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

DB_PATH = Path(__file__).resolve().parent.parent / "db" / "renmagic.db"

# (year, title_fragment, location_name, lat, lon)
# title_fragment is matched with LIKE '%fragment%' against the title column
# If multiple rows match, all get the same location.

LOCATIONS = [
    # ── ANCIENT ──────────────────────────────────────────────────────────────
    (-360, "Plato's Timaeus",           "Athens, Greece",              37.98,  23.73),
    (204,  "Birth of Plotinus",         "Lycopolis, Egypt",            27.19,  31.18),
    (234,  "Birth of Porphyry",         "Tyre, Lebanon",               33.27,  35.20),
    (245,  "Birth of Iamblichus",       "Chalcis, Syria",              36.17,  37.05),
    (250,  "Plotinus opens school",     "Rome, Italy",                 41.90,  12.49),
    (263,  "Porphyry joins Plotinus",   "Rome, Italy",                 41.90,  12.49),
    (270,  "Death of Plotinus",         "Campania, Italy",             41.05,  14.25),
    (300,  "Iamblichus writes",         "Apamea, Syria",               35.43,  36.40),
    (301,  "Porphyry publishes",        "Rome, Italy",                 41.90,  12.49),
    (305,  "Death of Porphyry",         "Rome, Italy",                 41.90,  12.49),
    (325,  "Death of Iamblichus",       "Syria",                       35.00,  38.00),
    (412,  "Birth of Proclus",          "Constantinople",              41.01,  28.97),
    (420,  "Augustine",                 "Hippo Regius, Algeria",       36.87,   7.76),
    (450,  "Proclus writes",            "Athens, Greece",              37.98,  23.73),
    (485,  "Death of Proclus",          "Athens, Greece",              37.98,  23.73),
    (500,  "Pseudo-Dionysius",          "Syria",                       35.00,  38.00),
    (529,  "Justinian closes",          "Athens, Greece",              37.98,  23.73),
    (600,  "Sefer Yetzirah",            "Palestine",                   31.77,  35.23),

    # ── MEDIEVAL ISLAMIC ────────────────────────────────────────────────────
    (801,  "Birth of Al-Kindi",         "Kufa, Iraq",                  32.03,  44.40),
    (820,  "House of Wisdom",           "Baghdad, Iraq",               33.34,  44.40),
    (850,  "Al-Kindi writes",           "Baghdad, Iraq",               33.34,  44.40),
    (873,  "Death of Al-Kindi",         "Baghdad, Iraq",               33.34,  44.40),
    (980,  "Birth of Avicenna",         "Bukhara, Uzbekistan",         39.77,  64.42),
    (1037, "Death of Avicenna",         "Hamadan, Iran",               34.80,  48.52),
    (1150, "Gerard of Cremona",         "Toledo, Spain",               39.86,  -4.02),
    (1180, "Liber de Causis",           "Paris, France",               48.85,   2.35),

    # ── MEDIEVAL EUROPEAN ───────────────────────────────────────────────────
    (1200, "Birth of Albertus",         "Lauingen, Germany",           48.57,  10.43),
    (1214, "Birth of Roger Bacon",      "Ilchester, England",          51.01,  -2.69),
    (1225, "Birth of Thomas Aquinas",   "Roccasecca, Italy",           41.56,  13.66),
    (1232, "Birth of Ramon Llull",      "Palma de Mallorca, Spain",    39.57,   2.65),
    (1245, "Aquinas studies",           "Cologne, Germany",            50.94,   6.96),
    (1256, "Picatrix translated into Castilian",
                                        "Toledo, Spain",               39.86,  -4.02),
    (1260, "Albertus Magnus writes",    "Cologne, Germany",            50.94,   6.96),
    (1267, "Roger Bacon presents",      "Oxford, England",             51.75,  -1.26),
    (1268, "Aquinas identifies",        "Paris, France",               48.85,   2.35),
    (1274, "Death of Thomas Aquinas",   "Fossanova, Italy",            41.44,  13.15),
    (1280, "Death of Albertus",         "Cologne, Germany",            50.94,   6.96),
    (1280, "Moses de León",             "Guadalajara, Spain",          40.63,  -3.17),
    (1292, "Death of Roger Bacon",      "Oxford, England",             51.75,  -1.26),
    (1300, "Picatrix translated into Latin",
                                        "Paris, France",               48.85,   2.35),
    (1316, "Death of Ramon Llull",      "Palma de Mallorca, Spain",    39.57,   2.65),

    # ── EARLY RENAISSANCE ───────────────────────────────────────────────────
    (1401, "Birth of Nicholas of Cusa", "Kues, Germany",               49.91,   7.13),
    (1433, "Birth of Marsilio Ficino",  "Figline Valdarno, Italy",     43.62,  11.46),
    (1440, "Cusa publishes",            "Venice, Italy",               45.44,  12.33),
    (1453, "Fall of Constantinople",    "Constantinople",              41.01,  28.97),
    (1455, "Birth of Johannes Reuchlin","Pforzheim, Germany",          48.89,   8.70),
    (1460, "Ficino begins translating", "Florence, Italy",             43.78,  11.25),
    (1462, "Birth of Johannes Trithemius",
                                        "Trittenheim, Germany",        49.83,   6.92),
    (1462, "Cosimo de' Medici",         "Florence, Italy",             43.81,  11.24),
    (1463, "Birth of Giovanni Pico",    "Mirandola, Italy",            44.88,  11.07),
    (1463, "Ficino completes Pimander", "Florence, Italy",             43.78,  11.25),
    (1464, "Death of Nicholas of Cusa", "Todi, Italy",                 42.78,  12.41),
    (1482, "Ficino publishes Theologia","Florence, Italy",             43.78,  11.25),
    (1486, "Birth of Heinrich Cornelius Agrippa",
                                        "Cologne, Germany",            50.94,   6.96),
    (1486, "Pico's 900 Theses",         "Rome, Italy",                 41.90,  12.49),
    (1487, "Papal condemnation",        "Rome, Italy",                 41.90,  12.49),
    (1487, "Pico publishes Heptaplus",  "Florence, Italy",             43.78,  11.25),
    (1489, "Ficino's De Vita",          "Florence, Italy",             43.78,  11.25),
    (1490, "Pico settles in Florence",  "Florence, Italy",             43.78,  11.25),
    (1492, "Ficino completes Plotinus", "Florence, Italy",             43.78,  11.25),
    (1493, "Birth of Paracelsus",       "Einsiedeln, Switzerland",     47.13,   8.74),
    (1494, "Death of Giovanni Pico",    "Florence, Italy",             43.78,  11.25),
    (1494, "Reuchlin's De Verbo",       "Pforzheim, Germany",          48.89,   8.70),
    (1499, "Death of Marsilio Ficino",  "Careggi, Italy",              43.81,  11.24),
    (1499, "Trithemius composes Steganographia",
                                        "Sponheim, Germany",           49.84,   7.40),

    # ── RENAISSANCE ──────────────────────────────────────────────────────────
    (1509, "Reuchlin-Pfefferkorn",      "Augsburg, Germany",           48.37,  10.90),
    (1510, "Agrippa's De Occulta",      "Dôle, France",                47.10,   5.50),
    (1515, "Birth of Johann Weyer",     "Grave, Netherlands",          51.76,   5.74),
    (1516, "Death of Johannes Trithemius",
                                        "Würzburg, Germany",           49.79,   9.95),
    (1516, "Trithemius' Polygraphia",   "Oppenheim, Germany",          49.85,   8.36),
    (1517, "Reuchlin's De Arte Cabalistica",
                                        "Hagenau, Alsace",             48.81,   7.79),
    (1517, "Luther's Ninety-Five Theses",
                                        "Wittenberg, Germany",         51.87,  12.65),
    (1522, "Death of Johannes Reuchlin","Stuttgart area, Germany",     48.78,   9.18),
    (1527, "Birth of John Dee",         "London, England",             51.51,  -0.13),
    (1530, "Agrippa publishes De Vanitate",
                                        "Antwerp, Belgium",            51.22,   4.40),
    (1531, "Agrippa's De Occulta Philosophia published",
                                        "Antwerp, Belgium",            51.22,   4.40),
    (1535, "Death of Heinrich Cornelius Agrippa",
                                        "Grenoble, France",            45.19,   5.72),
    (1535, "Birth of Giovan Battista Della Porta",
                                        "Vico Equense, Italy",         40.67,  14.43),
    (1538, "Birth of Reginald Scot",    "Brabourne, England",          51.12,   0.96),
    (1541, "Death of Paracelsus",       "Salzburg, Austria",           47.80,  13.04),
    (1548, "Birth of Giordano Bruno",   "Nola, Italy",                 40.93,  14.52),
    (1558, "Della Porta publishes Magia Naturalis (first",
                                        "Naples, Italy",               40.85,  14.27),
    (1563, "Weyer publishes",           "Cleves, Germany",             51.79,   6.14),
    (1564, "Dee's Monas Hieroglyphica", "Antwerp, Belgium",            51.22,   4.40),
    (1574, "Birth of Robert Fludd",     "Bearsted, England",           51.27,   0.56),
    (1575, "Birth of Jacob Boehme",     "Görlitz area, Germany",       51.15,  14.99),
    (1576, "Dee's library at Mortlake", "London, England",             51.47,  -0.26),
    (1580, "Bodin publishes",           "Paris, France",               48.85,   2.35),
    (1581, "Dee begins angelic conversations",
                                        "Mortlake, London",            51.47,  -0.26),
    (1582, "Edward Kelley becomes",     "Mortlake, London",            51.47,  -0.26),
    (1583, "Prague",                    "Prague, Bohemia",             50.08,  14.44),
    (1584, "Bruno's De la Causa",       "London, England",             51.51,  -0.13),
    (1584, "Scot publishes",            "London, England",             51.51,  -0.13),
    (1588, "Death of Johann Weyer",     "Tecklenburg, Germany",        52.22,   7.82),
    (1589, "Della Porta publishes expanded",
                                        "Naples, Italy",               40.85,  14.27),
    (1591, "Bruno arrested",            "Venice, Italy",               45.44,  12.33),
    (1597, "James VI",                  "Edinburgh, Scotland",         55.95,  -3.19),
    (1599, "Death of Reginald Scot",    "Smeeth, England",             51.13,   0.90),
    (1600, "Giordano Bruno",            "Rome, Italy",                 41.90,  12.47),
    (1602, "Birth of Athanasius Kircher",
                                        "Geisa, Germany",              50.69,  10.00),
    (1606, "Steganographia published",  "Frankfurt, Germany",          50.11,   8.68),
    (1608, "Death of John Dee",         "Mortlake, London",            51.47,  -0.26),

    # ── EARLY MODERN ────────────────────────────────────────────────────────
    (1614, "Birth of Francis Mercury van Helmont",
                                        "Vilvoorde, Belgium",          50.93,   4.43),
    (1614, "Fama Fraternitatis",        "Kassel, Germany",             51.31,   9.49),
    (1614, "Isaac Casaubon",            "London, England",             51.51,  -0.13),
    (1615, "Death of Giovan Battista",  "Naples, Italy",               40.85,  14.27),
    (1615, "Confessio Fraternitatis",   "Kassel, Germany",             51.31,   9.49),
    (1616, "Chemical Wedding",          "Strasbourg, Alsace",          48.58,   7.75),
    (1617, "Fludd's Utriusque",         "Oppenheim, Germany",          49.85,   8.36),
    (1619, "Kepler-Fludd",              "Linz, Austria",               48.31,  14.29),
    (1624, "Death of Jacob Boehme",     "Görlitz, Germany",            51.15,  14.99),
    (1631, "Mersenne",                  "Paris, France",               48.85,   2.35),
    (1637, "Death of Robert Fludd",     "London, England",             51.51,  -0.13),
    (1637, "Descartes publishes",       "Leiden, Netherlands",         52.16,   4.49),
    (1640, "Newton's alchemical",       "Cambridge, England",          52.21,   0.12),
    (1652, "Casaubon publishes A True", "London, England",             51.51,  -0.13),
    (1659, "Meric Casaubon",            "London, England",             51.51,  -0.13),
    (1677, "Van Helmont and Knorr",     "Sulzbach, Germany",           49.49,  11.75),
    (1680, "Death of Athanasius Kircher",
                                        "Rome, Italy",                 41.90,  12.49),
    (1687, "Newton publishes Principia","London, England",             51.51,  -0.13),
    (1698, "Death of Francis Mercury",  "Berlin, Germany",             52.52,  13.40),

    # ── SCHOLARSHIP ──────────────────────────────────────────────────────────
    (1958, "Walker publishes",          "London, England",             51.51,  -0.13),
    (1964, "Yates publishes Giordano",  "London, England",             51.51,  -0.13),
    (1966, "Yates publishes The Art",   "London, England",             51.51,  -0.13),
    (1971, "Keith Thomas",              "Oxford, England",             51.75,  -1.26),
    (1978, "Peters publishes",          "Philadelphia, USA",           39.95, -75.17),
    (1984, "Vickers",                   "Cambridge, England",          52.21,   0.12),
    (1988, "Copenhaver publishes essays","Los Angeles, USA",           34.07, -118.45),
    (1992, "Copenhaver publishes critical",
                                        "Los Angeles, USA",            34.07, -118.45),
    (2001, "Klaassen",                  "Saskatoon, Canada",           52.13, -106.67),
    (2005, "Hanegraaff edits",          "Amsterdam, Netherlands",      52.37,   4.90),
    (2012, "Hanegraaff publishes",      "Amsterdam, Netherlands",      52.37,   4.90),
    (2015, "Saif publishes",            "London, England",             51.51,  -0.13),
]


def run():
    conn = sqlite3.connect(str(DB_PATH))
    conn.execute("PRAGMA foreign_keys=ON")
    c = conn.cursor()

    # Add columns if they don't exist
    existing = {row[1] for row in c.execute("PRAGMA table_info(timeline_events)").fetchall()}
    for col, typ in [("location_name", "TEXT"), ("latitude", "REAL"), ("longitude", "REAL")]:
        if col not in existing:
            c.execute(f"ALTER TABLE timeline_events ADD COLUMN {col} {typ}")
            print(f"  Added column: {col}")
    conn.commit()

    assigned = 0
    skipped = 0

    for year, title_frag, location_name, lat, lon in LOCATIONS:
        rows = c.execute(
            "SELECT id FROM timeline_events WHERE year=? AND title LIKE ?",
            (year, f"%{title_frag}%")
        ).fetchall()
        if not rows:
            print(f"  WARNING no match: year={year} frag='{title_frag}'")
            skipped += 1
            continue
        for (event_id,) in rows:
            c.execute("""
                UPDATE timeline_events
                SET location_name=?, latitude=?, longitude=?,
                    updated_at=datetime('now')
                WHERE id=?
            """, (location_name, lat, lon, event_id))
            assigned += 1

    conn.commit()

    # Report unlocated events
    unlocated = c.execute(
        "SELECT year, title FROM timeline_events WHERE latitude IS NULL ORDER BY year"
    ).fetchall()
    if unlocated:
        print(f"\n  WARNING: {len(unlocated)} events still have no location:")
        for year, title in unlocated:
            print(f"    {year}: {title}")

    total = c.execute("SELECT COUNT(*) FROM timeline_events").fetchone()[0]
    located = c.execute(
        "SELECT COUNT(*) FROM timeline_events WHERE latitude IS NOT NULL"
    ).fetchone()[0]

    conn.close()
    print(f"\n  Assigned: {assigned}  Lookup misses: {skipped}")
    print(f"  Located: {located}/{total} events")
    print("Done.")


if __name__ == "__main__":
    run()
