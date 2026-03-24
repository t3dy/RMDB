# JOECHIPSCOPERMDB.md — Joe Chip Scope Freeze
## Renaissance Magic Database Project

**Date:** 2026-03-23
**Analyst:** Claude (plan-joe-chip-scope)
**Status:** SCOPE FROZEN

---

## Problem Decomposition

| # | Problem | Domain | Input | Output | Independent? | Depends on |
|---|---------|--------|-------|--------|-------------|------------|
| P1 | Convert 358 documents to markdown | Extraction | PDFs, EPUBs, HTML | `md/` directory tree + `conversion_manifest.json` | YES | Nothing |
| P2 | Design and create SQLite schema | Data modeling | Buckman critique, Hiro layers | `db/renmagic.db` with empty tables + `ONTOLOGY.md` | YES | Nothing |
| P3 | Extract deterministic metadata (filenames, PDF internals) | Extraction | 358 source files | `documents` table populated | NO | P1, P2 |
| P4 | Extract abstracts from .md files via regex | Extraction | `md/` files | `documents.summary` for ~70% of docs | NO | P1, P3 |
| P5 | Heuristic document type classification | Classification | Filenames, page counts, metadata | `documents.doc_type` for ~80% of docs | NO | P3 |
| P6 | Detect duplicates across corpus | Dedup | Document metadata | `data/duplicates.json` | NO | P3 |
| P7 | Detect language per document | Classification | `md/` files | `documents.language` | NO | P1, P3 |
| P8 | Extract Latin/Greek terms via regex + seed list | Extraction | `md/` files + seed list | `dictionary_terms` seeded + `data/kwic_concordance.json` | NO | P1, P2 |
| P9 | NER pass (persons, places, dates) via spaCy | Extraction | `md/` files | `data/ner_report.json` + `figures` seeded | NO | P1, P2 |
| P10 | TF-IDF topic clustering | Classification | `md/` files | `data/topic_clusters.json` + `topics` seeded | NO | P1, P2 |
| P11 | Seed figures from folder names + Wikidata API | Data assembly | Folder structure + Wikidata | `figures` table with bio facts | NO | P2 |
| P12 | Build project infrastructure (CLAUDE.md, docs, skills) | Scaffolding | All reports | Project skeleton | YES | Nothing |
| P13 | LLM classification of ambiguous documents | LLM enrichment | ~65 ambiguous docs | `doc_type`, `summary`, `topics` for remainder | NO | P3, P4, P5 |
| P14 | LLM dictionary definitions | LLM content gen | KWIC concordance + term list | `definition_brief`, `definition_long` for 800+ terms | NO | P8 |
| P15 | LLM figure biographies | LLM content gen | Wikidata + corpus refs | `biography`, `significance` for ~30 figures | NO | P9, P11 |
| P16 | LLM timeline event descriptions | LLM content gen | NER dates + Wikidata dates | `timeline_events` populated | NO | P9 |
| P17 | LLM library catalog (referenced primary sources) | LLM content gen | NER titles + corpus analysis | `texts` table populated with significance | NO | P9, P1 |
| P18 | Build static site generator | Frontend | All DB data + Jinja2 templates | `site/` directory | NO | P2 + some content |
| P19 | Cross-reference/influence network | Data modeling | Corpus analysis | `figure_influences`, `figure_texts`, etc. | NO | P9, P11 |
| P20 | Full-text search (FTS5) | Search | `md/` files + DB | `documents_fts` virtual table | NO | P1, P2 |
| P21 | Design writing templates | Content design | Voice decisions | `docs/WRITING_TEMPLATES.md` | YES | Nothing |
| P22 | Create 3 project-specific Claude skills | Tooling | Skill designs | `.claude/skills/renmagdb-*` | YES | Nothing |

---

## CORE PROBLEM

**RenMagDB converts a 358-file research corpus on Renaissance magic into a structured, searchable SQLite database with enough metadata and extracted content to power a scholarly reference website.**

---

## NON-GOALS (v1)

- **Full static website.** v1 builds the database and proves it works. The site is v2.
- **LLM-generated biographies, essays, or timeline descriptions.** v1 extracts and structures; v2 generates prose.
- **Complete dictionary with 800+ polished definitions.** v1 seeds terms with KWIC concordance and frequency data. v2 generates definitions.
- **Cross-reference/influence network.** v1 captures entities. v2 maps relationships between them.
- **Writing templates and house style guide.** Needed for content generation, which is v2.
- **Visual design, CSS, UX.** No site to design yet.
- **Tradition/school taxonomy.** Emerges from corpus analysis in v1 but isn't formalized until v2.
- **Deployment to GitHub Pages.** Nothing to deploy until v2.
- **Project-specific Claude skills.** Needed for v2 content generation, not v1 extraction.

---

## VERSION 1 SCOPE

**v1 delivers: a populated SQLite database + converted markdown corpus + project infrastructure.**

Specifically:

1. **Project infrastructure** (CLAUDE.md, docs, folder structure, requirements.txt)
2. **358 documents converted to markdown** with quality flags and conversion manifest
3. **SQLite database with Phase 1 schema** (documents, figures, texts, dictionary_terms, timeline_events, era_assignments, topics, join tables — per Buckman critique's phased approach)
4. **`documents` table fully populated** with deterministic metadata (filename parsing, PDF internals, abstract extraction, heuristic classification, language detection, duplicate flagging)
5. **`dictionary_terms` seeded** with regex-extracted Latin/Greek terms + KWIC concordance + frequency data (raw material, not polished definitions)
6. **`figures` seeded** with ~30 entries from folder mapping + Wikidata bio facts (dates, nationality, key works — not narrative biographies)
7. **NER report** (persons, places, dates per document) stored as JSON artifact
8. **TF-IDF topic clusters** stored as JSON artifact (input for v2 tradition taxonomy)
9. **FTS5 full-text search index** on documents (title, summary, full_text)
10. **`data/sample_rows.json`** demonstrating the schema works for 5 representative document types

**v1 exit test:** Run these queries and get correct results:
- "All documents about Ficino" (via document_figures)
- "All Latin terms appearing in Dee documents" (via term_documents)
- "All figures active in the Renaissance" (via era_assignments)
- "Full-text search for 'prima materia'" (via FTS5)
- "All potential duplicates" (via duplicate_group_id)

---

## LATER VERSIONS

### v2: LLM Enrichment + Content Generation
- LLM classification of the ~65 ambiguous documents (type, summary, topics)
- LLM dictionary definitions (800+ terms with brief + long definitions)
- LLM figure biographies (30 figures, museum-curator voice)
- LLM timeline event descriptions (~150 events)
- LLM library catalog (primary sources with significance descriptions)
- Formalize tradition taxonomy from TF-IDF clusters
- Writing templates (`docs/WRITING_TEMPLATES.md`)
- 3 project-specific Claude skills (`/renmagdb-define`, `/renmagdb-bio`, `/renmagdb-catalog`)

### v3: Static Website
- Jinja2 site generator (`build_site.py`)
- Dictionary pages (term → definition → usage → related terms → figures)
- Figure biography pages
- Timeline (filterable, interactive)
- Library catalog (browsable by era, tradition, figure)
- Document catalog (searchable, filterable)
- Client-side search (FTS5 → JSON index)
- CSS design system (warm parchment palette)
- UX audit (`/write-runciter-ux`)
- GitHub Pages deployment

### v4: Network & Exploration
- Cross-reference/influence network (figure → figure, text → text)
- Graph visualization (networkx → D3.js or similar)
- "Related documents" recommendations
- Advanced search (faceted, Boolean, semantic)
- Essay generation
- Curriculum/educational modules

---

## DEPENDENCY ORDER (v1)

```
1. P12: Project infrastructure          [Session 1, ~30 min]
   ├── CLAUDE.md, docs/, scripts/, folders
   ├── requirements.txt + pip install
   └── ONTOLOGY.md (schema design doc)

2. P1:  Document conversion             [Session 1, ~60 min]
   ├── convert_pdf.py (321 PDFs)
   ├── convert_epub.py (10 EPUBs)
   ├── convert_html.py (9 HTML)
   ├── convert_all.py (orchestrator)
   └── data/conversion_manifest.json

3. P2:  Schema + database scaffold      [Session 1, ~30 min]
   ├── data/sample_rows.json (5 examples)
   ├── init_db.py (Phase 1 DDL)
   └── Verify: insert sample rows, run test queries

   ── Can run P1 and P2 in parallel ──

4. P3:  Ingest document metadata         [Session 2, ~30 min]
   ├── ingest_documents.py
   └── 358 rows in documents table

5. P4:  Extract abstracts                [Session 2, ~15 min]
   ├── extract_abstracts.py
   └── ~250 documents get summary from abstract

6. P5:  Heuristic classification         [Session 2, ~15 min]
   ├── classify_heuristic.py
   └── ~280 documents get doc_type

7. P6:  Duplicate detection              [Session 2, ~10 min]
   ├── detect_duplicates.py
   └── data/duplicates.json

8. P7:  Language detection               [Session 2, ~10 min]
   ├── detect_language.py
   └── documents.language populated

9. P8:  Latin/Greek term extraction      [Session 2, ~20 min]
   ├── extract_terms.py (regex + seed list)
   └── dictionary_terms seeded + data/kwic_concordance.json

10. P9: NER pass                         [Session 2, ~20 min]
    ├── extract_ner.py (spaCy)
    └── data/ner_report.json

11. P10: TF-IDF topic clustering         [Session 2, ~15 min]
    ├── tag_tfidf.py
    └── data/topic_clusters.json + topics table seeded

12. P11: Seed figures                    [Session 2, ~20 min]
    ├── seed_figures.py (folder mapping + Wikidata)
    └── ~30 figures with bio facts

13. P20: FTS5 index                      [Session 2, ~10 min]
    ├── build_fts.py
    └── documents_fts populated

14. EXIT TEST                            [Session 2, ~10 min]
    ├── Run 5 verification queries
    └── PASS/FAIL → scope complete or iterate
```

**Estimated total: 2 sessions.** Session 1 = infrastructure + conversion + schema. Session 2 = all deterministic extraction and population.

---

## SCOPE FREEZE RULES

1. **If a new idea emerges during building:** Run `/plan-abendsen-parking`. Do not add it to v1.
2. **If a script "also could" do something extra:** It shouldn't. One script, one job.
3. **If you want to "just quickly" add LLM enrichment:** That's v2. The whole point of v1 is zero LLM content generation.
4. **If the schema needs a new table:** Ask: "Does v1 exit test require this table?" If no, it's v2.
5. **If conversion reveals the corpus is messier than expected:** Solve it with quality flags, not with scope expansion. Flag it, move on, fix in v2.

---

## WHAT v1 PROVES

When v1 is complete, you will have:
- **Evidence** that the corpus can be machine-read (conversion quality report)
- **Evidence** that the schema works (sample rows + test queries)
- **A populated database** that v2 can enrich without redesigning anything
- **JSON artifacts** (NER, TF-IDF, KWIC, Wikidata) that inform v2 decisions about traditions, dictionary scope, and biography depth
- **A project infrastructure** that any future Claude Code session can pick up via CLAUDE.md

v1 is the foundation. It's deliberately boring. The exciting stuff (definitions, biographies, timelines, the website itself) comes when you've earned it by proving the data layer works.

---

*Generated by plan-joe-chip-scope for the Renaissance Magic Database Project. Scope is now FROZEN.*
