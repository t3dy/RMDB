# HIROV2RMDB.md — HiroPlantagenet Decomposition (v2 Update)
## Renaissance Magic Database Project

**Date:** 2026-03-23 (updated mid-session)
**Analyst:** Claude (hiro-plantagenet, third pass)
**Context:** v2 Phase A COMPLETE. Phase B in progress. Updated with RMESSAY1.md (Yates/Copenhaver reframing), GNOSISDICTIONARYSTYLEANALYSISTAKEAWAYS.md (10 schema/template revisions), SWARMRMDB.md (agent constraints), BLUNDER4 (agents can't Bash).

---

## 1. Intent Atoms (v2 only — v1 atoms are DONE)

| # | Goal | Tag | Phase |
|---|------|-----|-------|
| B1 | Enhanced heuristic classification (resolve ~40 more docs) | CLASSIFICATION | A (deterministic) |
| B2 | Extract introductions from monographs (regex) | EXTRACTION | A |
| B3 | Seed timeline events from figure dates + publication years | PIPELINE | A |
| B4 | Seed primary sources from high-freq title terms + doc_type | PIPELINE | A |
| B5 | Build tradition taxonomy from term domain aggregation | ONTOLOGY | A |
| B6 | Curate generic terms (flag/filter top 15 common Latin) | DATA QUALITY | A |
| B7 | LLM classify ~60 remaining ambiguous documents | CLASSIFICATION | B (LLM) |
| B8 | LLM summarize ~160 English docs without abstracts/intros | EXTRACTION | B |
| B9 | LLM generate ~120 dictionary definitions (magic-specific first) | UI-SURFACING | B |
| B10 | LLM generate 29 figure biographies from corpus evidence | UI-SURFACING | B |
| B11 | LLM describe ~40 timeline events | UI-SURFACING | B |
| B12 | LLM describe ~40 primary source significance | UI-SURFACING | B |
| B13 | Finalize writing templates | META-CONTROL | DONE |
| B14 | Create 3 project-specific Claude skills | META-CONTROL | A |

---

## 2. Conflicts & Gaps (v2-specific)

### CONFLICTS

**CONFLICT 1: Generic terms vs magic-specific terms.**
The 200-term seed list includes ~15 terms (`ens`, `ratio`, `natura`, `forma`, `materia`, `essentia`, `causa`, `potentia`, `scientia`, `cognitio`, `contemplatio`, `experientia`) that are standard Latin philosophical vocabulary appearing at 1,000-53,000 frequency. Defining these as "Renaissance magic terms" is misleading.
**Resolution:** Phase A curates these before Phase B generates definitions. Options: narrow scope to magic-specific usage, deprioritize, or flag as GENERAL_PHILOSOPHY distinct from the magic dictionary.

**CONFLICT 2: Corpus-only biographies vs sparse ancient figures.**
BLUNDER3 rule says "corpus is the only source of truth." But Plato, Plotinus, Iamblichus have ZERO dedicated corpus documents. Writing their biographies purely from corpus evidence means writing about how OTHER scholars reference them — not about them directly.
**Resolution:** For sparse figures, the biography describes their ROLE IN THE CORPUS ("Plato appears in this corpus primarily through the Timaeus, which Ficino translated and which...") not their life story. This is honest and corpus-grounded.

**CONFLICT 3: TF-IDF clusters are noisy — should they be replaced or fixed?**
DECKARDV2RMDB found JSTOR boilerplate, OCR noise, and language clusters contaminating TF-IDF. The 117-doc megacluster is useless. Should we re-cluster with better stopwords, or abandon TF-IDF in favor of term-domain aggregation?
**Resolution:** Do both. Re-cluster with cleaned stopwords (Phase A) AND build tradition taxonomy from term domains. They serve different purposes: TF-IDF groups documents by textual similarity; domain aggregation maps intellectual traditions. Keep both.

### MISSING DECISIONS

1. **Term curation granularity:** Do we delete generic terms from dictionary_terms, recategorize them to a new domain "GENERAL_LATIN", or keep them with a priority flag? Decision needed before B9.
2. **Tradition naming source:** Should tradition names come from the corpus itself (e.g., how scholars label traditions) or from standard scholarly vocabulary? Decision needed before B5.
3. **Biography order:** Process corpus-rich figures first (15 with folders) or alphabetically? DECKARDV2RMDB recommends tiered — confirm.

### RESOLVED FROM v1

- ~~Era model~~ → `era_assignments` join table working correctly (11 Renaissance figures verified)
- ~~Documents vs texts boundary~~ → clear separation with `is_primary_source` flag ready
- ~~Tradition taxonomy~~ → emerges from term domains (DECKARDV2RMDB shift), not TF-IDF
- ~~Term variants~~ → `term_variants` table exists, not yet populated (v3)

---

## 3. Layer Architecture (v2 revised)

```
PHASE A: DETERMINISTIC ENRICHMENT     (zero LLM tokens)
  Atoms: B1, B2, B3, B4, B5, B6, B14
  Purpose: Squeeze maximum value from Python before spending LLM tokens
  Reasoning mode: deterministic (regex, aggregation, heuristic)
  Scripts: 6 new Python scripts + 3 Claude skill definitions
  Depends on: v1 complete

PHASE B: LLM ENRICHMENT               (~990K tokens)
  Atoms: B7, B8, B9, B10, B11, B12
  Purpose: Generate content that requires judgment and narrative synthesis
  Reasoning mode: generative + classificatory
  Scripts: 6 LLM-calling scripts using Buckman-revised prompts
  Depends on: Phase A complete
```

**Key difference from v1 HIRORMDB:** v1 had 6 layers with conversion and schema mixed in. v2 has just 2 phases because the infrastructure exists. Phase A is pure optimization; Phase B is pure content generation.

---

## 4. Rewritten Prompts (Per Phase)

### === PHASE A: DETERMINISTIC ENRICHMENT ===

**OBJECTIVE:** Run 6 Python scripts that resolve ~25% of v2's work without spending LLM tokens, reducing Phase B scope and cost.

**SCOPE CONSTRAINTS:**
- DO: Enhanced classification, introduction extraction, timeline/text seeding, tradition building, term curation, skill creation
- DO NOT: Call any LLM. Do not generate prose content. Do not modify writing templates.

**INPUTS:**
- `db/renmagic.db` (v1 populated database)
- `md/` directory (321 markdown files)
- `data/` artifacts (term_frequency.json, ner_report.json, topic_clusters.json, figures_seed.json)

**OUTPUT CONTRACT:**

| Script | Output | Validation |
|--------|--------|-----------|
| `classify_heuristic_v2.py` | ~40 more docs get doc_type | `SELECT COUNT(*) FROM documents WHERE doc_type IS NOT NULL` increases from 238 to ~278 |
| `extract_introductions.py` | ~50 monographs get summary from intro text | `SELECT COUNT(*) FROM documents WHERE summary IS NOT NULL` increases from 15 to ~65 |
| `seed_timeline.py` | ~40 events in timeline_events | `SELECT COUNT(*) FROM timeline_events` > 35 |
| `seed_texts.py` | ~40 texts in texts table | `SELECT COUNT(*) FROM texts` > 35 |
| `build_traditions.py` | Tradition labels from term domains in topics table | Updated topics with tradition-quality names |
| `curate_terms.py` | 15 generic terms flagged/recategorized | Terms marked for priority handling |

**DECISION RULES:**
- Enhanced classification uses: file size (<1MB = article, >10MB = monograph), first-line patterns ("Chapter" = chapter, journal header = article), PDF metadata Subject field
- Introduction extraction looks for: "Introduction", "Chapter 1", "Preface", "Foreword" headings, grabs first 500 chars after heading
- Timeline events generated from: figure birth/death (25 figures with dates), known publication dates from filename year field, ~10 hardcoded milestones (Ficino translates Hermetica 1463, Bruno burned 1600, etc.)
- Text seeding from: 23 PRIMARY_SOURCE documents + ~17 high-frequency title terms in dictionary_terms
- Tradition building: aggregate term counts per domain → "KABBALISTIC domain has 26 terms, 7984 total freq" → tradition "Kabbalah / Christian Cabala" with stats
- Term curation: terms with frequency >5000 AND domain=PHILOSOPHICAL get flagged as LOW_PRIORITY

**GATE TEST (Phase A → Phase B):**
- `documents` with doc_type: ≥270 (up from 238)
- `documents` with summary: ≥55 (up from 15)
- `timeline_events`: ≥35
- `texts`: ≥35
- Generic terms flagged
- Tradition labels assigned

---

### === PHASE B: LLM ENRICHMENT ===

**OBJECTIVE:** Generate all remaining content using the Buckman-revised LLM prompts. All output tagged `source_method='LLM_ASSISTED'`, `confidence='MEDIUM'`, `review_status='DRAFT'`.

**SCOPE CONSTRAINTS:**
- DO: Classify remaining ambiguous docs, summarize docs lacking summaries, generate dictionary definitions, write biographies, describe events and texts
- DO NOT: Build website. Do not create influence network. Do not write essays.

**INPUTS:**
- `db/renmagic.db` (Phase A enriched)
- `md/` files (for LLM context)
- `data/kwic_concordance.json` (for dictionary)
- `docs/WRITING_TEMPLATES.md` (voice and structure rules)
- `BUCKMANV2RMDB.md` (revised prompts A, B, C)

**OUTPUT CONTRACT:**

| Script | Uses Prompt | Scope | Output |
|--------|-------------|-------|--------|
| `enrich_classify.py` | A (revised) | ~60 docs | doc_type + summary for ambiguous docs |
| `enrich_summaries.py` | A variant | ~160 docs | summary for English docs without abstract/intro |
| `generate_dictionary.py` | B (revised) | ~120 terms | definition_brief + definition_long |
| `generate_biographies.py` | C (revised) | 29 figures | biography + significance + key_works + traditions |
| `describe_timeline.py` | mini-prompt | ~40 events | description field (2-3 sentences each) |
| `describe_texts.py` | mini-prompt | ~40 texts | significance field (3-5 sentences each) |

**VALIDATION LAYER:**
- doc_type must be in ENUM list
- summary ≤ 500 chars, must contain author surname
- definition_brief ≤ 100 chars, must contain English translation
- definition_long must name ≥1 figure
- biography must contain the figure's name
- All responses must be valid JSON
- Rejections logged, re-prompted once, then flagged LOW confidence

**TOKEN BUDGET:** ~990K total (DECKARDV2RMDB revised estimate)

**GATE TEST (Phase B → v2 complete):**
- `documents` with doc_type: 337 (100%)
- `documents` with summary: ≥200
- `dictionary_terms` with definition_brief: ≥120
- `figures` with biography: 29
- `timeline_events` with description: ≥35
- `texts` with significance: ≥35
- All LLM data: source_method='LLM_ASSISTED'
- Zero source_method='DETERMINISTIC' data overwritten by LLM

---

## 5. Execution Notes

### Session Estimates

| Phase | Scripts | Est. Time | Est. Tokens |
|-------|---------|-----------|-------------|
| A | 6 scripts + 3 skills | 1 session | 0 |
| B (classify + summarize) | 2 scripts | 1-2 sessions | ~640K |
| B (dictionary + bios) | 2 scripts | 1-2 sessions | ~265K |
| B (timeline + texts) | 2 scripts | 0.5 session | ~85K |
| **TOTAL** | **12 scripts** | **3-5 sessions** | **~990K** |

### Risk Register (v2-specific)

1. **LLM hallucination in biographies** — BLUNDER3 safeguard in prompt, but figures with sparse corpus evidence (Plato, Hermes Trismegistus) are high risk. Mitigation: confidence=LOW for sparse figures, flag for human review.
2. **Summary quality varies by document type** — Monograph intros are thesis-rich; article abstracts are structured; chapters and anthologies are harder. Mitigation: batch by doc_type so the LLM gets consistent input format.
3. **Generic term definitions** — "ens" in a Renaissance magic dictionary will confuse readers who know basic Latin philosophy. Mitigation: Phase A curation + domain-specific framing in prompt.
4. **Non-English documents** — 39 docs in Italian/German/French. LLM summaries of foreign text are lower quality. Mitigation: skip non-English in v2, flag for v3.

### What Changed from Original HIRORMDB.md

| Original Layer | Status | What Replaced It |
|---------------|--------|-----------------|
| Layer 0: Infrastructure | DONE (v1) | — |
| Layer 1: Conversion | DONE (v1) | — |
| Layer 2: Schema | DONE (v1) | — |
| Layer 3: Deterministic Data | DONE (v1) | — |
| Layer 4: Hybrid Enrichment | **SPLIT** into Phase A (deterministic) + Phase B first half (LLM classify/summarize) |
| Layer 5: Content Generation | **SPLIT** into Phase B second half (LLM dictionary/bio/timeline/library) |
| Layer 6: Site Build | **DEFERRED** to v3 |

The original 6-layer horizontal architecture is replaced by a 2-phase vertical split (A: Python, B: LLM) that's tighter, cheaper, and informed by actual data.

---

## Environment Status (Updated mid-session)

### Files in Place
- `CLAUDE.md` — project entry point, updated with v2 rules + BLUNDER lessons ✓
- `docs/WRITING_TEMPLATES.md` — 6 content templates, museum-curator voice ✓ (NEEDS REVISION per Gnosis takeaways)
- `docs/PIPELINE.md` — full script execution order (v1 + v2 Phase A + B planned) ✓
- `BUCKMANV2RMDB.md` — 3 revised LLM prompts (scored 34-35/40) ✓
- `DECKARDV2RMDB.md` — boundary map with 7 shifts ✓
- `JOECHIPV2RMDB.md` — v2 scope freeze ✓
- `STEINERGATERMDB.md` — v1 gate passed ✓
- `FATCOMPRESSRMDB.md` — 8 concept blocks for prompt injection ✓
- `SWARMRMDB.md` — agent constraints + staging protocol ✓
- `RMESSAY1.md` — "Magic" as scholarly category (Yates vs Copenhaver) ✓
- `GNOSISDICTIONARYSTYLEANALYSISTAKEAWAYS.md` — 10 schema/template revisions ✓
- `agile/` — board, epics, sprints, issues, BLUNDER1-4 ✓

### Phase A Scripts (ALL COMPLETE ✓)
- `scripts/classify_heuristic_v2.py` ✓ (93 more classified, 98% total)
- `scripts/extract_introductions.py` ✓ (90 intros, 31% total summaries)
- `scripts/seed_timeline.py` ✓ (58 events)
- `scripts/seed_texts.py` ✓ (36 primary sources)
- `scripts/build_traditions.py` ✓ (9 traditions)
- `scripts/curate_terms.py` ✓ (5 generic terms flagged)

### Phase B Scripts (IN PROGRESS)
- `scripts/enrich_summaries.py` ✓ (161 summaries generated, 79% total)
- `scripts/generate_dictionary.py` ✓ (46 definitions inserted so far)
- `scripts/generate_biographies.py` — NOT YET WRITTEN
- `scripts/describe_timeline.py` — NOT YET WRITTEN
- `scripts/describe_texts.py` — NOT YET WRITTEN

### Project Skills (NOT YET CREATED)
- `.claude/skills/renmagdb-define/` — deferred, generating definitions directly instead
- `.claude/skills/renmagdb-bio/` — deferred
- `.claude/skills/renmagdb-catalog/` — deferred

### Schema Revisions Needed (from GNOSISDICTIONARYSTYLEANALYSISTAKEAWAYS.md)
1. Add `category_type` to dictionary_terms (ACTOR_TERM / ANALYST_TERM / HYBRID)
2. Add `relationship_type` to figure_traditions join table
3. Add `reception_history` to texts table
4. Add `cited_documents` join table (terms → corpus documents that informed the definition)
5. Consider `self_description` and `external_label` fields on figures

### Swarm Constraints (from SWARMRMDB.md + BLUNDER4)
- Agents CANNOT: Bash, Python, SQL, pip, any shell command
- Agents CAN: Read, Write, Glob, Grep, WebFetch
- Use staging/ protocol: main session exports context → agent writes content → main session validates + inserts
- Main session handles ALL database operations

---

## Key Architectural Shift: The Copenhaver/Hanegraaff Reframing

RMESSAY1.md and the Gnosis Dictionary analysis revealed that our database categories need to reflect current scholarship, not the Yatesian "Hermetic tradition" narrative. This means:

1. **Tradition labels are navigation aids, not ontological claims** — present as overlapping lenses, not discrete boxes
2. **Distinguish actor terms from analyst terms** — what Renaissance figures called their work vs what scholars call it
3. **Figures are complex actors, not "magicians"** — lead biographies with what they DID, not which tradition they "belonged to"
4. **Include historiographic events on the timeline** — Yates 1964, Copenhaver's critiques, Hanegraaff 2006
5. **Major dictionary entries use flowing prose** — not the sectioned format, for tradition-level concepts

These revisions should be applied to WRITING_TEMPLATES.md and the Phase B generation prompts before continuing content generation.

---

*Generated by hiro-plantagenet (third pass) for RenMagDB v2. Updated with essay findings, Gnosis style analysis, and swarm constraints.*
