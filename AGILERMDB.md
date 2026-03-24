# AGILERMDB.md — Agile Development Framework
## Renaissance Magic Database Project

**Date:** 2026-03-23
**Methodology:** Epic/Ticket/Issue hierarchy with sprint logs and velocity tracking
**Artifact location:** `agile/`

---

## Directory Structure

```
agile/
├── BOARD.md                    # Current board state (TODO / IN PROGRESS / DONE / BLOCKED)
├── BACKLOG.md                  # Prioritized backlog (unpromoted ideas, v2+ items)
├── VELOCITY.md                 # Session velocity tracking + burndown notes
├── epics/
│   ├── EPIC-01-proof-of-pipeline.md
│   ├── EPIC-02-bulk-scale.md
│   ├── EPIC-03-entity-extraction.md
│   └── EPIC-04-topics-search-exit.md
├── tickets/
│   ├── TICKET-001.md           # Individual work items
│   ├── TICKET-002.md
│   └── ...
├── issues/
│   ├── ISSUE-001.md            # Bugs, blockers, data quality problems
│   └── ...
├── sprints/
│   ├── SPRINT-01.md            # Session log: attempted, passed, blocked, velocity
│   └── ...
└── retros/
    └── RETRO-01.md             # Post-sprint retrospective (feeds /plan-arctor-retro)
```

---

## Naming Conventions

| Artifact | Pattern | Example |
|----------|---------|---------|
| Epic | `EPIC-NN-short-name.md` | `EPIC-01-proof-of-pipeline.md` |
| Ticket | `TICKET-NNN.md` | `TICKET-001.md` |
| Issue | `ISSUE-NNN.md` | `ISSUE-001.md` |
| Sprint | `SPRINT-NN.md` | `SPRINT-01.md` |
| Retro | `RETRO-NN.md` | `RETRO-01.md` |

Numbering is global and sequential. Tickets and issues share separate sequences. Sprints = 1 per Claude Code session.

---

## Artifact Templates

### Epic Template
```markdown
# EPIC-NN: [Name]

**Slice:** [which Runciter slice]
**Status:** TODO | IN PROGRESS | DONE | BLOCKED
**Sprint:** [which sprint(s)]
**Acceptance gate:** [from SLICESLICEBABYRMDB.md PASS criteria]

## Tickets
| Ticket | Title | Status | Assignee |
|--------|-------|--------|----------|
| TICKET-NNN | ... | TODO | Claude / User |

## Gate Checklist
- [ ] [PASS criterion 1]
- [ ] [PASS criterion 2]
- [ ] ...

## Notes
[running notes, decisions, discoveries]
```

### Ticket Template
```markdown
# TICKET-NNN: [Title]

**Epic:** EPIC-NN
**Status:** TODO | IN PROGRESS | DONE | BLOCKED
**Priority:** P0 (critical path) | P1 (important) | P2 (nice-to-have)
**Effort:** S (< 15 min) | M (15-60 min) | L (1-2 hrs) | XL (2+ hrs)
**Sprint:** [assigned sprint]

## Description
[What needs to be done — specific, actionable]

## Acceptance Criteria
- [ ] [testable criterion 1]
- [ ] [testable criterion 2]

## Dependencies
- [TICKET-NNN if any]

## Files
- [files to create/modify]

## Notes
[implementation notes, decisions, blockers encountered]
```

### Issue Template
```markdown
# ISSUE-NNN: [Title]

**Type:** BUG | BLOCKER | DATA_QUALITY | DESIGN_DECISION | TECHNICAL_DEBT
**Severity:** CRITICAL | HIGH | MEDIUM | LOW
**Status:** OPEN | IN PROGRESS | RESOLVED | WONTFIX
**Related:** [TICKET-NNN or EPIC-NN]
**Sprint discovered:** SPRINT-NN

## Description
[What's wrong or what decision needs to be made]

## Evidence
[error output, query results, file paths]

## Resolution
[how it was fixed, or why WONTFIX]
```

### Sprint Template
```markdown
# SPRINT-NN: [Date]

**Session:** [Claude Code session identifier]
**Epic focus:** EPIC-NN
**Duration:** [approximate hours]

## Goals
- [ ] [what we planned to accomplish]

## Completed
| Ticket | Title | Effort | Notes |
|--------|-------|--------|-------|
| TICKET-NNN | ... | M | ... |

## Blocked
| Ticket | Blocker | Resolution |
|--------|---------|------------|
| TICKET-NNN | [what blocked it] | [how/when resolved] |

## Issues Discovered
| Issue | Severity | Status |
|-------|----------|--------|
| ISSUE-NNN | ... | OPEN |

## Velocity
- Tickets completed: N
- Story points (S=1, M=2, L=3, XL=5): N
- Tickets blocked: N
- Issues opened: N

## Notes
[what we learned, what changed, what surprised us]
```

### Board Template (BOARD.md)
```markdown
# Agile Board — RenMagDB v1

**Last updated:** [date]
**Current sprint:** SPRINT-NN
**Current epic:** EPIC-NN

## BLOCKED
| Ticket | Blocker |
|--------|---------|

## IN PROGRESS
| Ticket | Title | Epic | Sprint |
|--------|-------|------|--------|

## TODO (this sprint)
| Ticket | Title | Epic | Priority | Effort |
|--------|-------|------|----------|--------|

## DONE
| Ticket | Title | Epic | Sprint | Effort |
|--------|-------|------|--------|--------|
```

---

## Epic Breakdown (v1)

### EPIC-01: Proof of Pipeline (Slice 1)

| Ticket | Title | Priority | Effort | Dependencies |
|--------|-------|----------|--------|-------------|
| TICKET-001 | Create project scaffold (folders, .gitignore, .claude/) | P0 | M | — |
| TICKET-002 | Write CLAUDE.md | P0 | M | — |
| TICKET-003 | Write docs/ (SYSTEM.md, ONTOLOGY.md, PIPELINE.md, INTERFACE.md, ROADMAP.md) | P0 | L | — |
| TICKET-004 | Write requirements.txt + pip install | P0 | S | TICKET-001 |
| TICKET-005 | Write convert_pdf.py | P0 | L | TICKET-004 |
| TICKET-006 | Write convert_epub.py | P1 | M | TICKET-004 |
| TICKET-007 | Write convert_html.py | P1 | M | TICKET-004 |
| TICKET-008 | Convert Ficino folder (7 files) | P0 | S | TICKET-005, -006 |
| TICKET-009 | Write data/sample_rows.json (5 examples) | P0 | M | — |
| TICKET-010 | Write init_db.py (Phase 1 schema) | P0 | XL | TICKET-009 |
| TICKET-011 | Write ingest_documents.py | P0 | L | TICKET-010 |
| TICKET-012 | Write extract_abstracts.py | P0 | M | TICKET-011 |
| TICKET-013 | Write classify_heuristic.py | P0 | M | TICKET-011 |
| TICKET-014 | Write extract_terms.py + data/latin_seed_list.json | P0 | L | TICKET-011 |
| TICKET-015 | Write extract_ner.py | P0 | L | TICKET-004 |
| TICKET-016 | Run full pipeline on Ficino folder + gate test | P0 | M | ALL above |

**Total: 16 tickets, ~24 story points**

### EPIC-02: Bulk Scale (Slice 2)

| Ticket | Title | Priority | Effort | Dependencies |
|--------|-------|----------|--------|-------------|
| TICKET-017 | Write convert_all.py (orchestrator) | P0 | M | EPIC-01 |
| TICKET-018 | Run conversion on full corpus (358 files) | P0 | M | TICKET-017 |
| TICKET-019 | Review conversion_manifest.json, triage quality flags | P0 | M | TICKET-018 |
| TICKET-020 | Run ingest_documents.py on full corpus | P0 | M | TICKET-018 |
| TICKET-021 | Run extract_abstracts.py on full corpus | P0 | S | TICKET-020 |
| TICKET-022 | Run classify_heuristic.py on full corpus | P0 | S | TICKET-020 |
| TICKET-023 | Write detect_language.py + run on full corpus | P0 | M | TICKET-020 |
| TICKET-024 | Write detect_duplicates.py + run on full corpus | P0 | M | TICKET-020 |
| TICKET-025 | Slice 2 gate test (8 PASS criteria) | P0 | S | ALL above |

**Total: 9 tickets, ~14 story points**

### EPIC-03: Entity Extraction (Slice 3)

| Ticket | Title | Priority | Effort | Dependencies |
|--------|-------|----------|--------|-------------|
| TICKET-026 | Expand data/latin_seed_list.json to ~300 terms | P0 | L | EPIC-02 |
| TICKET-027 | Run extract_terms.py on full corpus | P0 | M | TICKET-026 |
| TICKET-028 | Run extract_ner.py on full corpus | P0 | M | EPIC-02 |
| TICKET-029 | Write seed_figures.py (folder mapping + Wikidata) | P0 | L | TICKET-028 |
| TICKET-030 | Populate join tables (document_figures, term_documents) | P0 | M | TICKET-027, -029 |
| TICKET-031 | Populate era_assignments for figures | P0 | M | TICKET-029 |
| TICKET-032 | Slice 3 gate test (9 PASS criteria) | P0 | S | ALL above |

**Total: 7 tickets, ~14 story points**

### EPIC-04: Topics + Search + Exit (Slice 4)

| Ticket | Title | Priority | Effort | Dependencies |
|--------|-------|----------|--------|-------------|
| TICKET-033 | Write tag_tfidf.py + run on full corpus | P0 | L | EPIC-03 |
| TICKET-034 | Write build_fts.py (FTS5 index) | P0 | M | EPIC-03 |
| TICKET-035 | Write validate_data.py | P0 | L | EPIC-03 |
| TICKET-036 | Run full validation + generate report | P0 | M | TICKET-035 |
| TICKET-037 | v1 EXIT TEST (5 queries from Joe Chip scope) | P0 | S | ALL above |

**Total: 5 tickets, ~10 story points**

---

## v1 Totals

| Metric | Value |
|--------|-------|
| Epics | 4 |
| Tickets | 37 |
| Total story points | ~62 |
| Estimated sprints (sessions) | 4 |
| Target velocity | ~15 points/sprint |

---

## Velocity Tracking Protocol

After each sprint:
1. Record completed tickets + story points in SPRINT-NN.md
2. Update VELOCITY.md with cumulative data
3. Update BOARD.md (move tickets between columns)
4. If velocity < 10 points/sprint: investigate blockers
5. If velocity > 20 points/sprint: check if acceptance criteria are being cut

---

## Board Rules

1. **WIP limit:** Max 3 tickets IN PROGRESS at once
2. **Blocked escalation:** Any ticket blocked >30 min → create ISSUE, reassess approach
3. **Definition of Done:** All acceptance criteria checked off, files committed, gate test (if last ticket in epic) passes
4. **No silent scope changes:** New work → new ticket. If it's not in an epic, it goes to BACKLOG.md
5. **Sprint planning:** Start each session by reviewing BOARD.md, promoting from BACKLOG if ahead of schedule
6. **Sprint close:** End each session by writing SPRINT-NN.md with velocity data

---

*Generated for the Renaissance Magic Database Project. Integrates with Runciter slices (SLICESLICEBABYRMDB.md) and Joe Chip scope (JOECHIPSCOPERMDB.md).*
