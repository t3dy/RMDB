# DECKARDV2RMDB.md — Deckard Boundary Re-Check (Post-v1 Data)
## Renaissance Magic Database Project

**Date:** 2026-03-23
**Analyst:** Claude (plan-deckard-boundary, second pass)
**Context:** v1 is complete. Re-evaluating boundaries with actual data to determine what v2 LLM work is truly necessary.

---

## BOUNDARY SHIFTS: What v1 Data Changed

### SHIFT 1: TF-IDF Topic Tagging — LLM DOWNGRADED to OPTIONAL

**Original plan:** LLM reviews TF-IDF clusters and assigns human-readable tradition names.

**What data showed:** TF-IDF produced 12 clusters. Of those:
- **5 are high-purity, figure-specific** (Trithemius 100%, Dee 100%, Pico 100%, Bruno 91%, witchcraft 75%). These don't need LLM — the cluster IS the label.
- **3 are language clusters** (German, Italian, Enochian primary text). These are useful metadata signals but not "traditions." Python `langdetect` already tagged these.
- **1 is a quality cluster** ("scanned ocr" — 18 docs with OCR noise). This is a data quality signal, not a topic.
- **1 is a JSTOR metadata cluster** (48 docs). This is extraction noise — JSTOR terms-of-use text contaminating TF-IDF.
- **1 is the "everything else" megacluster** (117 docs, 21% purity). This is unhelpful.
- **1 is tiny** (Peters/witchcraft, 4 docs).

**Revised boundary:** TF-IDF is useful for FIGURE-SPECIFIC clusters but FAILED at identifying intellectual traditions (Hermeticism, Kabbalah, Neoplatonism, etc.). The term extraction (186 terms with domain tags) is a BETTER source for tradition identification than TF-IDF.

**RECOMMENDATION:**
- **DETERMINISTIC:** Build tradition taxonomy from dictionary_terms.domain aggregation. Group terms by domain → derive traditions. No LLM needed.
- **DEMOTE LLM:** "Name TF-IDF clusters as traditions" (JOECHIPV2RMDB P8) → CANCEL. Replace with a Python script that aggregates term domains into tradition labels.
- **Token savings: ~15K**

---

### SHIFT 2: Document Classification — LLM SCOPE REDUCED

**Original plan:** LLM classifies 99 ambiguous documents.

**What data showed:** The 99 ambiguous documents break down as:
- Many are medium-length works (40-150 pages) without journal indicators — the heuristic couldn't distinguish "long article" from "short monograph" or "book chapter."
- Some have filenames that don't follow the standard patterns.

**Can we narrow this further with Python?** Yes:
- **PDF internal metadata check:** PyMuPDF `doc.metadata` may contain "Subject" or "Keywords" fields that heuristics didn't use.
- **First-line detection:** The first lines of the .md file often contain journal headers, chapter numbers, or book frontmatter that indicate type.
- **File size heuristic:** <1MB PDFs are almost certainly articles. >10MB are almost certainly monographs.

**RECOMMENDATION:**
- **ADD:** Python script `classify_heuristic_v2.py` with enhanced rules (file size, first-line patterns, PDF metadata fields). Estimate: resolves 30-40 more documents.
- **REDUCE LLM:** Only classify the remaining ~60 truly ambiguous docs. Down from 99.
- **Token savings: ~80K** (39 fewer LLM calls × ~2.1K tokens each)

---

### SHIFT 3: Document Summaries — LLM IS TRULY NEEDED but scope narrower

**Original plan:** LLM summarizes ~200 documents.

**What data showed:** Abstract regex caught only 15/337 (4%). But:
- **41 reviews** don't need summaries (the review IS a summary of another work)
- **23 primary sources** may not need summaries (they're the TEXT, not scholarship about a text)
- **15 already have abstracts**
- That leaves: ~258 documents that need summaries

**Can we narrow further?** Yes:
- **Python first-paragraph extraction:** For monographs, the first paragraph of the introduction often states the thesis. A heuristic that grabs the first 2-3 sentences after any heading containing "Introduction" would catch many.
- **Skip non-English documents:** 39 docs in Italian/German/French — summarizing foreign text is lower priority and higher error rate. Defer to v3.

**RECOMMENDATION:**
- **ADD:** Python script `extract_introductions.py` — grabs first paragraph after "Introduction" / "Chapter 1" / "Preface" headings. Estimate: catches 40-60 more summaries.
- **REDUCE LLM scope:** Summarize only English-language documents that lack both abstract and introduction extraction. Estimate: ~160 docs (down from 200).
- **SKIP:** Reviews (41), primary sources (23), non-English (39)
- **Token savings: ~120K**

---

### SHIFT 4: Dictionary Definitions — BOUNDARY UNCHANGED but CURATE FIRST

**Original plan:** LLM generates definitions for ~150 terms.

**What data showed:** The expanded seed list produced some extremely high-frequency generic terms:
- `ens` (53K), `ratio` (30K), `natura` (22K), `forma` (12K), `materia` (7.6K)
- These are basic Latin philosophical vocabulary, not Renaissance magic-specific terms

**RECOMMENDATION:**
- **DETERMINISTIC PRE-STEP:** Flag the top ~15 generic terms. Either:
  - Redefine them narrowly (e.g., "forma as used in Ficinian Neoplatonism")
  - Mark as LOW_PRIORITY and define last
  - Filter from the initial LLM batch entirely
- **PRIORITIZE:** Generate definitions for the ~100 most magic-specific terms first (domain = MAGICAL, KABBALISTIC, HERMETIC, ENOCHIAN, ALCHEMICAL). These have clearest KWIC context.
- **DEFER:** Broad PHILOSOPHICAL terms to a later pass when more corpus context is available.
- **Revised LLM scope:** ~120 terms in first pass (down from 150), prioritized by domain specificity.
- **Token savings: ~60K**

---

### SHIFT 5: Figure Biographies — BOUNDARY CONFIRMED, no change

**Original plan:** LLM generates 29 biographies from corpus evidence.

**What data showed:** All 29 figures are seeded with dates, nationality, significance. The corpus has strong evidence for the 15 folder-named figures (7-76 documents each). Ancient/medieval authorities (Plato, Plotinus, etc.) have sparse direct corpus evidence.

**RECOMMENDATION:** No boundary change. LLM is genuinely needed for narrative synthesis. But:
- **Process in two tiers:** 15 corpus-rich figures first (HIGH confidence expected), 14 sparse figures second (MEDIUM/LOW confidence).
- **Corpus-only rule (BLUNDER3)** is critical here — the Buckman-revised prompt enforces it.

---

### SHIFT 6: Timeline Events — MORE DETERMINISTIC than planned

**Original plan:** LLM generates event descriptions.

**What data showed:** NER extracted dates across the corpus. The seeded figures have birth/death years. Many key events are deterministic:
- Publication dates of major works (embedded in filenames: year field)
- Birth/death dates of all 25 figures with dates
- Trial dates (Bruno 1600, Dee investigated)

**RECOMMENDATION:**
- **DETERMINISTIC:** Python script `seed_timeline.py` generates ~40 events from: figure birth/death pairs + known publication dates from filename parsing + curated milestone list (hardcoded).
- **LLM ONLY FOR:** Event descriptions (2-3 sentences per event). But the events THEMSELVES are deterministic.
- **Revised approach:** Seed events first (Python), then batch-describe them (LLM). Much cheaper than having LLM identify AND describe events.
- **Token savings: ~15K** (LLM only writes descriptions, doesn't identify events)

---

### SHIFT 7: Library Catalog (Primary Sources) — MORE DETERMINISTIC than planned

**Original plan:** LLM extracts and describes ~50 primary sources.

**What data showed:** Many primary sources are already identifiable from:
- `dictionary_terms` with domain tags (e.g., "corpus hermeticum" freq 341, "de occulta philosophia" freq 598, "picatrix" freq 420)
- `figures` table (authored works can be inferred: Ficino → Theologia Platonica, Dee → Monas Hieroglyphica)
- Documents tagged `doc_type='PRIMARY_SOURCE'` (23 docs) ARE primary sources

**RECOMMENDATION:**
- **DETERMINISTIC:** Python script `seed_texts.py` creates `texts` rows from:
  1. The 23 PRIMARY_SOURCE documents (they ARE texts)
  2. High-frequency terms that are titles (corpus hermeticum, de occulta philosophia, picatrix, steganographia, monas hieroglyphica, zohar, timaeus, enneads, de vita, theologia platonica, ars notoria, sefer yetzirah, asclepius, pimander)
  3. `figure_texts` join from known authorship
- **LLM ONLY FOR:** Significance descriptions (why each text matters). The identification is deterministic.
- **Revised scope:** Python seeds ~40 texts, LLM writes significance for each. Down from LLM doing identification + description.
- **Token savings: ~50K**

---

## REVISED v2 BOUNDARY MAP

### DETERMINISTIC (Python, zero LLM tokens)

| Task | Method | Status |
|------|--------|--------|
| Build tradition taxonomy from term domains | Aggregate dictionary_terms.domain → tradition descriptions | NEW |
| Enhanced classification heuristic v2 | File size + first-line + PDF metadata | NEW |
| Extract introductions from monographs | Regex for "Introduction" headings | NEW |
| Curate generic terms (flag top 15) | Frequency threshold + domain filter | NEW |
| Seed timeline events from figures + filenames | Birth/death pairs + publication years | NEW |
| Seed primary sources from terms + doc_type | High-freq title terms + PRIMARY_SOURCE docs | NEW |

### LLM (reduced scope)

| Task | Original scope | Revised scope | Savings |
|------|---------------|---------------|---------|
| Classify ambiguous docs | 99 docs | ~60 docs | ~80K tokens |
| Generate summaries | ~200 docs | ~160 docs | ~120K tokens |
| Dictionary definitions | ~150 terms | ~120 terms (magic-specific first) | ~60K tokens |
| Figure biographies | 29 figures | 29 figures (no change) | — |
| Timeline event descriptions | ~50 events | ~40 events (events seeded by Python) | ~15K tokens |
| Primary source significance | ~50 texts | ~40 texts (texts seeded by Python) | ~50K tokens |
| Name TF-IDF clusters | 12 clusters | CANCELLED (use term domains) | ~15K tokens |

### TOTAL TOKEN BUDGET REVISION

| | Original (JOECHIPV2RMDB) | Revised | Savings |
|---|---|---|---|
| Classification | ~210K | ~130K | 38% |
| Summaries | ~640K | ~510K | 20% |
| Dictionary | ~195K | ~155K | 21% |
| Biographies | ~110K | ~110K | 0% |
| Timeline | ~35K | ~20K | 43% |
| Library | ~115K | ~65K | 43% |
| Tradition naming | ~15K | ~0K | 100% |
| **TOTAL** | **~1.32M** | **~990K** | **25%** |

**25% reduction** by adding 6 deterministic Python scripts and cancelling the TF-IDF labeling task.

---

## BOUNDARY VIOLATIONS DISCOVERED

### WASTE FOUND IN v1

| Finding | Recommendation |
|---------|---------------|
| TF-IDF JSTOR cluster (48 docs) | The JSTOR terms-of-use boilerplate is contaminating clustering. **Fix:** Add "jstor", "terms conditions", "jstor org" to TF-IDF stop words and re-cluster. |
| TF-IDF OCR cluster (18 docs) | Not a topic — it's a data quality flag. **Fix:** These 18 docs should be flagged in documents.quality_flag, not treated as a topic cluster. |
| Generic Latin terms dominating frequency | ens (53K) swamps all other terms. **Fix:** Cap frequency display at 10K or normalize by document count instead of raw frequency. |
| NER "John Dee's" as separate entity from "John Dee" | Possessive forms create duplicate entities. **Fix:** Strip possessives in NER post-processing. |

### NEW DETERMINISTIC OPPORTUNITIES

| Opportunity | Method | Benefit |
|-------------|--------|---------|
| Author extraction from first page | Regex for "by [Name]" in first 500 chars of .md | Fills author_from_filename gaps |
| Publisher extraction | Known publisher names in filenames | Enriches metadata |
| Citation network (who cites whom) | Regex for bibliography/reference sections | Maps influence without LLM |
| Page range extraction for chapters | Regex for "pp. NNN-NNN" in filenames | Helps chapter vs article disambiguation |

---

## RECOMMENDED v2 EXECUTION ORDER (Revised)

```
PHASE A: NEW DETERMINISTIC SCRIPTS (zero LLM tokens)
  1. classify_heuristic_v2.py (enhanced, resolves ~40 more docs)
  2. extract_introductions.py (grabs intros for ~50 monographs)
  3. seed_timeline.py (events from figure dates + publication years)
  4. seed_texts.py (primary sources from terms + doc_type)
  5. build_traditions.py (aggregate term domains into tradition labels)
  6. curate_terms.py (flag/filter generic terms)

PHASE B: LLM ENRICHMENT (with revised Buckman prompts)
  7. enrich_classify.py (~60 docs, Prompt A)
  8. enrich_summaries.py (~160 docs, Prompt A variant)
  9. generate_dictionary.py (~120 terms, Prompt B)
  10. generate_biographies.py (29 figures, Prompt C)
  11. describe_timeline.py (~40 events, mini-prompt)
  12. describe_texts.py (~40 texts, mini-prompt)
```

Phase A costs zero tokens and reduces Phase B's scope by 25%.

---

*Generated by plan-deckard-boundary (second pass) for RenMagDB v2. Boundary map updated with actual v1 data.*
