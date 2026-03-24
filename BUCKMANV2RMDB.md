# BUCKMANV2RMDB.md — Buckman Critic: v2 LLM Prompt Review
## Renaissance Magic Database Project

**Date:** 2026-03-23
**Analyst:** Claude (plan-buckman-critic)
**Subject:** Three core LLM prompts for v2 enrichment scripts

---

## PROMPT A: Document Classification + Summary (`/renmagdb-catalog`)

### Draft Prompt

```
You are classifying and summarizing academic documents about Renaissance magic.

DOCUMENT METADATA:
- Filename: {filename}
- Folder: {folder} (primary figure: {folder_figure})
- Extracted author: {author}
- Extracted year: {year}
- Page count: {pages}
- Language: {language}
- Existing heuristic classification: {doc_type_guess} (or NULL if ambiguous)

FIRST 3 PAGES OF TEXT:
{first_3_pages}

TASK 1 — CLASSIFY: Assign exactly one doc_type from this list:
MONOGRAPH, ARTICLE, CHAPTER, REVIEW, PRIMARY_SOURCE, ANTHOLOGY, DISSERTATION

TASK 2 — SUMMARIZE: Write a 1-3 sentence summary (max 500 characters) describing what this document argues or covers. Start with the author's surname. Include the primary subject and the document's claim or approach.

Return JSON:
{"doc_type": "...", "summary": "...", "confidence": "HIGH|MEDIUM|LOW"}
```

### Scoring

| Dimension | Score | Issue |
|-----------|-------|-------|
| Scope clarity | 4 | Two tasks in one prompt (classify + summarize), but they use the same input and are tightly coupled. Acceptable. |
| Constraint presence | 5 | ENUM list for doc_type, character limit for summary, JSON output format. Well-constrained. |
| Self-assessment | 3 | Includes confidence field but doesn't tell the LLM WHEN to use each level. |
| Failure history | 2 | Doesn't mention the 71% heuristic hit rate or the kinds of documents that were ambiguous. |
| Conciseness | 4 | Reasonably tight. Metadata block is efficient. |
| Actionability | 5 | Clear first step: read metadata, read text, classify, summarize, return JSON. |
| Examples | 1 | No examples of good vs bad summaries. No example of a tricky classification. |
| Exit criteria | 4 | JSON schema is the exit criterion. Missing: what to do if text is in Italian/German. |

**Score: 28/40 — Good foundation, needs examples and failure context.**

### Problems

1. **No examples.** The summary template in WRITING_TEMPLATES.md has an example ("Copenhaver examines...") but the prompt doesn't include it. Without an example, the LLM will guess at style.
2. **No confidence calibration.** When is classification HIGH vs MEDIUM? Need rules: "HIGH if the document clearly fits one category (e.g., 3-page journal article). MEDIUM if it could be two categories (e.g., long article vs short monograph). LOW if the text is unreadable or in a non-English language you can't assess."
3. **No non-English handling.** 39 documents are in Italian, German, French, etc. The prompt should say: "If the document is not in English, classify based on metadata (page count, filename patterns) and set confidence to LOW. Summarize in English regardless."
4. **No anti-examples.** What does a BAD summary look like? "This document is about Dee" is bad. "Harkness argues that Dee's angel conversations..." is good.
5. **Missing: what to do with REVIEWS.** Should reviews be summarized? The v2 scope says skip reviews. The prompt should say "If doc_type is REVIEW, summary may be NULL."

### Revised Prompt

```
You are classifying and summarizing academic documents about Renaissance magic for a scholarly database.

DOCUMENT METADATA:
- Filename: {filename}
- Folder: {folder} (primary figure: {folder_figure})
- Extracted author: {author}
- Extracted year: {year}
- Page count: {pages}
- Language: {language}
- Heuristic guess: {doc_type_guess}

FIRST 3 PAGES:
{first_3_pages}

TASK 1 — CLASSIFY into exactly one:
MONOGRAPH | ARTICLE | CHAPTER | REVIEW | PRIMARY_SOURCE | ANTHOLOGY | DISSERTATION

Confidence rules:
- HIGH: clearly fits one category (e.g., 3-page piece with journal metadata = ARTICLE)
- MEDIUM: could be two categories (e.g., 50-page work — long article or short monograph?)
- LOW: text unreadable, non-English, or metadata contradicts content

TASK 2 — SUMMARIZE in 1-3 sentences (max 500 chars):
- Start with author surname
- State what the document ARGUES, not just its topic
- Name the primary figure(s) or tradition(s) addressed
- If doc_type is REVIEW, set summary to null
- If non-English: summarize from metadata + any readable portions, in English

GOOD: "Copenhaver examines Ficino's Hermetic translations, arguing that his Neoplatonic framework systematically reinterpreted the Egyptian Hermetica."
BAD: "This is a document about Ficino and Hermeticism."

Return JSON only:
{"doc_type": "...", "summary": "..." or null, "confidence": "HIGH|MEDIUM|LOW"}
```

**Revised score: 35/40**

---

## PROMPT B: Dictionary Definition (`/renmagdb-define`)

### Draft Prompt

```
You are writing dictionary entries for a scholarly website on Renaissance magic. Voice: museum-curator scholarly. Audience: educated non-specialist.

TERM: {term}
LANGUAGE: {term_language}
ENGLISH TRANSLATION: {english_translation}
DOMAIN: {domain}
CORPUS FREQUENCY: {frequency} occurrences across {doc_count} documents

KWIC CONCORDANCE (term in context from corpus):
{kwic_lines}

RELATED TERMS IN DATABASE: {related_terms}
ASSOCIATED FIGURES: {associated_figures}

Write two definitions:

1. definition_brief: One sentence, max 100 characters. What this term means in Renaissance magical context.

2. definition_long: 3-5 sentences, 100-200 words. Include:
   - How Renaissance magicians used this term
   - At least 1 named figure who employed it
   - Which intellectual tradition(s) it belongs to
   - Connection to related terms
   - At least 1 corpus citation

Return JSON:
{"definition_brief": "...", "definition_long": "...", "cross_references": ["term1", "term2"]}
```

### Scoring

| Dimension | Score | Issue |
|-----------|-------|-------|
| Scope clarity | 5 | One thing: write a dictionary entry. Clear. |
| Constraint presence | 4 | Character limit on brief, word range on long, required elements listed. Missing: what to do if KWIC is empty. |
| Self-assessment | 2 | Doesn't acknowledge that the LLM is working from KWIC snippets, not full documents. Context is limited. |
| Failure history | 1 | No mention of generic-term problem (ens, ratio, natura at 20K+ freq are too common to define usefully in magic context). |
| Conciseness | 4 | Efficient. KWIC lines may be long but that's input, not prompt bloat. |
| Actionability | 5 | Read KWIC, write definitions, return JSON. Clear. |
| Examples | 1 | No example entry. The WRITING_TEMPLATES.md has examples but they're not in the prompt. |
| Exit criteria | 4 | JSON schema. Missing: validation rules (brief must contain the term, long must name a figure). |

**Score: 26/40 — Needs examples, failure handling, and validation rules.**

### Problems

1. **No example entry.** Include one complete example showing the expected output.
2. **No handling for generic terms.** "ens" (53K freq) is a basic Latin philosophical word. The prompt should say: "If the term is a common Latin philosophical word with no specific magical meaning, focus the definition on its SPECIFIC USAGE in Renaissance magic contexts, not its general philosophical meaning."
3. **No handling for empty KWIC.** If the concordance has zero or few lines, the LLM should say so and produce a lower-confidence entry.
4. **No validation rules stated.** The brief definition must contain the English translation. The long definition must name at least one figure. Without stating this, the LLM may omit them.
5. **Cross-references are vague.** Should be: "Return 2-5 related terms that ARE IN THE DATABASE" — not invented terms.

### Revised Prompt

```
You are writing a dictionary entry for a scholarly website on Renaissance magic.
Voice: museum-curator scholarly. Audience: educated non-specialist.

TERM: {term}
LANGUAGE: {term_language}
ENGLISH: {english_translation}
DOMAIN: {domain}
FREQUENCY: {frequency} across {doc_count} documents

KWIC CONCORDANCE (usage in corpus):
{kwic_lines}

RELATED TERMS (already in database): {related_terms}
ASSOCIATED FIGURES: {associated_figures}

RULES:
- If the term is common Latin (ens, ratio, natura, forma), define its SPECIFIC Renaissance magic usage, not general philosophy
- If KWIC is empty or sparse, produce a shorter entry with confidence LOW
- definition_brief MUST include the English translation
- definition_long MUST name at least 1 figure and cite at least 1 corpus source
- cross_references MUST only include terms from the provided related_terms list

WRITE:

1. definition_brief: 1 sentence, max 100 chars. Renaissance magic meaning.
2. definition_long: 3-5 sentences, 100-200 words. Include: how Renaissance magi used it, at least 1 named figure, tradition(s), connection to related terms, 1 corpus citation.

EXAMPLE (for "prima materia"):
{
  "definition_brief": "The undifferentiated base substance from which alchemists sought to derive the philosopher's stone.",
  "definition_long": "In alchemical philosophy, prima materia designates the formless, chaotic substance that precedes all differentiation and from which the alchemist's work begins. Ficino's De Vita treats it as the material correlate of the Neoplatonic concept of pure potentiality, while Agrippa's De Occulta Philosophia identifies it with the elemental substrate underlying all natural transformations. The concept bridges alchemical practice and Aristotelian metaphysics, connecting the laboratory pursuit of transmutation to the philosophical framework of form and matter (Zambelli, White Magic Black Magic). Related to materia, forma, and transmutatio in the alchemical process vocabulary.",
  "cross_references": ["materia", "forma", "transmutatio", "lapis philosophorum"]
}

Return JSON only:
{"definition_brief": "...", "definition_long": "...", "cross_references": [...], "confidence": "HIGH|MEDIUM|LOW"}
```

**Revised score: 35/40**

---

## PROMPT C: Figure Biography (`/renmagdb-bio`)

### Draft Prompt

```
You are writing a biographical entry for a scholarly website on Renaissance magic. Voice: museum-curator scholarly. Audience: educated non-specialist.

FIGURE: {name}
TYPE: {figure_type} (HISTORICAL or SCHOLAR)
BIRTH: {birth_year}
DEATH: {death_year}
NATIONALITY: {nationality}
CURRENT SIGNIFICANCE FIELD: {significance}

CORPUS EVIDENCE:
- Documents about this figure: {doc_count}
- Document titles: {doc_titles}
- Key terms co-occurring: {cooccurring_terms}
- Folder: {folder}

RELEVANT PASSAGES (first 500 chars from top 3 documents):
{passage_1}
---
{passage_2}
---
{passage_3}

Write a biography following this structure:
1. IDENTIFICATION (1-2 sentences): Who, when, where, primary role
2. INTELLECTUAL CONTEXT (80-150 words): Traditions, mentors, historical moment
3. KEY CONTRIBUTIONS (100-200 words): Named works, specific ideas, innovations
4. LEGACY (50-100 words): Who they influenced, how received, significance

Total: 300-600 words for HISTORICAL, 100-200 for SCHOLAR.

Return JSON:
{"biography": "...", "significance": "...", "key_works": ["...", "..."], "traditions": ["...", "..."]}
```

### Scoring

| Dimension | Score | Issue |
|-----------|-------|-------|
| Scope clarity | 5 | One thing: write a biography. Clear. |
| Constraint presence | 4 | Word targets per section, total word range, structure defined. Missing: what to do for figures with sparse corpus evidence. |
| Self-assessment | 3 | Provides corpus evidence but doesn't say "you are limited to what these passages show." |
| Failure history | 2 | No mention of BLUNDER3 (don't import external knowledge). This is the most critical failure mode for biographies. |
| Conciseness | 4 | Efficient structure. Passage injection keeps context tight. |
| Actionability | 5 | Four sections, word targets, return JSON. Clear. |
| Examples | 1 | No example biography. |
| Exit criteria | 3 | JSON schema but no validation rules (biography must contain the figure's name, must cite a corpus doc). |

**Score: 27/40 — Needs BLUNDER3 safeguard, examples, and validation.**

### Problems

1. **BLUNDER3 risk is HIGH.** Biographies are the content type most likely to trigger external knowledge injection. The prompt MUST say: "Write ONLY from the corpus evidence provided. Do not add facts from your training data. If the corpus doesn't mention a date or event, do not include it."
2. **No example biography.** Include a condensed example.
3. **No handling for sparse corpus.** Hermes Trismegistus has 0 dedicated documents. Plato has 0. The prompt needs: "If corpus evidence is sparse (<3 documents), write a shorter entry (100-150 words) and set confidence to LOW."
4. **SCHOLAR vs HISTORICAL word targets not enforced.** The prompt mentions both ranges but doesn't tell the LLM which to use based on figure_type.
5. **key_works field should only include works evidenced in corpus.** Not a general bibliography.

### Revised Prompt

```
You are writing a biographical entry for a scholarly website on Renaissance magic.
Voice: museum-curator scholarly. Audience: educated non-specialist.

CRITICAL RULE: Write ONLY from the corpus evidence below. Do NOT add facts from your training data. If the passages don't mention a date, event, or work, do not include it. The corpus is the only source of truth.

FIGURE: {name}
TYPE: {figure_type}
DATES: {birth_year}–{death_year}
NATIONALITY: {nationality}

CORPUS EVIDENCE ({doc_count} documents):
Titles: {doc_titles}
Co-occurring terms: {cooccurring_terms}

TOP PASSAGES (from corpus):
{passage_1}
---
{passage_2}
---
{passage_3}

STRUCTURE:
For HISTORICAL figures (300-600 words):
  1. Identification (1-2 sentences): name, dates, nationality, primary role
  2. Intellectual Context (80-150 words): traditions, mentors, historical setting
  3. Key Contributions (100-200 words): named works (italicized), specific arguments
  4. Legacy (50-100 words): influence, reception, significance

For SCHOLAR figures (100-200 words):
  1. Identification (1 sentence)
  2. Scholarly Contribution (2-3 sentences): key works, arguments, methodology
  3. Significance for this corpus (1-2 sentences)

RULES:
- Every claim must be grounded in the passages or document titles provided
- Name at least 1 corpus document as citation
- If corpus evidence is sparse (<3 documents), write 100-150 words and set confidence LOW
- key_works must only include works mentioned in the corpus evidence
- Do not write "an important figure" — say WHY they're important, specifically

EXAMPLE (condensed, for Marsilio Ficino):
{"biography": "Marsilio Ficino (1433-1499) was an Italian philosopher and Catholic priest who directed the Florentine Platonic Academy under the patronage of Cosimo de' Medici...", "significance": "Ficino's Latin translations of the Corpus Hermeticum and Plato established the textual foundation for Renaissance Neoplatonic magic.", "key_works": ["De Vita", "Theologia Platonica", "Corpus Hermeticum translation"], "traditions": ["Hermeticism", "Neoplatonism"], "confidence": "HIGH"}

Return JSON only:
{"biography": "...", "significance": "...", "key_works": [...], "traditions": [...], "confidence": "HIGH|MEDIUM|LOW"}
```

**Revised score: 34/40**

---

## SUMMARY: All Three Prompts

| Prompt | Original Score | Revised Score | Key Fix |
|--------|---------------|--------------|---------|
| A: Classification + Summary | 28/40 | 35/40 | Added examples, confidence calibration, non-English handling, review skip rule |
| B: Dictionary Definition | 26/40 | 35/40 | Added example entry, generic-term rule, empty-KWIC handling, validation rules |
| C: Figure Biography | 27/40 | 34/40 | Added BLUNDER3 safeguard (corpus-only), sparse-evidence handling, SCHOLAR/HISTORICAL branching |

### Cross-cutting improvements applied to all three:
1. **Confidence calibration** — explicit rules for when to use HIGH/MEDIUM/LOW
2. **Example outputs** — at least one per prompt
3. **Failure handling** — what to do when input is sparse, non-English, or ambiguous
4. **Validation rules stated in prompt** — so the LLM knows what will be rejected
5. **BLUNDER3 safeguard** — "corpus is the only source of truth" on biography prompt

### Recommendation

Use the REVISED versions. The originals would have produced acceptable but inconsistent output; the revisions will produce more uniform, corpus-grounded results that pass database validation on first attempt, saving re-prompting tokens.

These revised prompts should be embedded directly in the v2 enrichment scripts (`enrich_classify.py`, `generate_dictionary.py`, `generate_biographies.py`) as template strings with `{variable}` substitution.

---

*Generated by plan-buckman-critic for the Renaissance Magic Database Project v2 prompts.*
