# BUCKMANONTRMDB.md — Buckman Critic: Ontology Review
## Renaissance Magic Database Project

**Date:** 2026-03-23
**Analyst:** Claude (plan-buckman-critic)
**Subject:** The ontology/schema design as specified in HIRORMDB.md Layer 2 and the plan file

---

## 1. Scoring the Ontology Prompt

The "prompt" under review is the combined schema specification from HIRORMDB.md Layer 2 + DECKARDRMDB.md entity model + the plan's Layer 2 output contract.

| Dimension | Score (1-5) | Issue |
|-----------|-------------|-------|
| Scope clarity | 3 | Tries to define ALL tables at once. Should be phased: core entities first, join tables second, vocabularies third. |
| Constraint presence | 4 | CHECK constraints, ENUM values, provenance columns well-specified. Missing: cardinality constraints, NULL policies, index strategy. |
| Self-assessment | 2 | Doesn't acknowledge what we DON'T know yet — e.g., we haven't read the corpus. The schema assumes entity types that may not match reality. |
| Failure history | 1 | No mention of AtalantaClaudiens schema mistakes or lessons learned. That project went through 5 migrations — what broke and why? |
| Conciseness | 3 | ~20 tables is reasonable but some may be premature. Do we need `cultures` and `religions` as separate tables before we know what the corpus contains? |
| Actionability | 4 | init_db.py is a clear first step. Table definitions are concrete enough to write DDL. |
| Examples | 2 | No example rows. What does a `documents` row look like? What does a `figure_influences` edge look like? Without examples, edge cases hide. |
| Exit criteria | 2 | "Schema created" is not testable. Need: "INSERT 5 sample rows per table, run 3 cross-reference queries, verify FTS5 returns results." |

**Overall: 21/40 — Functional but underspecified. Needs examples, phasing, and failure awareness.**

---

## 2. Specific Problems Identified

### Problem 1: PREMATURE TABLES
The schema includes `cultures`, `religions`, and `traditions` as separate tables before we've read a single document. These may collapse into a single `contexts` or `traditions` table, or may not be needed at all.

**Risk:** Empty tables that never get populated. Schema complexity without data to justify it.

**Fix:** Phase the schema. Core tables in v1 (documents, figures, texts, dictionary_terms, timeline_events). Context tables in v2 AFTER Layer 3 data reveals what categories actually exist.

### Problem 2: `texts` vs `documents` BOUNDARY IS FUZZY
The plan says `documents` = the 358 files in the corpus, `texts` = referenced primary sources (Corpus Hermeticum, Picatrix, etc.). But some corpus files ARE primary sources (Dee's Monas Hieroglyphica PDF IS the text). A document can simultaneously be a corpus file AND a primary source text.

**Risk:** Data modeling confusion. Do we create both a `documents` row and a `texts` row for Dee's Monas? How do we link them?

**Fix:** Add `documents.is_primary_source BOOLEAN DEFAULT 0`. When a corpus file IS a primary source, set the flag and create a corresponding `texts` row with `texts.corpus_document_id` pointing back. This makes the relationship explicit.

### Problem 3: FIGURE TYPE CONFLATION
Unified `figures` table with `figure_type` HISTORICAL/SCHOLAR is clean but insufficient. Historical figures have birth_year/death_year/nationality/primary_tradition. Modern scholars have institutional_affiliation/specialization/active_decades. Forcing both into one table means many NULL columns.

**Risk:** Sparse table with columns that are only relevant to half the rows.

**Fix:** Keep the unified table but add a `figures_extended` JSON column for type-specific attributes. Or accept the NULLs — for ~60 total figures, the sparsity cost is negligible. The unified approach is correct for cross-referencing (a scholar CAN influence another scholar, a historical figure's work CAN be about another historical figure).

**Verdict:** Keep unified. Accept NULLs. Add a comment in ONTOLOGY.md explaining the design choice.

### Problem 4: MISSING CARDINALITY DOCUMENTATION
Join tables are listed but cardinality isn't specified. Is `figure_influences` one-to-many or many-to-many? Can a document have zero figures? Can a term belong to zero documents?

**Risk:** Scripts make wrong assumptions about required vs optional relationships.

**Fix:** Document cardinality for every join table:

| Join Table | Cardinality | Required? |
|-----------|-------------|-----------|
| `document_figures` | M:N | Optional (some docs are thematic, not figure-specific) |
| `document_texts` | M:N | Optional (not all docs reference specific primary sources) |
| `document_topics` | M:N | Required (every doc gets at least 1 topic) |
| `figure_traditions` | M:N | Required (every figure belongs to at least 1 tradition) |
| `figure_influences` | M:N, directed | Optional (not all influence relationships are known) |
| `figure_texts` | M:N | Optional (scholars don't author primary sources) |
| `text_traditions` | M:N | Required (every text belongs to at least 1 tradition) |
| `term_documents` | M:N | Required (terms must appear in at least 1 document) |
| `term_figures` | M:N | Optional |
| `term_links` | M:N, typed | Optional |
| `event_figures` | M:N | Optional (some events are institutional, not personal) |
| `event_texts` | M:N | Optional |

### Problem 5: NO EXAMPLE ROWS
The schema has zero example data. Without examples, we can't test whether the schema actually works for real data.

**Risk:** Schema looks good on paper but fails on insertion. Edge cases like "Bruno Lull" folder containing two figures, or a document with 6 authors, aren't tested.

**Fix:** Create `data/sample_rows.json` with 5 representative examples per table BEFORE writing init_db.py:
- A monograph (Yates, *Giordano Bruno and the Hermetic Tradition*)
- A journal article (from Ambix, with full metadata)
- A primary source that's also a corpus file (Dee's Monas Hieroglyphica)
- A review article (with "Review by_" in filename)
- A multi-author anthology chapter

### Problem 6: ERA MODEL IS UNDERSPECIFIED
"Flexible/overlapping" eras was decided but the schema doesn't reflect it. If a figure can belong to multiple eras, we need an `era_assignments` join table, not an `era` column on `figures`.

**Risk:** The `figures.era` column forces single assignment, contradicting the "flexible/overlapping" decision.

**Fix:** Remove `era` columns from `figures` and `texts`. Add:
```sql
CREATE TABLE era_assignments (
    id INTEGER PRIMARY KEY,
    entity_type TEXT CHECK(entity_type IN ('FIGURE','TEXT','EVENT')),
    entity_id INTEGER,
    era TEXT CHECK(era IN ('ANCIENT','MEDIEVAL','RENAISSANCE','EARLY_MODERN','ENLIGHTENMENT')),
    era_role TEXT, -- e.g., 'AUTHORED_IN', 'RECEIVED_IN', 'ACTIVE_IN'
    UNIQUE(entity_type, entity_id, era, era_role)
);
```
This lets Corpus Hermeticum be ANCIENT (authored) AND RENAISSANCE (received/translated). Ficino is RENAISSANCE (active) but his Plato translations engage ANCIENT texts.

### Problem 7: TRADITION TAXONOMY VS "LET IT EMERGE"
User decided "let it emerge from the corpus" but the schema has a `traditions` table with no seed data strategy. If traditions emerge from TF-IDF clustering in Layer 3, how do those clusters become rows in the `traditions` table?

**Risk:** The table exists but the pipeline to populate it is undefined.

**Fix:** Define a two-stage process:
1. Layer 3: TF-IDF produces ~8-15 topic clusters. Store as `data/topic_clusters.json`.
2. Layer 4: LLM reviews clusters, assigns human-readable names, creates `traditions` rows.
3. Document this pipeline in PIPELINE.md.

### Problem 8: DICTIONARY TERM LANGUAGE HANDLING
The schema has `term_language` but no strategy for variant spellings, transliterations, or cross-language equivalents. "Kabbalah" / "Cabala" / "Qabalah" / "קבלה" are the same concept.

**Risk:** Duplicate dictionary entries for the same term in different orthographies.

**Fix:** Add `dictionary_terms.canonical_form` (normalized) + `term_variants` table:
```sql
CREATE TABLE term_variants (
    id INTEGER PRIMARY KEY,
    term_id INTEGER REFERENCES dictionary_terms(id),
    variant TEXT NOT NULL,
    variant_language TEXT,
    variant_script TEXT, -- LATIN, HEBREW, GREEK, ARABIC
    UNIQUE(term_id, variant)
);
```

### Problem 9: FTS5 STRATEGY IS INCOMPLETE
"FTS5 on documents(title, summary) and dictionary_terms(term, definition_long)" is a start but misses the biggest search target: the full markdown text of converted documents.

**Risk:** Users can search titles and summaries but not document contents.

**Fix:** Add an FTS5 virtual table on the full .md content:
```sql
CREATE VIRTUAL TABLE documents_fts USING fts5(
    title, summary, full_text,
    content=documents, content_rowid=id
);
```
The `full_text` column can be populated from the .md files during Layer 3. This is the single most valuable search feature.

### Problem 10: NO PROVENANCE ON JOIN TABLES
Provenance columns (`source_method`, `review_status`, `confidence`) are specified for content tables but not for join tables. But join table rows ARE claims — "Ficino influenced Pico" is a scholarly claim with a source, not a self-evident fact.

**Risk:** Influence relationships, topic assignments, and text associations are inserted without tracking where they came from.

**Fix:** Add provenance columns to ALL join tables that represent scholarly claims:
- `figure_influences` (influence claims are interpretive)
- `document_texts` (which texts a document references is interpretive)
- `figure_traditions` (tradition assignment is interpretive)

Skip provenance on purely mechanical joins:
- `document_figures` when derived from folder mapping (deterministic)
- `term_documents` when derived from regex match (deterministic)

---

## 3. Revised Schema Specification

### Phasing

**Phase 1 (Layer 2, built immediately):**
- `documents` (with `is_primary_source` flag)
- `figures` (unified, with NULLable type-specific columns)
- `texts` (with `corpus_document_id` back-link)
- `dictionary_terms` + `term_variants`
- `timeline_events`
- `era_assignments` (flexible era model)
- `topics` (controlled vocabulary, starts empty, populated by Layer 3 TF-IDF)
- All join tables with cardinality documented
- `schema_version`
- FTS5 virtual tables (documents_fts with full_text)

**Phase 2 (after Layer 3 data reveals structure):**
- `traditions` (seeded from TF-IDF clusters)
- `figure_traditions`, `text_traditions` (populated after traditions exist)
- `provenance_log` (audit trail)

**Phase 3 (after Layer 5 content generation):**
- Any additional tables needed for website features (essays, reading_lists, etc.)

### Key Additions
- `documents.is_primary_source` BOOLEAN
- `texts.corpus_document_id` INTEGER REFERENCES documents(id)
- `era_assignments` join table (replaces era columns)
- `term_variants` table (handles orthographic variants)
- `documents_fts` with full_text column
- Provenance on interpretive join tables
- Cardinality documentation for all joins
- `data/sample_rows.json` created BEFORE init_db.py

---

## 4. Revised Prompt for Layer 2

```
ORIGINAL: ~800 words across HIRORMDB.md Layer 2
REVISED:  ~400 words (below)
CHANGES:  Added phasing, example row requirement, era_assignments table,
          term_variants table, full-text FTS5, provenance on interpretive joins,
          is_primary_source flag, cardinality documentation.
          Removed premature cultures/religions tables.
          Added exit criteria.
```

**REVISED LAYER 2 PROMPT:**

> Create SQLite schema for RenMagDB in two phases.
>
> **Phase 1 tables** (build now):
> `documents`, `figures`, `texts`, `dictionary_terms`, `term_variants`, `timeline_events`, `era_assignments`, `topics`, `schema_version`, plus join tables: `document_figures`, `document_texts`, `document_topics`, `figure_influences`, `figure_texts`, `term_documents`, `term_figures`, `term_links`, `event_figures`, `event_texts`.
>
> **Phase 2 tables** (build after Layer 3): `traditions`, `figure_traditions`, `text_traditions`, `provenance_log`.
>
> **Required on every content table:** `source_method`, `review_status`, `confidence`, `created_at`, `updated_at`.
> **Required on interpretive join tables** (`figure_influences`, `document_texts`, `figure_traditions`): `source_method`, `confidence`.
>
> **Key design decisions:**
> - `documents.is_primary_source` BOOLEAN links corpus files that ARE primary sources
> - `texts.corpus_document_id` back-links to the document row when applicable
> - `era_assignments` replaces era columns: `(entity_type, entity_id, era, era_role)`
> - `term_variants` handles Kabbalah/Cabala/Qabalah/קבלה
> - FTS5 on `documents(title, summary, full_text)` and `dictionary_terms(term, definition_long)`
>
> **Before writing init_db.py:** Create `data/sample_rows.json` with 5 examples per table. Test the schema against: a monograph, a journal article, a primary source that's also a corpus file, a review, and a multi-author chapter.
>
> **Exit criteria:** INSERT all sample rows successfully. Run 3 cross-reference queries: (1) "all documents about Ficino" via document_figures, (2) "all Latin terms in Dee documents" via term_documents, (3) "all figures active in the Renaissance era" via era_assignments. All return correct results.

---

*Generated by plan-buckman-critic for the Renaissance Magic Database Project.*
