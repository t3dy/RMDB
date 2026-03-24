# DEKANYRMDB.md — Dekany Style Audit
## Renaissance Magic Database — Generated Content

**Date:** 2026-03-23
**Analyst:** Claude (write-dekany-style)
**Scope:** 139 dictionary definitions + 266 document summaries

---

## STYLE AUDIT: Dictionary Definitions (139 entries)

### INCONSISTENCIES

| Type | Where | Example A | Example B | Recommendation |
|------|-------|-----------|-----------|---------------|
| **Opening pattern** | definition_long | "Logos ('word' or 'reason') designates..." | "The Heptarchia Mystica ('Mystical Heptarchy') is..." | STANDARDIZE: all entries should open with the Latin/Greek term followed by a gloss, then "designates/denotes/is" |
| **Parenthetical gloss** | definition_long | "Katharsis (Greek: 'purification')" with language tag | "Anima mundi ('soul of the world')" without tag | STANDARDIZE: always include language tag: "Term (Language: 'translation')" |
| **Article usage** | definition_long | "The Zohar is..." (with article) | "Kabbalah designates..." (no article) | OK — proper nouns take articles, generic terms don't. This is CORRECT variation. |
| **Cross-ref format** | definition_long | "*sephiroth*" italicized | "Corpus Hermeticum" not italicized | STANDARDIZE: all term cross-refs italicized, all work titles italicized |
| **Figure naming** | definition_long | "Ficino" (surname only) | "Marsilio Ficino" (full name) | STANDARDIZE: full name on first mention per entry, surname thereafter |
| **Citation format** | definition_long | "(Yates, Bruno and the Hermetic Tradition)" | "(Walker, Spiritual and Demonic Magic)" | CONSISTENT — good. Both use (Author, Short Title). |
| **Length** | definition_long | Average ~79 words | Template target: 100-200 words | SHORT: most entries are below the minimum. Second batch may be even shorter. |
| **Verb tense** | definition_long | "designates" (present) for what terms mean | "Ficino translated" (past) for historical events | CORRECT — matches WRITING_TEMPLATES.md rules. |

### PRIMARY STYLE DRIFT: **Definition length runs short (avg 79 words vs 100-200 target)**

This is the single biggest consistency issue. The first batch (46 entries) ran longer; the second batch (93 entries) appears to average shorter. This creates an uneven reading experience where some entries are substantive essays and others are quick glosses.

---

## STYLE AUDIT: Document Summaries (266 entries)

### INCONSISTENCIES

| Type | Where | Example A | Example B | Recommendation |
|------|-------|-----------|-----------|---------------|
| **Source method mixing** | summary field | Clean scholarly prose (DETERMINISTIC abstracts) | Raw text dumps (LLM_ASSISTED heuristic) | CRITICAL: heuristic summaries are extracting RAW TEXT, not generating prose |
| **Author name** | summary start | "Copenhaver examines..." (good) | "test examines Pico scholarship" (bad — "test" is filename noise) | FIX: validate author extraction before summary generation |
| **JSTOR boilerplate** | summary content | "JSTOR is a not-for-profit..." | actual scholarly content | CRITICAL: JSTOR terms-of-use text contaminating summaries |
| **OCR quality** | summary content | "OCR quality insufficient" (honest) | Garbled text presented as summary | FIX: OCR entries are correct; garbled text masquerading as summaries is worse |
| **TOC as summary** | summary content | Table of contents extracted as if it were a summary | Actual thesis statement | FIX: TOC extraction is NOT a summary — it's metadata |
| **Methodology** | absent | None of the summaries include methodology | Template now requires it | NEEDS REGENERATION: methodology field is empty for all 266 docs |

### PRIMARY STYLE DRIFT: **Heuristic summaries are raw text extraction, not scholarly prose**

The `enrich_summaries.py` script extracts first paragraphs and thesis statements via regex, but the results are often raw OCR text, JSTOR boilerplate, tables of contents, or sentence fragments — NOT the museum-curator scholarly summaries the template requires. The 15 regex-extracted abstracts and 5 true LLM-generated summaries are the only ones that match the intended voice.

**This is a quality problem, not a style problem.** The heuristic summaries should be flagged as `confidence='LOW'` and regenerated with actual LLM judgment in a future pass.

---

## STYLE GUIDE (Inferred from best examples)

| Dimension | Standard | Source |
|-----------|----------|--------|
| **Tense** | Present for definitions and arguments ("designates," "argues"); past for events ("translated," "published") | WRITING_TEMPLATES.md + consistent in definitions |
| **Voice** | Active preferred ("Ficino translated") over passive ("was translated by Ficino") | Consistent in definitions |
| **Formality** | Museum-curator scholarly: precise, specific, attributive | Consistent |
| **Person** | Third person throughout | Consistent |
| **Terminology** | Latin terms italicized; English glosses in parentheses on first use | Mostly consistent, some misses |
| **Citations** | (Author, Short Title) format | Consistent in definitions |
| **Capitalization** | Tradition names capitalized (Hermeticism, Kabbalah); Latin terms lowercase italic (*magia naturalis*) | Consistent |
| **Opening pattern** | term (Language: 'gloss') + "designates/denotes/is" | Needs standardization |

---

## FIXES NEEDED

### Critical (affects reader experience)
1. **Regenerate document summaries** using actual LLM judgment, not heuristic text extraction. Current summaries are raw text, not scholarly prose. (~160 summaries need rewriting)
2. **Add methodology field** to summaries when regenerating
3. **Clean JSTOR boilerplate** from summaries — detect and strip "JSTOR is a not-for-profit..." patterns
4. **Fix author extraction** — "test" as author surname, garbled names from OCR

### Important (consistency)
5. **Standardize definition_long opening** — term (Language: 'gloss') pattern for all
6. **Ensure full name on first mention** — "Marsilio Ficino" not just "Ficino" at first reference
7. **Italicize all cross-referenced terms** in definition_long consistently
8. **Extend short definitions** — second batch averages ~79 words, below 100-word minimum

### Minor (polish)
9. **Language tag in gloss** — always include: "(Greek: 'purification')" not just "('purification')"
10. **Work titles consistently italicized** — *De Occulta Philosophia* not "De Occulta Philosophia"

**Total: 10 inconsistencies. 4 critical, 4 important, 2 minor.**
**Quick fixes (find-replace): items 5, 6, 9 could be scripted.**
**Requires regeneration: items 1, 2, 8.**

---

*Generated by write-dekany-style for the Renaissance Magic Database Project.*
