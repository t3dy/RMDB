# BLUNDER1: Proposed LLM PDF Reading Instead of Python Scripting

**Type:** DESIGN_DECISION
**Severity:** MEDIUM
**Status:** RESOLVED
**Sprint discovered:** Pre-sprint (planning phase)

## What Happened

When the user asked to convert all documents to markdown and build a database, I initially proposed using Claude's built-in PDF reader tool (which processes PDFs at 20 pages per request) as the conversion method. I framed the conversion options around token cost tiers (50K-100K vs 300K-500K vs "millions") as if LLM reading were the only approach.

The user correctly called this out: "why would it cost so many tokens to convert? Can't we use python scripting?"

## Root Cause

**Failure to think Python-first.** I defaulted to using the tools I have built-in (Claude's PDF reader) instead of considering that the user has a full Python environment with PyMuPDF, pdfminer, and pypdf already installed. This is exactly the kind of boundary violation that `/plan-deckard-boundary` is designed to catch — using LLM for a task that is fully deterministic.

## Impact

- Would have wasted ~50K-500K+ tokens on something that costs zero tokens via Python
- Would have been dramatically slower (sequential 20-page reads vs. batch scripted extraction)
- Would have produced worse results (Claude's PDF reader is less reliable than PyMuPDF for structured extraction)

## How It Was Caught

User's direct correction during the planning Q&A phase.

## How To Avoid Next Time

1. **Run `/plan-deckard-boundary` BEFORE proposing solutions.** The boundary map would have immediately flagged "PDF text extraction" as DETERMINISTIC/WASTE.
2. **Default assumption: if Python can do it, Python should do it.** LLM is a last resort for tasks requiring judgment, not a first resort for everything.
3. **Check `pip list` and installed libraries before proposing any data processing approach.** The available tooling should shape the solution.
4. **Ask "what Python library handles this?" before asking "how many tokens will this cost?"**

## Resolution

Adopted Python-first approach across the entire pipeline. The Deckard boundary analysis now explicitly lists 10 WASTE violations where LLM would be used for tasks Python handles better.
