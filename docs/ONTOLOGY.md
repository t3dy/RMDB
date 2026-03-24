# ONTOLOGY.md — Schema Catalog
## RenMagDB — Schema Version 2

---

## Schema Version History

| Version | Date | Description |
|---------|------|-------------|
| 1 | 2026-03-23 | Phase 1: core entities, joins, FTS5, provenance |
| 2 | 2026-03-23 | v2: category_type, reception_history, self_description/external_label, cited_documents, figure_traditions |

---

## Core Entity Tables [BUILT]

### `documents` — Corpus files (337 rows)
| Column | Type | Notes |
|--------|------|-------|
| id | INTEGER PK | |
| path | TEXT UNIQUE | Relative path from corpus root |
| md_path | TEXT | Path to converted markdown |
| title | TEXT | Best available title |
| title_from_filename | TEXT | Cleaned filename |
| author_from_filename | TEXT | Extracted author |
| year | INTEGER | Publication year |
| format | TEXT | PDF/EPUB/HTML/CHM/OTHER |
| doc_type | TEXT | MONOGRAPH/ARTICLE/CHAPTER/REVIEW/PRIMARY_SOURCE/ANTHOLOGY/DISSERTATION/UNKNOWN |
| pages | INTEGER | Page count |
| chars | INTEGER | Character count |
| quality_flag | TEXT | GOOD/PARTIAL/SCANNED/EMPTY |
| language | TEXT | ISO language code |
| folder_figure | TEXT | Primary figure from folder name |
| is_primary_source | INTEGER | 1 if this document IS a primary text |
| duplicate_group_id | INTEGER | Links duplicate pairs |
| summary | TEXT | 1-3 sentence description (≤500 chars) |
| relevance | TEXT | PRIMARY/DIRECT/CONTEXTUAL |
| source_method, review_status, confidence | TEXT | Provenance |

### `figures` — Historical persons + modern scholars (29 rows)
| Column | Type | Notes |
|--------|------|-------|
| id | INTEGER PK | |
| name | TEXT UNIQUE | Canonical name |
| name_latin | TEXT | Latin form if different |
| figure_type | TEXT | HISTORICAL/SCHOLAR |
| birth_year, death_year | INTEGER | |
| nationality | TEXT | |
| biography | TEXT | 2-4 paragraph scholarly bio |
| significance | TEXT | 1-2 sentence significance |
| primary_tradition | TEXT | |
| key_works | TEXT | |
| wikidata_id | TEXT | For reference (not used as source — BLUNDER3) |
| self_description | TEXT | **[v2]** What the figure called their own work |
| external_label | TEXT | **[v2]** What opponents/scholars called it |
| source_method, review_status, confidence | TEXT | Provenance |

### `texts` — Referenced primary sources (36 rows)
| Column | Type | Notes |
|--------|------|-------|
| id | INTEGER PK | |
| title | TEXT | English title |
| title_latin | TEXT | Latin title |
| title_original | TEXT | Original language title |
| author_figure_id | INTEGER FK → figures | |
| corpus_document_id | INTEGER FK → documents | If this text IS in the corpus |
| era | TEXT | ANCIENT/MEDIEVAL/RENAISSANCE/EARLY_MODERN |
| tradition | TEXT | |
| language | TEXT | |
| significance | TEXT | Why this text matters |
| date_composed | TEXT | |
| reception_history | TEXT | **[v2]** How text was understood then vs now |
| source_method, review_status, confidence | TEXT | Provenance |

### `dictionary_terms` — Latin/Greek/Hebrew/Arabic terms (186 rows)
| Column | Type | Notes |
|--------|------|-------|
| id | INTEGER PK | |
| term | TEXT | Term in original language |
| term_language | TEXT | LATIN/GREEK/HEBREW/ARABIC/etc. |
| canonical_form | TEXT | Normalized form |
| english_translation | TEXT | |
| definition_brief | TEXT | ≤100 chars |
| definition_long | TEXT | 100-200 words |
| domain | TEXT | ALCHEMICAL/HERMETIC/KABBALISTIC/NEOPLATONIC/MAGICAL/ASTROLOGICAL/THEOLOGICAL/ENOCHIAN/PHILOSOPHICAL |
| category_type | TEXT | **[v2]** ACTOR_TERM/ANALYST_TERM/HYBRID |
| frequency | INTEGER | Corpus occurrence count |
| source_method, review_status, confidence | TEXT | Provenance |

### `timeline_events` — Historical events (58 rows)
| Column | Type | Notes |
|--------|------|-------|
| id | INTEGER PK | |
| year | INTEGER | |
| year_end | INTEGER | For ranges |
| event_type | TEXT | PUBLICATION/BIOGRAPHY/SCHOLARSHIP/TRIAL/INSTITUTION/TRANSLATION/DISCOVERY/POLITICAL/OTHER |
| title | TEXT | |
| description | TEXT | 2-3 sentences |
| source_method, review_status, confidence | TEXT | Provenance |

---

## Join/Relationship Tables [BUILT]

| Table | Relationship | Cardinality | Provenance? |
|-------|-------------|-------------|-------------|
| `document_figures` | document ↔ figure | M:N, optional | source_method |
| `document_texts` | document ↔ referenced text | M:N, optional | source_method, confidence |
| `document_topics` | document ↔ topic | M:N, required (≥1) | source_method |
| `figure_influences` | figure → figure (directed) | M:N, optional | source_method, confidence |
| `figure_texts` | figure ↔ text (authored/translated) | M:N, optional | relationship type |
| `figure_traditions` | figure ↔ tradition | M:N, typed | **[v2]** relationship_type: PRACTICED/STUDIED/CRITICIZED/SYNTHESIZED/INFLUENCED_BY/FOUNDED/TRANSMITTED |
| `term_documents` | term ↔ document occurrence | M:N, required (≥1) | frequency |
| `term_figures` | term ↔ figure | M:N, optional | |
| `term_links` | term ↔ term cross-ref | M:N, typed | link_type |
| `term_variants` | term → variant spellings | 1:N | |
| `event_figures` | event ↔ figure | M:N, optional | |
| `event_texts` | event ↔ text | M:N, optional | |
| `cited_documents` | **[v2]** term → corpus docs that informed definition | M:N | citation_context |

---

## Controlled Vocabulary Tables [BUILT]

| Table | Content |
|-------|---------|
| `topics` | 21 entries: 12 TF-IDF clusters + 9 tradition labels |
| `era_assignments` | Flexible era assignment (entity_type + entity_id + era + era_role) |
| `schema_version` | Migration tracking (v1, v2) |

---

## FTS5 Virtual Tables [BUILT]

| Table | Indexed Fields |
|-------|---------------|
| `documents_fts` | title, summary, full_text |
| `terms_fts` | term, english_translation, definition_long |

---

## Provenance Model

Every content table includes:
- `source_method`: DETERMINISTIC | CORPUS_EXTRACTION | LLM_ASSISTED | HUMAN_VERIFIED | SEED_DATA
- `review_status`: DRAFT | REVIEWED | VERIFIED
- `confidence`: HIGH | MEDIUM | LOW

**Rules:**
- Deterministic data: DETERMINISTIC + HIGH
- Seed data: SEED_DATA + HIGH
- LLM-generated data: LLM_ASSISTED + MEDIUM + DRAFT
- Never overwrite VERIFIED data without logging

---

## Current Population (as of v2 Phase B in-progress)

| Table | Rows | Notes |
|-------|------|-------|
| documents | 337 | 100% classified, 79% summarized |
| figures | 29 | 22 historical + 7 scholars, all with dates + significance |
| texts | 36 | Primary sources with metadata |
| dictionary_terms | 186 | 46 with definitions, 5 flagged generic |
| timeline_events | 58 | 18 with descriptions |
| topics | 21 | 12 TF-IDF + 9 tradition labels |
| era_assignments | 57 | Figures + texts |
| document_figures | 329 | From folder mapping |
| term_documents | 8,180 | From regex extraction |
| document_topics | 337 | From TF-IDF |
| figure_traditions | 35 | **[v2]** With relationship types |

---

*Schema version 2. Updated with Gnosis/Essay revisions per GNOSISDICTIONARYSTYLEANALYSISTAKEAWAYS.md.*
