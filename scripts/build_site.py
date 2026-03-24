"""Build static site from SQLite database.

Generates a complete static website in site/ directory with:
- Index page with project overview and stats
- Dictionary page with all defined terms
- Figures page with all seeded figures
- Timeline page with all events
- Library page with primary sources
- Catalog page with all corpus documents
- About/methodology page

Uses Jinja2-style string templates (inline, no external template files).
Vanilla HTML/CSS, no frameworks. GitHub Pages compatible.
"""

import io
import json
import sqlite3
import sys
from pathlib import Path

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

CORPUS_ROOT = Path(__file__).resolve().parent.parent
DB_PATH = CORPUS_ROOT / "db" / "renmagic.db"
SITE_DIR = CORPUS_ROOT / "site"

# ── CSS ──
CSS = """
:root {
    --bg: #f5f0e8;
    --bg-card: #fff;
    --text: #2c2418;
    --text-muted: #6b5e4f;
    --accent: #8b4513;
    --accent-light: #d4a574;
    --accent-hover: #a0522d;
    --header-bg: #2c2418;
    --header-text: #f5f0e8;
    --border: #d4c5a9;
    --shadow: rgba(44, 36, 24, 0.08);
    --font: 'Georgia', 'Times New Roman', serif;
    --font-mono: 'Consolas', 'Monaco', monospace;
}
* { margin: 0; padding: 0; box-sizing: border-box; }
body { font-family: var(--font); background: var(--bg); color: var(--text); line-height: 1.7; }
a { color: var(--accent); text-decoration: none; }
a:hover { color: var(--accent-hover); text-decoration: underline; }
header { background: var(--header-bg); color: var(--header-text); padding: 1.5rem 2rem; }
header h1 { font-size: 1.6rem; font-weight: 400; letter-spacing: 0.05em; }
header h1 span { font-weight: 700; }
header nav { margin-top: 0.5rem; }
header nav a { color: var(--accent-light); margin-right: 1.5rem; font-size: 0.9rem; text-transform: uppercase; letter-spacing: 0.08em; }
header nav a:hover { color: #fff; }
main { max-width: 1100px; margin: 2rem auto; padding: 0 2rem; }
h2 { font-size: 1.4rem; color: var(--accent); margin: 2rem 0 1rem; border-bottom: 1px solid var(--border); padding-bottom: 0.3rem; }
h3 { font-size: 1.1rem; color: var(--text); margin: 1.5rem 0 0.5rem; }
.stats-bar { display: flex; gap: 2rem; flex-wrap: wrap; margin: 1.5rem 0; }
.stat { background: var(--bg-card); padding: 1rem 1.5rem; border-radius: 6px; box-shadow: 0 1px 4px var(--shadow); border-left: 3px solid var(--accent); }
.stat .num { font-size: 1.8rem; font-weight: 700; color: var(--accent); }
.stat .label { font-size: 0.8rem; color: var(--text-muted); text-transform: uppercase; letter-spacing: 0.05em; }
.card-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(300px, 1fr)); gap: 1.5rem; margin: 1rem 0; }
.card { background: var(--bg-card); border-radius: 6px; padding: 1.2rem 1.5rem; box-shadow: 0 1px 4px var(--shadow); border-top: 2px solid var(--accent-light); }
.card h3 { margin: 0 0 0.3rem; font-size: 1rem; }
.card .meta { font-size: 0.8rem; color: var(--text-muted); margin-bottom: 0.5rem; }
.card p { font-size: 0.9rem; line-height: 1.6; }
.tag { display: inline-block; background: var(--accent-light); color: var(--header-bg); font-size: 0.7rem; padding: 0.15rem 0.5rem; border-radius: 3px; margin: 0.1rem; text-transform: uppercase; letter-spacing: 0.03em; }
.tag.hermetic { background: #c4956a; }
.tag.kabbalistic { background: #7a6b8a; color: #fff; }
.tag.neoplatonic { background: #5a7a6b; color: #fff; }
.tag.magical { background: #8b4513; color: #fff; }
.tag.astrological { background: #4a6a8a; color: #fff; }
.tag.theological { background: #6a5a4a; color: #fff; }
.tag.enochian { background: #3a5a7a; color: #fff; }
.tag.alchemical { background: #7a5a3a; color: #fff; }
.tag.philosophical { background: #5a6a5a; color: #fff; }
table { width: 100%; border-collapse: collapse; margin: 1rem 0; font-size: 0.9rem; }
th { background: var(--header-bg); color: var(--header-text); padding: 0.6rem 1rem; text-align: left; font-weight: 400; text-transform: uppercase; font-size: 0.75rem; letter-spacing: 0.05em; }
td { padding: 0.5rem 1rem; border-bottom: 1px solid var(--border); }
tr:hover td { background: rgba(139,69,19,0.03); }
.timeline-event { border-left: 3px solid var(--accent); padding: 0.8rem 1.5rem; margin: 0.8rem 0; background: var(--bg-card); border-radius: 0 6px 6px 0; }
.timeline-event .year { font-size: 1.1rem; font-weight: 700; color: var(--accent); }
.timeline-event .title { font-weight: 600; }
.timeline-event .desc { font-size: 0.9rem; color: var(--text-muted); margin-top: 0.3rem; }
.badge { display: inline-block; font-size: 0.7rem; padding: 0.1rem 0.4rem; border-radius: 3px; background: var(--border); color: var(--text-muted); }
.badge.draft { background: #ffeaa7; color: #856404; }
footer { text-align: center; padding: 2rem; color: var(--text-muted); font-size: 0.8rem; margin-top: 3rem; border-top: 1px solid var(--border); }
.search-box { width: 100%; padding: 0.7rem 1rem; border: 1px solid var(--border); border-radius: 6px; font-size: 1rem; font-family: var(--font); margin: 1rem 0; }
.search-box:focus { outline: 2px solid var(--accent); border-color: var(--accent); }
.disclosure { background: #fff3cd; border: 1px solid #ffc107; padding: 0.8rem 1rem; border-radius: 6px; font-size: 0.8rem; margin: 1rem 0; }
@media (max-width: 768px) {
    .stats-bar { flex-direction: column; }
    .card-grid { grid-template-columns: 1fr; }
    header { padding: 1rem; }
    main { padding: 0 1rem; }
}
"""

NAV = """<nav>
<a href="index.html">Home</a>
<a href="dictionary.html">Dictionary</a>
<a href="figures.html">Figures</a>
<a href="timeline.html">Timeline</a>
<a href="library.html">Library</a>
<a href="catalog.html">Catalog</a>
<a href="about.html">About</a>
</nav>"""

DISCLOSURE = '<div class="disclosure">This content was drafted by an AI language model based on scholarly sources in our corpus. It has not been reviewed by a human scholar. Citations should be verified against original sources. <span class="badge draft">DRAFT</span></div>'


def page(title, content, active=""):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} — RenMagDB</title>
<style>{CSS}</style>
</head>
<body>
<header>
<h1><span>RenMagDB</span> — Renaissance Magic Database</h1>
{NAV}
</header>
<main>
{content}
</main>
<footer>
RenMagDB &mdash; A digital humanities project cataloging Renaissance magic scholarship.
Built with Python + SQLite + Claude Code. <a href="https://github.com/t3dy/RMDB">GitHub</a>
</footer>
</body>
</html>"""


def build_index(conn):
    docs = conn.execute("SELECT COUNT(*) FROM documents").fetchone()[0]
    figs = conn.execute("SELECT COUNT(*) FROM figures").fetchone()[0]
    terms = conn.execute("SELECT COUNT(*) FROM dictionary_terms WHERE definition_brief IS NOT NULL AND definition_brief NOT LIKE '[GENERIC%'").fetchone()[0]
    events = conn.execute("SELECT COUNT(*) FROM timeline_events").fetchone()[0]
    texts = conn.execute("SELECT COUNT(*) FROM texts").fetchone()[0]
    traditions = conn.execute("SELECT COUNT(*) FROM topics WHERE description LIKE '%corpus occurrences%'").fetchone()[0]

    content = f"""
<h2>A Digital Exhibition of Renaissance Magic Scholarship</h2>
<p>RenMagDB catalogs a research corpus of {docs} scholarly documents on Renaissance magic — covering figures from Marsilio Ficino to John Dee, traditions from Hermeticism to Kabbalah, and texts from the <em>Corpus Hermeticum</em> to the Enochian <em>Calls</em>.</p>

{DISCLOSURE}

<div class="stats-bar">
<div class="stat"><div class="num">{docs}</div><div class="label">Documents</div></div>
<div class="stat"><div class="num">{figs}</div><div class="label">Figures</div></div>
<div class="stat"><div class="num">{terms}</div><div class="label">Dictionary Terms</div></div>
<div class="stat"><div class="num">{events}</div><div class="label">Timeline Events</div></div>
<div class="stat"><div class="num">{texts}</div><div class="label">Primary Sources</div></div>
<div class="stat"><div class="num">{traditions}</div><div class="label">Traditions</div></div>
</div>

<h2>Traditions</h2>
<div class="card-grid">
"""
    for row in conn.execute("SELECT name, description FROM topics WHERE description LIKE '%corpus occurrences%' ORDER BY name"):
        desc = (row[1] or "")[:200] + "..." if len(row[1] or "") > 200 else (row[1] or "")
        tag_class = row[0].lower().split()[0] if row[0] else ""
        content += f'<div class="card"><h3>{row[0]}</h3><p>{desc}</p></div>\n'

    content += "</div>"

    content += """
<h2>Key Figures</h2>
<div class="card-grid">
"""
    for row in conn.execute("SELECT name, birth_year, death_year, nationality, significance, figure_type FROM figures WHERE figure_type='HISTORICAL' ORDER BY birth_year"):
        dates = f"({row[1]}–{row[2]})" if row[1] else ""
        sig = (row[4] or "")[:150] + "..." if len(row[4] or "") > 150 else (row[4] or "")
        content += f'<div class="card"><h3>{row[0]} {dates}</h3><div class="meta">{row[3] or ""}</div><p>{sig}</p></div>\n'

    content += "</div>"
    return page("Home", content)


def build_dictionary(conn):
    content = "<h2>Dictionary of Renaissance Magic Terms</h2>\n"
    content += '<input type="text" class="search-box" id="dictSearch" placeholder="Search terms..." onkeyup="filterDict()">\n'
    content += DISCLOSURE + "\n"

    domains = conn.execute("SELECT DISTINCT domain FROM dictionary_terms WHERE definition_brief IS NOT NULL AND definition_brief NOT LIKE '[GENERIC%' ORDER BY domain").fetchall()

    for (domain,) in domains:
        tag_class = domain.lower() if domain else ""
        content += f'<h3><span class="tag {tag_class}">{domain}</span></h3>\n'
        terms = conn.execute("""
            SELECT term, term_language, english_translation, definition_brief, definition_long, category_type, frequency
            FROM dictionary_terms WHERE domain=? AND definition_brief IS NOT NULL AND definition_brief NOT LIKE '[GENERIC%'
            ORDER BY frequency DESC
        """, (domain,)).fetchall()

        for t in terms:
            cat_badge = f' <span class="badge">{t[5]}</span>' if t[5] else ""
            long_def = f"<p>{t[4]}</p>" if t[4] else ""
            content += f"""<div class="card dict-entry" data-term="{t[0].lower()}">
<h3><em>{t[0]}</em> ({t[1]}){cat_badge}</h3>
<div class="meta">{t[2]} &bull; freq: {t[6]}</div>
<p><strong>{t[3]}</strong></p>
{long_def}
</div>\n"""

    content += """
<script>
function filterDict() {
    const q = document.getElementById('dictSearch').value.toLowerCase();
    document.querySelectorAll('.dict-entry').forEach(el => {
        el.style.display = el.dataset.term.includes(q) || el.textContent.toLowerCase().includes(q) ? '' : 'none';
    });
}
</script>"""
    return page("Dictionary", content)


def build_figures(conn):
    content = "<h2>Figures</h2>\n" + DISCLOSURE + "\n"

    content += "<h3>Historical Figures</h3>\n<div class='card-grid'>\n"
    for row in conn.execute("""
        SELECT f.name, f.birth_year, f.death_year, f.nationality, f.significance, f.figure_type,
               (SELECT COUNT(*) FROM document_figures df WHERE df.figure_id = f.id) as doc_count
        FROM figures f WHERE f.figure_type='HISTORICAL' ORDER BY f.birth_year
    """):
        dates = f"({row[1]}–{row[2]})" if row[1] else ""
        sig = (row[4] or "")[:250]
        # Get traditions
        traditions = conn.execute("SELECT tradition, relationship_type FROM figure_traditions WHERE figure_id=(SELECT id FROM figures WHERE name=?)", (row[0],)).fetchall()
        trad_html = " ".join(f'<span class="tag">{t[1]}: {t[0]}</span>' for t in traditions)
        content += f"""<div class="card">
<h3>{row[0]} {dates}</h3>
<div class="meta">{row[3] or ""} &bull; {row[6]} corpus documents</div>
<p>{sig}</p>
<div>{trad_html}</div>
</div>\n"""
    content += "</div>\n"

    content += "<h3>Modern Scholars</h3>\n<div class='card-grid'>\n"
    for row in conn.execute("""
        SELECT f.name, f.birth_year, f.death_year, f.nationality, f.significance,
               (SELECT COUNT(*) FROM document_figures df WHERE df.figure_id = f.id) as doc_count
        FROM figures f WHERE f.figure_type='SCHOLAR' ORDER BY f.name
    """):
        dates = f"({row[1]}–{row[2]})" if row[1] else ""
        sig = (row[4] or "")[:250]
        content += f'<div class="card"><h3>{row[0]} {dates}</h3><div class="meta">{row[3] or ""} &bull; {row[5]} corpus documents</div><p>{sig}</p></div>\n'
    content += "</div>"
    return page("Figures", content)


def build_timeline(conn):
    content = "<h2>Timeline</h2>\n"
    events = conn.execute("SELECT year, year_end, event_type, title, description FROM timeline_events ORDER BY year").fetchall()
    for e in events:
        yr = str(e[0]) + (f"–{e[1]}" if e[1] else "")
        desc = f'<div class="desc">{e[4]}</div>' if e[4] else ""
        content += f'<div class="timeline-event"><div class="year">{yr}</div><div class="title">{e[3]}</div><div class="meta"><span class="tag">{e[2]}</span></div>{desc}</div>\n'
    return page("Timeline", content)


def build_library(conn):
    content = "<h2>Library of Primary Sources</h2>\n" + DISCLOSURE + "\n"
    content += "<p>Referenced primary texts from ancient, medieval, and Renaissance traditions.</p>\n"

    eras = ["ANCIENT", "MEDIEVAL", "RENAISSANCE", "EARLY_MODERN"]
    for era in eras:
        texts = conn.execute("""
            SELECT t.title, t.title_latin, t.era, t.tradition, t.language, t.date_composed, t.significance,
                   f.name as author_name
            FROM texts t LEFT JOIN figures f ON t.author_figure_id = f.id
            WHERE t.era = ? ORDER BY t.title
        """, (era,)).fetchall()
        if not texts:
            continue
        content += f"<h3>{era.replace('_',' ').title()}</h3>\n"
        for t in texts:
            author = t[7] or "Anonymous"
            trad_class = (t[3] or "").lower().split()[0]
            sig = f"<p>{t[6]}</p>" if t[6] else ""
            content += f"""<div class="card">
<h3><em>{t[0]}</em></h3>
<div class="meta">{author} &bull; {t[5] or ""} &bull; {t[4] or ""} <span class="tag {trad_class}">{t[3] or ""}</span></div>
{sig}
</div>\n"""

    return page("Library", content)


def build_catalog(conn):
    content = "<h2>Corpus Catalog</h2>\n"
    content += '<input type="text" class="search-box" id="catSearch" placeholder="Search documents..." onkeyup="filterCat()">\n'

    content += "<table><thead><tr><th>Title</th><th>Type</th><th>Figure</th><th>Lang</th></tr></thead><tbody>\n"
    for row in conn.execute("""
        SELECT title, doc_type, folder_figure, language
        FROM documents ORDER BY folder_figure, title
    """):
        title = (row[0] or "")[:80]
        content += f'<tr class="cat-row"><td>{title}</td><td><span class="badge">{row[1] or "?"}</span></td><td>{row[2] or ""}</td><td>{row[3] or ""}</td></tr>\n'
    content += "</tbody></table>\n"

    content += """
<script>
function filterCat() {
    const q = document.getElementById('catSearch').value.toLowerCase();
    document.querySelectorAll('.cat-row').forEach(el => {
        el.style.display = el.textContent.toLowerCase().includes(q) ? '' : 'none';
    });
}
</script>"""
    return page("Catalog", content)


def build_about(conn):
    content = """
<h2>About RenMagDB</h2>

<h3>What This Is</h3>
<p>RenMagDB is a digital humanities project cataloging a research corpus of 337 scholarly documents on Renaissance magic. The database indexes figures, texts, terms, traditions, and events across the intellectual world of Renaissance magical philosophy — from Marsilio Ficino's translations of the <em>Corpus Hermeticum</em> to John Dee's Enochian angel conversations.</p>

<h3>A Note on "Magic"</h3>
<p>"Renaissance magic" is a modern scholarly category, not a term most Renaissance figures would have used to describe their own work. Ficino called his project <em>prisca theologia</em> (ancient theology); Agrippa titled his synthesis <em>philosophia occulta</em> (occult philosophy); Dee described his angel conversations as divine revelation. The word <em>magia</em> was more often applied by opponents — Church authorities, rival scholars, inquisitors — to delegitimize intellectual work. We use the term as a scholarly convenience while acknowledging its constructed nature.</p>
<p>For more on this framing, see the project essay "Magic as a Scholarly Category: From Yates to Copenhaver" in the project repository.</p>

<h3>Methodology</h3>
<p>The database was built using a Python-first pipeline: documents were converted to markdown via PyMuPDF, metadata was extracted via regex and spaCy NER, terms were detected via a 200-term seed list, and topic clusters were generated via TF-IDF. AI-generated content (dictionary definitions, summaries) is tagged with <code>source_method='LLM_ASSISTED'</code> and marked as DRAFT pending human review.</p>

<h3>Coverage Gaps</h3>
<ul>
<li><strong>Arabic/Islamic transmission</strong> — Only one dedicated source (Liana Saif) for the entire Arabic pipeline</li>
<li><strong>Paracelsus</strong> — Referenced frequently but no dedicated corpus documents</li>
<li><strong>Women practitioners</strong> — Limited dedicated scholarship in this corpus</li>
<li><strong>Operative alchemy</strong> — Corpus treats alchemy philosophically; see the companion AlchemyDB for practical terms</li>
</ul>

<h3>Technology</h3>
<p>SQLite database + Python scripts + static HTML. No frameworks, no JavaScript frameworks, no build tools. Deployed via GitHub Pages.</p>
"""
    return page("About", content)


def main():
    SITE_DIR.mkdir(exist_ok=True)
    conn = sqlite3.connect(str(DB_PATH))

    pages = {
        "index.html": build_index(conn),
        "dictionary.html": build_dictionary(conn),
        "figures.html": build_figures(conn),
        "timeline.html": build_timeline(conn),
        "library.html": build_library(conn),
        "catalog.html": build_catalog(conn),
        "about.html": build_about(conn),
    }

    for filename, html in pages.items():
        (SITE_DIR / filename).write_text(html, encoding="utf-8")
        print(f"  Built: {filename}")

    conn.close()
    print(f"\nSite built: {len(pages)} pages in {SITE_DIR}")


if __name__ == "__main__":
    main()
