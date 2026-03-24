# WRITING_TEMPLATES.md — Voice Rules, Style Guide, and Content Templates
## RenMagDB — Renaissance Magic Database

---

## Voice & Register

**Target reader:** An educated non-specialist exploring a digital exhibition on Renaissance magic. They have general humanities literacy — perhaps a degree in history, literature, or philosophy — but no prior expertise in occultism, Kabbalah, or alchemical philosophy. Write as a museum curator would for a scholarly exhibition catalog: authoritative, specific, grounded in textual and historical evidence.

**Voice rules:**
- **Person:** Third person for all scholarly content. First person plural ("we") only in About/methodology pages.
- **Tense:** Present tense for what texts argue and what scholars claim. Past tense for historical events and biographical facts.
- **Specificity:** Name concrete details — texts, dates, cities, patrons, controversies. Avoid vague generalities like "an important figure" or "a significant contribution."
- **Attribution:** Always attribute interpretations to their source. "Yates argues..." not "The Hermetic tradition caused..." Write about what scholars argue, not what history "means."
- **No external knowledge injection:** All claims must be traceable to the corpus. Do not import facts that aren't evidenced in the 337 documents. (BLUNDER3 lesson: the corpus is the source of truth.)
- **Confidence language:** HIGH = declarative ("authored," "published in"). MEDIUM = hedging ("likely," "appears to," "scholars suggest"). LOW = explicit uncertainty ("may have," "the connection is speculative").
- **Citations:** Reference corpus documents by author surname and short title: `(Yates, Bruno and the Hermetic Tradition)` or `(Copenhaver, "Scholastic Philosophy...")`.
- **Latin terms:** Italicize on first use with English gloss in parentheses. Subsequent uses may be unglossed: "*magia naturalis* (natural magic)."

## AI-Generated Content Disclosure

All AI-drafted content must include this banner:

> This content was drafted by an AI language model based on the scholarly sources in our corpus. It has not been reviewed by a human scholar. Citations are provided but should be verified against the original sources.

Review status is tracked in the database: `review_status = 'DRAFT'` for all AI-generated content.

---

## TEMPLATE 1: Dictionary Entry

**Format:** Dictionary/glossary page for the website
**Audience:** Educated non-specialist; also useful as quick reference for researchers
**Total target:** 150-300 words (standard entries); 400-800 words (major tradition entries)

### IMPORTANT: The Copenhaver/Hanegraaff Framing (applies to ALL entries)

Every dictionary entry operates within the scholarly framework established in RMESSAY1.md and GNOSISDICTIONARYSTYLEANALYSISTAKEAWAYS.md:

- **Distinguish actor terms from analyst terms.** If the term was used BY Renaissance figures (e.g., *magia naturalis*, *prisca theologia*), note how THEY used it. If it's a modern scholarly category (e.g., "Hermeticism," "Western esotericism"), note that it is a retrospective label.
- **Do not reify traditions as discrete boxes.** When a term belongs to multiple traditions, say so. "This concept bridges Kabbalistic and Neoplatonic frameworks" is better than assigning it to one box.
- **Note the polemical dimension where relevant.** Many terms (magia, superstitio, haeresis) were accusations, not self-descriptions. Say who called what "magic" and why.
- **Specify the period of primary use.** A term meant differently in different centuries. "Kabbalah as understood by 13th-century Jewish mystics" ≠ "Kabbalah as adapted by Pico in 1486."

### Section 1: Headword & Translation
**Purpose:** Identify the term immediately
**Word target:** 1 line
**Required elements:** Term in original language (italicized), language tag, English translation
**Tone:** Neutral, reference-style
**Template:**
```
*[term]* ([language]) — [English translation]
```
**Example:** *prima materia* (Latin) — first matter

### Section 2: Brief Definition
**Purpose:** One-sentence definition for quick scanning
**Word target:** 15-30 words
**Required elements:** What the term means in its Renaissance magic context (not modern or general usage)
**Tone:** Precise, encyclopedic
**Template:**
```
[Definition that situates the term in Renaissance magical/philosophical discourse, mentioning
its primary domain and intellectual tradition.]
```
**Example:** In alchemical philosophy, the undifferentiated base substance from which all metals and, by extension, all created things are believed to derive through successive stages of refinement.

### Section 3: Long Definition
**Purpose:** Full scholarly explanation with context and usage
**Word target:** 100-200 words
**Required elements:**
- Origin/etymology where relevant
- How Renaissance magicians used the term (with at least 1 named figure)
- Which intellectual tradition(s) it belongs to
- How it connects to other terms in the dictionary (cross-references)
- At least 1 corpus citation
**Tone:** Museum-curator scholarly
**Template:**
```
[Paragraph explaining the term's intellectual history, its role in Renaissance magical
thought, which key figures employed it and how, and its relationship to adjacent concepts.
Reference at least one document from the corpus.]
```

### Section 4: Domain & Cross-References
**Purpose:** Navigation and categorization
**Required elements:** Domain tag, related terms (links), associated figures, key texts
**Template:**
```
Domain: [ALCHEMICAL / HERMETIC / KABBALISTIC / NEOPLATONIC / MAGICAL / etc.]
Related terms: [term1], [term2], [term3]
Key figures: [figure1], [figure2]
Key texts: [text1], [text2]
```

### Anti-patterns:
- Do NOT define the term only in its modern/scientific sense
- Do NOT write "this term is important" without saying why and to whom
- Do NOT use the term to define itself
- Do NOT omit the Renaissance-specific meaning in favor of general philosophy
- Do NOT assign a term to one tradition if it crosses multiple (note the overlaps)
- Do NOT treat analyst categories as if Renaissance figures used them (they didn't call themselves "Hermeticists")

### TEMPLATE 1B: Major Entry (Tradition-Level Concepts)

**Use for:** Entries on major traditions or concepts requiring 400-800 words: Hermeticism, Kabbalah, Neoplatonism, Alchemy, Astrology, Theurgy, etc. Modeled on Hanegraaff's *Dictionary of Gnosis & Western Esotericism* entry structure.

**Format:** Continuous scholarly prose (NOT sectioned). Flows from definition through historical development to Renaissance reception to modern scholarly framing.

**Required elements:**
1. Opening definition (what the term designates, noting it is a scholarly category if applicable)
2. Pre-Renaissance origins (ancient/medieval sources)
3. Renaissance adaptation (who adapted it, how, and why — name specific figures and texts)
4. Relationship to other traditions (how it overlaps with, draws on, or conflicts with adjacent traditions)
5. Scholarly framing (how modern scholars understand the term — Yates vs Copenhaver line where relevant)
6. Inline cross-references to other dictionary entries (marked with → or hyperlinks)
7. At least 2 corpus citations

**Category tag:** Include: `Category type: ANALYST_TERM` (for modern labels) or `ACTOR_TERM` (for Renaissance self-descriptions) or `HYBRID`

**Example opening (for "Hermeticism"):**
> Hermeticism is a modern scholarly label for the body of philosophical, religious, and magical ideas associated with the legendary Hermes Trismegistus and transmitted through the *Corpus Hermeticum*, the *Asclepius*, and related texts. Renaissance figures did not typically use this term to describe their own work; Ficino called his project a recovery of *prisca theologia* (→ancient theology), and Agrippa framed his synthesis as *philosophia occulta*. The category "Hermeticism" emerged retrospectively, largely through Frances Yates's influential *Giordano Bruno and the Hermetic Tradition* (1964), and has since been problematized by scholars including Copenhaver and Hanegraaff who argue against treating it as a coherent autonomous tradition...

---

## TEMPLATE 2: Figure Biography

**Format:** Biographical entry for the website's Figures section
**Audience:** Educated non-specialist wanting to understand a figure's role in Renaissance magic
**Total target:** 300-600 words (HISTORICAL figures), 100-200 words (SCHOLAR figures)

### Section 1: Identification
**Purpose:** Who, when, where
**Word target:** 1-2 sentences
**Required elements:** Full name, birth-death dates, nationality, primary role/title
**Tone:** Factual
**Template:**
```
[Full name] ([birth]–[death]) was a [nationality] [role/occupation] known for
[primary contribution to Renaissance magic/scholarship].
```
**Example:** Giovanni Pico della Mirandola (1463–1494) was an Italian philosopher known for his syncretic fusion of Kabbalah, Hermeticism, and Neoplatonic philosophy in his 900 Conclusiones.

### IMPORTANT: The Copenhaver/Hanegraaff Framing (applies to ALL biographies)

- **Lead with what the figure ACTUALLY DID** (translated texts, wrote philosophy, practiced medicine, advised monarchs) — not with their role in a "magical tradition."
- **Note the tension or complexity** in the figure's intellectual identity. Dee was a mathematician AND angel magician. Ficino was a Catholic priest AND planetary magician. Agrippa wrote De Occulta Philosophia AND its apparent recantation De Vanitate. The tension is the interesting part.
- **Use the figure's OWN terminology** for their work (self_description field) alongside the modern scholarly label (external_label field). Ficino called his work *prisca theologia*; scholars call it "Hermeticism."
- **Do not flatten figures into "magicians."** Present multiple dimensions: religious, scientific, political, institutional.

### Section 2: Intellectual Context
**Purpose:** Place the figure in their tradition(s) and time
**Word target:** 80-150 words
**Required elements:**
- Which intellectual tradition(s) they engaged with (use figure_traditions relationship_type: PRACTICED, STUDIED, CRITICIZED, SYNTHESIZED, etc.)
- Key mentors, patrons, or institutional affiliations
- The historical moment they operated in (what was happening that made their work possible/necessary)
- **The tension:** what doesn't fit neatly into one category? What was contradictory or surprising about this figure's position?
**Tone:** Narrative scholarly
**Template:**
```
[Paragraph situating the figure in their intellectual milieu, naming specific
traditions, predecessors, and historical circumstances.]
```

### Section 3: Key Contributions
**Purpose:** What they created, wrote, or argued that matters
**Word target:** 100-200 words
**Required elements:**
- Named works (titles in italics)
- Specific ideas or innovations attributed to them
- How their work connected to or diverged from predecessors
- At least 1 corpus citation
**Tone:** Analytical
**Template:**
```
[Paragraph describing the figure's major works and arguments, with specific titles,
dates, and ideas. Reference at least one corpus document discussing this figure.]
```

### Section 4: Legacy & Significance
**Purpose:** Why this figure matters to the story of Renaissance magic
**Word target:** 50-100 words
**Required elements:**
- Who they influenced (name specific successors)
- How their work was received (celebrated? condemned? forgotten then rediscovered?)
- Their relevance to the broader narrative of this corpus
**Tone:** Evaluative but grounded
**Template:**
```
[Paragraph on the figure's influence, reception, and significance for
understanding Renaissance magic as an intellectual tradition.]
```

### Anti-patterns:
- Do NOT write a Wikipedia-style comprehensive life story — focus on the magic-relevant arc
- Do NOT list works without explaining what they argued
- Do NOT claim influence without naming who was influenced
- Do NOT use modern moral judgments ("ahead of his time," "sadly persecuted")
- For SCHOLAR figures: focus on their scholarly contribution, not their personal biography

---

## TEMPLATE 3: Document Summary

**Format:** Catalog entry for a corpus document
**Audience:** Researcher deciding whether to read the full document
**Total target:** 50-150 words

### Structure:
**Template:**
```
[1-3 sentences describing what this document argues or covers, naming the author,
the primary subject(s), and the approach or methodology. End with a note on
the document's relevance to Renaissance magic scholarship.]
```

### Required elements:
- Author surname
- What the document argues (not just its topic — its CLAIM)
- Which figure(s) or tradition(s) it addresses
- Whether it's a primary source, monograph, article, or review
- **Methodology note** (NEW): What scholarly approach does the author use? This is critical for readers evaluating the scholarship. Use one of: PHILOLOGICAL (textual analysis/editing), HISTORICAL (archival/contextual history), PHILOSOPHICAL (argument reconstruction), BIOGRAPHICAL, ICONOGRAPHIC (image/visual analysis), SOCIOLOGICAL (social history of magic), COMPARATIVE (cross-tradition/cross-cultural), RECEPTION_HISTORY (how texts/ideas were received), EDITORIAL (critical edition)

### Anti-patterns:
- Do NOT begin with "This document..."
- Do NOT merely state the topic without the argument ("About Dee" vs "Argues that Dee's Enochian system derives from...")
- Do NOT exceed 500 characters for the summary field
- Do NOT omit methodology — "what approach" matters as much as "what claim"

**Example (revised with methodology):**
> Copenhaver examines the philosophical foundations of Ficino's Hermetic translations, arguing through philosophical analysis that Ficino's Neoplatonic framework systematically reinterpreted the Egyptian Hermetica through a Christianizing lens. [Methodology: PHILOSOPHICAL]

**Example (iconographic):**
> Zika traces the visual representation of witchcraft in early modern woodcuts and engravings, arguing that images of cannibalism and sabbath functioned as instruments of social control. [Methodology: ICONOGRAPHIC]

**Example (philological):**
> Perrone Compagni provides a critical edition of Agrippa's De Occulta Philosophia, establishing the textual transmission from the 1510 manuscript to the 1533 printed edition. [Methodology: EDITORIAL/PHILOLOGICAL]

---

## TEMPLATE 4: Timeline Event

**Format:** Entry in the interactive timeline
**Audience:** General reader scanning a chronological overview
**Total target:** 30-80 words

### Structure:
**Template:**
```
**[Year]** — [Event title]
[2-3 sentences describing what happened and why it matters for Renaissance magic.
Name the figure(s) and text(s) involved.]
```

### Required elements:
- Year (or year range)
- Event type tag (PUBLICATION / BIOGRAPHY / SCHOLARSHIP / TRIAL / TRANSLATION / etc.)
- At least 1 named figure or text
- Why it matters (not just what happened)

### SCHOLARSHIP events (new per Gnosis analysis):
Include major MODERN SCHOLARLY events alongside historical ones:
- 1614: Casaubon redates the Hermetica (historical event with historiographic impact)
- 1964: Yates publishes *Bruno and the Hermetic Tradition* (establishes "Yates thesis")
- 2006: Hanegraaff publishes *Dictionary of Gnosis & Western Esotericism* (institutional recognition)
Tag these as event_type: SCHOLARSHIP

### Anti-patterns:
- Do NOT write "In [year], [person] was born" for every figure — only include births that are milestones
- Do NOT include events without connecting them to the Renaissance magic narrative
- Prefer publications, translations, trials, and controversies over births and deaths

**Example:**
> **1463** — Ficino translates the Corpus Hermeticum
> At the request of Cosimo de' Medici, Marsilio Ficino sets aside his Plato translations to render the newly discovered Greek Hermetica into Latin. This translation — published as *Pimander* — ignites European interest in Egyptian wisdom and establishes Hermeticism as a legitimate ancient philosophical tradition.

---

## TEMPLATE 5: Library Catalog Entry (Primary Source)

**Format:** Entry in the Referenced Texts library
**Audience:** Reader wanting to understand the intellectual sources Renaissance magi drew on
**Total target:** 100-250 words (now includes reception history)

### Section 1: Identification
**Template:**
```
*[Title]* ([original language title if different])
Author: [attributed author or "Anonymous" / "Pseudo-[author]"]
Date: [composition date or range]
Language: [original language]
Tradition: [HERMETIC / KABBALISTIC / ALCHEMICAL / NEOPLATONIC / etc.]
Era: [ANCIENT / MEDIEVAL / RENAISSANCE]
```

### Section 2: Significance
**Purpose:** Why this text matters for Renaissance magic
**Word target:** 80-150 words
**Required elements:**
- What the text contains (briefly)
- How Renaissance magicians used it (name at least 1 figure)
- Its role in the intellectual genealogy (what tradition it belongs to, what it transmitted)
- At least 1 corpus citation
**Tone:** Authoritative
**Template:**
```
[Paragraph explaining why this text was important to Renaissance magical practitioners
and scholars, who used it and how, and what role it plays in the intellectual genealogy
documented by this corpus.]
```

### Section 3: Reception History (NEW — per Gnosis analysis)
**Purpose:** How this text was understood THEN versus NOW
**Word target:** 40-80 words
**Required elements:**
- How Renaissance figures understood the text (e.g., Ficino believed Corpus Hermeticum was pre-Mosaic)
- How modern scholarship understands it (e.g., Casaubon/modern scholars date it to 2nd-3rd century CE)
- The gap between these understandings, if significant
**Template:**
```
[2-3 sentences noting what Renaissance readers believed about this text versus what
modern scholarship has established. This is where the historiographic dimension lives.]
```
**Example (for Corpus Hermeticum):**
> Renaissance scholars from Ficino onward believed these texts preserved pre-Mosaic Egyptian revelation, making Hermes Trismegistus older than Moses. Isaac Casaubon's 1614 philological analysis demonstrated they were composed in the 2nd-3rd century CE, collapsing the chronological foundation of the *prisca theologia*. Modern scholarship treats the Hermetica as documents of Greco-Egyptian religious syncretism.

### Anti-patterns:
- Do NOT describe the text's content in isolation from its Renaissance reception
- Do NOT assume the reader knows what e.g. the Zohar or Picatrix contains
- Do NOT present the Renaissance understanding as "wrong" — present it as historically situated

---

## TEMPLATE 6: Tradition/School Description

**Format:** Description for a tradition or intellectual school (used in taxonomy pages)
**Audience:** Reader navigating by intellectual tradition rather than by figure
**Total target:** 150-300 words

### Structure:
**Template:**
```
## [Tradition Name]

[2-3 sentences defining the tradition and its core claims or practices.]

**Key figures:** [figure1], [figure2], [figure3]
**Key texts:** [text1], [text2], [text3]
**Core concepts:** [term1], [term2], [term3]
**Era:** [primary period of activity]
**Relationship to Renaissance magic:** [1-2 sentences on how this tradition fed into
the Renaissance magical synthesis]

[Optional: 2-3 sentences on how this tradition is represented in our corpus —
which folders, which scholars study it.]
```

### Required elements:
- Definition that a non-specialist can understand
- At least 3 key figures
- At least 2 key texts
- Connection to the Renaissance magic narrative

### Anti-patterns:
- Do NOT assume the reader knows what "Neoplatonic" or "Hermetic" means
- Do NOT define by exclusion ("unlike...") before defining positively
- Do NOT conflate the historical tradition with modern New Age usage

---

## CROSS-CUTTING RULES

1. **Every piece of generated content must be traceable to the corpus.** If you can't cite a corpus document, don't make the claim.
2. **Every piece gets the AI disclosure banner** (stored as `review_status='DRAFT'`).
3. **Latin/Greek/Hebrew terms are italicized on first use** with English gloss.
4. **Cross-reference liberally** — link terms to figures, figures to texts, texts to timeline events.
5. **Provenance fields are mandatory:** `source_method='LLM_ASSISTED'`, `confidence='MEDIUM'`, `review_status='DRAFT'`.
6. **Length limits are hard constraints:** summaries ≤500 chars, brief definitions ≤100 chars.

---

*Generated by write-dominic-template for the Renaissance Magic Database Project.*
