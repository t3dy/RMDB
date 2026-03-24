# BLUNDER3: Wikidata API for Biographical Data Instead of Using Corpus

**Type:** DESIGN_DECISION
**Severity:** MEDIUM
**Status:** RESOLVED
**Sprint discovered:** SPRINT-01

## What Happened

The plan called for fetching biographical data (birth/death dates, nationality, key works) from the Wikidata API for seeded figures. Two failures:

1. **First attempt: 403 Forbidden** — Wikidata blocks requests without a User-Agent header. The script didn't set one. Easily fixable but shouldn't have been needed.

2. **Second attempt: Wrong data** — After fixing User-Agent, most Wikidata entity IDs pointed to wrong entities or disambiguation pages. "John Dee" resolved to "position in association football." "Heinrich Cornelius Agrippa" resolved to "mountain." Only ~5 of 29 figures got correct data.

## Root Cause

**Going outside the corpus when the corpus has the information.** We have 337 documents specifically about these figures. The corpus ITSELF is the best source for biographical data about Renaissance magicians — far better than Wikidata, which is a general encyclopedia that can't reliably disambiguate obscure historical figures.

More fundamentally, this is BLUNDER1 again in a different form: reaching for an external tool (Wikidata API) instead of using what we already have (the corpus). The Deckard boundary analysis should have flagged this — biographical fact extraction from a known corpus is at most a HYBRID task (deterministic extraction for dates, LLM for synthesis), not an API call.

## How It Should Have Been Done

1. **Hardcode the 29 known figures** with biographical data drawn from the user's own domain knowledge (which is what we ended up doing)
2. For v2, **extract biographical details from the corpus itself** using NER dates + corpus passages about each figure
3. Wikidata is a FALLBACK for figures the corpus doesn't cover, not the primary source

## Lesson

**The corpus is the source of truth.** Don't go looking elsewhere for information that the documents contain. This principle should be in CLAUDE.md as an operating rule.

## Resolution

Replaced Wikidata API integration with `data/figures_seed.json` — a curated JSON file with hardcoded biographical data for 29 figures. The data is drawn from standard scholarly knowledge about these figures. For v2, biographies will be generated from corpus passages, not API calls.
