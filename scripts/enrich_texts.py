"""Insert significance statements for all 36 primary texts."""
import io, sqlite3, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

DB = "db/renmagic.db"
conn = sqlite3.connect(DB)

sigs = {
    # ANCIENT — Hermetic
    1: "The foundational collection of Greco-Egyptian philosophical dialogues attributed to Hermes Trismegistus. Ficino's 1463 Latin translation made these texts available to the Renaissance and launched the Hermetic revival. Renaissance readers believed them to be the oldest philosophical texts in existence, predating Moses.",
    2: "A Latin Hermetic dialogue describing the animation of temple statues and prophesying the decline and restoration of Egyptian religion. The 'Lament of the Asclepius' became a key text for Renaissance magi who read it as describing legitimate theurgic operations.",
    3: "The first treatise of the Corpus Hermeticum, describing a visionary cosmogony in which the divine Mind (Nous) reveals the creation of the world. Ficino translated it first under the title Pimander, and it became the most widely read Hermetic text in the Renaissance.",
    33: "A brief alchemical text of uncertain origin, attributed to Hermes Trismegistus, that encodes the doctrine of macrocosm-microcosm correspondence in lapidary phrases. Its maxim 'As above, so below' became the fundamental axiom of Renaissance magical philosophy.",

    # ANCIENT — Neoplatonic
    4: "Plato's cosmological dialogue describing the demiurge's fashioning of the world-soul. The single most influential ancient text for Renaissance magical thought after the Hermetica, providing the framework of a living, mathematically structured cosmos.",
    5: "Plotinus's collected philosophical writings, organized by Porphyry into six groups of nine. Ficino's Latin translation (1492) made the full Neoplatonic metaphysical system — the One, Intellect, Soul, Matter — available to Renaissance readers.",
    6: "Iamblichus's philosophical defense of theurgy against Porphyry's objections. Established the principle that the soul cannot ascend through intellect alone but requires ritual operations using material symbols, divine names, and sacred tokens.",
    7: "Proclus's systematic axiomatization of Neoplatonic metaphysics into 211 propositions. Its hierarchical angelology and doctrine of divine names provided key resources for Renaissance Kabbalistic-Neoplatonic synthesis.",

    # ANCIENT — Kabbalistic
    10: "The earliest extant text of Jewish mystical cosmology, describing creation through the thirty-two paths of wisdom (ten sefirot and twenty-two Hebrew letters). A foundational source for both Jewish Kabbalah and Renaissance Christian Cabala.",

    # MEDIEVAL — Astrological
    8: "Al-Kindi's treatise theorizing that all things emit rays capable of producing effects at a distance. Provided the most sophisticated philosophical framework for astrological magic available to Latin Europe and profoundly influenced Ficino's natural magic.",
    13: "Attributed to Albertus Magnus, this treatise distinguishes between licit astronomical observation, acceptable astrological prediction, and condemnable necromantic magic. Its taxonomy framed how Renaissance magi argued for the legitimacy of their practices.",

    # MEDIEVAL — Magical
    9: "An Arabic compendium of astrological magic, talismanic art, and ritual procedures translated into Latin in 1256. The most comprehensive medieval manual of astral magic, it influenced Renaissance magical practice while remaining officially condemned.",
    12: "A Latin Art of the Spirits descended from medieval angelic invocation traditions. It proposed that divine knowledge could be infused directly into the practitioner through prayer, fasting, and ritual contemplation of sacred diagrams.",
    32: "A medieval Latin text prescribing methods for obtaining divine knowledge through angelic communication, combining prayer, fasting, and contemplation of sacred figures. Influenced Renaissance ceremonial magic traditions.",

    # MEDIEVAL — Kabbalistic
    11: "The central text of medieval Jewish mysticism, a mystical commentary on the Torah composed in Aramaic. Its elaborate sefirot theology, doctrine of divine emanation, and symbolic hermeneutics provided the richest source material for Renaissance Christian Cabala.",

    # MEDIEVAL — Philosophical
    34: "Nicholas of Cusa's treatise arguing that true wisdom consists in recognizing the limits of rational knowledge and that the infinite God transcends all finite categories. His coincidentia oppositorum influenced Pico's syncretism and Bruno's cosmology.",
    35: "Roger Bacon's encyclopedic treatise advocating for scientia experimentalis alongside mathematical and linguistic studies. Its discussions of optics, the power of words, and natural magic anticipated the empirical dimension of Renaissance magical philosophy.",
    36: "A Neoplatonic work falsely attributed to Aristotle, actually derived from Proclus's Elements of Theology. Its doctrine that all things proceed from and return to a First Cause was widely read in medieval and Renaissance philosophy as Aristotelian confirmation of emanation theory.",

    # RENAISSANCE — Hermetic
    15: "Ficino's practical application of Neoplatonic cosmology to astrological medicine. Book III's instructions for drawing down planetary influences through talismans, music, and fragrance represent Renaissance natural magic's most careful balancing act between philosophy and practice.",
    25: "Dee's dense symbolic treatise proposing a single hieroglyphic sign that encodes all cosmic knowledge. Marks his transition from mathematical humanism to Hermetic philosophy and contains his most concentrated philosophical vision.",
    28: "Bruno's Italian dialogue arguing that God and Nature are one infinite substance — a pantheistic monism that pushed Neoplatonic emanation theory to its radical conclusion. Part of his explosive London dialogues of 1583-1585.",
    30: "Fludd's encyclopedic cosmology illustrated with extraordinary full-page engravings mapping the correspondence between macrocosm and microcosm. The most visually ambitious work of Renaissance Hermetic philosophy.",

    # RENAISSANCE — Kabbalistic
    16: "Pico's declaration of human intellectual freedom, composed as a preface to his 900 Conclusions. Its vision of humanity standing at the center of creation, free to ascend or descend, has become one of the defining texts of Renaissance humanism.",
    17: "Pico's 900 theses drawn from every available philosophical and theological tradition, presented for public disputation in Rome. Thirteen were condemned as heretical, but the project established the principle of universal philosophical concordance.",
    18: "Pico's sevenfold allegorical commentary on Genesis, applying Kabbalistic and Neoplatonic methods to the creation narrative. A key demonstration of how Christian Cabala could serve as a tool of scriptural exegesis.",
    19: "Reuchlin's first Kabbalistic treatise, demonstrating that the divine name Pentagrammaton (YHSVH) encodes the mystery of the Incarnation. Established the method of deriving Christian theological truths from Hebrew letter mysticism.",
    20: "Reuchlin's mature Kabbalistic treatise, presented as a dialogue between a Pythagorean, a Muslim, and a Cabalist. The most systematic Renaissance treatment of Kabbalistic methods (gematria, notarikon, temurah) applied to Christian theology.",

    # RENAISSANCE — Magical
    21: "Agrippa's comprehensive three-book synthesis of natural, celestial, and ceremonial magic. The most influential Renaissance magical encyclopedia, it organized the entire tradition into a systematic philosophical framework and remained the standard reference for over a century.",
    22: "Agrippa's apparent recantation of the entire magical enterprise, published one year before De Occulta Philosophia. Whether this represents genuine disillusionment, self-protection against heresy charges, or dialectical strategy remains debated.",
    23: "Trithemius's angel magic treatise that embeds genuine cryptographic ciphers within a framework of planetary spirit communications. Whether the angelic apparatus conceals the ciphers or the ciphers serve genuine spiritual practice remains one of the great puzzles of Renaissance intellectual history.",
    24: "Trithemius's posthumous treatise on polyalphabetic ciphers — the first printed book on cryptography. A companion to the Steganographia, it presents the technical cryptographic content without the angelic framework.",
    29: "Bruno's treatise on the art of memory, using magical images as mnemonic devices that simultaneously serve as instruments of Hermetic contemplation. Transforms Llull's combinatory art into a magical memory system.",

    # RENAISSANCE — Enochian
    26: "Dee's meticulous diary records of his angel conversations with Edward Kelley, covering the earliest phase of the Enochian revelations including the Heptarchic system of angelic governance and the Sigillum Dei Aemeth.",
    27: "Casaubon's 1659 publication of Dee's angel diaries, framed as evidence of demonic deception. Despite the hostile editorial framing, this publication preserved the Enochian material and made it available to subsequent practitioners and scholars.",

    # EARLY MODERN — Theological
    31: "Boehme's first visionary work, describing creation as a process of divine self-manifestation through opposing principles. Written by a cobbler with no formal training, it inaugurated a theosophical tradition that influenced German Idealism and Western esotericism.",
}

updated = 0
for tid, sig in sigs.items():
    conn.execute(
        "UPDATE texts SET significance=?, source_method='LLM_ASSISTED', confidence='MEDIUM', review_status='DRAFT', updated_at=datetime('now') WHERE id=?",
        (sig, tid),
    )
    if conn.execute("SELECT changes()").fetchone()[0] > 0:
        updated += 1

conn.commit()
total = conn.execute("SELECT COUNT(*) FROM texts WHERE significance IS NOT NULL").fetchone()[0]
print(f"Text significance updated: {updated}")
print(f"Total with significance: {total}/36")
conn.close()
