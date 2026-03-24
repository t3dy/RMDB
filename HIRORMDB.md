# HIRORMDB.md — HiroPlantagenet Decomposition Report
## Renaissance Magic Database Project

**Date:** 2026-03-23
**Analyst:** Claude (hiro-plantagenet)
**Source prompt:** User's multi-objective request covering document conversion, database design, website content, and infrastructure planning.

---

## 1. Intent Atoms

| # | Goal | Tag |
|---|------|-----|
| A1 | Convert 321 PDFs to .md via PyMuPDF | EXTRACTION |
| A2 | Convert 10 EPUBs to .md via ebooklib+BS4 | EXTRACTION |
| A3 | Convert 9 HTML files to .md via html2text | EXTRACTION |
| A4 | Extract metadata from filenames (author, year, journal, DOI) via regex | EXTRACTION |
| A5 | Extract PDF internal metadata (title, author, page count, TOC) via PyMuPDF | EXTRACTION |
| A6 | Detect duplicates across corpus (cross-format pairs, same work diff editions) | DEDUP |
| A7 | Detect language per document | CLASSIFICATION |
| A8 | Design SQLite schema (documents, figures, texts, traditions, dictionary, timeline) | ONTOLOGY |
| A9 | Design provenance model (source_method, review_status, confidence) | ONTOLOGY |
| A10 | Build catalog of all 358 files with deterministic metadata | PIPELINE |
| A11 | Generate brief summaries per document | EXTRACTION (LLM) |
| A12 | Classify document types (monograph, article, chapter, primary source, review) | CLASSIFICATION |
| A13 | Tag documents by topic/tradition (Hermetic, Kabbalistic, Neoplatonic, etc.) | CLASSIFICATION |
| A14 | Score document relevance (PRIMARY/DIRECT/CONTEXTUAL) | CLASSIFICATION |
| A15 | Extract Latin/Greek terms from corpus via regex + dictionary | EXTRACTION |
| A16 | NER pass for person names, places, dates via spaCy | EXTRACTION |
| A17 | Build dictionary (800-1500 terms with Latin + English + definitions) | UI-SURFACING |
| A18 | Build figure biographies (~30 key figures) | UI-SURFACING |
| A19 | Build timeline (events from extracted dates + editorial additions) | UI-SURFACING |
| A20 | Build library catalog (ancient, medieval, renaissance primary sources) | UI-SURFACING |
| A21 | Design writing templates for website content types | META-CONTROL |
| A22 | Build static site generator (Jinja2 templates, SQLite queries) | PIPELINE |
| A23 | Design folder structure, CLAUDE.md, init files, environment | META-CONTROL |
| A24 | Design Claude skill set for the project | META-CONTROL |
| A25 | Provide token cost tiers (minimal/standard/comprehensive) | META-CONTROL |
| A26 | Build cross-reference/influence network (figures, texts, traditions) | ONTOLOGY |
| A27 | FTS5 full-text search index | PIPELINE |

---

## 2. Conflicts & Gaps

### CONFLICTS

**CONFLICT 1: Conversion scope vs. database scope.**
The prompt asks to "convert all documents to .md" AND "build a database." These are separate pipelines with different outputs. The .md files are both standalone deliverables for human reading AND inputs to the database pipeline.
**Resolution:** Layer 1 produces .md files. Layer 3 reads .md files + metadata to populate the database. Clean separation.

**CONFLICT 2: "Ingest as much information as possible" vs. token budget realism.**
Comprehensive entity extraction across 321 PDFs (~30-50M tokens of raw text) is infeasible for LLM processing in any single pass.
**Resolution:** Deterministic extraction (Python) maximizes data capture at zero LLM cost. LLM is reserved only for judgment tasks (summaries, classification, definitions).

**CONFLICT 3: Dictionary "800-1500 terms" vs. corpus reality.**
The actual count of extractable Latin terms depends on the seed list quality and corpus language distribution. Many documents may be in Italian, German, or French.
**Resolution:** Start with a curated seed list of ~300 known Renaissance magic terms, expand via corpus frequency analysis, then LLM-generate definitions for the final set.

**CONFLICT 4: "Library of texts" is ambiguous.**
Does "library" mean (a) a bibliography of the 358 files in the corpus, or (b) a catalog of primary sources REFERENCED BY those files (Corpus Hermeticum, Picatrix, De Occulta Philosophia, etc.)? The user says "ancient, medieval, renaissance sources" — which implies (b).
**Resolution:** Both. The corpus IS the bibliography. The referenced-works catalog is a separate entity extracted from the corpus. Two tables: `documents` (the 358 files) and `texts` (referenced primary sources).

**CONFLICT 5: Template design vs. template execution.**
Templates for website content depend on schema design; schema depends on entity model; entity model depends on corpus analysis.
**Resolution:** Schema design in Layer 2, template design finalized before Layer 5 (content generation). Templates are part of infrastructure, not content.

### MISSING DECISIONS

1. **Project name** — What is this project called? Affects folder naming, DB filename, website title, GitHub repo name. (e.g., "RenMagDB", "ArsMagica", "RenaissanceMagicDB", user's choice)
2. **Website voice/register** — Museum-curator scholarly? Accessible-educational? Encyclopedia-neutral? Affects all writing templates.
3. **Figure scope** — Are modern scholars (Yates, Copenhaver, Walker) "figures" in the database alongside historical subjects (Dee, Ficino, Pico)? Or only historical?
4. **Tradition taxonomy** — What traditions count? Hermeticism, Kabbalah, Neoplatonism, Alchemy, Astrology, Demonology, Natural Philosophy, Theurgy — how granular?
5. **Era boundaries** — Where does "Medieval" end and "Renaissance" begin? (1350? 1400? 1450?) Where does "Renaissance" end? (1600? 1650? 1700?)
6. **Primary source scope** — Only texts directly about magic? Or also foundational philosophical texts (Plato's Timaeus, Aristotle's De Anima) that Renaissance magicians drew on?
7. **Skill needs** — Which Claude skills should be project-specific vs. reuse existing PKD skills?

### IMPLICIT ASSUMPTIONS

- All PDFs contain extractable text (not all scanned-only). Reality: some older scans may yield garbage.
- The 15 folder names map cleanly to historical figures. Reality: "Bruno Lull" is two figures; "Christian Cabalah" is a tradition, not a figure; "Vittoria Perrone Compagni" is a modern scholar.
- English is the primary language. Reality: significant Latin, Italian, German, and French content in the corpus.
- The user will do multiple Claude Code sessions for the LLM-heavy layers.

---

## 3. Layer Architecture

```
LAYER 0: INFRASTRUCTURE        Atoms: A23, A24, A25
  Purpose: Create project scaffold, config, docs, environment
  Reasoning mode: deterministic
  LLM tokens: zero (beyond Claude Code session)
  Depends on: nothing

LAYER 1: DOCUMENT CONVERSION   Atoms: A1, A2, A3
  Purpose: Convert all 358 corpus files to markdown
  Reasoning mode: deterministic (Python scripting)
  LLM tokens: zero
  Depends on: Layer 0

LAYER 2: SCHEMA + SCAFFOLD     Atoms: A8, A9, A26
  Purpose: Design and create SQLite schema, init scripts, migration framework
  Reasoning mode: deterministic
  LLM tokens: zero
  Depends on: Layer 0

LAYER 3: DETERMINISTIC DATA    Atoms: A4, A5, A6, A7, A10, A15, A16
  Purpose: Populate DB with all Python-extractable data
  Reasoning mode: deterministic (regex, NER, fuzzy match)
  LLM tokens: zero
  Depends on: Layers 1, 2

LAYER 4: HYBRID ENRICHMENT     Atoms: A11, A12, A13, A14
  Purpose: LLM-assisted classification, tagging, summarization
  Reasoning mode: classificatory + analytical
  LLM tokens: 460K-1M (tier-dependent)
  Depends on: Layer 3

LAYER 5: CONTENT GENERATION    Atoms: A17, A18, A19, A20, A21
  Purpose: Generate dictionary, biographies, timeline, library entries
  Reasoning mode: generative
  LLM tokens: 280K-1.7M (tier-dependent)
  Depends on: Layer 4

LAYER 6: SITE BUILD            Atoms: A22, A27
  Purpose: Static site generation, search index, validation
  Reasoning mode: deterministic (Jinja2 + SQLite)
  LLM tokens: zero
  Depends on: Layer 5
```

**Parallelism:** Layers 1 and 2 can run in parallel (no dependencies between them). All other layers are sequential.

---

## 4. Rewritten Prompts (Per Layer)

### === LAYER 0: INFRASTRUCTURE SETUP ===

**OBJECTIVE:** Create the project scaffold: folder structure, configuration files, Python environment, Claude operational documents, and Claude skill definitions.

**SCOPE CONSTRAINTS:**
- DO: Create directories, config files, documentation templates, requirements.txt, .gitignore, CLAUDE.md
- DO NOT: Write any data-processing scripts. No database creation. No document conversion.

**INPUTS:**
- `C:/Dev/Claudiens/` as reference architecture
- `C:/Dev/renaissance magic/DECKARDRMDB.md` for library inventory
- `C:/Dev/renaissance magic/HIRORMDB.md` (this document) for layer architecture

**OUTPUT CONTRACT:**
```
C:\Dev\renaissance magic\
├── CLAUDE.md                       # Project entry point + operating rules
├── DOCUMENTAIRTRAFFICCONTROL.md    # Which doc to read for which task
├── PHASESTATUS.md                  # Session log + current blockers
├── DECKARDRMDB.md                  # [existing] Boundary analysis
├── HIRORMDB.md                     # [existing] Layer decomposition
├── requirements.txt                # All Python dependencies
├── .gitignore                      # db/, site/, __pycache__, etc.
├── .claude/
│   ├── settings.local.json         # Permission whitelist
│   └── launch.json                 # Preview server config
├── docs/
│   ├── SYSTEM.md                   # Architecture + data flow + provenance model
│   ├── ONTOLOGY.md                 # Full schema catalog
│   ├── PIPELINE.md                 # Script execution order (all 6 layers)
│   ├── INTERFACE.md                # Website sections + page templates
│   ├── ROADMAP.md                  # Phase tracking (PLANNED/READY/BUILT)
│   ├── WRITING_TEMPLATES.md        # Voice rules per content type
│   └── SWARMGUIDELINES.md          # Multi-agent operation patterns
├── scripts/                        # Python scripts (populated per layer)
├── db/                             # SQLite database (generated)
├── staging/                        # Swarm agent output staging
├── md/                             # Markdown conversion output
│   ├── Agrippa/
│   ├── Bruno Lull/
│   ├── Dee/
│   ├── Ficino/
│   ├── Pico/
│   └── ... (mirrors corpus structure)
├── site/                           # Static site output
├── data/                           # Seed data, manifests, JSON artifacts
│   ├── conversion_manifest.json
│   ├── term_seed_list.json
│   └── figure_seed_list.json
└── templates/                      # Jinja2 templates for site generation
```

**DECISION RULES:**
- CLAUDE.md must reference both DECKARDRMDB.md and HIRORMDB.md
- CLAUDE.md must include behavioral triggers from the PKD planning protocol
- `md/` mirrors corpus folder structure exactly (preserves provenance)
- `requirements.txt` includes: PyMuPDF, pdfminer.six, pypdf, beautifulsoup4, html2text, ebooklib, spacy, rapidfuzz, networkx, Jinja2, python-slugify, langdetect, markdown

---

### === LAYER 1: DOCUMENT CONVERSION ===

**OBJECTIVE:** Convert all 358 corpus files to markdown via Python scripting. Pure format conversion — no metadata extraction, no database writes.

**SCOPE CONSTRAINTS:**
- DO: PDF→md, EPUB→md, HTML→md, CHM→md. Log conversion quality.
- DO NOT: Extract metadata, classify documents, or touch the database.

**INPUTS:**
- `C:/Dev/renaissance magic/` (all 358 source files)
- Libraries: PyMuPDF, ebooklib, BeautifulSoup4, html2text

**OUTPUT CONTRACT:**
- `md/` directory: one .md file per source file, mirroring folder structure
- `data/conversion_manifest.json`: array of objects:
  ```json
  {
    "source_path": "string",
    "md_path": "string",
    "format": "PDF|EPUB|HTML|CHM",
    "pages": "int",
    "chars": "int",
    "quality_score": "float (0-1, ratio of non-empty pages)",
    "quality_flag": "GOOD|PARTIAL|SCANNED|EMPTY",
    "timestamp": "ISO8601"
  }
  ```
- Scripts: `scripts/convert_pdf.py`, `scripts/convert_epub.py`, `scripts/convert_html.py`, `scripts/convert_all.py` (orchestrator)
- All scripts idempotent (skip if .md exists and source file unchanged)

**DECISION RULES:**
- PDF heading detection: font size > 1.2x body average → heading. H1 for >1.5x, H2 for >1.2x.
- Quality flag thresholds: GOOD (>0.8), PARTIAL (0.3-0.8), SCANNED (<0.3), EMPTY (0 chars)
- EPUB: preserve internal heading hierarchy from XHTML chapter structure.
- Skip non-document files (GIF, JPG, CSS, .crdownload). Log skips.
- If PDF yields zero text: create .md with `<!-- SCANNED: OCR needed -->` header.

---

### === LAYER 2: SCHEMA DESIGN + DATABASE SCAFFOLD ===

**OBJECTIVE:** Design and create the SQLite schema. Create init_db.py with all DDL. Document in ONTOLOGY.md.

**SCOPE CONSTRAINTS:**
- DO: Define all tables, CHECK constraints, indexes, FTS5 virtual tables. Write init_db.py.
- DO NOT: Populate any data. That's Layer 3.

**INPUTS:**
- AtalantaClaudiens `scripts/init_db.py` and `docs/ONTOLOGY.md` as patterns
- DECKARDRMDB.md entity model
- This document's Layer 3 output contract (what data must be storable)

**OUTPUT CONTRACT:**

**Core entity tables:**

| Table | Purpose |
|-------|---------|
| `documents` | Every file in corpus (358 rows expected) |
| `figures` | Historical persons AND modern scholars |
| `texts` | Primary sources referenced in scholarship |
| `traditions` | Intellectual movements/schools |
| `dictionary_terms` | Latin/Greek/Hebrew/Arabic terms |
| `timeline_events` | Historical events and milestones |

**Join/relationship tables:**

| Table | Relationship |
|-------|-------------|
| `document_figures` | document ↔ figure (many-to-many) |
| `document_texts` | document ↔ referenced text |
| `document_topics` | document ↔ topic tag |
| `figure_traditions` | figure ↔ tradition |
| `figure_influences` | figure → figure (directed, with influence_type) |
| `figure_texts` | figure ↔ text (authored/translated/commented) |
| `text_traditions` | text ↔ tradition |
| `term_documents` | term occurrence in document |
| `term_figures` | term associated with figure |
| `term_links` | term ↔ term cross-reference |
| `event_figures` | event ↔ figure |
| `event_texts` | event ↔ text |

**Controlled vocabulary tables:**

| Table | Values |
|-------|--------|
| `topics` | Controlled tag vocabulary |
| `eras` | ANCIENT, MEDIEVAL, RENAISSANCE, EARLY_MODERN, ENLIGHTENMENT |
| `schema_version` | Migration tracking |
| `provenance_log` | Audit trail |

**Every content table includes:** `source_method`, `review_status`, `confidence`, `created_at`, `updated_at`

**DECISION RULES:**
- `documents` = the corpus (physical files). `texts` = referenced primary sources (intellectual works). Distinct entities.
- `figures.figure_type`: HISTORICAL or SCHOLAR. Both are first-class.
- All ENUM values enforced via CHECK constraints.
- FTS5 on: `documents(title, summary)`, `dictionary_terms(term, definition_long)`, `figures(name, biography)`.
- Schema starts at version 1. Migrations are additive only.
- Database filename: `db/renmagic.db` (or project-name-dependent).

---

### === LAYER 3: DETERMINISTIC DATA POPULATION ===

**OBJECTIVE:** Populate the database with all data extractable by Python without LLM assistance.

**SCOPE CONSTRAINTS:**
- DO: Filename parsing, PDF metadata extraction, folder mapping, duplicate detection, language detection, Latin term extraction, NER.
- DO NOT: Summarize, classify by judgment, or generate prose. Those are Layer 4+5.

**INPUTS:**
- `data/conversion_manifest.json` (Layer 1)
- `md/` directory (Layer 1)
- `db/renmagic.db` schema (Layer 2)

**OUTPUT CONTRACT:**
- `documents`: 358 rows, deterministic fields populated (path, title_from_filename, author_from_filename, year, format, pages, chars, quality_flag, folder_figure, language)
- `figures`: ~30 rows seeded from folder names + top NER person entities
- `dictionary_terms`: seeded with regex-matched Latin/Greek terms (term + frequency + source document)
- `data/duplicates.json`: flagged pairs for review
- `data/ner_report.json`: top entities per document
- `data/term_frequency.json`: term occurrence matrix
- All records: `source_method='DETERMINISTIC'`, `confidence='HIGH'`

**DECISION RULES:**
- Filename regex priority order: DOI → journal/vol/issue → author → year → publisher
- HTML entity decoding on filenames before parsing
- Duplicate threshold: rapidfuzz ratio > 85 on normalized titles
- spaCy NER: first 5000 chars per .md file, top 20 entities stored
- Latin term seed: ~300 curated terms. Match case-insensitive in corpus.
- Folder mapping hardcoded for 15 directories (handle "Bruno Lull" → two figures, "Christian Cabalah" → tradition not figure)

---

### === LAYER 4: HYBRID ENRICHMENT ===

**OBJECTIVE:** LLM-assisted classification, tagging, summarization, and relevance scoring.

**SCOPE CONSTRAINTS:**
- DO: Document type classification, topic tagging, summaries, relevance scoring.
- DO NOT: Generate website content (dictionary definitions, biographies, essays). That's Layer 5.

**INPUTS:**
- First 3 pages of each .md file
- `db/renmagic.db` (Layer 3 data)

**OUTPUT CONTRACT:**
- `documents.doc_type`: MONOGRAPH | ARTICLE | CHAPTER | REVIEW | PRIMARY_SOURCE | ANTHOLOGY | DISSERTATION
- `documents.summary`: 1-3 sentences, ≤500 chars, must contain author surname
- `document_topics`: tags from controlled `topics` vocabulary
- `documents.relevance`: PRIMARY | DIRECT | CONTEXTUAL
- All: `source_method='LLM_ASSISTED'`, `confidence='MEDIUM'`, `review_status='DRAFT'`

**TOKEN COST TIERS:**

| Tier | What you get | ~Tokens |
|------|-------------|---------|
| MINIMAL | doc_type classification only, no summaries | ~180K |
| STANDARD | doc_type + summaries for top 100 + topic tags | ~450K |
| COMPREHENSIVE | everything for all 321 documents | ~1M |

**DECISION RULES:**
- Process folder-named figures first (highest relevance likelihood)
- Reject any classification not in ENUM list
- Summaries validated: non-empty, ≤500 chars, contains author surname
- Failed validations: re-prompt once, then log as LOW confidence

---

### === LAYER 5: CONTENT GENERATION ===

**OBJECTIVE:** Generate website content: dictionary definitions, figure biographies, timeline descriptions, library catalog entries.

**SCOPE CONSTRAINTS:**
- DO: Write definitions, biographies, descriptions, catalog entries. Apply writing templates.
- DO NOT: Build the site. That's Layer 6.

**INPUTS:**
- `md/` files (relevant passages)
- `db/renmagic.db` (Layers 3+4 data)
- `docs/WRITING_TEMPLATES.md` (voice rules)

**OUTPUT CONTRACT:**

| Content Type | Count | Fields |
|-------------|-------|--------|
| Dictionary terms | 300-1500 | definition_brief (≤100ch), definition_long (3-5 sent), domain |
| Figure biographies | ~30 | biography (2-4 para), significance (1-2 sent) |
| Timeline events | 50-200 | description (2-3 sent), sourced from NER + editorial |
| Library entries | 50-100 | significance, tradition, era |

**TOKEN COST TIERS:**

| Tier | Scope | ~Tokens |
|------|-------|---------|
| MINIMAL | 300 terms (brief only) + 15 bios + 50 events | ~280K |
| STANDARD | 800 terms (brief+long) + 30 bios + 100 events + 50 library | ~850K |
| COMPREHENSIVE | 1500 terms (all fields) + 30 bios + 200 events + 100 library + 10 essays | ~1.7M |

**DECISION RULES:**
- Writing templates MUST be finalized before any generation script runs
- All definitions must contain the term. All biographies must contain the figure's name.
- AI disclosure on all generated content
- All: `source_method='LLM_ASSISTED'`, `review_status='DRAFT'`

---

### === LAYER 6: SITE BUILD + VALIDATION ===

**OBJECTIVE:** Generate the static website from SQLite. Validate data integrity. Zero LLM tokens.

**SCOPE CONSTRAINTS:**
- DO: Jinja2 templating, HTML/CSS/JS generation, search index, validation reports.
- DO NOT: Generate any content. All content comes from the database.

**INPUTS:**
- `db/renmagic.db` (fully populated)
- `templates/` (Jinja2 templates)

**OUTPUT CONTRACT:**
- `site/` directory with: index, dictionary, timeline, figures, library, catalog, about, search pages
- `site/data/search.json` (client-side search index)
- Validation report: orphans, missing fields, provenance coverage %
- All pages cross-linked: terms → figures → texts → timeline events

**DECISION RULES:**
- Vanilla HTML/CSS/JS only, GitHub Pages compatible
- AI-generated content carries disclosure badge
- Build script idempotent: wipe `site/` and regenerate
- Warm parchment CSS palette (or user-specified)

---

## 5. Execution Notes

### Token Cost Summary (Combined Layers 4+5)

| Tier | Layer 4 | Layer 5 | TOTAL | Sessions Est. |
|------|---------|---------|-------|---------------|
| MINIMAL | ~180K | ~280K | **~460K** | 1-2 |
| STANDARD | ~450K | ~850K | **~1.3M** | 3-5 |
| COMPREHENSIVE | ~1M | ~1.7M | **~2.7M** | 6-10 |

**Layers 0-3 and 6: ZERO LLM tokens** (beyond Claude Code writing the scripts).

### Parallelism
- Layers 1 and 2 are independent — can run in parallel
- Everything else is sequential

### Human Review Recommended
- After Layer 1: check `data/conversion_manifest.json` for SCANNED/EMPTY flags
- After Layer 3: review `data/duplicates.json`, spot-check NER results
- After Layer 4: review DRAFT summaries and classifications (sample 20-30)
- After Layer 5: review dictionary definitions and biographies before site build

### Caching / Versioning
- Layer 2 schema: version-tracked, rarely changes after initial design
- Layer 1 conversion: idempotent, cached by file modification time
- Layer 3 deterministic data: re-runnable, idempotent
- Layers 4+5 LLM outputs: expensive to regenerate — version the DB after each layer

### Risk Register
1. **OCR quality** — scanned-only PDFs yield empty text. Mitigation: quality flag + optional Tesseract fallback.
2. **Filename parsing edge cases** — HTML entities, multi-author works. Mitigation: log parse failures.
3. **spaCy NER noise** — "Renaissance" detected as location, etc. Mitigation: stop-list filter.
4. **Dictionary scale uncertainty** — corpus may yield fewer than 800 unique Latin terms. Mitigation: assess after Layer 3 before committing to a tier.
5. **Cross-format dedup** — title matching unreliable across PDF/EPUB. Mitigation: combine title + author + page count similarity.

---

*Generated by hiro-plantagenet for the Renaissance Magic Database Project.*
