# Claude Code Instructions — RenMagDB

## Project Overview

RenMagDB is a SQLite database and future static website for Renaissance magic scholarship. It ingests a 358-file research corpus (PDFs, EPUBs, HTML) covering figures like Dee, Ficino, Pico, Agrippa, Bruno, Fludd, Trithemius, Reuchlin, Kircher, and Böhme.

**Architecture:** SQLite → Python scripts → static HTML → GitHub Pages (replicating AtalantaClaudiens pattern from `C:\Dev\Claudiens\`)

## Key Documents

### v1 Reports (foundation — still authoritative for architecture decisions)
| Document | Purpose |
|----------|---------|
| `DECKARDRMDB.md` | Deterministic vs LLM boundary map (v1) |
| `HIRORMDB.md` | Original 6-layer decomposition (v1) |
| `BUCKMANONTRMDB.md` | Ontology critique (10 schema fixes) |
| `PKDSKILLSRMDB.md` | 24-skill deployment map |
| `JOECHIPSCOPERMDB.md` | v1 scope freeze |
| `SLICESLICEBABYRMDB.md` | 4 vertical slices with acceptance gates |
| `AGILERMDB.md` | Agile framework |
| `LAMPTONRMDB.md` | Corpus analysis (entities, topics, relations, gaps) |
| `STEINERGATERMDB.md` | v1 gate verification (PASSED) |

### v2 Reports (current — supersede v1 where they overlap)
| Document | Purpose |
|----------|---------|
| `JOECHIPV2RMDB.md` | v2 scope freeze |
| `HIROV2RMDB.md` | v2 2-phase architecture (Phase A deterministic + Phase B LLM) |
| `DECKARDV2RMDB.md` | Boundary re-check — 7 shifts, 25% token savings |
| `BUCKMANV2RMDB.md` | 3 LLM prompts critiqued and revised (34-35/40) |
| `FATCOMPRESSRMDB.md` | 8 concept blocks for LLM prompt injection |
| `SWARMRMDB.md` | Swarm architecture — agents can't Bash, use staging/ protocol |
| `RMESSAY1.md` | Essay: "Magic" as scholarly category (Yates vs Copenhaver) |
| `GNOSISDICTIONARYSTYLEANALYSISTAKEAWAYS.md` | Style/schema revisions from Hanegraaff analysis |

### Living Documents
| Document | Purpose |
|----------|---------|
| `docs/WRITING_TEMPLATES.md` | 6 content templates, museum-curator voice |
| `docs/PIPELINE.md` | Script execution order |
| `agile/BOARD.md` | Current agile board state |

## Document Routing

- **Schema questions:** `docs/ONTOLOGY.md` + `BUCKMANONTRMDB.md`
- **Pipeline questions:** `docs/PIPELINE.md` + `DECKARDV2RMDB.md`
- **v2 scope questions:** `JOECHIPV2RMDB.md`
- **v2 architecture:** `HIROV2RMDB.md` (supersedes HIRORMDB.md)
- **v2 boundaries:** `DECKARDV2RMDB.md` (supersedes DECKARDRMDB.md)
- **LLM prompts:** `BUCKMANV2RMDB.md` (3 revised prompts for Phase B)
- **Writing voice:** `docs/WRITING_TEMPLATES.md`
- **Corpus analysis:** `LAMPTONRMDB.md`
- **Current work:** `agile/BOARD.md` + latest `agile/sprints/SPRINT-NN.md`
- **Blunders/lessons:** `agile/issues/BLUNDER*.md`

## Operating Rules

1. **Python-first.** Use Python libraries for everything deterministic. LLM only for judgment tasks.
2. **Provenance always.** Every DB row gets `source_method`, `review_status`, `confidence`.
3. **Idempotent scripts.** All scripts use `CREATE TABLE IF NOT EXISTS`, `INSERT OR IGNORE`, skip-if-exists logic.
4. **Corpus is the source of truth.** Do NOT go to Wikipedia, Wikidata, or external APIs for content the corpus contains. (BLUNDER3 lesson.)
5. **"Magic" is a scholarly category, not a neutral descriptor.** Follow RMESSAY1.md and GNOSISDICTIONARYSTYLEANALYSISTAKEAWAYS.md: distinguish actor terms from analyst terms, avoid reifying traditions as discrete boxes, present figures as complex actors not "magicians." (Copenhaver/Hanegraaff line.)
6. **Scope discipline.** v2 is frozen per `JOECHIPV2RMDB.md`. New ideas → `/plan-abendsen-parking`.
7. **Gate discipline.** Phase A must pass gate before Phase B begins.
8. **Agile tracking.** Create TICKET/ISSUE .md files as work proceeds. Log BLUNDER*.md on crashes/failures.
9. **UTF-8 encoding.** All Python scripts must include `sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')`. (BLUNDER2 lesson.)
10. **Swarm constraints.** Agents CANNOT run Bash/Python/SQL. Use staging/ protocol per SWARMRMDB.md. Main session handles all DB operations. (BLUNDER4 lesson.)

## Behavioral Triggers

- If building without scoping: suggest `/plan-joe-chip-scope`
- If adding unplanned features: suggest `/plan-abendsen-parking`
- If skipping a gate: flag with `GATE WARNING`
- If prompts getting long: suggest `/plan-isidore-tokens`
- If corpus analysis needed: suggest `/plan-lampton-corpus`

## Key Decisions

- **Project name:** RenMagDB
- **DB filename:** `db/renmagic.db`
- **Figures:** Unified table (HISTORICAL + SCHOLAR) with `figure_type`
- **Voice:** Museum-curator scholarly
- **Library scope:** Full intellectual genealogy (ancient → Islamic → patristic → Renaissance). Liana Saif's book is primary source for Islamic thread.
- **Eras:** Flexible/overlapping via `era_assignments` join table
- **Traditions:** 9 traditions derived from term domain aggregation (DECKARDV2RMDB shift)
- **v1 status:** COMPLETE. Gate passed (STEINERGATERMDB.md). 337 docs, 29 figures, 186 terms, 12 TF-IDF topics, FTS5 index.
- **v2 status:** Phase A COMPLETE. Phase B (LLM enrichment) ready to begin.
- **Current state:** 331/337 docs classified (98%), 105/337 with summaries, 58 timeline events, 32 primary texts, 9 tradition labels.

## Python Libraries

Core: PyMuPDF, pdfminer.six, pypdf, BeautifulSoup4, html2text, ebooklib
NLP: spaCy (en_core_web_sm), langdetect, rapidfuzz, scikit-learn
Data: sqlite3 (stdlib), networkx, Jinja2, python-slugify
API: wikipedia-api, requests
