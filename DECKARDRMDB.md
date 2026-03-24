# DECKARDRMDB.md — Deckard Boundary Report
## Renaissance Magic Database Project

**Date:** 2026-03-23
**Analyst:** Claude (plan-deckard-boundary)
**Corpus:** 358 files (~321 PDFs, 10 EPUBs, 9 HTML, misc), 2.7 GB
**Target:** SQLite database → static website (dictionary, timeline, biographies, library, templates)

---

## DETERMINISTIC TASKS (Use Python libraries, NOT LLM)

### Document Conversion & Text Extraction

| Task | Tool/Library | Why Deterministic |
|------|-------------|-------------------|
| PDF → text extraction | **PyMuPDF (fitz)** | Binary format parsing — structured, no judgment needed |
| PDF → markdown with headings/structure | **PyMuPDF** + heuristics (font size → heading level) | Font metrics are numeric; heading detection is rule-based |
| EPUB → markdown | **ebooklib** + **BeautifulSoup** | EPUB is XHTML internally — pure DOM parsing |
| HTML → markdown | **BeautifulSoup** + **markdownify** or **html2text** | Tag-to-markdown mapping is 1:1 deterministic |
| CHM → text | **pychm** or extract + parse HTML | Compiled HTML archive, structured extraction |
| Image extraction from PDFs | **PyMuPDF** `page.get_images()` | Binary extraction, no interpretation |

### Metadata Extraction from Filenames

| Task | Tool/Library | Why Deterministic |
|------|-------------|-------------------|
| Author name extraction | **Regex patterns** on filenames | Naming conventions are consistent enough for rules |
| Journal/volume/issue parsing | **Regex** (e.g., `vol \d+ iss \d+`) | Highly structured patterns in filenames |
| DOI extraction | **Regex** (`10\.\d{4,}/\S+`) | DOI format is standardized |
| Year extraction | **Regex** (`\b(1[4-9]\d{2}|20[0-2]\d)\b`) | Four-digit year pattern |
| Publisher extraction | **Keyword matching** against known publishers | Finite set, exact match |
| Folder → subject figure mapping | **Path parsing** | Folder name IS the classification |
| Source detection (libgen, etc.) | **String matching** | Suffix patterns are fixed |

### Metadata Extraction from PDF Internals

| Task | Tool/Library | Why Deterministic |
|------|-------------|-------------------|
| PDF metadata (title, author, creator) | **PyMuPDF** `doc.metadata` | Embedded metadata, direct read |
| Page count | **PyMuPDF** `len(doc)` | Numeric property |
| Creation/modification dates | **PyMuPDF** `doc.metadata` | Embedded timestamp |
| Table of contents extraction | **PyMuPDF** `doc.get_toc()` | Structured bookmark tree |
| First N pages text (for catalog) | **PyMuPDF** `page.get_text()` | Paginated extraction, no judgment |
| Font inventory (for structure detection) | **PyMuPDF** `page.get_text("dict")` | Font metadata is numeric |

### Database & Schema Operations

| Task | Tool/Library | Why Deterministic |
|------|-------------|-------------------|
| Schema creation (CREATE TABLE) | **sqlite3** | DDL is pure structure |
| Data insertion/updates | **sqlite3** parameterized queries | CRUD, no judgment |
| Migration scripts | **sqlite3** + PRAGMA checks | Idempotent ALTER TABLE |
| Cross-reference linking | **SQL JOINs** | Relational joins are deterministic |
| Full-text search indexing | **SQLite FTS5** | Built-in tokenizer, no LLM needed |
| Duplicate detection | **fuzzy string matching** via **thefuzz** (fuzzywuzzy) or **rapidfuzz** | Levenshtein distance is algorithmic |
| Citation parsing | **regex** + heuristics or **anystyle** (Ruby) / **GROBID** (Java) | Structured format parsing |

### Site Generation

| Task | Tool/Library | Why Deterministic |
|------|-------------|-------------------|
| Template rendering | **Jinja2** or string templates | Variable substitution, no judgment |
| Markdown → HTML | **markdown** or **markdown-it-py** | Spec-defined conversion |
| CSS/JS bundling | File concatenation | Pure I/O |
| URL/slug generation | **slugify** | Algorithmic text normalization |
| Navigation generation | **sqlite3** queries → template | Data-driven, deterministic |
| Timeline rendering | **sqlite3** ORDER BY year → template | Sort + render |
| Cross-link injection | **Regex substitution** | Pattern match → hyperlink |

### Text Analysis (Deterministic)

| Task | Tool/Library | Why Deterministic |
|------|-------------|-------------------|
| Latin/Greek term detection | **Regex** + known term dictionary | Pattern match against word list |
| Word frequency / TF-IDF | **scikit-learn** `TfidfVectorizer` or **collections.Counter** | Mathematical computation |
| Language detection | **langdetect** or **lingua** | Statistical model, no LLM needed |
| Named entity extraction (names, places, dates) | **spaCy** NER models | Trained ML model, runs locally, deterministic per input |
| Co-occurrence matrices | **numpy/scipy** | Linear algebra |
| Citation network graph | **networkx** | Graph algorithms |
| Concordance / KWIC index | **nltk** or custom | Sliding window over text |

---

## PROBABILISTIC TASKS (LLM Appropriate — Claude Code)

### Content Summarization & Description

| Task | Why LLM Needed |
|------|----------------|
| Document summaries (1-3 sentences from extracted text) | Requires reading comprehension and editorial judgment about what matters |
| Emblem/figure descriptions for website | Creative synthesis of scholarly material into accessible prose |
| Dictionary term definitions | Must synthesize meaning across multiple scholarly contexts |
| Biography writing for key figures | Narrative construction from factual data |
| "Significance" fields (why a text matters) | Evaluative judgment about intellectual history |

### Classification with Fuzzy Boundaries

| Task | Why LLM Needed |
|------|----------------|
| Document type classification (monograph vs article vs chapter vs primary source) | Edge cases: "is a 40-page journal piece an article or a monograph chapter?" |
| Topic/theme tagging beyond folder assignment | A Dee paper might also be about Kabbalah, alchemy, and Elizabeth I |
| Relevance scoring (PRIMARY / DIRECT / CONTEXTUAL) | Requires understanding intellectual relationships |
| Era/period assignment for texts | "Is Corpus Hermeticum ancient, medieval, or Renaissance?" — depends on framing |
| Tradition classification (Hermetic, Kabbalistic, Neoplatonic, etc.) | Overlapping traditions, texts belong to multiple |

### Semantic Extraction

| Task | Why LLM Needed |
|------|----------------|
| Key argument extraction from abstracts | Scholarly abstracts vary wildly in structure |
| Influence/citation relationship mapping | "Pico drew on Reuchlin" vs "Pico preceded Reuchlin" requires comprehension |
| Latin term contextualization (definitions in context) | Same Latin term means different things in different traditions |
| Identifying primary sources referenced in secondary literature | Embedded references require reading comprehension |

### Website Content Generation

| Task | Why LLM Needed |
|------|----------------|
| Essay drafting | Creative/analytical writing |
| Dictionary entry long-form definitions | Synthesis across sources |
| Timeline event descriptions | Narrative framing of historical facts |
| "How to read this" introductory texts | Pedagogical framing requires judgment |
| Template-guided writing (following house style) | Style adherence is probabilistic |

---

## VALIDATION LAYERS (Where LLM Output Enters Deterministic Systems)

| Boundary Point | Validation Method |
|---------------|-------------------|
| LLM summary → `documents.summary` column | Length check (≤500 chars), non-empty, no hallucinated dates |
| LLM classification → `documents.doc_type` | Must be one of ENUM values; reject unknowns |
| LLM topic tags → `document_topics` join table | Tags must exist in `topics` table; new tags flagged for review |
| LLM biography → `figures.biography_html` | Must contain figure's name, must reference at least 1 source |
| LLM dictionary definition → `dictionary_terms.definition_long` | Must contain the term itself, length bounds, no self-reference loops |
| LLM influence claims → `figure_influences` join table | Both figure IDs must exist; direction must be stated |
| LLM era assignment → `texts.era` | Must be one of ENUM values (ANCIENT/MEDIEVAL/RENAISSANCE/EARLY_MODERN) |
| LLM relevance score → `documents.relevance` | Must be PRIMARY/DIRECT/CONTEXTUAL; log confidence |

**Provenance tracking on ALL LLM-generated data:**
- `source_method = 'LLM_ASSISTED'`
- `confidence = 'MEDIUM'` (default, upgradable by human review)
- `review_status = 'DRAFT'` (never auto-promote)

---

## BOUNDARY VIOLATIONS TO AVOID

### WASTE (Using LLM where Python libraries suffice)

| Violation | Recommendation |
|-----------|---------------|
| Using Claude to read PDF text | Use **PyMuPDF** `page.get_text()` — 1000x faster, zero tokens |
| Using Claude to extract PDF metadata | Use **PyMuPDF** `doc.metadata` — instant, complete |
| Using Claude to convert HTML to markdown | Use **html2text** or **markdownify** — deterministic, free |
| Using Claude to parse EPUB structure | Use **ebooklib** — DOM parsing, no interpretation needed |
| Using Claude to detect Latin terms | Use **regex** + dictionary lookup — exact match, no ambiguity |
| Using Claude to count pages or words | Use **PyMuPDF** / `len()` — arithmetic |
| Using Claude to parse filenames for metadata | Use **regex** — patterns are fixed and documented |
| Using Claude to build citation networks | Use **networkx** after deterministic extraction — graph algorithms |
| Using Claude to do full-text search | Use **SQLite FTS5** — built for this, fast, ranked results |
| Using Claude to detect duplicate documents | Use **rapidfuzz** string similarity — algorithmic, tunable threshold |

### RISK (Using deterministic code where judgment is needed)

| Violation | Recommendation |
|-----------|---------------|
| Hardcoding topic assignments by folder alone | Folder = primary figure, but papers often span multiple topics. Use LLM for secondary topic tagging |
| Regex-only author extraction from filenames | Works for 80% but fails on edge cases (multiple authors, editors, translators). Use LLM fallback |
| Rule-based document type classification | Heuristics (page count, filename patterns) get ~70%. LLM needed for ambiguous cases |
| Template-only biography generation | Pure template fill produces lifeless text. LLM needed for narrative quality |

### DANGER (LLM output flowing to DB without validation)

| Violation | Mitigation |
|-----------|-----------|
| LLM summaries inserted directly | REQUIRE: length bounds, non-empty, provenance tags |
| LLM topic tags creating new DB records | REQUIRE: whitelist check; unknown tags → staging table for review |
| LLM date claims inserted as facts | REQUIRE: cross-check against deterministic metadata; flag conflicts |
| LLM influence claims becoming edges in graph | REQUIRE: both nodes must exist; log source text that prompted claim |

---

## PYTHON LIBRARY INVENTORY — What We Should Use

### Already Installed
- **PyMuPDF (fitz)** 1.27.1 — PDF text extraction, metadata, TOC, images
- **pdfminer.six** — Alternative PDF text extraction (better for some layouts)
- **pypdf** 6.7.0 — PDF manipulation (merge, split, metadata)
- **BeautifulSoup4** 4.14.3 — HTML/XML parsing
- **Markdown** 3.10.2 — Markdown rendering
- **markdown-it-py** 4.0.0 — CommonMark-compliant markdown

### Need to Install
- **html2text** or **markdownify** — HTML → Markdown conversion
- **ebooklib** — EPUB parsing
- **spaCy** + `en_core_web_sm` — NER (names, places, dates)
- **rapidfuzz** — Fast fuzzy string matching (dedup)
- **networkx** — Citation/influence graph construction
- **Jinja2** — Template rendering for site generation
- **python-slugify** — URL-safe slug generation
- **langdetect** or **lingua-language-detector** — Language detection

### Optional / Later Phase
- **scikit-learn** — TF-IDF, topic modeling
- **nltk** — Concordance, tokenization
- **GROBID** (Java service) — Academic citation parsing (heavy but accurate)
- **Tesseract** + **pytesseract** — OCR for scanned-only PDFs (if PyMuPDF extraction is blank)

---

## RECOMMENDED PROCESSING PIPELINE ORDER

```
Phase 1: DETERMINISTIC (Python only, zero LLM tokens)
  1. PDF → text extraction (PyMuPDF)
  2. EPUB → text extraction (ebooklib + BS4)
  3. HTML → markdown (html2text)
  4. Filename metadata parsing (regex)
  5. PDF internal metadata extraction (PyMuPDF)
  6. TOC extraction where available (PyMuPDF)
  7. Duplicate detection (rapidfuzz)
  8. Language detection per document (langdetect)
  9. Latin/Greek term extraction (regex + dictionary)
  10. NER pass for names, places, dates (spaCy)
  11. Write all .md files + catalog.json

Phase 2: HYBRID (Python extraction → LLM judgment)
  12. Document type classification (heuristics + LLM fallback)
  13. Topic/tradition tagging (folder-based + LLM secondary tags)
  14. Relevance scoring (LLM with extracted text as context)
  15. Brief summaries from first pages (LLM)

Phase 3: LLM CONTENT GENERATION (Claude Code)
  16. Dictionary term definitions
  17. Figure biographies
  18. Timeline event descriptions
  19. Essay drafting
  20. Template-guided website content

Phase 4: DETERMINISTIC (Python only)
  21. SQLite schema creation + data insertion
  22. Cross-reference linking (SQL)
  23. FTS5 indexing
  24. Static site generation (Jinja2)
  25. Validation + QA scripts
```

---

## TOKEN COST ESTIMATES (LLM Phases Only)

| Phase | Estimated Input Tokens | Estimated Output Tokens | Notes |
|-------|----------------------|------------------------|-------|
| Phase 2 (classification/tagging) | ~200K | ~50K | First 2-3 pages per doc × 321 docs |
| Phase 2 (summaries) | ~300K | ~100K | Abstract/intro text per doc |
| Phase 3 (dictionary, ~1000 terms) | ~500K | ~200K | Context passages + definitions |
| Phase 3 (biographies, ~30 figures) | ~300K | ~100K | Multi-source synthesis per figure |
| Phase 3 (timeline, ~200 events) | ~100K | ~50K | Event descriptions |
| Phase 3 (essays, ~20) | ~400K | ~200K | Long-form scholarly content |
| **TOTAL LLM WORK** | **~1.8M** | **~700K** | Spread across multiple sessions |

**Phase 1 (deterministic) token cost: ZERO.** All Python scripting.

---

*Generated by plan-deckard-boundary for the Renaissance Magic Database Project.*
