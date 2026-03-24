# SLICESLICEBABYRMDB.md — Runciter Vertical Slices
## Renaissance Magic Database Project (v1)

**Date:** 2026-03-23
**Analyst:** Claude (plan-runciter-slice)
**Scope:** v1 only (per JOECHIPSCOPERMDB.md frozen scope)
**Status:** SLICES DEFINED

---

## Core Data Flow

```
Raw corpus (358 files)
  → Python conversion → md/ files
    → Python extraction → metadata, abstracts, terms, entities
      → SQLite insertion → renmagic.db
        → SQL queries → verified results (EXIT TEST)
```

---

## SLICE 1: Proof of Pipeline (One Folder, Full Stack)

**Purpose:** Prove the ENTIRE pipeline works end-to-end on a small sample before scaling. This is the boring foundational slice.

```
Input:    C:\Dev\renaissance magic\Ficino\ (7 files: 6 PDFs + 1 EPUB)
          + project infrastructure (nothing exists yet)

Pipeline: 1. Create project scaffold (folders, CLAUDE.md, docs, requirements.txt)
          2. pip install all dependencies
          3. Write + run convert_pdf.py on 7 Ficino files → md/Ficino/
          4. Write + run convert_epub.py (if EPUB present)
          5. Write data/sample_rows.json (5 example rows including 1 Ficino doc)
          6. Write + run init_db.py (Phase 1 schema, all tables)
          7. Write + run ingest_documents.py on Ficino folder only
          8. Write + run extract_abstracts.py on md/Ficino/
          9. Write + run classify_heuristic.py on Ficino docs
          10. Write + run extract_terms.py on md/Ficino/ (regex + seed list)
          11. Write + run extract_ner.py on md/Ficino/ (spaCy)
          12. Run 3 test queries against the DB

Output:   - Project scaffold exists with all folders and docs
          - md/Ficino/ contains 7 .md files
          - db/renmagic.db exists with all Phase 1 tables
          - documents table has 7 rows with metadata
          - dictionary_terms has seed entries from Ficino corpus
          - data/ner_report.json has entities from Ficino docs
          - 3 queries return correct results

PASS when:
  1. All 7 Ficino files converted (check conversion_manifest.json: 0 EMPTY, ≤1 SCANNED)
  2. sample_rows.json inserted successfully into all tables
  3. SELECT * FROM documents WHERE folder_figure='Ficino' returns 7 rows
  4. SELECT * FROM dictionary_terms returns >0 rows
  5. At least 1 abstract extracted from Ficino docs
  6. NER extracts "Marsilio Ficino" as a PERSON entity

Dependencies: None (this is Slice 1)
Effort:        1 session (~2-3 hours)
```

**Why Ficino?** Small folder (7 files), mix of formats, well-known figure for easy NER validation, likely to have abstracts. Big enough to test pipeline, small enough to debug.

---

## SLICE 2: Bulk Conversion + Metadata Ingestion

**Purpose:** Scale conversion and metadata ingestion to the full 358-file corpus. Prove the pipeline handles edge cases at scale.

```
Input:    All 358 files across 15 folders + root
          Scripts from Slice 1 (already written and tested)

Pipeline: 1. Run convert_all.py on entire corpus
          2. Review conversion_manifest.json for quality flags
          3. Run ingest_documents.py on all folders
          4. Run extract_abstracts.py on all md/ files
          5. Run classify_heuristic.py on all documents
          6. Run detect_language.py on all documents
          7. Run detect_duplicates.py across full corpus

Output:   - md/ tree: 358 .md files mirroring corpus structure
          - conversion_manifest.json: full quality report
          - documents table: 358 rows, all deterministic fields populated
          - ~250 documents with regex-extracted abstracts
          - ~280 documents with heuristic doc_type
          - All documents with language detection
          - data/duplicates.json with flagged pairs

PASS when:
  1. conversion_manifest.json shows 358 entries
  2. Quality breakdown: count GOOD + PARTIAL + SCANNED + EMPTY (all sum to 358)
  3. SELECT COUNT(*) FROM documents = 358
  4. SELECT COUNT(*) FROM documents WHERE summary IS NOT NULL > 200 (abstracts)
  5. SELECT COUNT(*) FROM documents WHERE doc_type IS NOT NULL > 250 (heuristic classification)
  6. SELECT COUNT(*) FROM documents WHERE language IS NOT NULL = 358
  7. data/duplicates.json exists (may be empty — that's fine)
  8. No Python script crashes on any file (graceful error handling for all edge cases)

Dependencies: Slice 1 must PASS
Effort:        1 session (~1-2 hours, mostly runtime)
```

**Key edge cases to survive:**
- "Bruno Lull" folder (two figures in one folder name)
- HTML files in Dee/ with companion `_files/` directories
- The .chm file in trithemius/
- The .crdownload incomplete file (skip gracefully)
- Filenames with HTML entities (`&_039_`, `&amp_`)
- PDFs that yield zero text (scanned-only)
- Very large PDFs (>500 pages)

---

## SLICE 3: Entity Extraction (Terms + NER + Figures)

**Purpose:** Extract structured entities from the converted corpus — Latin/Greek terms, named entities, and figure profiles. This is where the database starts becoming a knowledge base, not just a file catalog.

```
Input:    md/ directory (358 .md files from Slice 2)
          db/renmagic.db (358 document rows from Slice 2)
          data/latin_seed_list.json (~300 curated Renaissance magic terms)

Pipeline: 1. Create data/latin_seed_list.json (curated term list)
          2. Run extract_terms.py on all md/ files
             → regex match seed terms + frequency count + KWIC concordance
          3. Run extract_ner.py on all md/ files (spaCy en_core_web_sm)
             → persons, places, dates per document
          4. Run seed_figures.py
             → 15 folder-name figures + top NER persons
             → Wikidata API for bio facts (dates, nationality, key works)
          5. Populate join tables: document_figures, term_documents
          6. Populate era_assignments for seeded figures

Output:   - dictionary_terms: 200-500 seeded terms with frequency + KWIC
          - data/kwic_concordance.json: term-in-context extracts
          - data/ner_report.json: entities per document
          - figures: ~30 rows with Wikidata bio facts
          - document_figures: join table populated
          - term_documents: join table populated
          - era_assignments: figures assigned to eras
          - data/term_frequency.json: frequency matrix

PASS when:
  1. SELECT COUNT(*) FROM dictionary_terms > 150
  2. SELECT COUNT(*) FROM figures > 20
  3. SELECT COUNT(*) FROM document_figures > 100 (many docs linked to figures)
  4. SELECT COUNT(*) FROM term_documents > 500 (terms found in many docs)
  5. SELECT * FROM figures WHERE name LIKE '%Ficino%' returns 1 row with birth_year=1433
  6. data/kwic_concordance.json contains >3 context lines per top-50 term
  7. data/ner_report.json has entries for all 358 documents
  8. SELECT COUNT(*) FROM era_assignments > 20 (figures assigned to eras)
  9. Query: "All Latin terms in Dee documents" returns results via term_documents JOIN

Dependencies: Slice 2 must PASS
Effort:        1 session (~1-2 hours)
```

**Latin seed list strategy:** Curate ~300 terms across domains:
- Alchemical: prima materia, lapis philosophorum, opus magnum, nigredo, albedo, rubedo, citrinitas, tinctura, elixir, aqua vitae...
- Hermetic: anima mundi, spiritus mundi, mens, nous, logos, emanatio, sympathia, antipathia...
- Kabbalistic: sephiroth, ain soph, tikkun, devekut, gematria, notarikon, temurah...
- Neoplatonic: henosis, theurgia, daimon, to hen, psyche, hypostasis, proodos, epistrophe...
- Astrological: decanus, ascendens, medium coeli, imum coeli, aspectus, dignitas...
- General magical: magia naturalis, magia ceremonialis, talismanum, sigillum, incantatio, invocatio...

---

## SLICE 4: Topic Clustering + Search + Validation

**Purpose:** Add TF-IDF topic discovery, full-text search, and run the complete exit test battery. This is the capstone slice that proves v1 is complete.

```
Input:    md/ directory (358 .md files)
          db/renmagic.db (fully populated from Slices 2-3)

Pipeline: 1. Run tag_tfidf.py on all md/ files
             → scikit-learn TF-IDF → cluster into 8-15 topic groups
             → Seed topics table with cluster labels
             → Populate document_topics join table
          2. Run build_fts.py
             → Create documents_fts virtual table (FTS5)
             → Index title + summary + full_text from md/ files
          3. Run validate_data.py
             → Orphan detection (figures with no documents, terms with no documents)
             → Missing required fields audit
             → Provenance coverage report
             → Cardinality check (per Buckman critique)
          4. Run EXIT TEST (5 queries from JOECHIPSCOPERMDB.md)

Output:   - topics table: 8-15 rows with cluster labels
          - document_topics: every document tagged with ≥1 topic
          - documents_fts: full-text search index operational
          - data/validation_report.json: data quality report
          - data/topic_clusters.json: TF-IDF output for v2 tradition taxonomy
          - EXIT TEST: 5/5 queries pass

PASS when:
  1. SELECT COUNT(*) FROM topics BETWEEN 8 AND 15
  2. SELECT COUNT(*) FROM document_topics >= 358 (every doc has ≥1 topic)
  3. FTS5 query: SELECT * FROM documents_fts WHERE documents_fts MATCH 'prima materia' returns results
  4. EXIT TEST query 1: "All documents about Ficino" returns ≥7 rows ✓
  5. EXIT TEST query 2: "All Latin terms in Dee documents" returns ≥10 terms ✓
  6. EXIT TEST query 3: "All figures active in the Renaissance" returns ≥15 figures ✓
  7. EXIT TEST query 4: "Full-text search for 'prima materia'" returns results ✓
  8. EXIT TEST query 5: "All potential duplicates" returns data/duplicates.json matches ✓
  9. validation_report.json shows <5% orphan rate
  10. All source_method values are 'DETERMINISTIC' (no LLM data in v1)

Dependencies: Slice 3 must PASS
Effort:        1 session (~1 hour)
```

---

## SLICE SUMMARY

| Slice | Name | What it proves | Effort | Cumulative |
|-------|------|---------------|--------|------------|
| 1 | Proof of Pipeline | Full stack works on 7 files | 1 session | 1 session |
| 2 | Bulk Scale | Pipeline survives 358 files + edge cases | 1 session | 2 sessions |
| 3 | Entity Extraction | DB is a knowledge base, not just a file list | 1 session | 3 sessions |
| 4 | Topics + Search + Exit | v1 is complete, searchable, validated | 1 session | 4 sessions |

**Total v1: 4 slices, ~4 sessions.** (Revised up from Joe Chip's 2-session estimate because vertical slicing revealed more work per slice than horizontal layering suggested.)

---

## GATE RULES

```
GATE WARNING: Do not skip to Slice N+1 before Slice N acceptance test passes.
The whole point is discipline.
```

- **Slice 1 → 2 gate:** All 7 Ficino files converted, schema works, test queries pass. If Slice 1 fails, the pipeline design is wrong — fix it before scaling.
- **Slice 2 → 3 gate:** 358 documents converted and ingested. If Slice 2 fails on edge cases, fix error handling before adding extraction complexity.
- **Slice 3 → 4 gate:** Entities extracted, figures seeded, join tables populated. If Slice 3 NER or term extraction is garbage, tune parameters before building search on bad data.
- **Slice 4 → v2 gate:** All 5 exit test queries pass. validation_report.json shows clean data. If Slice 4 fails, v1 is not done — do not start LLM enrichment.

---

## WHAT EACH SLICE LEAVES FOR THE NEXT

| After Slice | Database State | JSON Artifacts | Scripts Written |
|-------------|---------------|----------------|-----------------|
| 1 | 7 docs, schema proven, sample rows | conversion_manifest (partial), ner_report (partial) | convert_*.py, init_db.py, ingest_documents.py, extract_abstracts.py, classify_heuristic.py, extract_terms.py, extract_ner.py |
| 2 | 358 docs, metadata complete | conversion_manifest (full), duplicates.json | detect_language.py, detect_duplicates.py, convert_all.py |
| 3 | +terms, +figures, +joins | kwic_concordance.json, ner_report (full), term_frequency.json, wikidata_figures.json | seed_figures.py, latin_seed_list.json |
| 4 | +topics, +FTS5, validated | topic_clusters.json, validation_report.json | tag_tfidf.py, build_fts.py, validate_data.py |

---

## v2 SLICE PREVIEW (not frozen, just sketched)

After v1 exit test passes, v2 slices would look like:

- **Slice 5:** LLM enrichment (classify ambiguous docs, generate summaries for abstract-less docs)
- **Slice 6:** Dictionary definitions (KWIC → LLM → polished entries for top 300 terms)
- **Slice 7:** Figure biographies + timeline events (Wikidata facts → LLM → narrative prose)
- **Slice 8:** Library catalog (NER-extracted primary sources → LLM → significance descriptions)
- **Slice 9:** Static site generator (dictionary + figures + timeline + catalog pages)
- **Slice 10:** Search + deploy (client-side search, GitHub Pages)

But those are NOT frozen. v2 scope will be defined after v1 exit test passes and `/plan-lampton-corpus` analyzes what the data actually looks like.

---

*Generated by plan-runciter-slice for the Renaissance Magic Database Project. Ready to start Slice 1?*
