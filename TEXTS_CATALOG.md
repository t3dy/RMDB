# Primary Texts Catalog — RenMagDB

**Compiled:** 2026-06-14 · **Maintainer:** RenMagDB project
**Purpose:** Catalog every primary text written by our historical figures; mark what we have read vs. what we still need; flag untranslated / unpublished / archival materials; and record web-researched sourcing leads for acquisition.

---

## Legend

| Mark | Meaning |
|------|---------|
| ✅ **READ** | Primary text (or a scholarly edition of it) is in our reading corpus (`corpus_document_id` set) |
| 🟡 **IN DB / UNREAD** | Catalogued in the `texts` table but we hold no copy in the corpus |
| ❌ **GAP** | Not in the database at all — needs to be added and sourced |
| 🌐 **SOURCING** | Web-researched acquisition lead recorded below |

**Database state at compile time:** 36 texts in `texts`, 29 figures, **5 primary texts linked to corpus documents we actually hold** (Pico *Heptaplus*, Agrippa *De Occulta Philosophia*, Reuchlin *De Arte Cabalistica*, Trithemius *Steganographia*, Dee *Monas Hieroglyphica*). Everything else is, at best, catalogued-but-unread.

> **Headline finding:** Our reading corpus is overwhelmingly *secondary scholarship* (Yates, Copenhaver, Zambelli, Clark, Hanegraaff, etc.). We have written 20 figure essays largely from that scholarship — but we have read almost none of the **primary sources** themselves. Closing this gap is the single biggest lever on the project's scholarly integrity.

---

## Part 1 — Reading-status summary

| Tradition cluster | Figures with essays | Primary texts we hold | Primary texts we lack |
|---|---|---|---|
| Ancient / Neoplatonic | Plato, Plotinus, Porphyry, Iamblichus | 0 | all |
| Islamic | Al-Kindi, Avicenna | 0 | all |
| Medieval | Albertus Magnus, Aquinas, Roger Bacon | 0 | all |
| Renaissance core | Ficino, Pico, Agrippa, Bruno, Dee | 3 (Pico, Agrippa, Dee) | most |
| Renaissance/early-modern | Paracelsus, Trithemius, Reuchlin, Della Porta, Fludd, Böhme | 2 (Trithemius, Reuchlin) | most |
| Critics / skeptics | Reginald Scot, Johann Weyer | 0 | all |

**Six figures have essays but no figure row in the database at all:** Thomas Aquinas, Porphyry, Giovan Battista Della Porta, Avicenna, Reginald Scot, Johann Weyer. These must be inserted into `figures` before their texts can be linked.

---

## Part 2 — Catalog by figure

### Ancient & Neoplatonic foundations

**Plato (c. 427–347 BCE)** — figure #89
- *Timaeus* — 🟡 IN DB (#4). The cosmological dialogue underwriting all later correspondence-cosmology. 🌐 Reliable text: Cornford, *Plato's Cosmology* (1937); Zeyl trans. (Hackett, 2000); Greek in Burnet OCT. Freely available (Perseus / Project Gutenberg, Jowett).
- *Republic*, *Symposium*, *Phaedrus*, *Phaedo* — ❌ GAP. Relevant to Ficino's *De Amore* and to the theory of the soul; worth cataloguing the dialogues Ficino actually translated.

**Plotinus (204–270)** — figure #90
- *Enneads* — 🟡 IN DB (#5). 🌐 Standard: Armstrong, 7 vols, Loeb (Greek+English, in print). Single-vol English: Gerson et al., *The Enneads* (Cambridge, 2018) or MacKenna (public domain, archive.org). Ficino's Latin *Enneads* (1492) is itself a primary Renaissance reception document worth a separate entry.

**Porphyry (234–305)** — ❌ figure GAP (essay written, no DB row)
- *Letter to Anebo* — ❌ GAP. The provocation behind Iamblichus's *De Mysteriis*. 🌐 Greek/English in the Society of Biblical Literature *De Mysteriis* volume (Clarke/Dillon/Hershbell, 2003) which prints the letter.
- *Isagoge* — ❌ GAP. The medieval logic primer. 🌐 Barnes trans. (Oxford, 2003).
- *Life of Plotinus* — ❌ GAP. Prefaces the *Enneads*; Armstrong Loeb vol. 1.
- *On the Cave of the Nymphs*, *Sententiae*, *De Abstinentia* — ❌ GAP.

**Iamblichus (245–325)** — figure #92
- *De Mysteriis* (*On the Mysteries*) — 🟡 IN DB (#6). 🌐 Clarke, Dillon & Hershbell, SBL Writings from the Greco-Roman World 4 (2003) — the standard Greek+English edition.
- *Protrepticus*, *De Vita Pythagorica*, *Theologoumena Arithmeticae* — ❌ GAP.

**Proclus (412–485)** — figure #91
- *Elements of Theology* — 🟡 IN DB (#7). 🌐 Dodds, 2nd ed. (Oxford, 1963), the definitive Greek+English. (Proclus has no essay yet — candidate addition.)

### Islamic transmission

**Al-Kindi (801–873)** — figure #93
- *De Radiis Stellarum* (*On the Stellar Rays* / *On Rays*) — 🟡 IN DB (#8). The theory-of-rays text central to medieval magic. 🌐 Latin ed. d'Alverny & Hudry, *AHDLMA* 41 (1974). No standard full English translation — **untranslated; sourcing = the Latin edition only.** Flag for translation-needed list.

**Avicenna / Ibn Sīnā (980–1037)** — ❌ figure GAP
- *Kitāb al-Shifāʾ* (*The Book of Healing*) — ❌ GAP. 🌐 Metaphysics: Marmura, *The Metaphysics of The Healing* (BYU, 2005, Arabic+English).
- *Canon of Medicine* (*al-Qānūn fī al-Ṭibb*) — ❌ GAP. 🌐 Gruner partial English (1930); Bakhtiar's multi-volume English (Great Books of the Islamic World).
- *Risāla fī al-ʿishq* (*Treatise on Love*) and the *Pointers and Reminders* — ❌ GAP.

### Medieval Latin natural philosophy

**Albertus Magnus (c. 1200–1280)** — figure #95
- *Speculum Astronomiae* — 🟡 IN DB (#13). Attribution debated. 🌐 Zambelli et al., *The Speculum Astronomiae and Its Enigma* (Kluwer, 1992) — we hold the Zambelli review-context already; the edition itself is the target.
- *De Mineralibus*, *De Animalibus* — ❌ GAP. 🌐 Wyckoff trans. of *Book of Minerals* (Oxford, 1967).
- Pseudo-Albertan *Liber Aggregationis* / *Secrets of Albertus Magnus* — ❌ GAP (important for *reception* even though spurious).

**Thomas Aquinas (1225–1274)** — ❌ figure GAP
- *Summa Theologiae* (esp. IIa-IIae qq. 92–96 on superstition & divination) — ❌ GAP. 🌐 Freely available (Latin+English, Aquinas Institute / newadvent.org).
- *Summa contra Gentiles* (III, on fate, celestial influence, demons) — ❌ GAP.
- *De occultis operibus naturae* — ❌ GAP. The short treatise on hidden powers; directly germane. 🌐 McAllister trans. (CUA, 1939).

**Roger Bacon (1214–1292)** — figure #96 (0 texts despite #35 *Opus Majus* sitting unattributed)
- *Opus Majus* — 🟡 IN DB (#35, **author_figure_id is null — needs relinking to #96**). 🌐 Burke trans., 2 vols (Pennsylvania, 1928; archive.org).
- *Opus Minus*, *Opus Tertium* — ❌ GAP (Brewer, Rolls Series, 1859; archive.org).
- *Epistola de secretis operibus artis et naturae* (*Letter on Secret Works*) — ❌ GAP. The alchemy/wonders letter; high relevance.
- *De multiplicatione specierum* — ❌ GAP (Lindberg, Oxford, 1983).

### Renaissance core

**Marsilio Ficino (1433–1499)** — figure #79
- *Theologia Platonica* — 🟡 IN DB (#14). 🌐 **Allen & Hankins, *Platonic Theology*, 6 vols, I Tatti Renaissance Library (Harvard, 2001–2006)** — Latin+English, in print. ([source](https://www.amazon.com/Platonic-Theology-Books-Renaissance-Library/dp/0674003454))
- *De Vita Libri Tres* (*Three Books on Life*) — 🟡 IN DB (#15). 🌐 **Kaske & Clark, *Three Books on Life*** (Renaissance Society of America / MRTS, 1989) — Latin+English, the standard.
- *De Amore* (commentary on Plato's *Symposium*) — ❌ GAP. 🌐 Jayne trans. (Spring Publications).
- *Letters of Marsilio Ficino* — ❌ GAP. 🌐 **Shepheard-Walwyn, 11+ vols (1975–2020), trans. School of Economic Science** — the standard English. ([source](https://plato.stanford.edu/entries/ficino/)) **Candidate for "unpublished/under-circulated correspondence" — the full Latin *Epistolae* span more than the translated selection.**
- Ficino's Latin translations of the *Corpus Hermeticum* (*Pimander*, 1471), Plato (1484), and Plotinus (1492) — ❌ GAP, but these are pivotal *reception* documents and should each be catalogued.

**Giovanni Pico della Mirandola (1463–1494)** — figure #76
- *Heptaplus* (1489) — ✅ READ (#18 → corpus #234).
- *Oration on the Dignity of Man* (1486) — 🟡 IN DB (#16). 🌐 **Borghesi/Papio/Riva, Cambridge 2012** (Latin+English) — we already hold this PDF in `Pico/`; **relink to corpus.**
- *900 Conclusiones / Theses* (1486) — 🟡 IN DB (#17). 🌐 **Farmer, *Syncretism in the West: Pico's 900 Theses*** (MRTS, 1998) — we hold this PDF in `Pico/`; **relink to corpus.**
- *Disputationes adversus astrologiam divinatricem* — ❌ GAP. The anti-astrology treatise; crucial counter-current. 🌐 Garin's Italian/Latin ed. (Vallecchi); no complete modern English.
- *Commento*, *De Ente et Uno* — ❌ GAP.

**Heinrich Cornelius Agrippa (1486–1535)** — figure #78
- *De Occulta Philosophia Libri Tres* — ✅ READ (#21 → corpus #338). 🌐 Latin critical: **Perrone Compagni, Brill 1992**; English: Tyson/Freake (Llewellyn). ([source](https://brill.com/edcollbook/title/1024))
- *De Vanitate Scientiarum et Artium* — 🟡 IN DB (#22). 🌐 1575 English (archive.org); modern partial eds.
- Correspondence (*Epistolae*, in the *Opera*, Lyon) — ❌ GAP; valuable for the recantation problem.

**Giordano Bruno (1548–1600)** — figure #77
- *De Umbris Idearum* (1582) — 🟡 IN DB (#29). 🌐 Latin in Tocco/Vitelli *Opera Latine* (Warburg digitization, giordanobruno.it); English trans. Scapparone / Gosnell.
- *De la Causa, Principio et Uno* (1584) — 🟡 IN DB (#28). 🌐 **de Lucca & Blackwell, *Cause, Principle and Unity, and Essays on Magic*, Cambridge Texts in the History of Philosophy (1998)** — also contains *De Magia* and *De Vinculis in Genere* in English. ([source](https://www.cambridge.org/us/academic/subjects/philosophy/philosophy-texts/giordano-bruno-cause-principle-and-unity-and-essays-magic))
- *De Magia* / *De Magia Mathematica* / *De Vinculis in Genere* — ❌ GAP (the explicitly magical Latin works). 🌐 English in the Cambridge volume above; new Black Letter Press translation; Latin in the Warburg *Bibliotheca Bruniana Electronica*.
- *Spaccio de la Bestia Trionfante*, *Cena de le Ceneri*, *De l'Infinito Universo et Mondi* — ❌ GAP (the Italian dialogues).

**John Dee (1527–1608)** — figure #75
- *Monas Hieroglyphica* (1564) — ✅ READ (#25 → corpus #117).
- *Five Books of Mystery* (*Mysteriorum Libri Quinque*, 1581–83) — 🟡 IN DB (#26). 🌐 **Peterson, *John Dee's Five Books of Mystery* (Weiser, 2003) — full text free on archive.org.** ([source](https://archive.org/details/JohnDeesFiveBooksOfMysterJosephH.Peterson))
- *A True and Faithful Relation…* (Casaubon, 1659) — 🟡 IN DB (#27). 🌐 esotericarchives.com transcription; Casaubon original on archive.org (typographically corrupt — flag).
- *Mathematicall Praeface* to Euclid (1570) — ❌ GAP. Essential for the "mathematics vs. magic" essay argument.
- *Propaedeumata Aphoristica* (1558) — ❌ GAP. 🌐 Shumaker & Heilbron (California, 1978).

### Renaissance / early-modern

**Paracelsus (1493–1541)** — figure #87 — **0 texts in DB (major gap)**
- *Astronomia Magna* (*Philosophia Sagax*) — ❌ GAP.
- *Opus Paramirum*, *Volumen Medicinae Paramirum*, *Paragranum* — ❌ GAP.
- *Archidoxis* (alchemical) and *De Vita Longa* — ❌ GAP.
- *Liber de Nymphis, Sylphis, Pygmaeis et Salamandris* — ❌ GAP (the elemental-spirits treatise).
- 🌐 **Critical edition + English: Andrew Weeks, *Paracelsus: Essential Theoretical Writings*, Aries/Brill (2008)** — German+English parallel, the modern standard. ([source](https://brill.com/display/title/13599?language=en)) German complete: **Sudhoff, *Sämtliche Werke*, 14 vols (1922–1933)** — not historical-critical but the working complete text. Older English: Waite, *Hermetic and Alchemical Writings* (1894, archive.org).

**Johannes Trithemius (1462–1516)** — figure #80
- *Steganographia* (c. 1499, pub. 1606) — ✅ READ (#23 → corpus #17). 🌐 Decryption keys: Ernst (1996) & Reeds (1998); Adam McLean edition (we hold it).
- *Polygraphia* (1518) — 🟡 IN DB (#24).
- *Antipalus Maleficiorum*, *De Septem Secundeis* — ❌ GAP.

**Johannes Reuchlin (1455–1522)** — figure #81
- *De Arte Cabalistica* (1517) — ✅ READ (#20 → corpus #285). 🌐 **Goodman trans., *On the Art of the Kabbalah* (Nebraska, 1993)** — Latin+English.
- *De Verbo Mirifico* (1494) — 🟡 IN DB (#19).

**Giovan Battista Della Porta (c. 1535–1615)** — ❌ figure GAP (essay written, no DB row), 0 texts
- *Magia Naturalis* (1558; expanded 20-book ed. 1589) — ❌ GAP. 🌐 **1658 English *Natural Magick* free on archive.org** (`naturalmagickbyj00port`). ([source](https://archive.org/details/naturalmagickbyj00port))
- *De Furtivis Literarum Notis* (cryptography, 1563) — ❌ GAP.
- *De Humana Physiognomonia* (1586) — ❌ GAP.

**Robert Fludd (1574–1637)** — figure #82
- *Utriusque Cosmi… Historia* (1617–1621) — 🟡 IN DB (#30). 🌐 Latin folios digitized (e.g. Wellcome, ETH-Bibliothek Zürich e-rara). No complete modern English; **flag untranslated.**
- *Apologia Compendiaria… Rosae Crucis* (1616), *Mosaicall Philosophy* (1659, English) — ❌ GAP.

**Jacob Böhme (1575–1624)** — figure #84
- *Aurora* (*Morgenröte im Aufgang*, 1612) — 🟡 IN DB (#31). 🌐 **Weeks & Hessayon critical English (Brill, *Aurora / Ein Morgen Röte*)**; Sparrow's 17th-c. English (Jacob Boehme Online / archive.org).
- *Mysterium Magnum*, *Signatura Rerum*, *De Tribus Principiis*, *The Way to Christ* — ❌ GAP. 🌐 Sparrow translations largely public-domain online.

### Critics & skeptics

**Reginald Scot (1538–1599)** — ❌ figure GAP, 0 texts
- *The Discoverie of Witchcraft* (1584) — ❌ GAP. 🌐 Nicholson facsimile (1886) and the Brinsley Nicholson text free on archive.org / gutenberg; Montague Summers ed. (1930).

**Johann Weyer (1515–1588)** — ❌ figure GAP, 0 texts
- *De Praestigiis Daemonum* (1563; 6th ed. 1583) — ❌ GAP. 🌐 **Mora (ed.) & Shea (trans.), *Witches, Devils, and Doctors in the Renaissance*, MRTS (1991) — full text on archive.org** (`witchesdevilsdoc0000weye`). ([source](https://archive.org/details/witchesdevilsdoc0000weye))
- *De Lamiis* (1577), *Pseudomonarchia Daemonum* (the demon-catalogue appendix) — ❌ GAP. 🌐 *Pseudomonarchia* English on esotericarchives.com.

---

## Part 3 — Anonymous / pseudonymous traditional texts (already in DB)

These have no single author and are catalogued unattributed:

| Text | DB id | Status | Sourcing lead |
|------|-------|--------|---------------|
| *Corpus Hermeticum* | #1 | 🟡 | Copenhaver, *Hermetica* (Cambridge, 1992) — we hold Copenhaver scholarship; get the edition |
| *Asclepius* | #2 | 🟡 | Copenhaver, *Hermetica* (same vol.) |
| *Pimander* | #3 | 🟡 | = CH I; Ficino's 1471 Latin is the Renaissance vector |
| *Picatrix* (*Ghāyat al-Ḥakīm*) | #9 | 🟡 | **Pingree Latin (Warburg, 1986); Greer & Warnock complete English (2011)** ([source](https://www.amazon.com/Complete-Picatrix-Classic-Astrological-Atratus/dp/1257767852)) |
| *Sefer Yetzirah* | #10 | 🟡 | Kaplan trans. (Weiser) |
| *Zohar* | #11 | 🟡 | Matt, *The Zohar: Pritzker Edition*, 12 vols (Stanford) |
| *Emerald Tablet* | #33 | 🟡 | Latin/Arabic; in any Hermetic/alchemical reader |
| *Ars Notoria* | #32 | 🟡 | Véronèse critical ed.; Peterson English |
| *Liber de Causis* | #36 | 🟡 | Guagliardo trans. (CUA, 1996) |
| *De Docta Ignorantia* (Cusanus) | #34 | 🟡 | Hopkins trans.; **relink to figure #94 Nicholas of Cusa** |
| *Ars Magna* (Llull) | #12 | 🟡 | Bonner, *Selected Works of Ramon Llull* (Princeton) — **relink to #86** |

---

## Part 4 — Untranslated / hard-to-source materials (translation- or acquisition-needed)

Ordered by scholarly priority for the project:

1. **Al-Kindi, *De Radiis*** — no standard complete English translation exists; only the d'Alverny & Hudry Latin (1974). **Highest "untranslated" flag** — central to the rays/influence thread, yet inaccessible to English readers.
2. **Robert Fludd, *Utriusque Cosmi Historia*** — vast Latin folios, never fully translated. Sourcing = e-rara / Wellcome facsimiles.
3. **Pico, *Disputationes adversus astrologiam*** — no complete modern English; Garin's Latin/Italian only.
4. **Bruno, Latin magical works** (*De Magia*, *De Vinculis*) beyond the Cambridge selection — full Latin only in the Warburg *Bibliotheca Bruniana Electronica*.
5. **Ficino, complete *Epistolae*** — the Shepheard-Walwyn English is a *selection* across 11 vols; the full Latin correspondence (Gentile's critical ed. of the *Lettere*) exceeds it. Candidate for "under-circulated correspondence."
6. **Paracelsus** — only a fraction is in modern critical English (Weeks); the bulk lives in Sudhoff's German *Sämtliche Werke*.
7. **Trithemius, *Antipalus Maleficiorum*** — little-edited, manuscript-bound.

**No genuinely *unpublished* (manuscript-only, never-printed) item is confirmed here** — but the closest are Trithemius's *Antipalus*, Dee's surviving diary manuscripts beyond the printed *Five Books*/*True Relation* (Bodleian / Sloane MSS, British Library), and Fludd's unpublished correspondence. These would require archival/MS digitization requests rather than a purchase.

---

## Part 5 — Acquisition shortlist (free vs. purchase)

**Free / public-domain (download now, add to corpus):**
- Dee, *Five Books of Mystery* (Peterson) — archive.org
- Weyer, *De Praestigiis* (Mora/Shea) — archive.org
- Della Porta, *Natural Magick* 1658 — archive.org
- Scot, *Discoverie of Witchcraft* — archive.org / Gutenberg
- Agrippa, *De Occulta* (we hold) + Tyson English; Böhme (Sparrow) online; Plotinus (MacKenna) online; Bruno Latin *Opera* (Warburg)

**Purchase / library (modern critical editions — highest value):**
- Ficino, *Platonic Theology*, 6 vols (I Tatti / Harvard)
- Ficino, *Three Books on Life* (Kaske & Clark)
- Bruno, *Cause, Principle and Unity & Essays on Magic* (Cambridge)
- Paracelsus, *Essential Theoretical Writings* (Weeks / Brill)
- Picatrix, complete English (Greer & Warnock) + Pingree Latin (Warburg)
- Iamblichus, *De Mysteriis* (Clarke/Dillon/Hershbell, SBL)
- Copenhaver, *Hermetica* (Cambridge)

---

## Part 6 — Database remediation tasks (derived from this catalog)

1. **Insert 6 missing figure rows:** Aquinas, Porphyry, Della Porta, Avicenna, Reginald Scot, Johann Weyer.
2. **Relink orphaned texts:** *Opus Majus* (#35 → Roger Bacon #96), *De Docta Ignorantia* (#34 → Cusanus #94), *Ars Magna* (#12 → Llull #86).
3. **Relink corpus copies we already hold:** Pico *Oration* and *900 Theses* PDFs in `Pico/` → set `corpus_document_id`.
4. **Add the GAP texts** above to `texts` with `source_method='LLM_ASSISTED'`, `review_status='DRAFT'`, `confidence='MEDIUM'`, plus the sourcing lead in `reception_history`.
5. **Populate `figures.key_works`** — currently empty for every figure.

> All sourcing leads in this document are **acquisition pointers**, not content. Per project rule #4 (corpus is source of truth), no claims from these external editions enter figure/term content until the edition is actually read and ingested.
