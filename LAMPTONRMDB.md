# LAMPTONRMDB.md — Lampton Corpus Analysis
## Renaissance Magic Database Project

**Date:** 2026-03-23
**Analyst:** Claude (plan-lampton-corpus)
**Status:** Post-Slice 2 — based on actual extracted data, not estimates

---

## CORPUS ANALYSIS: RenMagDB Research Collection

**DOCUMENTS:** 337 files, 321 unique markdown conversions
- **PDF:** 321 | **EPUB:** 10 | **HTML:** 5 | **CHM/TXT:** 1
- **Total extracted text:** ~150M chars across all .md files
- **Languages:** English 88%, Italian 5%, German 3%, French 1%, other 3%
- **Classifications:** Articles 90, Monographs 82, Reviews 41, Primary Sources 23, Anthologies 2, Unclassified 99

---

## ENTITIES

### People (from NER, frequency ≥ 20 across 337 documents)

**TIER 1 — Dominant Figures (corpus anchors):**

| Figure | NER Mentions | Folder Docs | Role |
|--------|-------------|-------------|------|
| John Dee | 355+ (combined variants) | 76 | English mathematician-magus, Enochian magic, Monas Hieroglyphica |
| Giovanni Pico della Mirandola | 306+ (combined) | 73 | Italian syncretic philosopher, 900 Theses, Christian Kabbalah |
| Giordano Bruno | 216+ (combined) | 30 | Italian cosmologist-magus, memory arts, heretical pantheism |
| Heinrich Cornelius Agrippa | 110+ | 25 | German occult philosopher, De Occulta Philosophia |
| Marsilio Ficino | 59+ | 7 | Italian Neoplatonist, Hermetica translator, Platonic theology |

**TIER 2 — Major Supporting Figures:**

| Figure | Evidence | Role |
|--------|----------|------|
| Johannes Trithemius | 32 dedicated docs | German abbot, Steganographia, cryptography-magic |
| Johannes Reuchlin | 13 dedicated docs | German Hebraist, De Arte Cabalistica, Christian Kabbalah |
| Robert Fludd | 5 dedicated docs | English Rosicrucian physician, cosmic harmonics |
| Athanasius Kircher | 3 dedicated docs | Jesuit polymath, Egyptology, magnetism |
| Jacob Böhme | 6 dedicated docs | German mystic, theosophy, Aurora |
| Francis Mercury van Helmont | 2 dedicated docs | Kabbalist, transmigration of souls |
| Paracelsus | 49 NER mentions | Swiss physician-alchemist, iatrochemistry |

**TIER 3 — Modern Scholars (prominent in corpus):**

| Scholar | Evidence | Specialization |
|---------|----------|---------------|
| Brian P. Copenhaver | 17 dedicated docs | Hermetica, Ficino, Renaissance philosophy |
| Frances A. Yates | NER frequent, 2+ monographs | Hermetic tradition, memory arts, Bruno |
| D.P. Walker | 1 major monograph | Spiritual and demonic magic, Ficino |
| Paola Zambelli | 2 monographs | Astrology, magic, white/black magic distinction |
| Charles Zika | 6 dedicated docs | Witchcraft, visual culture, demonology |
| Vittoria Perrone Compagni | 4 dedicated docs | Medieval/Renaissance magic philosophy |
| Adam McLean | 2 docs in root | Alchemy, angel magic, Trithemius |

**TIER 4 — Ancient/Medieval Authorities (referenced, not corpus authors):**

| Figure | Term Frequency Evidence | Era |
|--------|------------------------|-----|
| Plato | "timaeus" 1370 mentions | Ancient |
| Plotinus | "enneads" 360 mentions | Ancient |
| Hermes Trismegistus | "corpus hermeticum" 341, "asclepius" 684, "pimander" 317 | Ancient (attributed) |
| Pseudo-Aristotle (Sirr al-Asrar) | Referenced via Saif | Ancient/Medieval Islamic |
| Al-Kindi | Referenced via Saif, "picatrix" 420 | Medieval Islamic |
| Nicholas of Cusa | "docta ignorantia" 111, "coincidentia oppositorum" 78 | Medieval |
| Ramon Llull | "ars combinatoria" in Bruno/Lull folder, 30 docs | Medieval |

### Concepts (from term extraction, frequency-ranked)

**PHILOSOPHICAL FRAMEWORK (28,286 total occurrences):**
- forma (12,765) — Aristotelian/Neoplatonic form
- materia (7,654) — matter, prima materia
- corpus (2,403) — body, as distinct from spiritus
- spiritus (1,330) — spirit, intermediary between soul and body
- intellectus (863) — intellect, active/passive
- virtus (350) — power, virtue, occult quality
- animus (169) — soul/mind
- coincidentia oppositorum (78) — Cusan unity of opposites

**KABBALISTIC TRADITION (7,984 total):**
- kabbalah (3,251) — the tradition itself
- cabala (3,165) — Latinized variant (significant: nearly equal frequency with Hebrew form)
- zohar (941) — core Kabbalistic text
- gematria (223) — letter-number interpretation
- sephiroth (218) — divine emanations / Tree of Life
- ain soph — below threshold but expected in Pico/Reuchlin docs

**NEOPLATONIC TRADITION (5,998 total):**
- daemon/daimon (2,376 combined) — spiritual intermediary
- nous (1,402) — divine intellect
- emanatio (851) — procession from the One
- logos (506) — divine reason/word
- enneads (360) — Plotinus' central work
- hypostasis (195) — levels of being
- to hen (153) — the One

**MAGICAL PRACTICE (4,326 total):**
- monas hieroglyphica (809) — Dee's central symbol
- steganographia (617) — Trithemius' "hidden writing"
- de occulta philosophia (598) — Agrippa's magnum opus
- incantatio (538) — incantation
- invocatio (534) — invocation of spirits
- picatrix (420) — Arabic grimoire
- ars notoria (328) — angelic invocation for knowledge
- magia naturalis (192) — "natural" vs demonic magic
- sigillum (173) — seals/sigils
- grimoire (78) — book of magic

**HERMETIC TRADITION (2,662 total):**
- asclepius (684) — Hermetic dialogue
- hermetica (591) — the corpus
- prisca theologia (370) — ancient theology (Ficino's framing)
- corpus hermeticum (341) — core texts
- pimander (317) — first Hermetic treatise
- anima mundi (193) — world soul
- spiritus mundi (67) — world spirit

**ALCHEMICAL TRADITION (2,409 total):**
- sulphur (889) — one of the tria prima
- mercurius (374) — mercury, both metal and principle
- transmutatio (355) — transmutation of metals/soul
- elixir (318) — perfecting agent
- putrefactio (182) — first alchemical stage
- sublimatio (70) — purification process
- nigredo/albedo/rubedo — below threshold (surprising; may indicate corpus is more philosophical than operational)

### Works (Primary Sources Referenced)

**HERMETIC:**
- Corpus Hermeticum (freq: 341) — Ficino's 1463 translation
- Asclepius (freq: 684) — Latin Hermetic dialogue
- Pimander (freq: 317) — First treatise of Hermetica

**KABBALISTIC:**
- Zohar (freq: 941) — Core medieval Kabbalistic text
- Sefer Yetzirah — referenced in Pico/Reuchlin docs

**NEOPLATONIC:**
- Timaeus (freq: 1,370) — Plato's cosmological dialogue
- Enneads (freq: 360) — Plotinus

**MAGICAL:**
- De Occulta Philosophia (freq: 598) — Agrippa
- Steganographia (freq: 617) — Trithemius
- Monas Hieroglyphica (freq: 809) — Dee
- Picatrix (freq: 420) — Arabic grimoire (Ghayat al-Hikam)
- Ars Notoria (freq: 328) — Medieval angel-summoning text
- De Vita (freq: 1,272) — Ficino's Three Books on Life

**THEOLOGICAL:**
- Theologia Platonica (freq: 399) — Ficino
- Oration on the Dignity of Man — Pico (in folder via NER)

### Places (from NER, filtered for genuine locations)

Primary loci: Florence, London, Wittenberg, Rome, Basel, Venice, Prague, Paris, Louvain, Tübingen, Mortlake (Dee's home)

---

## TOPICS (Clustered from term + document evidence)

### Topic 1: CHRISTIAN KABBALAH
**Entities:** Pico, Reuchlin, cabala/kabbalah, sephiroth, gematria, zohar, sefer yetzirah, ain soph
**Documents:** 73 (Pico) + 13 (Reuchlin) + 1 (Christian Cabalah) + scattered = ~95 docs
**Finding:** This is the LARGEST thematic cluster by document count. The near-equal frequency of "kabbalah" (3,251) vs "cabala" (3,165) reflects the corpus straddling Jewish and Christian traditions.

### Topic 2: ENOCHIAN & ANGELIC MAGIC
**Entities:** Dee, monas hieroglyphica, invocatio, incantatio, ars notoria, sigillum, angel magic
**Documents:** 76 (Dee folder) + 2 (McLean angel magic) = ~78 docs
**Finding:** Dee dominates this cluster. His Monas Hieroglyphica (809 freq) is the single most-referenced primary work symbol. The HTML files contain diary excerpts — unique primary source material.

### Topic 3: HERMETIC PHILOSOPHY & PRISCA THEOLOGIA
**Entities:** Ficino, Copenhaver, corpus hermeticum, asclepius, pimander, prisca theologia, anima mundi, hermetica
**Documents:** 7 (Ficino) + 17 (Copenhaver) + Yates monograph + Walker monograph = ~30 docs
**Finding:** Despite fewer dedicated documents, Hermetic terms pervade the entire corpus. "asclepius" (684) and "hermetica" (591) appear across many non-Hermetic folders, showing Hermeticism as the substrate of Renaissance magic.

### Topic 4: NEOPLATONIC FRAMEWORK
**Entities:** Ficino, Plotinus, daemon/daimon, nous, emanatio, logos, enneads, hypostasis, to hen, theologia platonica
**Documents:** Ficino folder + Bruno/Lull + scattered across all folders
**Finding:** Neoplatonism is not a "topic" so much as the philosophical LANGUAGE of the entire corpus. Terms like daemon (1,871), nous (1,402), and emanatio (851) appear across every folder. This is the intellectual framework within which all other traditions operate.

### Topic 5: NATURAL MAGIC & OCCULT PHILOSOPHY
**Entities:** Agrippa, de occulta philosophia, magia naturalis, virtus, sympathia/antipathia, influxus
**Documents:** 25 (Agrippa) + scattered = ~35 docs
**Finding:** Agrippa's synthesis of natural magic is the practical counterpart to Ficinian/Hermetic theory. "de occulta philosophia" (598) is the most-referenced practical magic treatise in the corpus.

### Topic 6: CRYPTOGRAPHY, STEGANOGRAPHY & HIDDEN KNOWLEDGE
**Entities:** Trithemius, steganographia, ars notoria, hidden writing, codes
**Documents:** 32 (Trithemius)
**Finding:** A distinctive sub-cluster where magic intersects with information technology. Trithemius' cryptographic work is sometimes classified as magic, sometimes as proto-computer science.

### Topic 7: ALCHEMY & TRANSMUTATION
**Entities:** sulphur, mercurius, transmutatio, elixir, prima materia, nigredo/albedo/rubedo, putrefactio
**Documents:** Scattered across folders, not concentrated in any single folder
**Finding:** SURPRISING: No dedicated alchemy folder. Alchemical terms (2,409 total) are distributed across the corpus rather than concentrated. This corpus treats alchemy as a dimension of broader magical philosophy, not as a standalone subject. The low frequency of operational stage terms (nigredo, albedo, rubedo below threshold) suggests the corpus emphasizes alchemy's philosophical meaning over laboratory practice.

### Topic 8: WITCHCRAFT, DEMONOLOGY & PERSECUTION
**Entities:** Zika, Thomas, Peters, witchcraft, demons, trials
**Documents:** 6 (Zika) + Keith Thomas monograph + Edward Peters monograph + scattered reviews = ~12 docs
**Finding:** A distinct sociological cluster examining magic from the perspective of persecution and popular belief, rather than intellectual practice.

### Topic 9: ARABIC/ISLAMIC TRANSMISSION
**Entities:** Saif, picatrix, Al-Kindi, De Radiis, Sirr al-Asrar
**Documents:** 1 (Saif monograph) + Picatrix references scattered
**Finding:** COVERAGE GAP. Only 1 dedicated source (Saif) for the entire Islamic transmission pipeline. "picatrix" (420) appears frequently, showing the corpus REFERENCES Arabic sources but has limited scholarship specifically ABOUT the Arabic tradition. Liana Saif's book is critical infrastructure.

### Topic 10: COSMOLOGY & ASTROLOGY
**Entities:** Bruno, Fludd, decanus, ascendens, dignitas, influxus
**Documents:** 30 (Bruno) + 5 (Fludd) + Pico's anti-astrology disputations
**Finding:** Astrology terms are the lowest-frequency domain (340 total). The corpus engages more with the philosophical framework OF astrology than with astrological practice.

---

## RELATIONS (Key intellectual connections visible in corpus)

### Influence Chains (Directional)
```
Hermes Trismegistus --[attributed source]--> Corpus Hermeticum
Corpus Hermeticum --[translated by]--> Ficino (1463)
Ficino --[influenced]--> Pico della Mirandola
Ficino --[influenced]--> Agrippa
Pico --[synthesized]--> Reuchlin (Christian Kabbalah)
Agrippa --[synthesized De Occulta Philosophia from]--> Ficino + Trithemius + Pico
Trithemius --[teacher of]--> Agrippa
Trithemius --[influenced]--> Dee (Steganographia -> Monas)
Dee --[extended]--> Agrippa's angel magic framework
Bruno --[extended]--> Llull's combinatory art + Ficino's Hermeticism
Fludd --[extended]--> Paracelsian + Hermetic cosmology
Böhme --[independent parallel]--> Kabbalistic theosophy
Kircher --[synthesized]--> Egyptian Hermeticism + Jesuit universalism
```

### Tradition Flows
```
Ancient Greek (Plato/Timaeus, Plotinus/Enneads)
  ↓
Hermetic corpus (Corpus Hermeticum, Asclepius, Pimander)
  ↓
Arabic intermediaries (Al-Kindi, Picatrix, pseudo-Aristotle) ← Saif documents this
  ↓
Medieval Kabbalah (Zohar, Sefer Yetzirah)
  ↓
Renaissance synthesis:
  Ficino (Neoplatonic Hermeticism) → Pico (syncretic Kabbalah) → Reuchlin (Christian Kabbalah)
  Trithemius (angel magic + cryptography) → Agrippa (practical occultism)
  Dee (Enochian system) ← draws on ALL of the above
  Bruno (cosmic memory art) ← Llull + Ficino + Hermetica
```

### Opposition/Controversy Relations
```
Pico --[attacked]--> judicial astrology (Disputationes)
Church --[condemned]--> Bruno (burned 1600)
Church --[investigated]--> Dee (but never convicted)
Reuchlin --[defended Jewish books against]--> Pfefferkorn/Dominicans
Trithemius --[Steganographia suspected of]--> demon invocation
Agrippa --[De Vanitate recants]--> De Occulta Philosophia (but does it?)
```

---

## KNOWLEDGE GRAPH SCHEMA (Revised from corpus evidence)

### Nodes
| Type | Count (estimated) | Source |
|------|------------------|--------|
| HISTORICAL_FIGURE | ~30 | Folder mapping + NER top persons |
| MODERN_SCHOLAR | ~20 | Folder mapping + NER + bibliography |
| PRIMARY_TEXT | ~50 | Term extraction + NER titles |
| TRADITION | ~10 | Domain clustering from term extraction |
| CONCEPT | 84+ | Seed term list (expandable) |
| PLACE | ~15 | NER GPE extraction |
| EVENT | ~100 | NER dates + Wikidata (future) |

### Edges
| Type | Example | Source |
|------|---------|--------|
| INFLUENCED | Ficino -> Pico | Corpus analysis + LLM judgment |
| AUTHORED | Agrippa -> De Occulta Philosophia | Deterministic |
| TRANSLATED | Ficino -> Corpus Hermeticum | Deterministic |
| BELONGS_TO | Ficino -> Hermeticism | Domain classification |
| REFERENCES | [document] -> [primary text] | Term co-occurrence |
| SUBJECT_OF | [document] -> [historical figure] | Folder mapping |
| OCCURRED_IN | [event] -> [place] | NER |
| CONTEMPORARY_OF | Ficino <-> Pico | Birth/death dates |
| OPPOSED | Pico -> judicial astrology | Corpus evidence |
| TEACHER_OF | Trithemius -> Agrippa | Corpus evidence |

---

## COVERAGE GAPS

### Critical Gaps
1. **Arabic/Islamic transmission** — Only 1 dedicated source (Saif). The pipeline from Al-Kindi through the Picatrix translations to Latin Europe is underrepresented relative to its importance. Need additional scholarship on: Harranians, Jabir ibn Hayyan, Ibn Arabi, Razi.

2. **Paracelsus** — 49 NER mentions but ZERO dedicated documents. He's referenced everywhere but has no folder. This is a significant gap for a Renaissance magic corpus.

3. **Women practitioners** — Zero dedicated documents on women in Renaissance magic (aside from tangential Agrippa "Declamation on the Female Sex"). Missing: female alchemists, cunning women, witchcraft defendants as agents rather than victims.

4. **Ramon Llull** — Shares a folder with Bruno ("Bruno Lull") but Llull's own Ars Magna and combinatory art is underrepresented as an independent tradition. 30 docs in the folder, but how many are specifically about Llull vs. Bruno?

5. **Operative alchemy** — Low frequency of practical alchemical stage terms (nigredo, albedo, rubedo below detection threshold). The corpus treats alchemy philosophically. If the website should cover alchemical practice, additional sources needed.

6. **Visual/material culture** — Only Zika's work engages with images and visual representation of magic. Missing: emblem books (beyond Atalanta Fugiens, which is in the sister project), talismanic images, astrological diagrams.

### Secondary Gaps
7. **Eastern connections** — No documents on Byzantine transmission, Ethiopian magic, or Chinese alchemy parallels.
8. **Rosicrucianism** — Fludd was Rosicrucian but no dedicated Rosicrucian documents.
9. **Reformation context** — Limited coverage of how Protestant/Catholic split affected magical practice.
10. **Legal/institutional history** — Peters' "Magician, Witch, and the Law" covers this but alone.

---

## RECOMMENDED PIPELINE (Updated from actual data)

### What Worked (keep doing)
1. **Folder-based figure mapping** — 15 folders map cleanly to primary figures. This is the strongest signal.
2. **Seed term extraction** — 84/87 terms found in corpus. Good seed list coverage.
3. **Heuristic classification** — 71% coverage without LLM is strong for v1.
4. **Language detection** — Clean 88% English majority with interesting Italian/German minority.
5. **Duplicate detection** — 66 pairs caught, including cross-format pairs.

### What Needs Improvement
1. **NER quality** — Too much noise: "Vol", "Koninklijke Brill NV", "p. cm", "I. Title", "ed" are not people. Need a stop-list filter before seeding figures. Current 16 seeded figures include garbage entries.
2. **Abstract extraction** — 4% hit rate. Expand regex to catch "This paper argues...", "This study examines...", or first-paragraph-after-title heuristics for monographs.
3. **Term seed list expansion** — 87 terms found 84 matches, but many important terms are missing: "philosophia occulta" (alternate form), "ars memoriae" (memory art), "mundus imaginalis" (imaginal world), "scala naturae" already in list but low freq. Need ~200 more domain-specific terms.
4. **Figure deduplication** — "John Dee" and "Dee" and "John Dee's" are separate NER entities. Need a normalization pass.

### Next Steps (Slice 3-4)
1. **Clean NER data** — Apply stop-list, merge variants (Dee/John Dee/Dee's)
2. **Expand seed list** to ~300 terms based on what the corpus actually contains
3. **Seed figures from Wikidata** — The 15 folder-mapped figures + top NER persons, with biographical data
4. **TF-IDF clustering** — Will likely produce 8-12 clusters corresponding to the 10 topics identified above
5. **Build FTS5 index** — Full-text search across all 321 .md files

---

*Generated by plan-lampton-corpus for the Renaissance Magic Database Project. Based on actual extracted data from 337 documents, 84 terms, 5,303 unique NER persons.*
