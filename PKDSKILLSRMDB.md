# PKDSKILLSRMDB.md — PKD Skills Deployment Map
## Renaissance Magic Database Project

**Date:** 2026-03-23
**Analyst:** Claude (skill inventory review)
**Subject:** How the 37 PKD skills apply to planning and building RenMagDB

---

## Executive Summary

Of 37 available skills, **24 are directly applicable** to RenMagDB across the project lifecycle. The project is a perfect fit for the PKD system because it's fundamentally a **knowledge corpus + research system + scholarly publication** — exactly the domain these skills were designed for.

Key insight: RenMagDB can be built almost entirely through skill-driven workflow, with each skill triggering at natural project inflection points. The skills below are organized by when they fire in the project lifecycle.

---

## PHASE 0: PRE-BUILD PLANNING (Before any code)

### Already Completed

| Skill | Status | Output |
|-------|--------|--------|
| `/plan-deckard-boundary` | DONE | `DECKARDRMDB.md` — deterministic vs LLM task map |
| `/hiro-plantagenet` | DONE | `HIRORMDB.md` — 6-layer decomposition |
| `/plan-buckman-critic` | DONE | `BUCKMANONTRMDB.md` — ontology critique |

### Still Needed

| Skill | Purpose for RenMagDB | Priority | When |
|-------|----------------------|----------|------|
| `/plan-joe-chip-scope` | **Freeze v1 scope.** We have a 6-layer plan but haven't formally defined what "v1 done" means. Is v1 just the catalog? Catalog + dictionary? Full site? This prevents scope creep across layers. | CRITICAL | Before Layer 0 |
| `/plan-runciter-slice` | **Define vertical slices with acceptance gates.** Each slice should deliver one visible feature end-to-end: (1) document catalog, (2) figure profiles, (3) dictionary, (4) timeline, (5) library, (6) search. Each slice has PASS criteria. | CRITICAL | After joe-chip-scope |
| `/plan-lampton-corpus` | **Analyze the actual corpus.** We've inventoried files but haven't analyzed what the corpus CONTAINS — entities, topics, relations, coverage gaps. Lampton is designed exactly for this: take a document collection and extract its knowledge structure. Run on the .md files after Layer 1 conversion. | CRITICAL | After Layer 1 |
| `/plan-brady-graph` | **Design the knowledge graph.** After Lampton identifies entities and relations, Brady structures them into a queryable graph: node types, edge types, properties, evidence chains. This directly informs the `figure_influences`, `text_traditions`, and cross-reference join tables. | HIGH | After lampton-corpus |
| `/plan-bohlen-constraint` | **Ground the "full intellectual genealogy" decision.** User wants library scope from ancient through Islamic intermediaries to Renaissance. Bohlen asks: what information do we ACTUALLY HAVE? Liana Saif's book covers the Islamic thread. What covers the patristic? The ancient? Bohlen prevents promising more than the corpus can deliver. | HIGH | After lampton-corpus |
| `/plan-mayerson-prereq` | **Verify environment before building.** Check Python 3.14 compatibility with all libraries, verify spaCy model downloads, confirm SQLite version supports FTS5, test PyMuPDF on sample PDFs. | HIGH | Before Layer 1 |

---

## PHASE 1: BUILDING (Layers 0-3)

| Skill | Purpose for RenMagDB | When to Fire |
|-------|----------------------|-------------|
| `/plan-buckman-execute` | **Convert the plan into a task list.** Takes the 6-layer plan and produces concrete file-by-file task lists with session estimates and critical path. | Start of Layer 0 |
| `/plan-steiner-gate` | **Gate check between layers.** Before moving from Layer 1 → 2 → 3, verify acceptance criteria are met. "Did all 358 files convert? Did the schema pass sample row insertion? Did NER extract at least 20 figures?" | At every layer boundary |
| `/plan-kevin-pipeline` | **Break complex extraction prompts into stages.** If the Layer 3 NER + term extraction + abstract extraction pipeline gets tangled, Kevin splits it into clean stages with defined inputs/outputs per stage. | If any Layer 3 script tries to do too much |
| `/plan-abendsen-parking` | **Park new ideas.** When building the catalog you'll think "we should also add image analysis" or "let's scrape JSTOR metadata." PARK IT. Don't expand scope mid-layer. | Every time a new idea surfaces during building |
| `/plan-isidore-tokens` | **Optimize prompts before LLM layers.** Before Layer 4 sends 100+ documents to Claude for summarization, Isidore audits the prompt for redundancy and compression. Saves 20-40% on token cost. | Before Layer 4 execution |
| `/plan-regan-simplify` | **Review code after each script.** After writing convert_pdf.py, ingest_documents.py, etc., Regan checks for reuse opportunities, quality issues, N+1 queries. | After completing each script |

---

## PHASE 2: LLM ENRICHMENT (Layers 4-5)

| Skill | Purpose for RenMagDB | When to Fire |
|-------|----------------------|-------------|
| `/plan-buckman-critic` | **Critique every LLM prompt before execution.** The dictionary generation prompt, biography prompt, and classification prompt should each pass Buckman review. Score on 8 dimensions, fix weaknesses BEFORE burning tokens. | Before each Layer 4/5 script runs |
| `/plan-deckard-boundary` | **Re-check boundaries after data.** After Layer 3, re-run Deckard to see if new information changes the boundary map. Maybe TF-IDF handled topic tagging so well that Layer 4 LLM tagging isn't needed. | After Layer 3, before Layer 4 |
| `/plan-eldritch-swarm` | **Design multi-agent processing.** If Layer 4/5 batch processing benefits from parallel agents (one for classification, one for summarization, one for term definitions), Eldritch defines roles, communication artifacts, and handoff patterns. | If batch processing warrants parallelism |
| `/plan-fat-compress` | **Compress Renaissance magic concepts into reusable prompt components.** Your corpus contains dense conceptual frameworks (Hermetic philosophy, Kabbalistic tree, alchemical stages). Fat extracts these into structured concept blocks that can be injected into LLM prompts as context. | Before Layer 5 dictionary/biography generation |

---

## PHASE 3: WEBSITE & CONTENT (Layers 5-6)

| Skill | Purpose for RenMagDB | When to Fire |
|-------|----------------------|-------------|
| `/write-dominic-template` | **Create writing templates for every content type.** Dictionary entries, figure biographies, timeline event descriptions, library catalog entries, essays — each needs a template with sections, word targets, required elements, and tone. This feeds `docs/WRITING_TEMPLATES.md` and the Layer 5 generation scripts. | Before Layer 5 |
| `/write-dekany-style` | **Enforce style consistency.** After generating 800 dictionary entries and 30 biographies, Dekany audits for style drift: tense consistency, terminology, formality level, citation format. Catches "some entries say 'alchemy' and others say 'alchymie'." | After Layer 5, before Layer 6 |
| `/write-archer-evaluate` | **Evaluate generated content quality.** Score biographies and dictionary entries against structured criteria. Identify the weakest entries for revision. | After Layer 5 |
| `/write-rachael-aesthetic` | **Audit the site's visual design.** Color system, typography hierarchy, spacing logic. Does the warm parchment palette communicate "scholarly" or "crafty"? Does the dictionary page's layout work for Latin terms with diacritics? | During Layer 6 |
| `/write-runciter-ux` | **Full UX audit of the finished site.** Navigation, search, data display, responsive layout, accessibility, information architecture. The paired audit covers both functionality and design. | After Layer 6, before deploy |
| `/write-chip-copy` | **Audit all user-facing text.** Button labels, search placeholders, empty states, error messages, tooltips, breadcrumbs. Catches "Search scholars" vs "Find people" inconsistencies. | After Layer 6, before deploy |

---

## PHASE 4: LAUNCH & RETROSPECTIVE

| Skill | Purpose for RenMagDB | When to Fire |
|-------|----------------------|-------------|
| `/github-pages-deploy` | **Deploy to GitHub Pages.** Handle the static site deployment, troubleshoot 404s, configure custom domain if needed. | After Layer 6 passes UX audit |
| `/plan-tagomi-briefing` | **Generate a briefing for future sessions.** After v1 ships, create a structured briefing so any future Claude Code session can pick up where you left off. | After v1 deploy |
| `/plan-arctor-retro` | **Run a retrospective.** What worked in the 6-layer pipeline? What failed? What would you do differently? Extracts lessons for v2. | After v1 deploy |
| `/plan-runciter-audit` | **Audit for failure modes.** Mid-project or post-v1, identify anti-patterns, fragile scripts, missing error handling, data integrity risks. | Mid-project or post-v1 |

---

## SKILLS NOT NEEDED (and why)

| Skill | Why Not |
|-------|---------|
| `/plan-fatmode-growth` | RenMagDB uses familiar tech (Python, SQLite, static HTML). No steep learning curve to manage. |
| `/plan-pris-pedagogy` | RenMagDB is a reference tool, not a teaching game. If an educational component is added later, revisit. |
| `/plan-taverner-curriculum` | Same — no curriculum component in v1. PARK for v2. |
| `/plan-freck-narrative` | Nice-to-have for a README or blog post but not critical path. |
| `/plan-bulero-refactor` | Premature — the system doesn't exist yet. Run this if the codebase bloats during building. |
| `/plan-mercer-reframe` | Useful if a feature request feels wrong, but no feature requests yet. On-call basis. |
| `/plan-rosen-artifact` | JSON schemas can be written directly from ONTOLOGY.md. Rosen adds a layer of indirection. |
| `/pkdbiostyle` | PKD-specific biographical formatting. Not directly applicable. Could adapt the pattern. |
| `/pkdquerypataudit` | PKD Exegesis-specific audit. Could adapt as a template for RenMagDB audit. |
| `/write-isidore-critique` | For evaluating argumentative writing. Dictionary entries and bios don't make arguments. |
| `/pdf-catalog` | Overlaps with what we're building custom. RenMagDB's catalog is more sophisticated. |

---

## RECOMMENDED SKILL SEQUENCE (Full Project)

```
PRE-BUILD:
  1. /plan-joe-chip-scope          → freeze v1 scope
  2. /plan-runciter-slice          → define vertical slices + acceptance gates
  3. /plan-mayerson-prereq         → verify environment

LAYER 0 (Infrastructure):
  4. /plan-buckman-execute         → convert plan to task list

LAYER 1 (Conversion):
  5. /plan-steiner-gate            → verify conversion complete
  6. /plan-lampton-corpus          → analyze corpus contents
  7. /plan-brady-graph             → design knowledge graph from corpus
  8. /plan-bohlen-constraint       → ground library scope in actual data

LAYER 2 (Schema):
  9. /plan-steiner-gate            → verify schema passes sample rows

LAYER 3 (Deterministic Data):
  10. /plan-regan-simplify         → review scripts for quality
  11. /plan-steiner-gate           → verify data population complete
  12. /plan-deckard-boundary       → re-check boundaries with real data

LAYER 4 (LLM Enrichment):
  13. /plan-isidore-tokens         → optimize prompts
  14. /plan-buckman-critic         → critique each LLM prompt
  15. /plan-fat-compress           → compress domain concepts for prompts
  16. /plan-steiner-gate           → verify enrichment complete

LAYER 5 (Content Generation):
  17. /write-dominic-template      → create writing templates
  18. /plan-buckman-critic         → critique generation prompts
  19. /write-dekany-style          → audit style consistency
  20. /write-archer-evaluate       → evaluate content quality
  21. /plan-steiner-gate           → verify content complete

LAYER 6 (Site Build):
  22. /write-rachael-aesthetic     → audit visual design
  23. /write-runciter-ux           → full UX audit
  24. /write-chip-copy             → audit UI text

DEPLOY:
  25. /github-pages-deploy         → publish
  26. /plan-tagomi-briefing        → create briefing for future work
  27. /plan-arctor-retro           → retrospective

THROUGHOUT:
  /plan-abendsen-parking           → park every new idea that emerges
  /plan-steiner-gate               → gate check at every layer boundary
  /plan-kevin-pipeline             → if any script/prompt gets tangled
```

---

## NEW PROJECT-SPECIFIC SKILLS TO CREATE (3)

Based on the project's unique needs, create these skills in `.claude/skills/`:

### 1. `/renmagdb-define` — Dictionary Term Generation
- **Purpose:** Generate dictionary entries from KWIC concordance + corpus context
- **Input:** Term, concordance lines, domain classification, related terms
- **Output:** `definition_brief` (≤100 chars), `definition_long` (3-5 sentences), `domain`, `registers` (if multi-register), `significance_to_renaissance_magic`
- **Voice:** Museum-curator scholarly
- **Constraint:** Must contain the term itself. Must cite at least one corpus source. Must provide English translation of Latin/Greek/Hebrew.

### 2. `/renmagdb-bio` — Figure Biography Generation
- **Purpose:** Generate figure biographies from Wikidata facts + corpus references
- **Input:** Figure name, Wikidata JSON, corpus document list, NER mentions, tradition associations
- **Output:** `biography` (2-4 paragraphs), `significance` (1-2 sentences), `key_works` list, `intellectual_context`
- **Voice:** Museum-curator scholarly
- **Constraint:** Must reference at least 1 corpus document. Must place figure in intellectual tradition(s). Must note figure's relationship to magic specifically.

### 3. `/renmagdb-catalog` — Document Classification + Summary
- **Purpose:** Classify and summarize documents where Python heuristics failed
- **Input:** First 3 pages of .md file, filename metadata, heuristic classification attempt (if any)
- **Output:** `doc_type`, `summary` (1-3 sentences, ≤500 chars), `topic_tags` (from controlled vocabulary), `relevance` score
- **Voice:** Concise scholarly
- **Constraint:** `doc_type` must be one of ENUM values. Summary must contain author surname. Topic tags must exist in `topics` table or be flagged as NEW.

---

## CORPUS-SPECIFIC NOTE: Liana Saif

The user flagged Liana Saif's book (`saif arabic influences occult phil.pdf`) as the primary source for the Islamic intellectual genealogy thread. This means:

- `/plan-lampton-corpus` should give special attention to this text when mapping the Arabic/Islamic transmission path
- `/plan-bohlen-constraint` should use Saif's coverage to ground what we can and can't say about Islamic intermediaries
- The `texts` table should include Arabic sources Saif identifies (Al-Kindi's *De Radiis*, Picatrix/*Ghāyat al-Ḥakīm*, pseudo-Aristotelian *Sirr al-Asrār*, etc.)
- Dictionary terms should include Arabic terminology Saif uses alongside Latin equivalents

---

*Generated by PKD skill system review for the Renaissance Magic Database Project.*
