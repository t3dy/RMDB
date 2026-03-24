# JOECHIPV2RMDB.md — Joe Chip Scope Freeze (v2)
## Renaissance Magic Database — LLM Enrichment + Content Generation

**Date:** 2026-03-23
**Analyst:** Claude (plan-joe-chip-scope)
**Status:** SCOPE FROZEN
**Prerequisite:** v1 gate passed (STEINERGATERMDB.md)

---

## What v1 Proved

v1 built a populated SQLite database with 337 documents, 29 figures, 186 terms, 12 topics, and 8,180 term-document links — all deterministic, zero LLM tokens. The foundation works.

## What v1 Left Undone (the enrichment gap)

| Gap | Count | What's needed |
|-----|-------|---------------|
| Unclassified documents | 99/337 | LLM doc_type assignment |
| Documents without summaries | 322/337 | LLM summarization (abstracts only caught 15) |
| Terms without definitions | 186/186 | LLM definition generation (brief + long) |
| Figures without biographies | 29/29 | LLM biography generation |
| Timeline events | 0 | LLM event descriptions from NER dates + seed data |
| Referenced primary texts (library) | 0 | LLM extraction + significance descriptions |
| Tradition taxonomy | 0 formalized | TF-IDF clusters need LLM naming + descriptions |
| Generic term curation | ~15 terms | "ens" (53K freq) etc. — too common, need filtering |

---

## Problem Decomposition

| # | Problem | Domain | Input | Output | Independent? | Depends on |
|---|---------|--------|-------|--------|-------------|------------|
| P1 | Curate generic terms (remove/recategorize overly common terms) | Data quality | dictionary_terms table | Cleaned term list | YES | Nothing |
| P2 | Classify 99 ambiguous documents | LLM classification | First 3 pages of .md | doc_type for 99 docs | YES | Nothing |
| P3 | Generate summaries for 322 documents | LLM summarization | First 3 pages of .md | summary field (≤500 chars) | YES | Nothing |
| P4 | Define writing templates (voice, structure, style) | Design | Decisions from planning | WRITING_TEMPLATES.md | YES | Nothing |
| P5 | Generate dictionary definitions (brief + long) | LLM content gen | KWIC concordance + term data | definition_brief, definition_long | NO | P1, P4 |
| P6 | Generate figure biographies | LLM content gen | Figures seed + corpus refs | biography field (2-4 para) | NO | P4 |
| P7 | Seed timeline events from NER dates + editorial | Hybrid | NER report + seed data | timeline_events populated | NO | P6 |
| P8 | Name TF-IDF clusters as traditions | LLM classification | topic_clusters.json | traditions described | NO | P2 |
| P9 | Extract primary source references (library) | LLM extraction | Corpus text + NER | texts table populated | NO | P3 |
| P10 | Create 3 project-specific Claude skills | Tooling | Skill designs | .claude/skills/renmagdb-* | YES | P4 |

---

## CORE PROBLEM

**v2 enriches the v1 database with LLM-generated content: classifications, summaries, definitions, biographies, and timeline events, following the writing templates and provenance model established in v1.**

---

## NON-GOALS (v2)

- **Static website.** No HTML generation, no Jinja2 templates, no CSS. That's v3.
- **Cross-reference/influence network.** No figure_influences edges. That's v4.
- **Essays.** No long-form analytical writing. v4.
- **Graph visualization.** v4.
- **Deployment.** Nothing to deploy yet.
- **Exhaustive library catalog.** v2 seeds the `texts` table with ~50 primary sources. Full coverage is v3+.
- **Semantic search / embeddings.** FTS5 is sufficient. RAG is unnecessary with this corpus size.

---

## VERSION 2 SCOPE

**v2 delivers: enriched database with LLM-generated content in every content field, ready to feed a site generator.**

Specifically:

1. **Writing templates finalized** (`docs/WRITING_TEMPLATES.md`) — museum-curator voice, per-content-type structure
2. **3 project Claude skills** (`/renmagdb-define`, `/renmagdb-bio`, `/renmagdb-catalog`)
3. **99 ambiguous documents classified** (doc_type assigned via LLM)
4. **~200 document summaries generated** (top-priority docs: monographs + unreviewed articles; skip reviews and docs with existing abstracts)
5. **Generic terms curated** (~15 overly common terms filtered or recategorized)
6. **~150 dictionary definitions generated** (brief + long, prioritized by frequency, skip generic philosophical terms)
7. **29 figure biographies generated** (2-4 paragraphs each, drawn from corpus, not external sources)
8. **~50 timeline events seeded** (from NER dates + curated key milestones)
9. **~50 primary source references** (texts table populated with referenced works + significance)
10. **TF-IDF clusters named** as proper tradition labels

**v2 exit test:**
- `SELECT COUNT(*) FROM documents WHERE doc_type IS NOT NULL` = 337 (100%)
- `SELECT COUNT(*) FROM documents WHERE summary IS NOT NULL` > 200
- `SELECT COUNT(*) FROM dictionary_terms WHERE definition_brief IS NOT NULL` > 140
- `SELECT COUNT(*) FROM figures WHERE biography IS NOT NULL` = 29
- `SELECT COUNT(*) FROM timeline_events` > 40
- `SELECT COUNT(*) FROM texts` > 40
- All LLM data tagged: `source_method='LLM_ASSISTED'`, `confidence='MEDIUM'`, `review_status='DRAFT'`

---

## TOKEN BUDGET STRATEGY

**Python-first, again.** Before spending LLM tokens:

1. **Batch by similarity.** Group documents by folder/topic so Claude gets thematic context once and processes many.
2. **Pre-extract context.** For each doc, Python assembles: filename metadata + first 2 pages of .md + abstract (if any) + folder figure. This is the LLM input — not the whole document.
3. **Structured output.** Every LLM prompt returns JSON with named fields. Validation rejects malformed responses.
4. **Skip where unnecessary.** Reviews don't need summaries (the review IS a summary). Primary sources may not need classification. Documents with abstracts already have summaries.

**Estimated token budget:**

| Task | Docs/Items | Input/item | Output/item | Total est. |
|------|-----------|-----------|------------|-----------|
| Classify 99 docs | 99 | ~2K | ~100 | ~210K |
| Summarize ~200 docs | 200 | ~3K | ~200 | ~640K |
| Define ~150 terms | 150 | ~1K (KWIC) | ~300 | ~195K |
| 29 biographies | 29 | ~3K | ~800 | ~110K |
| 50 timeline events | 50 | ~500 | ~200 | ~35K |
| 50 library entries | 50 | ~2K | ~300 | ~115K |
| Tradition naming | 12 | ~1K | ~200 | ~15K |
| **TOTAL** | | | | **~1.3M** |

This is ~1.3M tokens, achievable across 3-5 Claude Code sessions.

---

## LATER VERSIONS

### v3: Static Website
- Jinja2 site generator
- All page types: dictionary, figures, timeline, library, catalog, search
- CSS design system
- GitHub Pages deployment
- UX audit

### v4: Network + Advanced Features
- Cross-reference/influence network (figure_influences)
- Graph visualization
- Essays
- Advanced search (faceted, semantic)
- Educational modules

---

## DEPENDENCY ORDER (v2)

```
1. P4:  Writing templates          [Session 1, ~30 min]
        └── WRITING_TEMPLATES.md finalized
        └── Content structure per type defined

2. P10: Create 3 project skills    [Session 1, ~30 min]
        └── /renmagdb-define, /renmagdb-bio, /renmagdb-catalog

3. P1:  Curate generic terms       [Session 1, ~15 min]
        └── Filter/flag overly common terms

   ── Sessions 1 tasks are parallelizable ──

4. P2:  Classify 99 documents      [Session 2, ~45 min]
        └── LLM via /renmagdb-catalog prompts
        └── All doc_types assigned

5. P3:  Summarize ~200 documents   [Session 2-3, ~90 min]
        └── LLM via /renmagdb-catalog prompts
        └── Batch by folder for context efficiency

6. P5:  Dictionary definitions     [Session 3, ~60 min]
        └── LLM via /renmagdb-define prompts
        └── ~150 terms with brief + long definitions

7. P6:  Figure biographies         [Session 3-4, ~45 min]
        └── LLM via /renmagdb-bio prompts
        └── 29 biographies from corpus evidence

8. P7:  Timeline events            [Session 4, ~20 min]
        └── Seed from NER dates + curated milestones

9. P9:  Primary source references  [Session 4, ~30 min]
        └── Extract from corpus + LLM significance

10. P8: Tradition naming           [Session 4, ~10 min]
        └── LLM labels for 12 TF-IDF clusters

11. EXIT TEST                      [Session 4, ~10 min]
```

**Estimated total: 4 sessions.**

---

## SCOPE FREEZE RULES (v2)

1. **No website work.** If tempted to "just quickly" add a page template: PARK IT.
2. **No influence network.** If tempted to map who influenced whom: PARK IT.
3. **Provenance always.** Every LLM insertion: `source_method='LLM_ASSISTED'`, `confidence='MEDIUM'`, `review_status='DRAFT'`.
4. **Validate before insert.** Every LLM response is validated against ENUM constraints before DB insertion.
5. **Corpus is the source.** Do NOT go to Wikipedia, Wikidata, or other external sources for content. The corpus has the information. (BLUNDER3 lesson.)
6. **Writing templates before content.** Do NOT generate biographies or definitions without `WRITING_TEMPLATES.md` finalized first.

---

*Generated by plan-joe-chip-scope for RenMagDB v2. Scope is now FROZEN.*
