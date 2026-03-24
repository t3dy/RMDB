# SWARMRMDB.md — Eldritch Swarm Analysis
## Renaissance Magic Database Project

**Date:** 2026-03-23
**Analyst:** Claude (plan-eldritch-swarm)
**Context:** Post-BLUNDER4. Reassessing what agents can and cannot do.

---

## THE HARD CONSTRAINT

**Background agents in Claude Code CANNOT run Bash or Python.** This was documented in AtalantaClaudiens' SWARMGUIDELINES.md, confirmed by BLUNDER4 (two summary agents failed because they couldn't execute sqlite3 writes), and is a permanent architectural limitation.

Agents CAN:
- Read files (Read tool)
- Search files (Glob, Grep)
- Write files (Write, Edit tools)
- Fetch web content (WebFetch)
- Launch sub-agents (Agent tool)

Agents CANNOT:
- Run Python scripts (Bash tool blocked)
- Execute SQL queries
- Install packages
- Run any shell command
- Interact with databases directly

---

## SAFE SWARM PATTERNS FOR RenMagDB

### Pattern 1: Research Agents (SAFE)

**Use for:** Exploring the corpus, reading markdown files, extracting information for the main session to process.

```
Agent reads md/ files → writes findings to staging/ JSON → main session reads + inserts into DB
```

**Example tasks:**
- "Read the first 2000 chars of each Dee document and list all person names mentioned" → agent writes `staging/dee_persons.json`
- "Read KWIC concordance for 20 terms and draft definition_brief for each" → agent writes `staging/draft_definitions.json`
- "Read figure seed data and draft biography outlines" → agent writes `staging/bio_outlines.json`

### Pattern 2: Writing Agents (SAFE)

**Use for:** Generating content (definitions, summaries, biographies) that the main session then validates and inserts.

```
Main session exports context to staging/ → Agent reads context + generates content → writes to staging/ → Main session validates + inserts into DB
```

**Example workflow:**
1. Main session runs: `python export_term_context.py` → creates `staging/term_contexts.json` with KWIC + metadata per term
2. Agent reads `staging/term_contexts.json` + `docs/WRITING_TEMPLATES.md`
3. Agent writes `staging/definitions_batch_1.json` with generated definitions
4. Main session runs: `python import_definitions.py staging/definitions_batch_1.json` → validates + inserts

### Pattern 3: Audit Agents (SAFE)

**Use for:** Reviewing generated content, checking data quality, producing reports.

```
Main session exports DB state to JSON → Agent reads + audits → writes report to staging/
```

**Example tasks:**
- "Review these 30 biographies for voice consistency against WRITING_TEMPLATES.md"
- "Check these definitions for the BLUNDER3 violation (external knowledge injection)"
- "Audit cross-references: do all cited documents exist in the documents table?"

### Pattern 4: Parallel Research (SAFE)

**Use for:** Exploring multiple folders/topics simultaneously.

```
Launch 2-3 Explore agents in parallel, each searching different folders
```

**Example:** "Agent 1: analyze Dee folder for Enochian terms. Agent 2: analyze Pico folder for Kabbalistic terms. Agent 3: analyze root files for general magic themes."

---

## UNSAFE SWARM PATTERNS (DO NOT USE)

### Anti-Pattern 1: Database-Writing Agents ❌
**What BLUNDER4 tried:** Agent generates summaries AND inserts them into SQLite.
**Why it fails:** Agent can't run `python` or `sqlite3`.
**Fix:** Agent writes to staging JSON. Main session inserts.

### Anti-Pattern 2: Script-Running Agents ❌
**What it would try:** Agent runs `python scripts/extract_terms.py`.
**Why it fails:** No Bash access.
**Fix:** Main session runs all scripts. Agents only read/write files.

### Anti-Pattern 3: API-Calling Agents ❌
**What it would try:** Agent calls Wikidata API or other external services.
**Why it fails:** No Bash for `curl` or `python requests`. WebFetch might work but is unreliable for APIs.
**Fix:** Main session handles all API calls. (Or better: don't call APIs — BLUNDER3.)

### Anti-Pattern 4: Validation Agents That Need DB Access ❌
**What it would try:** Agent checks "does this figure ID exist in the database?"
**Why it fails:** Can't query SQLite.
**Fix:** Export validation data to JSON first, then agent reads JSON.

---

## RECOMMENDED SWARM ARCHITECTURE FOR v2 PHASE B

### Main Session Responsibilities (CANNOT DELEGATE)
- All Python script execution
- All database reads and writes
- All pip/spacy/library operations
- Running gate tests
- Schema migrations

### Delegatable to Agents
| Task | Agent Type | Input | Output |
|------|-----------|-------|--------|
| Draft dictionary definitions | Writing agent | staging/term_contexts.json | staging/definitions_batch_N.json |
| Draft figure biographies | Writing agent | staging/figure_contexts.json | staging/bios_batch_N.json |
| Draft text significance | Writing agent | staging/text_contexts.json | staging/text_sigs.json |
| Audit generated content | Audit agent | staging/*_batch_N.json + WRITING_TEMPLATES.md | staging/audit_report.json |
| Research specific figures | Explore agent | md/{folder}/ | staging/research_{figure}.json |

### The Staging Directory Protocol

```
staging/
├── term_contexts.json          # Exported by main session (Python)
├── figure_contexts.json        # Exported by main session (Python)
├── text_contexts.json          # Exported by main session (Python)
├── definitions_batch_1.json    # Written by writing agent
├── definitions_batch_2.json    # Written by writing agent
├── bios_batch_1.json           # Written by writing agent
├── text_sigs.json              # Written by writing agent
├── audit_report.json           # Written by audit agent
└── ... (one file per agent output)
```

**Rule:** Agents write to `staging/`. Main session reads from `staging/` and writes to `db/`. This is a one-way flow. Agents never touch `db/`.

---

## PARALLELISM OPPORTUNITIES

Given the staging pattern, these tasks can be parallelized:

1. **Dictionary definitions:** Split 147 terms into 3 batches by domain. Launch 3 writing agents in parallel, each producing a staging JSON.
2. **Figure biographies:** Split 29 figures into 2 batches (15 corpus-rich + 14 sparse). Launch 2 writing agents.
3. **Text significance:** All 36 texts in one batch (small enough for one agent).

**Maximum parallel agents:** 3 (Claude Code limit)

**Expected speedup:** 2-3x for dictionary definitions (the largest task)

**BUT:** Given BLUNDER4's lesson, consider whether the complexity of the staging protocol is worth it versus just doing the work sequentially in the main session. For 147 definitions at ~30 seconds each, sequential processing takes ~75 minutes. Parallel with staging overhead might save 30 minutes but adds debugging complexity.

**Recommendation:** Use agents for RESEARCH and AUDIT. Do content GENERATION in the main session where DB access is available. The staging protocol is justified only for very large batches (>100 items) where parallelism provides clear time savings.

---

*Generated by plan-eldritch-swarm for the Renaissance Magic Database Project. Incorporates lessons from BLUNDER4 and AtalantaClaudiens SWARMGUIDELINES.md.*
