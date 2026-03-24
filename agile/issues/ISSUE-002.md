# ISSUE-002: Heuristic Classification Covers 71% (238/337) vs 80% Target

**Type:** DATA_QUALITY
**Severity:** LOW
**Status:** OPEN
**Related:** TICKET-022, EPIC-02

## Description

classify_heuristic.py classified 238/337 documents (71%), missing the 80% target by 9 percentage points. 99 documents remain UNKNOWN.

## Analysis

Classification breakdown: ARTICLE=90, MONOGRAPH=82, REVIEW=41, PRIMARY_SOURCE=23, ANTHOLOGY=2.

The 99 ambiguous cases are likely:
- Short-to-medium PDFs (40-150 pages) without clear journal indicators
- Edited volumes/chapters that don't match monograph or article patterns
- Works with unconventional filenames

## Resolution

Accept for v1. 71% is still a strong majority, and the ambiguous cases are genuinely hard to classify without reading content. These are ideal candidates for Layer 4 LLM classification in v2.
