"""Export concepts from DB to Hugo content files in website/content/concepts/."""

import sqlite3
import json
import sys
import io
import os
import re

DB_PATH = "db/renmagic.db"
OUTPUT_DIR = "website/content/concepts"


def slugify_related(name: str) -> str:
    """Convert a concept title to its slug for internal links."""
    return re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")


def build_frontmatter(row: dict) -> str:
    related_figures = json.loads(row["related_figures"] or "[]")
    related_concepts = json.loads(row["related_concepts"] or "[]")

    lines = [
        "---",
        f'title: "{row["title"].replace(chr(34), chr(39))}"',
        f'slug: "{row["slug"]}"',
        f'category: "{row["category"] or ""}"',
        f'summary: "{(row["summary"] or "").replace(chr(34), chr(39))}"',
        f"word_count: {row['word_count'] or 0}",
        f'review_status: "{row["review_status"] or "DRAFT"}"',
    ]

    if related_figures:
        lines.append("related_figures:")
        for fig in related_figures:
            lines.append(f'  - "{fig}"')

    if related_concepts:
        lines.append("related_concepts:")
        for c in related_concepts:
            lines.append(f'  - "{c}"')

    lines.append("---")
    return "\n".join(lines)


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    c = conn.cursor()

    rows = c.execute(
        "SELECT * FROM concepts ORDER BY category, title"
    ).fetchall()

    written = 0
    for row in rows:
        row = dict(row)
        slug = row["slug"]
        fm = build_frontmatter(row)
        body = row["body"] or ""
        content = f"{fm}\n\n{body}\n"

        out_path = os.path.join(OUTPUT_DIR, f"{slug}.md")
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(content)
        written += 1
        print(f"  Wrote: {slug}.md  ({row['title']})")

    conn.close()
    print(f"\nExported {written} concept files to {OUTPUT_DIR}/")


if __name__ == "__main__":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
    main()
