# PIPELINE.md — Script Execution Order
## RenMagDB

---

## v1 Scripts (COMPLETE — all run and verified)

```
# 1. Conversion (Layer 1)
python scripts/convert_pdf.py          # 321 PDFs -> md/
python scripts/convert_epub.py         # 10 EPUBs -> md/
python scripts/convert_html.py         # 5 HTML -> md/
python scripts/convert_all.py          # Orchestrator for all formats

# 2. Schema (Layer 2)
python scripts/init_db.py              # Creates db/renmagic.db with Phase 1 schema

# 3. Deterministic Population (Layer 3)
python scripts/ingest_documents.py     # 337 docs -> documents table
python scripts/extract_abstracts.py    # Regex abstract extraction (15 hits)
python scripts/classify_heuristic.py   # Rule-based doc_type (238/337)
python scripts/detect_language.py      # langdetect (337/337)
python scripts/detect_duplicates.py    # rapidfuzz dedup (66 pairs)
python scripts/extract_terms.py        # Regex + 200-term seed list (186 found, 8180 links)
python scripts/extract_ner.py          # spaCy NER (5303 persons)

# 4. Entities + Search (Layer 3 continued)
python scripts/seed_figures.py         # 29 figures from curated JSON
python scripts/tag_tfidf.py            # TF-IDF 12 topic clusters
python scripts/build_fts.py            # FTS5 full-text search index
python scripts/validate_data.py        # Data integrity report
```

## v2 Phase A Scripts (COMPLETE — deterministic enrichment)

```
python scripts/classify_heuristic_v2.py   # Enhanced classification (93 more, total 331/337)
python scripts/extract_introductions.py   # Intro paragraph extraction (90 more, total 105 summaries)
python scripts/seed_timeline.py           # 58 events from figure dates + milestones
python scripts/seed_texts.py              # 32 primary sources from curated list
python scripts/build_traditions.py        # 9 traditions from term domain aggregation
python scripts/curate_terms.py            # Flag 5 generic terms (ens, ratio, natura, forma, materia)
```

## v2 Phase B Scripts (PENDING — LLM enrichment, ~990K tokens)

```
# Prompts defined in BUCKMANV2RMDB.md (revised, scored 34-35/40)

python scripts/enrich_classify.py         # LLM classify ~6 remaining ambiguous docs
python scripts/enrich_summaries.py        # LLM summarize ~160 English docs without summaries
python scripts/generate_dictionary.py     # LLM definitions for ~120 magic-specific terms
python scripts/generate_biographies.py    # LLM biographies for 29 figures
python scripts/describe_timeline.py       # LLM descriptions for ~40 undescribed events
python scripts/describe_texts.py          # LLM significance for ~32 primary sources
```

## v3 Scripts (PLANNED — static website)

```
python scripts/build_site.py              # Jinja2 -> static HTML
python scripts/generate_search_index.py   # FTS5 -> JSON for client-side search
```

## Full Rebuild (v1 + v2 Phase A)

```bash
# From clean state:
python scripts/init_db.py
python scripts/convert_all.py
python scripts/ingest_documents.py
python scripts/extract_abstracts.py
python scripts/classify_heuristic.py
python scripts/detect_language.py
python scripts/detect_duplicates.py
python scripts/extract_terms.py
python scripts/extract_ner.py
python scripts/seed_figures.py
python scripts/tag_tfidf.py
python scripts/build_fts.py
python scripts/classify_heuristic_v2.py
python scripts/extract_introductions.py
python scripts/seed_timeline.py
python scripts/seed_texts.py
python scripts/build_traditions.py
python scripts/curate_terms.py
python scripts/validate_data.py
```
