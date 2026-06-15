"""Export timeline events to website/static/data/timeline.json for the Leaflet map.

Run: python scripts/export_timeline_json.py
"""

import io
import json
import sqlite3
import sys
from pathlib import Path

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

DB_PATH = Path(__file__).resolve().parent.parent / "db" / "renmagic.db"
OUT_PATH = Path(__file__).resolve().parent.parent / "website" / "static" / "data" / "timeline.json"


def run():
    conn = sqlite3.connect(str(DB_PATH))
    conn.row_factory = sqlite3.Row
    c = conn.cursor()

    rows = c.execute("""
        SELECT
            te.id,
            te.year,
            te.year_end,
            te.event_type,
            te.title,
            te.description,
            te.location_name,
            te.latitude,
            te.longitude,
            GROUP_CONCAT(f.name, '|') AS figure_names
        FROM timeline_events te
        LEFT JOIN event_figures ef ON ef.event_id = te.id
        LEFT JOIN figures f ON f.id = ef.figure_id
        WHERE te.latitude IS NOT NULL
        GROUP BY te.id
        ORDER BY te.year
    """).fetchall()

    events = []
    for row in rows:
        fig_names = [n for n in (row["figure_names"] or "").split("|") if n]
        events.append({
            "id": row["id"],
            "year": row["year"],
            "year_end": row["year_end"],
            "event_type": row["event_type"],
            "title": row["title"],
            "description": row["description"],
            "location_name": row["location_name"],
            "lat": row["latitude"],
            "lon": row["longitude"],
            "figures": fig_names,
        })

    conn.close()

    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(OUT_PATH, "w", encoding="utf-8") as f:
        json.dump(events, f, ensure_ascii=False, indent=2)

    print(f"Exported {len(events)} events → {OUT_PATH}")


if __name__ == "__main__":
    run()
