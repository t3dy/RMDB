# BLUNDER5: Heuristic Summaries Are Raw Text Dumps, Not Scholarly Prose

**Type:** DATA_QUALITY
**Severity:** HIGH
**Status:** OPEN
**Sprint discovered:** SPRINT-01

## What Happened

`enrich_summaries.py` was designed to generate summaries for 161 documents by extracting thesis statements and first paragraphs via regex patterns. The Dekany style audit revealed that most of these "summaries" are actually:

1. **Raw OCR text** — garbled character sequences presented as summaries
2. **JSTOR boilerplate** — "JSTOR is a not-for-profit service..." legal text
3. **Tables of contents** — chapter listings, not thesis descriptions
4. **Sentence fragments** — mid-sentence cuts from introduction paragraphs
5. **Filename metadata** — title strings passed through as "summaries"

Only ~20 of the 266 summaries are actual scholarly prose (the 15 regex-extracted abstracts + 5 from the failed LLM agents).

## Root Cause

**Heuristic text extraction is not summarization.** The script's regex patterns (`This article argues...`, `This book examines...`) worked for ~7 documents. For the other 154, the fallback grabbed the first "meaningful sentence" — which, in OCR-extracted PDFs, is often JSTOR metadata, publisher boilerplate, or garbled text.

The deeper error: treating this as a DETERMINISTIC task when it's genuinely PROBABILISTIC. The Deckard boundary analysis correctly identified that summaries need LLM judgment, but the Python-first optimization strategy tried to squeeze more out of heuristics than they could deliver.

## Impact

- 154 document summaries are LOW quality (raw text, not prose)
- The `documents.summary` field is contaminated with non-summary content
- These summaries would embarrass the project if surfaced on a website
- The methodology field (new in schema v3) is empty for all 266 documents

## Lesson

**Python-first doesn't mean Python-only.** The Deckard boundary is real: summaries that capture what a document ARGUES require reading comprehension, which is LLM work. Regex can extract ABSTRACTS (structured text with markers), but cannot generate SUMMARIES (which require understanding the content).

## Resolution Options

1. **Mark heuristic summaries as LOW confidence** and regenerate with LLM in a focused pass
2. **Clear all heuristic summaries** and regenerate from scratch with proper LLM prompts
3. **Tier the summaries**: keep the 20 good ones (abstracts + LLM), clear the 154 bad ones, regenerate those

## Recommended: Option 3
Keep: 15 regex abstracts (source_method=DETERMINISTIC) + 5 LLM summaries
Clear: 154 heuristic extractions that are raw text dumps
Regenerate: those 154 with actual LLM reading of first 2-3 pages
