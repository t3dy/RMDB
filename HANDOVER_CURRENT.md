# RenMagDB — Handover (2026-06-14)

## TL;DR

The site is **live**: **https://t3dy.github.io/RMDB/**
It deploys automatically via GitHub Actions on every push that touches `website/**`.
20 figure essays + 10 tradition essays + a primary-texts catalog are written, committed, and deployed. The database has been partially remediated. The biggest remaining gaps are the **dictionary section** (data exists, pages not built), **~8 more figure essays**, and **reading the actual primary sources** (we've read scholarship, not sources).

---

## What is DONE and verified

### Live website (Hugo → GitHub Pages)
- **URL:** https://t3dy.github.io/RMDB/ — verified 200 on home, `/figures/`, `/traditions/`, `/texts/`, and individual pages.
- **Repo:** https://github.com/t3dy/RMDB (`main`)
- **Generator:** Hugo extended **0.163.1**. Site source lives in `website/`. Theme: `renmagdb-theme` (in-repo).
- **Deploy mechanism:** `.github/workflows/hugo.yml` — installs hugo-extended, builds from `./website`, deploys via `actions/deploy-pages`. Pages `build_type` = **workflow** (NOT a branch source).
- **184 pages** built (home, 20 figures, 10 traditions, texts page, taxonomies).

### Content
- **20 figure essays** (`website/content/figures/01–20`), 5,000–5,400 words each, all with actor/analyst-terminology framing:
  Ficino, Dee, Pico, Agrippa, Bruno, Paracelsus, Trithemius, Albertus Magnus, Fludd, Böhme, Aquinas, Plotinus, Porphyry, Roger Bacon, Della Porta, Avicenna, Iamblichus, Al-Kindi, Reginald Scot, Johann Weyer.
- **10 tradition essays** (`website/content/traditions/01–10`), 2,200–3,500 words:
  Hermeticism, Neoplatonism, Kabbalah, Alchemy, Astrology, Demonology, Islamic Magic, Theurgy, Rosicrucianism, Witchcraft.
- **Primary-texts catalog**: `TEXTS_CATALOG.md` (full, internal) + `website/content/texts.md` (reader-facing `/texts/` page). Marks READ vs IN-DB-UNREAD vs GAP; web-researched sourcing leads for every major edition.

### Figure/text selection is evidence-based
Driven by `scripts/extended_corpus_reader.py` over 35 scholarship PDFs. Every figure mentioned in ≥3 documents now has an essay. Results in `extended_corpus_analysis.json`.

### Database remediation (partial)
`scripts/remediate_figures_texts.py` (idempotent) already ran:
- Inserted 6 missing figures: Aquinas, Porphyry, Della Porta, Avicenna, Scot, Weyer → **28 HISTORICAL figures**.
- Relinked orphaned texts: *Opus Majus*→Roger Bacon, *De Docta Ignorantia*→Cusanus.

### Cleanup
- Removed the stale March-era hand-built site in `docs/` that was shadowing the Hugo build at the Pages root. (This was the cause of an initial "live site shows old content" bug — see Gotchas.)

---

## Repo / environment facts (important)

- **Working dir:** `C:\Dev\renaissance magic`
- **Database:** `db/renmagic.db` — **161 MB, NOT in git** (over GitHub's 100 MB limit). It lives only on this machine. Do not `git add` it. Back it up separately.
- **Corpus PDFs/EPUBs:** hundreds of files in the repo root and subfolders — **untracked by design**. Don't commit them.
- **Hugo binary:** installed at `C:\Users\PC\AppData\Local\hugo\hugo.exe` (not on PATH for new shells; call by full path or re-add).
- **Local preview:** `python serve.py` serves `website/public` (auto-port via `PORT` env); or use the Claude preview server config in `.claude/launch.json` (name `renmagdb-preview`).
- **Build locally:** `cd website && "C:\Users\PC\AppData\Local\hugo\hugo.exe" --cleanDestinationDir`
- **DB tables of note:** `figures` (35 rows: 28 historical + 7 scholars), `texts` (36), `figure_texts`, `dictionary_terms` (186), `timeline_events`, `documents` + FTS. Provenance columns everywhere: `source_method`, `review_status`, `confidence`.

---

## Remaining work (prioritized)

### 1. Build the Dictionary section (HIGH — data already exists)
`data/definitions.json` (113 KB) and `dictionary_terms` (186 terms) exist, but `/dictionary/` has **no pages**. Generate `website/content/dictionary/*.md` from the DB/JSON. The nav link already points to `/dictionary/`. Per the project goal, expand brief defs to 500–1,200-word essays with actor/analyst framing.

### 2. Create the empty nav sections (QUICK)
Nav links exist for **/essays/** and **/about/** but have no content → likely 404. Add `website/content/about.md` and an essays landing page (or remove the menu items).

### 3. ~8 more figure essays (MEDIUM)
Figures in the DB / referenced but without essays: **Reuchlin, Plato, Proclus, Ramon Llull, Nicholas of Cusa, Athanasius Kircher, Francis Mercury van Helmont, Hermes Trismegistus**. Confirm priority against `extended_corpus_analysis.json` before writing.

### 4. Finish DB remediation from `TEXTS_CATALOG.md` Part 6 (MEDIUM)
- Add the GAP texts to `texts` (tag `LLM_ASSISTED`/`DRAFT`/`MEDIUM`, put sourcing lead in `reception_history`).
- Relink corpus copies we already hold: Pico *Oration* & *900 Theses* PDFs in `Pico/` → set `corpus_document_id`.
- Populate `figures.key_works` (empty for every figure).

### 5. Source & ingest actual primary texts (DEEP — the real scholarly gap)
We've read **secondary scholarship**, not primary sources. `TEXTS_CATALOG.md` Part 5 has a free-download shortlist (Dee *Five Books*, Weyer, Della Porta, Scot — all on archive.org) and a purchase list (Ficino *Platonic Theology*, Bruno Cambridge, Paracelsus/Weeks, Picatrix, Iamblichus). Untranslated flags: Al-Kindi *De Radiis*, Fludd *Utriusque Cosmi*, Pico *Disputationes*.

### 6. Finish systematic reading (DEEP)
`reading_tracker` / `reading_tracker.json`: ~35 of 42 docs analyzed by script (keyword-level, not close-read). 7 remain; deeper close-reading is the long tail.

---

## Gotchas / lessons

- **The `docs/` trap (fixed):** Pages had been serving a stale hand-built site from `main:/docs`. We removed it and switched Pages to **workflow** build_type. If the live site ever shows old content again, check `gh api repos/t3dy/RMDB/pages` — `build_type` must be `workflow`, and there must be no `docs/` site.
- **CDN lag:** after a deploy, new pages can 404 for ~30–60s while the Pages CDN swaps. Poll, don't panic.
- **CRLF warnings** on every `git add` of `website/public` are harmless (LF→CRLF notices on Windows).
- **PowerShell:** no `&&`; use `;`. The Hugo binary isn't on PATH — full path required.
- **Project rules (CLAUDE.md):** corpus is source of truth (no Wikipedia for content); "magic" is an analyst category (actor vs. analyst terms); all DB writes get provenance fields; scripts must be idempotent + UTF-8 wrapped.

---

## Quick commands

```powershell
# Build site
cd "C:\Dev\renaissance magic\website"; & "C:\Users\PC\AppData\Local\hugo\hugo.exe" --cleanDestinationDir

# Preview locally (from repo root)
python serve.py    # serves website/public

# Deploy = just push; Actions builds + deploys
git add website/ ; git commit -m "..." ; git push origin main

# Check deploy
gh run list --workflow=hugo.yml --limit 3
gh api repos/t3dy/RMDB/pages --jq '{build_type, html_url, status}'
```
