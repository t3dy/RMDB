# EPIC-01: Proof of Pipeline

**Slice:** 1 (from SLICESLICEBABYRMDB.md)
**Status:** IN PROGRESS
**Sprint:** SPRINT-01
**Acceptance gate:** Full pipeline works on 7 Ficino files

## Tickets
| Ticket | Title | Status |
|--------|-------|--------|
| TICKET-001 | Create project scaffold | DONE |
| TICKET-002 | Write CLAUDE.md | DONE |
| TICKET-003 | Write docs/ | TODO |
| TICKET-004 | requirements.txt + pip install | DONE |
| TICKET-005 | Write convert_pdf.py | IN PROGRESS |
| TICKET-006 | Write convert_epub.py | TODO |
| TICKET-007 | Write convert_html.py | TODO |
| TICKET-008 | Convert Ficino folder | TODO |
| TICKET-009 | Write sample_rows.json | TODO |
| TICKET-010 | Write init_db.py | TODO |
| TICKET-011 | Write ingest_documents.py | TODO |
| TICKET-012 | Write extract_abstracts.py | TODO |
| TICKET-013 | Write classify_heuristic.py | TODO |
| TICKET-014 | Write extract_terms.py + seed list | TODO |
| TICKET-015 | Write extract_ner.py | TODO |
| TICKET-016 | Gate test | TODO |

## Gate Checklist
- [ ] All 7 Ficino files converted (0 EMPTY, ≤1 SCANNED)
- [ ] sample_rows.json inserted into all tables
- [ ] SELECT * FROM documents WHERE folder_figure='Ficino' returns 7 rows
- [ ] SELECT * FROM dictionary_terms returns >0 rows
- [ ] At least 1 abstract extracted from Ficino docs
- [ ] NER extracts "Marsilio Ficino" as PERSON
