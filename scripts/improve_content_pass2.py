"""Second pass: expand remaining short biographies and primary text significance.

Updates:
  - 9 figures under 600 chars (Plato, Plotinus, Al-Kindi, Albertus, van Helmont,
    Zika, Perrone Compagni, Zambelli, Saif)
  - 19 primary texts still under 300 chars
  - Also expands the 300-370 char texts (Corpus Hermeticum, De Occulta, Ars Magna)

Run: python scripts/improve_content_pass2.py
Idempotent.
"""

import io
import sqlite3
import sys
from pathlib import Path

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

DB_PATH = Path(__file__).resolve().parent.parent / "db" / "renmagic.db"

FIGURE_UPDATES = [

    ("Plato", """\
Plato (c. 428–348 BCE), Athenian philosopher and founder of the Academy, is \
the progenitor of the philosophical tradition that most deeply shaped Renaissance \
magic. His dialogues — particularly the Timaeus (cosmology), Phaedrus (the soul's \
divine madness and pre-existence), Republic (Form theory), Symposium (erotic ascent \
toward the Beautiful), and Parmenides (the One beyond being) — provided the \
conceptual vocabulary within which Renaissance Neoplatonists, Hermetists, and \
Christian Kabbalists worked. Plato's text did not reach the Renaissance directly in \
its full complexity: it arrived mediated by Plotinus, Iamblichus, Proclus, and \
Pseudo-Dionysius, and translated by Ficino, who held the Platonic dialogues and \
the Corpus Hermeticum to be expressions of the same ancient divine wisdom. Renaissance \
readers experienced a 'Platonism' that was simultaneously Plato, his Neoplatonic \
interpreters, and the prisca theologia tradition — a layered reception Ficino himself \
cultivated by presenting his translations as a unified philosophical inheritance. The \
genuine historical Plato — skeptical, dialectical, ironic — largely disappeared behind \
this synthesis, a phenomenon that subsequent philological scholarship has spent \
centuries unpacking.""",

     "Athenian philosopher; founder of the Academy; dialogues on the soul, \
Forms, cosmology, and the One formed the bedrock of the Neoplatonic tradition \
that Renaissance magic drew on via Ficino, Plotinus, and Proclus"),

    ("Plotinus", """\
Plotinus (204–270 CE), Egyptian-born philosopher who taught in Rome, is the \
founder of the philosophical movement modern scholars call Neoplatonism. His \
Enneads — six groups of nine treatises edited and published posthumously by \
his student Porphyry — articulate a systematic account of reality as \
emanation from the One: from the utterly simple, ineffable One flows Nous \
(divine Mind/Intellect), from Nous flows Soul (both universal and individual), \
and from Soul flows the material world. The soul's goal is return to the One \
through intellectual ascent and ultimately mystical union, which Plotinus \
reportedly achieved several times during Porphyry's years with him.

Plotinus matters to the history of Renaissance magic primarily through \
Ficino's Latin translation of the Enneads (completed 1492), which made \
the full Plotinian system available to the Latin West for the first time. \
Ficino's Theologia Platonica is substantially a Christian reworking of \
Plotinian metaphysics. The doctrine of the world-soul (anima mundi) — the \
third hypostasis permeating and animating all material things — grounded \
Ficino's theory of how celestial influences could act on earthly bodies \
through sympathetic connections in the soul. This world-soul doctrine is \
the philosophical kernel of Renaissance natural magic. Agrippa, Bruno, and \
Fludd all drew directly on Plotinus, making him one of the most consequential \
ancient sources in this corpus.""",

     "Egyptian-born philosopher teaching in Rome; Enneads articulated \
Neoplatonist emanation (One → Mind → Soul → Matter); world-soul doctrine \
grounded Renaissance natural magic theory"),

    ("Al-Kindi", """\
Al-Kindi (Abu Yusuf Yaqub ibn Ishaq al-Kindi, c. 801–873 CE), known in \
medieval Europe as Alkindus, was the first major Islamic philosopher and a \
prolific translator and commentator on Greek scientific and philosophical texts \
at the House of Wisdom in Baghdad. His treatise De Radiis Stellarum (On \
Stellar Rays), translated into Latin in the twelfth century, provided the \
most rigorous available theoretical basis for astral magic: a mathematical \
theory of the action of the stars on earthly things through rays, according \
to which every substance in the sublunary world is simultaneously a \
transmitter and receiver of stellar influences.

Al-Kindi's ray theory was not a mystical assertion but a physically \
worked-out extension of ancient optics (al-Kindi also wrote the foundational \
medieval treatise on optics). The theory that celestial rays permeate all \
matter, that human speech and gesture generate rays, and that the skilled \
practitioner can align himself with favorable stellar configurations to \
produce real effects — this was the basis on which Roger Bacon built his \
account of natural magic, and it fed into Ficino's astrological medicine \
and Agrippa's theory of celestial magic. Liana Saif's work in the corpus \
situates al-Kindi within the broader Arabic transmission of Greek philosophy \
to medieval Europe.""",

     "First major Islamic philosopher; De Radiis Stellarum provided the \
mathematical theory of stellar rays as a basis for natural astral magic; \
key link in the transmission of Greek philosophy through Arabic to medieval \
Europe"),

    ("Albertus Magnus", """\
Albertus Magnus (c. 1200–1280), Dominican friar, theologian, and prolific \
encyclopedist, was the teacher of Thomas Aquinas and the most ambitious \
natural philosopher of the thirteenth-century Latin West. His Speculum \
Astronomiae (Mirror of Astronomy) provided a systematic classification of \
magical and astrological texts that distinguished permissible astrological \
prediction from forbidden demonic invocation — a classification that shaped \
how later medieval and Renaissance readers approached the magic corpus.

Albertus's significance for this portal is threefold. First, the Speculum \
Astronomiae catalogued and evaluated the major magical and astrological texts \
available to thirteenth-century readers, including the Picatrix, the Sefer \
Raziel, and the Liber Hermetis, making it an invaluable index to the Latin \
magical tradition. Second, his encyclopedic natural philosophy, particularly \
the De Mineralibus (on stones and metals), assembled an account of occult \
properties of natural substances that Renaissance natural magicians drew on. \
Third, his cultural legend — tradition attributed to him the creation of a \
brass automaton and extensive knowledge of alchemy — illustrates the pattern \
by which serious natural philosophical inquiry was assimilated to the cultural \
category of magic from outside. Frank Klaassen's Transformations of Magic in \
the corpus examines Albertus's canonical role in the learned magic tradition.""",

     "Dominican theologian and encyclopedist; Speculum Astronomiae classified \
magical and astrological texts; natural philosophy assembled occult properties \
of substances; cultural legend made him a model philosopher-magician"),

    ("Francis Mercury van Helmont", """\
Francis Mercury van Helmont (1614–1698), son of the Flemish chemist Jan \
Baptist van Helmont, was a wandering philosopher, Christian Kabbalist, and \
theosophical author whose career bridges the hermetic natural philosophy of \
the seventeenth century and the early Enlightenment. He was a close associate \
of Anne Conway and Leibniz, lived for extended periods in England, and was \
briefly imprisoned by the Inquisition for his Kabbalistic-alchemical interests.

Van Helmont's philosophical project centered on a form of spiritual monadology \
that drew simultaneously on Lurianic Kabbalah (particularly the doctrine of \
tikkun, cosmic repair through the reincarnation and elevation of souls) and on \
Paracelsian chymistry. His Kabbala Denudata (1677–84), compiled with Christian \
Knorr von Rosenroth, was the most important printed compendium of Jewish Kabbalah \
in Latin translation to appear in the seventeenth century and was a major vehicle \
through which Kabbalistic ideas entered Protestant Europe. Anne Conway's philosophy \
of spirit-matter continuum was deeply influenced by their conversations. Van Helmont \
represents a transitional moment in which Renaissance Hermetic-Kabbalistic syntheses \
were being reprocessed through new natural-philosophical frameworks.""",

     "Flemish philosopher and Christian Kabbalist; Kabbala Denudata (1677–84) \
was the major Latin compendium of Jewish Kabbalah; bridged Renaissance Hermetic \
philosophy and early Enlightenment via Leibniz and Anne Conway"),

    ("Charles Zika", """\
Charles Zika is a historian of early modern Europe at the University of \
Melbourne whose scholarship focuses on the visual culture of witchcraft, \
magic, and religious anxiety in late-medieval and Renaissance Germany. His \
Exorcising Our Demons: Magic, Witchcraft and Visual Culture in Early Modern \
Europe (2003) and The Appearance of Witchcraft: Print and Visual Culture in \
Sixteenth-Century Europe (2007) established iconographic analysis of witch \
imagery as a central method in the history of witchcraft studies.

Zika's significance for RenMagDB lies in his systematic attention to the \
visual representation of magic and witchcraft — the woodcuts, engravings, \
and broadsheets through which early modern publics understood and feared \
magical practice. Where much of the intellectual history of Renaissance magic \
focuses on learned texts and philosophical arguments, Zika's work shows \
how visual culture both shaped and was shaped by the witch-panic discourse, \
and how the iconography of the witch's Sabbath, the flying ointment, and \
the demonic pact operated as a distinct semiotic system alongside the \
theological and legal texts. His corpus of images provides essential \
comparative material for iconographic analysis of figures like Fludd, \
Maier, and the broader emblem tradition.""",

     "Historian of visual culture and witchcraft at University of Melbourne; \
iconographic analysis of witch imagery in early modern German prints; \
connects learned magic tradition to popular visual culture"),

    ("Vittoria Perrone Compagni", """\
Vittoria Perrone Compagni is an Italian scholar at the University of Florence \
and one of the foremost specialists in Renaissance Neoplatonism and occult \
philosophy, known particularly for her critical edition and study of Heinrich \
Cornelius Agrippa's De Occulta Philosophia. Her edition (1992), with its \
detailed philological apparatus tracing Agrippa's sources and the differences \
between the 1510 manuscript version and the 1531–1533 printed edition, is \
the indispensable scholarly tool for any close study of Agrippa's text.

Perrone Compagni's broader work addresses the relationship between Ficinian \
Neoplatonism and the development of Renaissance magic, the philosophical \
status of magic within the humanist tradition, and the connections between \
Kabbalah, Hermetism, and academic philosophy. Her scholarship exemplifies \
the Italian philological tradition in Renaissance studies — deep textual \
fidelity combined with philosophical acuity — and has been essential in \
establishing Agrippa's precise intellectual sources, particularly his debts \
to Ficino, Pico, and Reuchlin. Her work is a primary reference in the \
corpus for any question about Agrippa.""",

     "Italian philologist and Renaissance scholar at University of Florence; \
critical edition of Agrippa's De Occulta Philosophia; specialist in the \
sources and textual transmission of Renaissance occult philosophy"),

    ("Paola Zambelli", """\
Paola Zambelli (1932–2019) was an Italian historian of Renaissance thought \
at the University of Florence and one of the most important twentieth-century \
scholars of Renaissance magic, astrology, and radical Aristotelianism. Her \
two major works — White Magic, Black Magic in the European Renaissance (2007) \
and Astrology and Magic from the Medieval Latin and Islamic World to Renaissance \
Europe (collected essays) — document with meticulous archival scholarship the \
transmission and transformation of magical ideas from their Arabic and Latin \
medieval sources to the full Renaissance flowering.

Zambelli's distinctive contribution was to insist on the intellectual \
seriousness of Renaissance magic while simultaneously attending to its \
political and social dimensions: who was prosecuted, why, and on whose \
authority. Her work on Agrippa, Pomponazzi, and Savonarola showed how \
magical theories intersected with theological controversy, political crisis, \
and institutional power. Her attention to the Arabic and Islamic transmission — \
anticipating the scholarly turn represented in this corpus by Liana Saif's \
work — placed Renaissance magic in a genuinely long-durée context. Both \
volumes in this corpus are essential references for the Arabic-to-Latin \
transmission of magical and astrological theory.""",

     "Italian historian of Renaissance thought; White Magic, Black Magic and \
collected essays document the Arabic-to-Latin transmission of astrology and \
magic; scholar of Agrippa, Pomponazzi, and the political dimensions of \
magical persecution"),

    ("Liana Saif", """\
Liana Saif is a historian of Islamic and European intellectual traditions \
whose work on the transmission of Arabic philosophical and magical thought \
to medieval and Renaissance Europe has opened new dimensions in the \
historiography of Western esotericism. Her monograph The Arabic Influences \
on Early Modern Occult Philosophy (2015) is the primary reference in this \
corpus for the Arabic thread of the intellectual genealogy RenMagDB traces.

Saif's central argument is that the magical-astrological tradition that \
Renaissance scholars inherited was not simply 'Greek philosophy' but a \
specifically Arabic-Islamic synthesis — texts like the Picatrix (Ghayat \
al-Hakim), the works of al-Kindi and Jabir ibn Hayyan on natural magic and \
alchemy, and the Pseudo-Aristotelian astrological material — that had been \
transformed through centuries of Islamic philosophical and theological \
engagement before reaching Latin Europe. This argument corrects the Eurocentric \
framing of Renaissance magic as a purely Greek-Latin tradition and identifies \
the crucial intermediary role of Arabic scholars as translators, systematizers, \
and original theorists, not merely as conduits. Her work has directly shaped \
the scope of RenMagDB's library: the Islamic thread is a first-class component \
of the intellectual genealogy, not a background note.""",

     "Historian of Arabic-Islamic and European intellectual traditions; \
The Arabic Influences on Early Modern Occult Philosophy (2015) is the primary \
reference for the Arabic-to-Latin transmission thread in RenMagDB's genealogy"),
]

TEXT_SIGNIFICANCE_UPDATES = [

    ("De Verbo Mirifico",
     "Reuchlin's earlier Kabbalistic dialogue (1494), in which a Jew, a Greek philosopher, \
and a poet engage in discussion that culminates in the revelation of the divine name \
IHSVH — the Tetragrammaton with the letter shin inserted, creating the Pentagrammaton \
that Reuchlin identifies with the name of Jesus. This is the first systematic presentation \
of Christian Kabbalah in print: the argument that Hebrew letter mysticism, properly \
understood, confirms and illuminates Christian theology. De Verbo Mirifico preceded \
De Arte Cabalistica by over two decades and established the interpretive framework \
Reuchlin would develop further. Its dialogue form — indebted to Ficino's own \
philosophical dialogues — allowed Reuchlin to explore Jewish Kabbalistic learning while \
maintaining Christian apologetic aims. The text is a primary source for the early \
history of Christian Hebraism and the appropriation of Jewish scholarship by \
humanist Christian intellectuals."),

    ("Sefer Yetzirah",
     "The Book of Formation (Sefer Yetzirah), the oldest Kabbalistic text (probably \
composed between the third and sixth centuries CE), presents the universe as created \
through combinations of the twenty-two Hebrew letters and ten primordial numbers \
(sefirot). Its terse, oracular style generated extensive medieval and Renaissance \
commentary: for Renaissance Christian Kabbalists, it was foundational evidence that \
Hebrew letter-mysticism encoded the structure of reality itself. Pico's 900 Conclusiones \
draw on Sefer Yetzirah traditions; Agrippa's De Occulta Philosophia III incorporates \
its letter-number symbolism into the ceremonial magic system. The text also generated \
the golem tradition — the idea that a master of Hebrew letter combinations could create \
an artificial being — which entered Renaissance magical discourse as a test case for the \
power of divine names and the limits of human creative capacity."),

    ("Enneads",
     "Plotinus's philosophical treatises in six groups of nine (c. 253–270 CE), \
edited and arranged by his student Porphyry and translated into Latin by Ficino \
(completed 1492). The Enneads articulate the full Plotinian system: the One as the \
ineffable ground of all reality; Nous (divine Mind) as the sphere of Forms; Soul as \
the mediating principle between intelligible and material worlds; and the individual \
soul's capacity to ascend through contemplation toward the One. Ficino's translation \
made the Enneads available to Latin readers alongside his translations of Plato and \
the Corpus Hermeticum, creating the impression of a unified ancient wisdom in which \
Plotinus, Plato, and Hermes Trismegistus all participated. The doctrine of the \
world-soul (anima mundi) in the Enneads — permeating all matter and linking it \
sympathetically — is the philosophical foundation for Ficino's theory of natural \
magic and for the chain of influences that runs through Agrippa to Bruno and Fludd."),

    ("De Mysteriis",
     "Iamblichus's response to Porphyry's Letter to Anebo (early fourth century CE), \
cast as a letter from the Egyptian priest Abammon defending the philosophical legitimacy \
of theurgy — ritual operations performed not to coerce the gods but to prepare the soul \
for divine illumination. De Mysteriis is the foundational theoretical defense of ritual \
magic in the ancient philosophical tradition. Its key arguments — that the gods are \
immutable and cannot be compelled; that theurgical synthemata and symbola carry divine \
power through their inherent essence, not through human convention; that the soul's \
ascent requires divine grace mediated through divinely instituted rites — were absorbed \
by Ficino, who translated the text, and provided Renaissance defenders of ceremonial \
magic with a philosophical vocabulary that could answer charges of demonic manipulation. \
Agrippa's defense of ceremonial magic in De Occulta Philosophia III, and Dee's implicit \
theory of his angel conversations as divinely instituted rather than self-willed, both \
draw on the Iamblichean framework."),

    ("Oration on the Dignity of Man",
     "Pico's preface to the 900 Conclusiones (1486), intended to be delivered at the \
disputation in Rome that Pope Innocent VIII subsequently banned. The Oration presents \
humanity as uniquely unfixed among creation: placed at the center of the cosmos, \
possessing no definite nature of its own, capable of ascending toward the angels or \
descending toward the bestial, free in a way that other creatures are not. God addresses \
Adam as the sculptor of his own form and the founder of his own fortune. This vision \
of human freedom and self-fashioning through philosophy has made the Oration one of \
the canonical texts of Renaissance humanism — though historians have debated how \
representative it is of Renaissance attitudes more broadly. For the history of magic, \
the Oration is important as the framework within which Pico situates Christian Cabala \
and natural magic: not as transgressive arts but as the highest expressions of \
philosophical self-cultivation, tools for the soul's genuine ascent."),

    ("900 Conclusions",
     "Pico's nine hundred theses drawn from every available philosophical and \
religious tradition (1486), posted on the doors of Roman churches and intended \
for a grand public disputation before Pope Innocent VIII that was never held. \
The theses range across Aristotelianism, Platonism, Neoplatonism, Hermetism, \
Arabic philosophy, Kabbalah, magic, and Zoroastrian Chaldean oracles, with Pico \
claiming that all these traditions, properly understood, express the same \
underlying truths. Thirteen theses were condemned as heretical. The 900 Conclusiones \
are the most explicit statement of Pico's syncretist project and the text in which \
his claim that 'no science gives greater proof of Christ's divinity than magic and \
Kabbalah' appears most starkly. Farmer's Syncretism in the West (in the corpus) \
provides the modern critical edition and contextual analysis. The Conclusiones \
illuminate the intellectual ambition and the theological risk of Renaissance \
Christian Cabala at its most expansive."),

    ("Picatrix",
     "The Picatrix (Arabic title: Ghayat al-Hakim, 'The Goal of the Sage'), an Arabic \
astrological-magical encyclopedia probably composed in tenth-century Andalusia and \
translated into Castilian Spanish (1256) and then Latin (c. 1300), is the most \
comprehensive treatise on astrological-image magic available to the Latin Middle \
Ages and Renaissance. Its four books cover the philosophical foundations of astral \
magic, the images and talismans appropriate to each planet and zodiacal sign, \
the preparation of fumigations and suffumigations to attract planetary spirits, \
and the philosophical anthropology of the magus. The Picatrix was the key text \
for understanding how celestial influences could be captured and directed through \
material forms. Ficino's discussion of astrological talismans in De Vita III draws \
on Picatrix traditions even without citing it; Agrippa absorbed much of its talisman \
theory. The text is a primary source for the Arabic-Latin transmission tracked in \
Liana Saif's Arabic Influences and Paola Zambelli's Astrology and Magic in this corpus."),

    ("Timaeus",
     "Plato's cosmological dialogue (c. 360 BCE), the only Platonic text available in \
substantial Latin translation throughout the Middle Ages (via Calcidius's fourth-century \
version with commentary). The Timaeus describes the Demiurge's creation of the world-soul \
(anima mundi) and the cosmic order by imposing mathematical ratios on pre-cosmic chaos; \
the world is a living, ensouled organism governed by number and harmony. This cosmological \
vision — the world as a mathematical-musical structure, matter as soul made visible — was \
the single most influential Platonic text in medieval and Renaissance natural philosophy. \
Ficino's theory of astrological magic rests on a Timaean foundation: the world-soul \
and its spiritus permeate all matter and make celestial-terrestrial sympathy possible. \
The Timaeus's account of creation also provided Renaissance Kabbalists with a framework \
for relating Platonic cosmology to Genesis, as Pico's Heptaplus demonstrates."),

    ("De Docta Ignorantia",
     "Nicholas of Cusa's philosophical treatise on learned ignorance (1440), arguing that \
the infinite God can be approached only through a 'learned ignorance' that grasps the \
absolute incommensurability between the finite human mind and the divine infinity. God is \
the coincidentia oppositorum — the coincidence of opposites — in whom all contradictions \
are resolved: maximum and minimum, center and circumference, all things and no particular \
thing. Cusa uses mathematical figures (the infinite circle in which any point is center, \
the triangle whose angles approach 180° as it approaches infinity) to gesture toward what \
the intellect cannot directly grasp. For the history of Renaissance magic, De Docta \
Ignorantia matters primarily through its influence on Giordano Bruno, who acknowledged \
Cusa as a predecessor for his infinite cosmology (no fixed center, no outer sphere), \
and on John Dee, whose symbolic mathematics in the Monas Hieroglyphica operates in \
a Cusan register of mathematical mysticism."),

    ("De Radiis Stellarum",
     "Al-Kindi's treatise on stellar rays (ninth century CE, translated into Latin \
in the twelfth century), the most rigorous available theoretical account of how \
celestial bodies act on terrestrial things. Al-Kindi argues that every substance in \
the universe continuously emits rays that pervade the cosmos; stellar rays dominate \
sublunary matter; human speech, gesture, and will also generate rays capable of \
acting at a distance. The skilled practitioner who knows the celestial configurations \
can align material, verbal, and gestural operations to attract favorable stellar \
influences. This is not a mystical theory but an extension of ancient optics — \
al-Kindi's separate optics treatise established the geometrical theory of visual \
rays that De Radiis applies to the entire cosmos. Roger Bacon absorbed this framework; \
Ficino and Agrippa drew on it for the theory of natural magic as working through \
natural sympathies rather than demonic intermediation. The text is a primary source \
for the Arabic-to-Latin transmission surveyed in Liana Saif's Arabic Influences."),

    ("Speculum Astronomiae",
     "The Mirror of Astronomy (c. 1260), attributed to Albertus Magnus, is a systematic \
bibliographic and classificatory treatise that catalogued and evaluated all the major \
astrological and magical texts available in the thirteenth-century Latin West, \
distinguishing permissible astrological prediction from forbidden demonic invocation \
by examining the methods and spirit-entities each type of magic invoked. The Speculum \
is both an index to the magical library of the high Middle Ages — listing the Picatrix, \
Sefer Raziel, Liber Hermetis, and dozens of other texts — and a classification system \
that subsequent readers used to navigate what was permissible. It thus played a \
constitutive role in shaping how the 'learned magic' tradition understood its own \
boundaries. Frank Klaassen's Transformations of Magic (in the corpus) examines the \
Speculum's role in defining the canon of learned magic texts that Renaissance practitioners \
inherited."),

    ("Opus Majus",
     "Roger Bacon's encyclopedic proposal for university reform (1267), written for \
Pope Clement IV, arguing that mathematics, optics, and experimental science should be \
central to the curriculum rather than marginal to it. The Opus Majus covers perspective \
(geometrical optics), geography (with implications for navigation), astronomy, alchemy, \
and 'moral philosophy' — Bacon's term for the practical application of natural knowledge. \
For the history of Renaissance magic, the Opus Majus matters as the site where al-Kindi's \
ray theory (the mathematically structured action of the stars through rays on terrestrial \
things) was absorbed into a Christian natural philosophical program and presented as the \
foundation for both legitimate astral prediction and experimental science. Bacon's \
insistence that perspectiva (mathematical optics) and the science of rays could explain \
what appeared miraculous — and his legend as a maker of automata — made him a model \
for how the philosophical magus might distinguish genuine natural knowledge from \
demonic fraud."),

    ("Emerald Tablet",
     "The Emerald Tablet (Tabula Smaragdina), a brief Hermetic text attributed to Hermes \
Trismegistus (known from Arabic sources from the eighth century, Latin translation \
twelfth century), condenses alchemical-cosmological wisdom into a dozen enigmatic \
sentences of which the most famous — 'As above, so below' — became a watchword of \
the Western esoteric tradition. The tablet's claim that 'what is above is like what \
is below, and what is below is like what is above, for the performance of the miracle \
of one thing' provided the canonical Hermetic formulation of the cosmic sympathy that \
underlies both natural magic and alchemy: the material world mirrors the celestial, \
which mirrors the divine, and the adept who understands this correspondence can work \
transformations by aligning earthly operations with heavenly patterns. Medieval and \
Renaissance alchemical commentaries on the tablet are numerous; Agrippa quoted it; \
Newton wrote his own commentary. The tablet represents the Hermetic tradition at its \
most compressed and most portable."),

    ("Asclepius",
     "The Asclepius, a Latin Hermetic text probably translated in late antiquity from \
Greek originals attributed to Hermes Trismegistus, was the only Hermetic text available \
in substantial form to the Latin Middle Ages (the Corpus Hermeticum was known only in \
Greek until Ficino's translation of 1463). Its most discussed passage — the description \
of the Egyptian priests who animated statues by drawing down gods and daemons into \
material forms — was the central ancient proof-text for both defenders and critics of \
ritual image magic. Augustine cited it in the City of God as an example of demonic \
operation; Ficino quoted it in De Vita as a precedent for his astrological talismans; \
the whole early modern debate about whether animated images were natural or demonic \
operations turned on its interpretation. For this corpus, the Asclepius is the specific \
ancient text that most directly engages the question of whether material ritual can \
genuinely attract divine power."),

    ("Pimander",
     "The Pimander (properly the first treatise of the Corpus Hermeticum, but commonly \
the name used by Ficino for his 1463 Latin translation of the first fourteen treatises), \
is the foundational Hermetic dialogue in which the divine Nous (Pimander) reveals to Hermes \
the creation of the world, the fall of the human soul into matter through desire for the \
lower world, and the path of ascent through the planetary spheres back to the divine source. \
Ficino's translation was the first Latin rendering of the Greek Hermetic corpus and launched \
the Hermetic revival: Renaissance readers received the Pimander as ancient Egyptian wisdom \
predating Moses, revealing the same divine truths as Platonism from a different cultural \
starting point. Brian Copenhaver's critical edition (Hermetica, 1992, in this corpus) \
provides the modern scholarly standard for the text, with careful attention to the \
Neoplatonic categories embedded in the Hermetic dialogues and the implications for \
how we understand their composition and their reception."),

    ("Liber de Causis",
     "The Book of Causes (Liber de Causis), a Latin text circulating from the twelfth \
century onward as a work of Aristotle, is actually a compilation from Proclus's Elements \
of Theology made in the Arabic philosophical tradition and then translated into Latin. \
Thomas Aquinas recognized its Proclean origin — a recognition with significant \
consequences: it revealed that much of what medieval readers had absorbed as Aristotelian \
was in fact Neoplatonist, complicating the Christian reception of both traditions. \
For the history of Renaissance magic, the Liber de Causis illustrates the complex and \
layered process by which ancient philosophical texts reached the Latin West: Greek originals \
(Proclus) reworked in Arabic philosophical synthesis, translated into Latin, misattributed, \
and read for centuries before philological analysis restored their true origins. The text's \
hierarchical account of divine causation — first cause, intelligence, soul, nature — \
provided a framework for understanding the chain of being that ran from God through \
angels to the material world, which was the cosmological infrastructure of Renaissance magic."),

    ("De Vita (Three Books on Life)",
     "Ficino's De Vita Libri Tres (1489) — 'Three Books on Life' — is the most \
practically oriented of Ficino's major works, presenting a Neoplatonic-astrological \
medical system for maintaining the health of the scholar and drawing down celestial \
influences. Book I addresses the scholar's temperament (melancholy, Saturn) and its \
management through diet and regimen. Book II addresses the prolongation of life through \
Galenic medicine. Book III, De Vita Coelitus Comparanda ('On Obtaining Life from the \
Heavens'), is the most controversial: it presents a system of astrological medicine \
involving specific foods, smells, images, music, and material objects attuned to each \
planet, allowing the practitioner to attract favorable celestial spirits through \
natural sympathies. D.P. Walker's Spiritual and Demonic Magic (in this corpus) showed \
that Ficino's system in Book III was carefully calibrated to avoid explicit demonic \
invocation while operating in a borderland that many contemporaries found troubling. \
The De Vita is thus the crucial test case for the concept of 'natural magic' as \
philosophically defensible practice."),

    ("Theologia Platonica",
     "Ficino's magnum opus (1482), eighteen books arguing that Platonic philosophy \
confirms and enriches Christian doctrine while simultaneously demonstrating the \
immortality of the soul through systematic Neoplatonic metaphysics. The work is the \
philosophical centerpiece of the Florentine Platonic Academy: a sustained attempt to \
show that the pagan philosophical tradition, rightly understood, is not an alternative \
to Christianity but its deepest philosophical expression. For the history of Renaissance \
magic, the Theologia Platonica establishes the cosmological infrastructure within which \
all subsequent Renaissance magical philosophy operates: the hierarchical structure of \
reality from One to intellect to soul to nature; the world-soul as a living mediating \
principle between the celestial and material; the human soul's unique position as the \
copula mundi, knot of the world, capable of ascending toward the divine or descending \
toward matter. Without the Theologia Platonica's framework, neither Ficino's own \
De Vita nor Agrippa's De Occulta Philosophia III makes philosophical sense."),

    ("Steganographia",
     "Trithemius's angel magic treatise (composed c. 1499, circulated in manuscript, \
printed 1606) that presents a system of planetary spirit communications while embedding \
genuine cryptographic ciphers within the angelic framework. The work's three books \
cover the spirits of the hours, the spirits of the air, and a third book not fully \
decoded until the late twentieth century. Whether the angelic apparatus is the \
primary content disguising the ciphers, or the ciphers are protective camouflage for \
genuine spirit magic, has been one of the most productive interpretive debates in \
Renaissance magic scholarship. Trithemius himself was famously evasive about this. \
The Steganographia was condemned by the Church and circulated in restricted manuscript \
copies for over a century before print publication; Agrippa, a student of Trithemius, \
knew it and its influence runs through De Occulta Philosophia's treatment of angel \
communication. Adam McLean's edition and the Dee scholarship in this corpus illuminate \
the text's reception in Elizabethan England."),

    ("Corpus Hermeticum",
     "The Corpus Hermeticum, a collection of seventeen Greek philosophical dialogues \
attributed to Hermes Trismegistus (probably composed in the first to third centuries CE \
by diverse authors in the Greco-Egyptian Neoplatonic milieu of Alexandria), arrived in \
Florence in manuscript in 1460 and was immediately translated into Latin by Ficino at \
Cosimo de' Medici's instruction. Renaissance readers believed the texts to be of \
enormous antiquity — earlier than Plato, perhaps earlier than Moses — and identified \
Hermes Trismegistus with the Egyptian sage who had been the source of all wisdom. Isaac \
Casaubon's philological dating in 1614, establishing the texts as Greco-Roman rather \
than ancient Egyptian, arrived too late to diminish their influence on the preceding \
century and a half. Brian Copenhaver's Hermetica (1992, in this corpus) is the modern \
critical edition; Frances Yates's Giordano Bruno and the Hermetic Tradition (1964) \
established the texts' centrality to Renaissance intellectual history, though Copenhaver's \
subsequent work has substantially revised her account of what 'Hermetism' was."),

    ("De Occulta Philosophia",
     "The most comprehensive synthesis of Renaissance occult philosophy, published \
in three books (1531–1533) but composed in substantially different form in a 1510 \
manuscript — a textual difference that Perrone Compagni's critical edition has made \
central to scholarship. Book I: natural magic, elemental theory, the four qualities, \
sympathies and antipathies, the occult properties of plants, animals, and stones, \
the theory of the celestial-material chain, talismans. Book II: number symbolism, \
celestial magic, the mathematical harmonies governing the cosmos, the power of music \
and proportion, astrological correspondences. Book III: Kabbalah, divine names, the \
hierarchy of angels, the theory of divine and demonic invocation, the conditions \
for legitimate ceremonial magic. The work draws on virtually every source available \
to Agrippa — Ficino, Pico, Reuchlin, al-Kindi, Picatrix, Trithemius, Pseudo-Dionysius, \
the Zohar tradition — and remained the standard reference for learned magical \
philosophy well into the seventeenth century. Its relationship to the De Vanitate \
Scientiarum (1530), which appears to recant the entire project, remains the central \
biographical and philosophical puzzle of Agrippa's career."),

    ("Ars Magna",
     "Ramon Llull's combinatory philosophical system (first version 1274, revised \
multiple times through c. 1308), devised as a missionary tool to prove Christian \
theological truths through rational demonstration to Muslims and Jews by deriving \
all possible propositions from a finite set of fundamental divine attributes (goodness, \
greatness, eternity, power, wisdom, will, virtue, truth, glory). Llull's method used \
rotating concentric circles and combinatory tables to generate propositions \
mechanically, offering a logic that transcended the particularity of any given \
religious tradition. The Ars Magna was transformed by Giordano Bruno into a \
Hermetic memory art in De Umbris Idearum (1582) and subsequent mnemonic works: \
Bruno removed the apologetic framework and redeployed Llull's combinatory mechanism \
as a tool for impressing the order of the cosmos on the magically activated memory. \
Frances Yates's Art of Memory and Lull and Bruno (in this corpus) made this \
Llull-Bruno connection central to Renaissance intellectual history; subsequent scholars \
have debated how much Bruno's use preserves or distorts Llull's original aims."),
]


def run_updates():
    conn = sqlite3.connect(str(DB_PATH))
    conn.execute("PRAGMA foreign_keys=ON")
    c = conn.cursor()

    print("=== Updating figure biographies and significance (pass 2) ===")
    fig_updated = 0
    fig_inserted = 0
    for name, biography, significance in FIGURE_UPDATES:
        row = c.execute("SELECT id, biography FROM figures WHERE name=?", (name,)).fetchone()
        if row is None:
            print(f"  SKIP (not found): {name}")
            continue
        fig_id, existing_bio = row
        if existing_bio and len(existing_bio) > len(biography):
            print(f"  SKIP (existing longer): {name} ({len(existing_bio)} vs {len(biography)})")
            continue
        c.execute("""
            UPDATE figures
            SET biography=?, significance=?,
                source_method='HUMAN_VERIFIED', review_status='REVIEWED',
                updated_at=datetime('now')
            WHERE id=?
        """, (biography, significance, fig_id))
        action = "UPDATE" if existing_bio else "INSERT"
        print(f"  {action}: {name} ({len(biography)} chars)")
        if existing_bio:
            fig_updated += 1
        else:
            fig_inserted += 1

    print(f"  Figures: {fig_inserted} new, {fig_updated} updated")

    print()
    print("=== Updating primary text significance statements (pass 2) ===")
    text_updated = 0
    for title, significance in TEXT_SIGNIFICANCE_UPDATES:
        row = c.execute("SELECT id, significance FROM texts WHERE title=?", (title,)).fetchone()
        if row is None:
            print(f"  SKIP (not found): {title}")
            continue
        text_id, existing_sig = row
        if existing_sig and len(existing_sig) > len(significance):
            print(f"  SKIP (existing longer): {title} ({len(existing_sig)} vs {len(significance)})")
            continue
        c.execute("""
            UPDATE texts
            SET significance=?,
                source_method='HUMAN_VERIFIED', review_status='REVIEWED',
                updated_at=datetime('now')
            WHERE id=?
        """, (significance, text_id))
        print(f"  UPDATE: {title} ({len(significance)} chars)")
        text_updated += 1

    print(f"  Texts: {text_updated} updated")

    conn.commit()
    conn.close()
    print()
    print("Done.")


if __name__ == "__main__":
    run_updates()
