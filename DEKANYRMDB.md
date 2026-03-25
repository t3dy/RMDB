# DEKANYRMDB.md — Dekany Style Audit v2

## Renaissance Magic Database — All Generated Content

**Date:** 2026-03-24 (v2 — supersedes v1 audit of 2026-03-23)
**Analyst:** Claude (write-dekany-style)
**Scope:** 29 biographies, 139 dictionary definitions, 58 event descriptions, 36 text significance statements, 337 document summaries

---

## STYLE GUIDE (Established — User-Approved Decisions)

| Dimension | Standard | Rationale |
|-----------|----------|-----------|
| **Tense** | Past for deceased historical figures; present for living scholars and non-historical figures (Hermes Trismegistus) | Standard academic convention. Living scholars "is" because their work continues; deceased figures "was" as historical record. |
| **Voice** | Active, third person. Zero first/second person. | Museum-curator register. No "we," "you," or "I." Verified: 0 instances of "you" or "we" across all content. |
| **Formality** | High scholarly. No contractions, no colloquialisms. | Consistent with art-historical/intellectual-historical writing. |
| **Terminology: Kabbalah/Cabala** | "Kabbalah/Kabbalistic" for Jewish mystical tradition; "Cabala" for Renaissance Christian adaptations ("Christian Cabala"). **Never** "Christian Kabbalah," "Qabbalah," or "Kabbala." | Preserves the genuine historical distinction between Jewish Kabbalah and Renaissance Latin Cabala (Idel vs. Wirszubski convention). User-approved. |
| **Terminology: Magic** | "magic" (English analytical term), *magia* (Latin actor term). No "magick" ever. Qualified forms: "natural magic," "ceremonial magic," "demonic magic," "astral magic." | Per RMESSAY1.md: "magic" is a scholarly category, not a neutral descriptor. |
| **Latin/Greek/Hebrew terms** | Italicized on every occurrence (*anima mundi*, *magia naturalis*, *spiritus mundi*). Work titles also italicized (*De Occulta Philosophia*, *Corpus Hermeticum*). In HTML: `<em>` tags. | Standard academic practice. User-approved. |
| **Citations** | Parenthetical: (Surname, *Short Title*). Multiple: (Clulee, *Dee's Mathematics*; Harkness, *John Dee's Conversations*). | More informative than surname-only; lighter than full bibliographic reference. User-approved. |
| **Dashes** | Spaced em dash ( — ) for parenthetical insertions. En dash (–) for date and page ranges only. No double hyphens. | Already consistent across corpus: 205 em dashes, 30 en dashes, 0 double hyphens. |
| **Capitalization** | Tradition names capitalized: Hermeticism, Kabbalah, Neoplatonism, Rosicrucianism. Descriptive terms lowercase: natural magic, ceremonial magic, astral magic. | Traditions are proper nouns (named intellectual movements); magic types are descriptive categories. |
| **Person** | Third person exclusively. "One" acceptable for general statements. | Already perfect: 0 "you," 0 "we," 53 "one." |
| **Dates** | "c." for approximate: "(c. 1200–1280)." Full dates for events: "1463 Latin translation." | Consistent. |
| **Definition opening** | Term (Language: 'gloss') + "designates/denotes/is" | Needs standardization — some entries omit language tag. |
| **Figure naming** | Full name on first mention per entry, surname thereafter. | Needs enforcement in some entries. |

---

## INCONSISTENCIES FOUND

### Critical

| # | Type | Where | Example A | Example B | Fix |
|---|------|-------|-----------|-----------|-----|
| 1 | **Terminology** | Biographies, dictionary | "Christian Cabala" (12×) | "Christian Kabbalah" (2×) | Find-replace "Christian Kabbalah" → "Christian Cabala" |
| 2 | **Terminology** | Dictionary | "Kabbala" (2× — variant) | "Kabbalah" (20×) | Find-replace "Kabbala" → "Kabbalah" (except in "Christian Cabala") |
| 3 | **Content error** | Text significance ID=12 | Ars Magna described as angelic invocation (= Ars Notoria) | Should be Llull's combinatory system | Rewrite significance statement |
| 4 | **Citation format** | Biographies | "(Voss, Marsilio Ficino)" with title | "(Clulee; Harkness; Szönyi)" without | Standardize to (Surname, *Short Title*) |

### Important

| # | Type | Where | Example A | Example B | Fix |
|---|------|-------|-----------|-----------|-----|
| 5 | **Terminology** | Dictionary | "kabbalah" (1× lowercase) | "Kabbalah" | Capitalize |
| 6 | **Definition length** | Dictionary | Avg ~79 words | Template target: 100–200 | Extend short definitions in future pass |
| 7 | **Language tag** | Dictionary openings | "(Greek: 'purification')" with tag | "('soul of the world')" without | Add language tags |
| 8 | **Full name** | Various | "Ficino" on first mention | "Marsilio Ficino" (correct) | Add full name on first use |

### Minor

| # | Type | Where | Details | Fix |
|---|------|-------|---------|-----|
| 9 | **Latin italicization** | HTML output | Some Latin terms lack `<em>` in HTML | Update build_site.py |
| 10 | **Summary quality** | Document summaries | ~179 heuristic-extracted summaries are raw text, not prose | Regenerate with LLM reading (future session) |

---

## PRIMARY STYLE DRIFT

**Kabbalah/Cabala terminology** — Two instances of "Christian Kabbalah" and two of "Kabbala" violate the established spelling policy. Quick find-replace fix.

**Ars Magna misattribution** — The significance statement for text ID=12 (Llull's Ars Magna) describes the Ars Notoria instead. Content error, not style drift.

**Citation format** — Split between (Surname, *Title*) and (Surname) only. User approved (Surname, *Short Title*) — needs retroactive application.

---

## AUDIT BY CONTENT TYPE

### Biographies (29 entries) — Grade: A-
- Voice: Excellent. Museum-curator throughout.
- Tense: Correct split (past/present for deceased/living).
- Opening pattern: Consistent "[Name] ([dates]) was/is a [nationality] [role]..."
- Length: Major figures get 200-400 words; ancient/minor figures get 50-150. Appropriate proportional treatment.
- Issue: Citation format inconsistent.

### Dictionary Definitions (139 entries) — Grade: B+
- Voice: Excellent. Scholarly precision throughout.
- Opening: Mostly follows term + gloss + "designates" pattern. Some miss language tag.
- Cross-references: Good use of italicized term references (*sephiroth*, *anima mundi*).
- Length: Runs short of template target. First batch (46) longer than second batch (93).
- Issue: Some definitions need language tags standardized.

### Timeline Events (58 entries) — Grade: A
- Voice: Consistent museum-curator.
- Tense: Clean past tense throughout.
- Pattern: Consistent "[Figure] was born/died in [place]. [Significance statement]."
- Length: 1-3 sentences, appropriate for timeline format.
- No issues found.

### Text Significance (36 entries) — Grade: A-
- Voice: Consistent scholarly.
- Pattern: Opens with genre/description, then significance.
- Length: 1-3 sentences, appropriate.
- Issue: Ars Magna misattribution (content error, not style).

### Document Summaries (337 entries) — Grade: C+
- 139 good summaries (DETERMINISTIC abstracts + quality LLM extractions)
- ~179 heuristic-extracted summaries are raw text, not scholarly prose
- JSTOR boilerplate contamination cleaned in v2 pass
- Methodology classification added (147/337) but incomplete
- **This remains the weakest content type and should be priority for future improvement.**

---

## ACTION ITEMS

| Priority | # | Action | Type | Effort |
|----------|---|--------|------|--------|
| NOW | 1 | Replace "Christian Kabbalah" → "Christian Cabala" in DB | Find-replace | 2 min |
| NOW | 2 | Replace "Kabbala" → "Kabbalah" (non-Cabala contexts) | Find-replace | 2 min |
| NOW | 3 | Fix Ars Magna significance (text ID=12) | DB update | 2 min |
| NOW | 4 | Capitalize "kabbalah" → "Kabbalah" | Find-replace | 1 min |
| NEXT | 5 | Standardize citation format in biographies | Manual edit | 15 min |
| NEXT | 6 | Add language tags to dictionary openings | Script | 10 min |
| NEXT | 7 | Update build_site.py to auto-italicize Latin terms | Script | 10 min |
| FUTURE | 8 | Extend short dictionary definitions to 100+ words | LLM pass | 30 min |
| FUTURE | 9 | Regenerate 179 heuristic summaries with LLM reading | LLM pass | 60+ min |
| FUTURE | 10 | Add full name on first mention where missing | Script | 10 min |

---

## OVERALL ASSESSMENT

The generated content is **remarkably consistent** for 599 separate text blocks produced across multiple generation sessions. The museum-curator voice never drops; formality is uniform; person stays in third throughout; tense follows the correct academic convention. The Kabbalah/Cabala split is the only terminology problem that needs a policy decision (now made and documented). One content error (Ars Magna misattribution). Citation format needs standardization.

**Overall Grade: B+**
- Biographies: A-
- Dictionary: B+
- Timeline: A
- Texts: A-
- Summaries: C+ (quality issue, not style issue)

The style guide above should be treated as the binding reference for all future content generation.

---

*Generated by write-dekany-style for the Renaissance Magic Database Project.*
