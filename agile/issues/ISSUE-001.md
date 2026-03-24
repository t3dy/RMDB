# ISSUE-001: Abstract Extraction Rate Low (4% vs expected 70%)

**Type:** DATA_QUALITY
**Severity:** MEDIUM
**Status:** OPEN
**Related:** TICKET-021, EPIC-02
**Sprint discovered:** SPRINT-01

## Description

extract_abstracts.py found abstracts in only 15/337 documents (4%). The original estimate was ~70%.

## Root Cause

The 70% estimate assumed most PDFs are journal articles with structured "Abstract:" sections. In reality:
- ~82 documents are monographs (books) — these don't have abstracts
- ~41 are reviews — typically no abstract section
- ~23 are primary sources — no abstract
- Many journal articles in this corpus are older (1940s-1980s) and predate structured abstract conventions

The regex patterns look for explicit "Abstract" or "Summary" headers, which only exist in modern journal articles.

## Resolution Options

1. **Expand regex patterns** — look for introductory paragraphs, "This article argues...", "In this paper..." patterns
2. **Defer to Layer 4 LLM** — generate summaries for abstract-less docs (this was always the plan for v2)
3. **Accept the 4% rate** — these are the documents where deterministic extraction works; the rest need LLM

## Decision

Accept for v1. The 15 extracted abstracts prove the pipeline works. LLM summarization in v2 will cover the rest. Low abstract rate does NOT block Slice 2 gate — the PASS criterion was ">0", not ">200".
