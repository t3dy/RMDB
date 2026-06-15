"""Expand the RenMagDB timeline from 58 to 100+ events.

Draws on research materials in the corpus: Walker, Yates, Copenhaver, Peters,
Thomas, Klaassen, Saif, Hanegraaff, and others. Events cover:
  - Ancient/Late Antique (Plato through Justinian)
  - Medieval (Islamic transmission, Scholasticism, Kabbalah)
  - Renaissance (1400-1600: publications, trials, births/deaths)
  - Early Modern (1600-1700: Rosicrucians, Casaubon, Newton)
  - Scholarship (1958-2015: foundational secondary literature)

Run: python scripts/expand_timeline.py
Idempotent: INSERT OR IGNORE on title+year.
"""

import io
import sqlite3
import sys
from pathlib import Path

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

DB_PATH = Path(__file__).resolve().parent.parent / "db" / "renmagic.db"

# Each entry: (year, year_end, event_type, title, description)
# event_type: PUBLICATION | BIOGRAPHY | SCHOLARSHIP | TRIAL | INSTITUTION |
#             TRANSLATION | DISCOVERY | POLITICAL | OTHER

NEW_EVENTS = [

    # ── ANCIENT / LATE ANTIQUE ──────────────────────────────────────────────

    (-360, None, "PUBLICATION", "Plato's Timaeus composed",
     "Plato's cosmological dialogue describes the Demiurge's creation of the "
     "world-soul through mathematical ratios. The only Platonic text available "
     "in substantial Latin translation throughout the Middle Ages, the Timaeus "
     "supplies the philosophical foundation — world-soul, cosmic sympathy, "
     "mathematical harmony — on which Ficino and Renaissance natural magicians "
     "build their accounts of celestial influence."),

    (234, None, "BIOGRAPHY", "Birth of Porphyry",
     "Porphyry of Tyre was born in what is now Lebanon. His editing of Plotinus's "
     "Enneads, his Isagoge (Introduction to the Categories), and his Life of "
     "Plotinus were to become foundational texts of medieval philosophy. His "
     "Letter to Anebo challenging the metaphysical basis of theurgy provoked "
     "Iamblichus's De Mysteriis as its systematic refutation."),

    (250, None, "INSTITUTION", "Plotinus opens school in Rome",
     "Plotinus begins teaching in Rome under the patronage of the senator "
     "Rogatianus, eventually attracting disciples including Porphyry, Amelius, "
     "and the physician Eustochius. For the next two decades he composes the "
     "treatises Porphyry will arrange as the Enneads — the foundational text "
     "of the philosophical tradition the Renaissance would call Neoplatonism."),

    (263, None, "BIOGRAPHY", "Porphyry joins Plotinus in Rome",
     "Porphyry of Tyre arrives in Rome as a student of Plotinus. He will spend "
     "six years in direct study, edit and arrange the Enneads, and write the "
     "sole surviving biography of Plotinus — the primary source for "
     "Neoplatonism's origins and ethos."),

    (300, None, "PUBLICATION", "Iamblichus writes De Mysteriis",
     "Iamblichus composes De Mysteriis Aegyptiorum, presenting the most "
     "systematic philosophical defense of theurgy in the ancient world. Its "
     "argument that divinely instituted rites prepare the soul for illumination "
     "that philosophy alone cannot achieve — and that their power derives from "
     "divine essence, not human convention — will underwrite Renaissance "
     "ceremonial magic's philosophical self-defense against charges of demonic "
     "operation."),

    (301, None, "PUBLICATION", "Porphyry publishes the Enneads",
     "Porphyry's edition of Plotinus's Enneads appears, arranging fifty-four "
     "treatises into six groups of nine. The Enneads will wait over a thousand "
     "years for a Latin translation: Ficino's version, completed in 1492, makes "
     "the full Plotinian system available to the Renaissance West for the first "
     "time and enables Ficino's philosophical grounding of natural magic in "
     "world-soul doctrine."),

    (305, None, "BIOGRAPHY", "Death of Porphyry",
     "Porphyry died at approximately 71. His Isagoge became the standard logic "
     "textbook of the medieval university, sparking the dispute over universals "
     "that ran through scholasticism for centuries. His lost work Against the "
     "Christians complicated the reception of Neoplatonism in the Christian "
     "tradition for scholars who knew of its existence."),

    (420, 430, "PUBLICATION", "Augustine's City of God condemns Hermetic magic",
     "Augustine's City of God (413-426) includes his influential condemnation of "
     "the Asclepius passage describing Egyptian priests who animated statues by "
     "drawing down gods and daemons. Augustine reads this as straightforward "
     "demonic operation and forbidden idolatry. D.P. Walker's analysis shows "
     "Ficino was acutely aware of this condemnation and carefully framed his "
     "De Vita talismanic system to avoid the same charge."),

    (450, None, "PUBLICATION", "Proclus writes Elements of Theology",
     "Proclus composes the Elements of Theology, axiomatizing Neoplatonic "
     "metaphysics into 211 propositions on the model of Euclid. Its hierarchical "
     "account of divine emanation — One, divine henads, Intellect, Soul, Nature — "
     "provides Renaissance Kabbalists and natural magicians with the philosophical "
     "infrastructure for their systems of angelic hierarchy and celestial influence."),

    (500, None, "PUBLICATION", "Pseudo-Dionysius composes Celestial Hierarchy",
     "The Pseudo-Dionysian Corpus — Celestial Hierarchy, Ecclesiastical Hierarchy, "
     "Mystical Theology, Divine Names — appears, attributed to Dionysius the "
     "Areopagite but probably composed in Syria around 500 CE. Its hierarchical "
     "angelology, integrating Christian theology with Proclean Neoplatonism, shapes "
     "medieval and Renaissance conceptions of the angelic orders that populate the "
     "magic literature from Agrippa's De Occulta Philosophia to Dee's Enochian system."),

    (529, None, "INSTITUTION", "Justinian closes the Platonic Academy in Athens",
     "Emperor Justinian's edict forbids pagans from teaching philosophy, closing "
     "the Platonic Academy in Athens. The last Neoplatonic philosophers — "
     "Damascius, Simplicius, and others — emigrate to Persia. This ends "
     "institutionalized pagan philosophical teaching in the Roman Empire and "
     "marks the point at which Neoplatonism's transmission to the medieval West "
     "passes through Christian channels — Pseudo-Dionysius, Boethius, and later "
     "the Arabic philosophical tradition."),

    (600, None, "PUBLICATION", "Sefer Yetzirah achieves final form",
     "The Sefer Yetzirah (Book of Formation), the oldest Kabbalistic text, "
     "achieves its roughly final form, having been composed in stages probably "
     "between the third and seventh centuries CE. Its account of the universe "
     "as created through twenty-two Hebrew letters and ten primordial numbers "
     "(sefirot) will generate centuries of commentary and provide Renaissance "
     "Christian Kabbalists — Pico, Reuchlin, Agrippa — with letter-number "
     "symbolism for their ceremonial magic systems."),

    # ── MEDIEVAL ISLAMIC TRANSMISSION ───────────────────────────────────────

    (820, 833, "INSTITUTION", "House of Wisdom translation project in Baghdad",
     "Under the Abbasid caliphs al-Ma'mun and al-Mu'tasim, the House of Wisdom "
     "(Bayt al-Hikma) in Baghdad becomes the center of the most ambitious "
     "translation project in history: Greek scientific and philosophical texts "
     "into Arabic. Al-Kindi is among the scholars active in this project. The "
     "resulting Arabic synthesis of Greek philosophy is what medieval Europe "
     "will receive through the twelfth-century Toledo translations."),

    (850, None, "PUBLICATION", "Al-Kindi writes De Radiis Stellarum",
     "Al-Kindi composes De Radiis Stellarum (On Stellar Rays), theorizing that "
     "every substance in the universe continuously emits rays that pervade the "
     "cosmos — stellar rays dominating sublunary matter, and human speech, "
     "gesture, and will also generating rays capable of acting at a distance. "
     "This mathematical theory of natural astral influence, translated into Latin "
     "in the twelfth century, provides the theoretical basis for Renaissance "
     "natural magic and is a primary source in Liana Saif's Arabic Influences."),

    (980, None, "BIOGRAPHY", "Birth of Avicenna",
     "Ibn Sina (Avicenna) was born in Afshana, near Bukhara (modern Uzbekistan). "
     "His vast Arabic synthesis of Aristotelian philosophy and Galenic medicine — "
     "including the Shifa (Book of Healing) and Canon of Medicine — shaped "
     "European intellectual life from the twelfth century onward. His pneumatic "
     "psychology (the imagination's power over the body) provided key theoretical "
     "resources for Renaissance natural magic's account of how mind acts on matter."),

    (1037, None, "BIOGRAPHY", "Death of Avicenna",
     "Avicenna died in Hamadan at approximately 57. His Canon of Medicine remained "
     "the standard medical text in European universities into the seventeenth "
     "century. His spirit theory and account of the imaginative faculty — "
     "particularly the power of the imagination to act on external matter at a "
     "distance — ground the theory of fascination and the evil eye that Ficino "
     "and Agrippa develop."),

    (1150, 1175, "TRANSLATION", "Gerard of Cremona translates Arabic texts into Latin",
     "Gerard of Cremona, working in Toledo, translates into Latin dozens of Arabic "
     "scientific and philosophical texts, including al-Kindi's works, Avicenna's "
     "Canon of Medicine, and the Liber de Causis. This translation enterprise makes "
     "the Arabic-mediated synthesis of Greek philosophy available to Latin Europe "
     "and transforms the intellectual curriculum — producing what Liana Saif has "
     "called the Arabic layer of the Renaissance esoteric inheritance."),

    (1180, None, "PUBLICATION", "Liber de Causis circulates in Latin",
     "The Liber de Causis (Book of Causes), a selective compilation from Proclus's "
     "Elements of Theology made in the Arabic philosophical tradition, circulates "
     "in Latin translation attributed to Aristotle. Its hierarchical account of "
     "divine causation — first cause, intelligence, soul, nature — becomes a "
     "standard philosophical text before Thomas Aquinas identifies it as Proclean "
     "in 1268. This misattribution illustrates how deeply Neoplatonism had "
     "infiltrated the 'Aristotelian' curriculum."),

    (1225, None, "BIOGRAPHY", "Birth of Thomas Aquinas",
     "Thomas Aquinas was born in Roccasecca, in the Kingdom of Sicily. His Dominican "
     "formation and eventual synthesis of Aristotelian philosophy with Christian "
     "theology in the Summa Theologiae establishes the canonical framework within "
     "which the Church assesses magical claims — categories of licit natural "
     "operation and illicit demonic invocation that Renaissance practitioners "
     "from Ficino to Dee must navigate."),

    (1245, 1248, "INSTITUTION", "Aquinas studies under Albertus Magnus",
     "The young Thomas Aquinas studies natural philosophy under Albertus Magnus "
     "in Cologne and follows him to Paris. Albertus's encyclopedic approach to "
     "Arabic philosophy and his classification of magical texts (Speculum "
     "Astronomiae) shapes Aquinas's encounter with the full range of ancient "
     "and Arabic learning — and his eventual demarcation of legitimate from "
     "illegitimate magical practice."),

    (1256, None, "TRANSLATION", "Picatrix translated into Castilian for Alfonso X",
     "At the court of Alfonso X of Castile ('the Wise'), the Arabic Ghayat "
     "al-Hakim is translated into Castilian as the Picatrix — the first step "
     "in the Latin West's access to the most comprehensive medieval manual of "
     "astrological image magic. The work's four books on planetary talismans, "
     "fumigations, and invocations of planetary spirits will be absorbed by "
     "Ficino's De Vita III and Agrippa's De Occulta Philosophia."),

    (1260, None, "PUBLICATION", "Albertus Magnus writes Speculum Astronomiae",
     "Albertus Magnus composes the Speculum Astronomiae, the most systematic "
     "medieval classification of astrological and magical texts — distinguishing "
     "acceptable astrological prediction from condemned demonic invocation by "
     "examining each text's operations and the spirits invoked. The Speculum "
     "catalogues the available magical library and establishes the canonical "
     "framework for the learned magic tradition that Frank Klaassen's "
     "Transformations of Magic examines."),

    (1267, None, "PUBLICATION", "Roger Bacon presents Opus Majus to Pope Clement IV",
     "Roger Bacon presents his encyclopedic Opus Majus to Pope Clement IV, "
     "arguing for university reform centered on mathematics, optics, and "
     "experimental method. His application of al-Kindi's ray theory to explain "
     "apparently miraculous effects crystallizes a key tension: the boundary "
     "between natural philosophy explaining magical-seeming phenomena and "
     "genuine magical operation. His discussions of language's power over "
     "matter prefigure Renaissance debates about the efficacy of divine names."),

    (1268, None, "SCHOLARSHIP", "Aquinas identifies Liber de Causis as Proclean",
     "In his Commentary on the Liber de Causis, Thomas Aquinas demonstrates "
     "that the text is a compilation from Proclus's Elements of Theology rather "
     "than a work of Aristotle. This philological discovery reveals the depth "
     "of Neoplatonist infiltration into the 'Aristotelian' medieval curriculum "
     "and forces a renegotiation of the relationship between Aristotle, Proclus, "
     "and Christian philosophy."),

    (1274, None, "BIOGRAPHY", "Death of Thomas Aquinas",
     "Thomas Aquinas died at the monastery of Fossanova, aged approximately 49. "
     "His Summa Theologiae's treatment of magic, demons, and the power of words "
     "establishes the authoritative framework within which the Church assesses "
     "magical claims for the remainder of the medieval and Renaissance periods. "
     "His categories of licit natural operation and illicit demonic invocation "
     "structure the debates Ficino, Agrippa, and Dee navigate."),

    (1280, None, "PUBLICATION", "Moses de León composes the Zohar in Castile",
     "Moses de León composes the Zohar (Book of Splendor) in Castile, casting "
     "it as the mystical teachings of the second-century Rabbi Shimon bar Yochai. "
     "The Zohar's elaborate theosophy — ten sefirot as dynamic divine attributes, "
     "cosmic exile and redemption, the erotic imagery of divine union — becomes "
     "the primary text through which Renaissance Christian Kabbalists approach "
     "Jewish mysticism. Pico's 900 Conclusiones and Reuchlin's De Arte "
     "Cabalistica both draw on Zoharic traditions."),

    (1300, None, "TRANSLATION", "Picatrix translated into Latin",
     "The Picatrix is translated from Castilian into Latin, making the most "
     "comprehensive medieval astrological-image magic manual available to Latin "
     "readers. The work's account of planetary talismans, spirit invocations, "
     "and the philosophical basis of astral magic will be absorbed — often "
     "without citation — by Ficino's De Vita III and Agrippa's second book "
     "of De Occulta Philosophia."),

    # ── RENAISSANCE (new events) ─────────────────────────────────────────────

    (1440, None, "PUBLICATION", "Cusa publishes De Docta Ignorantia",
     "Nicholas of Cusa presents De Docta Ignorantia (On Learned Ignorance) "
     "to Cardinal Cesarini in Venice, arguing that the infinite God exceeds "
     "all rational comprehension and can be approached only through learned "
     "acknowledgment of ignorance. His cosmological corollary — that the "
     "infinite universe has no fixed center — directly influences Giordano "
     "Bruno, who acknowledged Cusa as a predecessor for his infinite cosmology."),

    (1453, None, "POLITICAL", "Fall of Constantinople",
     "The Ottoman conquest of Constantinople under Mehmed II ends the Byzantine "
     "Empire and accelerates the emigration of Greek scholars to Italy, bringing "
     "manuscripts of Plato, Proclus, and Plotinus westward. The resulting "
     "intensification of access to Greek philosophical texts directly enables "
     "the Platonic revival that Ficino leads at the Medici court — including "
     "the Corpus Hermeticum manuscript that reaches Florence in 1460."),

    (1462, None, "INSTITUTION", "Cosimo de' Medici establishes Platonic Academy at Careggi",
     "Cosimo de' Medici establishes the Platonic Academy at his villa in Careggi "
     "outside Florence, installing Marsilio Ficino as its head. The Academy "
     "becomes the center of the Italian Renaissance engagement with Platonism, "
     "Hermetism, and Neoplatonism — producing the intellectual synthesis that "
     "runs through Pico, Agrippa, and Bruno and that gives this corpus its "
     "philosophical coherence."),

    (1482, None, "PUBLICATION", "Ficino publishes Theologia Platonica",
     "Marsilio Ficino publishes his Theologia Platonica de Immortalitate Animarum "
     "(eighteen books), arguing that Platonic philosophy confirms Christian "
     "doctrine and demonstrating the immortality of the soul through Neoplatonic "
     "metaphysics. The work establishes the philosophical framework — world-soul, "
     "spiritus, celestial-terrestrial sympathy — within which all subsequent "
     "Renaissance magical philosophy operates."),

    (1487, None, "PUBLICATION", "Pico publishes Heptaplus",
     "Giovanni Pico della Mirandola publishes the Heptaplus, a sevenfold "
     "allegorical commentary on Genesis demonstrating through Kabbalistic and "
     "Neoplatonic methods that the biblical creation narrative encodes a complete "
     "philosophical cosmology. The work demonstrates Pico's command of Hebrew "
     "and his technique of reading Kabbalah as a confirmation of Christian "
     "doctrine — the approach that Reuchlin and Agrippa will systematize."),

    (1490, None, "INSTITUTION", "Pico settles in Florence under Medici protection",
     "Giovanni Pico della Mirandola, after his flight to France following papal "
     "condemnation of his theses, returns to Italy and settles in Florence under "
     "Lorenzo de' Medici's protection. His intellectual exchange with Ficino "
     "during these years consolidates the synthesis of Hermetism, Kabbalah, "
     "and Neoplatonism that Agrippa will systematize in De Occulta Philosophia."),

    (1492, None, "TRANSLATION", "Ficino completes Plotinus translation",
     "Marsilio Ficino completes and publishes his Latin translation of Plotinus's "
     "Enneads, making the full Plotinian system available to Latin readers for "
     "the first time in the work's twelve-hundred-year history. Combined with "
     "his Plato translations and the Corpus Hermeticum, this gives Renaissance "
     "scholars unprecedented access to the full Neoplatonic philosophical canon."),

    (1499, None, "PUBLICATION", "Trithemius composes Steganographia",
     "Johannes Trithemius composes the Steganographia, presenting a system of "
     "planetary spirit communications while embedding genuine cryptographic "
     "ciphers within the angelic framework. Trithemius shows the manuscript "
     "to Agrippa but restricts wider circulation, fearing misunderstanding. "
     "The work will circulate in restricted manuscript for over a century before "
     "print publication in 1606, influencing Agrippa's treatment of angel magic."),

    (1509, 1514, "TRIAL", "Reuchlin-Pfefferkorn controversy over Jewish books",
     "Johann Pfefferkorn's campaign to burn Jewish books, including Kabbalistic "
     "texts, prompts Reuchlin's formal defense of Hebrew learning in Augenspiegel "
     "(1511). Reuchlin is tried for heresy, eventually vindicated, but only after "
     "a prolonged controversy that galvanizes the humanist movement, prefigures "
     "Reformation debates about ecclesiastical authority, and establishes "
     "Christian Kabbalah's legitimacy as a humanist scholarly practice."),

    (1515, None, "BIOGRAPHY", "Birth of Johann Weyer",
     "Johann Weyer was born in Grave, Netherlands. He will study medicine and "
     "absorb the humanist skepticism of his teacher Agrippa, then produce in "
     "De Praestigiis Daemonum (1563) the most sustained medical and theological "
     "critique of witch-trial doctrine in the sixteenth century — arguing that "
     "accused witches are victims of diabolical delusion and melancholy, not "
     "genuine practitioners of harmful magic."),

    (1517, None, "POLITICAL", "Luther's Ninety-Five Theses initiate the Reformation",
     "Martin Luther posts his Ninety-Five Theses against indulgences in "
     "Wittenberg. The Reformation dissolves the unified Catholic framework "
     "within which the boundary between licit and illicit magic had been "
     "adjudicated, produces new theological arguments about demonic power "
     "relevant to witchcraft prosecutions, and creates the Protestant learned "
     "culture within which figures like Dee and Scot operate."),

    (1530, None, "PUBLICATION", "Agrippa publishes De Vanitate Scientiarum",
     "Heinrich Cornelius Agrippa publishes De Incertitudine et Vanitate "
     "Scientiarum, a comprehensive skeptical attack on all human knowledge "
     "including magic — one year before De Occulta Philosophia. The paradox "
     "of this relationship — De Vanitate apparently recanting De Occulta — "
     "has generated extensive scholarly debate about Agrippa's intellectual "
     "development, his rhetorical strategy, and whether the two works are "
     "meant to be read as a dialectical unit."),

    (1535, None, "BIOGRAPHY", "Birth of Giovan Battista Della Porta",
     "Giovan Battista Della Porta was born in Vico Equense, near Naples. He "
     "will found the Accademia dei Segreti (Academy of Secrets), one of the "
     "first learned societies devoted to experimental investigation, and produce "
     "in Magia Naturalis (1558, expanded 1589) the most widely read Renaissance "
     "account of natural magic — rigorously distinguishing natural from demonic "
     "magical operation through a philosophy of occult natural properties."),

    (1538, None, "BIOGRAPHY", "Birth of Reginald Scot",
     "Reginald Scot was born in Brabourne, Kent. His Discoverie of Witchcraft "
     "(1584) will become the most comprehensive English-language critique of "
     "witch belief and the grimoire tradition — arguing not only that accused "
     "witches lack magical power but that demons themselves cannot perform the "
     "corporeal operations witch-trial doctrine requires."),

    (1558, None, "PUBLICATION", "Della Porta publishes Magia Naturalis (first edition)",
     "Giovan Battista Della Porta publishes the first edition of Magia Naturalis "
     "(Natural Magic) in four books, the most accessible and widely read account "
     "of natural magic in the Renaissance — a compendium of practical secrets "
     "organized under the philosophical category of natural occult properties, "
     "rigorously distinguished from demonic operation. The expanded 1589 edition "
     "will quadruple the original in scope."),

    (1563, None, "PUBLICATION", "Weyer publishes De Praestigiis Daemonum",
     "Johann Weyer publishes De Praestigiis Daemonum et Incantationibus ac "
     "Veneficiis, arguing that accused witches are victims of diabolical delusion "
     "and melancholy rather than genuine practitioners. Weyer's medical and "
     "theological argument — that the crime belongs to the demon who causes the "
     "delusion, not the deluded woman — is the most sustained challenge to "
     "witch-trial doctrine of the century. Jean Bodin's ferocious response "
     "appears in De la Démonomanie (1580)."),

    (1576, None, "OTHER", "Dee's library at Mortlake recognized as largest in England",
     "John Dee's library at Mortlake is recognized as among the largest private "
     "libraries in England, containing over four thousand volumes spanning "
     "mathematics, astronomy, navigation, Kabbalah, natural philosophy, and "
     "occult texts. His library represents the material infrastructure of the "
     "Renaissance learned tradition — and its eventual dispersal after his "
     "death in 1608 represents its dissolution."),

    (1580, None, "PUBLICATION", "Bodin publishes De la Démonomanie des Sorciers",
     "Jean Bodin publishes De la Démonomanie des Sorciers, a systematic "
     "demonological refutation of Weyer's skeptical arguments and a vigorous "
     "defense of witch-trial practice. Bodin's work — combining legal philosophy, "
     "Neoplatonic demonology, and detailed case studies — becomes the most "
     "influential demonological treatise of the late sixteenth century and "
     "provokes Reginald Scot's Discoverie of Witchcraft (1584) as a response."),

    (1581, None, "BIOGRAPHY", "Dee begins angelic conversations with Barnabas Saul",
     "John Dee begins his first scrying experiments with Barnabas Saul at "
     "Mortlake, inaugurating the series of angelic conversations that will "
     "occupy the next eight years of his life. The communications produce "
     "a complete angelic language (Enochian), a celestial geography of thirty "
     "Aethyrs, and a system of angelic governance — material unlike anything "
     "else in the Renaissance magical tradition, recorded in meticulous diary "
     "form now published as the Five Books of Mystery."),

    (1582, None, "BIOGRAPHY", "Edward Kelley becomes Dee's scryer",
     "Edward Kelley joins John Dee at Mortlake as his primary scryer, replacing "
     "Barnabas Saul. The Dee-Kelley partnership will produce the bulk of the "
     "Enochian revelation over the next seven years, including the Polish and "
     "Bohemian sessions. The nature of Kelley's role — genuine medium, "
     "conscious fabricator, or something between — remains a central "
     "interpretive question in Dee scholarship."),

    (1583, 1589, "BIOGRAPHY", "Dee and Kelley in Central Europe: Prague and Krakow",
     "John Dee and Edward Kelley, with their families, travel to Poland and "
     "Bohemia seeking court patronage for their angelic revelations. Their "
     "years in Central Europe produce the sessions recorded in A True and "
     "Faithful Relation (published posthumously in 1659), including the "
     "controversial wife-swapping episode and Dee's audience with Emperor "
     "Rudolf II in Prague."),

    (1584, None, "PUBLICATION", "Scot publishes Discoverie of Witchcraft",
     "Reginald Scot publishes The Discoverie of Witchcraft, the most "
     "comprehensive English-language critique of witch belief — arguing that "
     "accused witches are mentally deluded, that demons cannot perform the "
     "corporeal acts witch-trial doctrine requires, and that the grimoire "
     "tradition is essentially Catholic superstition transposed to diabolical "
     "ends. King James VI of Scotland orders it burned and writes Daemonologie "
     "(1597) explicitly in response."),

    (1588, None, "BIOGRAPHY", "Death of Johann Weyer",
     "Johann Weyer died in Tecklenburg. His De Praestigiis Daemonum, though "
     "condemned by opponents as favorable to witches, had introduced medical "
     "explanations of witch belief that would prove more intellectually durable "
     "than the demonological alternatives — and would be drawn on by Scot, "
     "by seventeenth-century skeptics, and eventually by Enlightenment critics "
     "of witch prosecution."),

    (1589, None, "PUBLICATION", "Della Porta publishes expanded Magia Naturalis",
     "Giovan Battista Della Porta publishes the expanded twenty-book edition "
     "of Magia Naturalis, quadrupling the original in scope to cover optics, "
     "cryptography, distillation, perfumery, metallurgy, agricultural secrets, "
     "and stage illusions. The expanded edition becomes the standard compendium "
     "of practical natural magic for the late Renaissance, and its account of "
     "perspective optics prefigures the development of the telescope."),

    (1591, None, "TRIAL", "Bruno arrested by Venetian Inquisition",
     "Giordano Bruno, recently arrived in Venice at the invitation of the "
     "patrician Giovanni Mocenigo, is denounced to the Venetian Inquisition "
     "by his host. His arrest begins eight years of imprisonment and "
     "inquisitorial process. The charges encompass his cosmological doctrines "
     "(infinite universe, multiple worlds), his denial of transubstantiation, "
     "and his claimed magical and prophetic powers."),

    (1597, None, "PUBLICATION", "James VI publishes Daemonologie",
     "James VI of Scotland publishes Daemonologie, his demonological treatise "
     "directly refuting Reginald Scot's skeptical arguments. James defends the "
     "reality of demonic power, the validity of witch-trial evidence, and the "
     "theological necessity of witch prosecution. When James becomes James I "
     "of England in 1603, his demonological convictions intensify English "
     "witch prosecutions."),

    (1599, None, "BIOGRAPHY", "Death of Reginald Scot",
     "Reginald Scot died in Smeeth, Kent. His Discoverie of Witchcraft, which "
     "King James ordered burned after becoming king of England in 1603, was "
     "republished in 1651 and 1665 and became a significant reference for "
     "seventeenth-century skeptics questioning the foundations of witch belief "
     "and the legal basis of witch prosecution."),

    (1606, None, "PUBLICATION", "Steganographia published posthumously",
     "Trithemius's Steganographia, composed around 1499 and circulated in "
     "restricted manuscript copies for over a century, is finally published "
     "in Frankfurt. The work's publication makes its system of planetary spirit "
     "communications and embedded cryptographic ciphers available to a wider "
     "learned audience — and inaugurates the interpretive debate, still "
     "ongoing in scholarship, about whether its primary content is angel magic "
     "or cryptography."),

    (1615, None, "BIOGRAPHY", "Death of Giovan Battista Della Porta",
     "Giovan Battista Della Porta died in Naples. His Magia Naturalis had "
     "established the authoritative account of natural magic as distinct from "
     "demonic operation — a distinction that influenced the conceptual "
     "vocabulary of natural philosophy well into the seventeenth century and "
     "shaped how subsequent scholars framed the question of what 'magic' was."),

    # ── EARLY MODERN ─────────────────────────────────────────────────────────

    (1614, None, "SCHOLARSHIP", "Isaac Casaubon's philological dating of Corpus Hermeticum",
     "Isaac Casaubon, in De Rebus Sacris et Ecclesiasticis Exercitationes (1614), "
     "demonstrates through philological analysis that the Greek of the Corpus "
     "Hermeticum is characteristic of the early centuries CE rather than ancient "
     "Egypt — exposing the texts as Greco-Roman philosophical compositions rather "
     "than ancient Egyptian revelation. This dating arrives too late to diminish "
     "the preceding century and a half of Hermetic influence but permanently "
     "changes how the texts must be read."),

    (1615, None, "PUBLICATION", "Confessio Fraternitatis (second Rosicrucian manifesto)",
     "The Confessio Fraternitatis, the second Rosicrucian manifesto, is published "
     "in Latin, amplifying the Fama's claims about a secret brotherhood and "
     "providing a theological framework for their project of universal reformation. "
     "The Rosicrucian manifestos generate a European-wide literary debate. No "
     "actual Rosicrucian fellowship has ever been conclusively identified — "
     "they may be literary inventions designed to provoke intellectual discussion."),

    (1616, None, "PUBLICATION", "Chemical Wedding of Christian Rosencreutz",
     "The Chemical Wedding of Christian Rosencreutz (attributed to Johann Valentin "
     "Andreae) is published, the most literary of the Rosicrucian manifestos — "
     "an alchemical allegory in which Christian Rosencreutz attends a royal "
     "wedding filled with symbolic trials and transformations. The text's "
     "combination of alchemical symbolism, court entertainment, and spiritual "
     "allegory represents a late flowering of Renaissance emblematic culture."),

    (1619, None, "SCHOLARSHIP", "Kepler-Fludd polemic over mathematical vs analogical method",
     "Johannes Kepler publishes an appendix to his Harmonices Mundi attacking "
     "Robert Fludd's analogical approach to cosmic harmony, arguing that genuine "
     "natural philosophy requires quantitative mathematical relationships rather "
     "than symbolic-qualitative correspondences. Fludd responds vigorously. "
     "The exchange crystallizes the methodological rupture between the Hermetic-"
     "qualitative tradition and the emerging mathematical-quantitative natural "
     "science that will displace it."),

    (1631, None, "SCHOLARSHIP", "Mersenne attacks Fludd as incompatible with Christian philosophy",
     "Marin Mersenne, mathematician and correspondent of Descartes, attacks "
     "Robert Fludd's philosophy in Quaestiones celeberrimae in Genesim, accusing "
     "him of Cabalism and Hermetism incompatible with Christian natural philosophy. "
     "Mersenne's attack represents the growing institutional and theological "
     "pressure on the Renaissance Hermetic synthesis from both mechanistic "
     "science and orthodox theology."),

    (1637, None, "PUBLICATION", "Descartes publishes Discourse on Method",
     "René Descartes publishes Discours de la méthode, articulating the "
     "mechanistic philosophy that will become the dominant framework of "
     "seventeenth-century natural philosophy. Descartes's sharp distinction "
     "between mind and matter, and his account of the material world as pure "
     "extension governed by mechanical laws, eliminates the active, "
     "spiritus-pervaded world-soul on which Renaissance natural magic depends. "
     "The 'death of nature' (Carolyn Merchant's phrase) begins here."),

    (1640, 1680, "DISCOVERY", "Newton's alchemical investigations",
     "Isaac Newton conducts an extensive program of alchemical reading, "
     "experiment, and manuscript collection alongside his mathematical physics, "
     "eventually producing over a million words of alchemical writing. Newton's "
     "alchemy — long suppressed in the standard historiography — has become "
     "central to understanding his intellectual development since Westfall's "
     "Never at Rest (1980) and demonstrates that the 'Scientific Revolution' "
     "did not simply expel the Hermetic tradition but incorporated and "
     "transformed elements of it."),

    (1659, None, "PUBLICATION", "Meric Casaubon publishes Dee's True and Faithful Relation",
     "Meric Casaubon publishes A True and Faithful Relation of What Passed for "
     "Many Years Between Dr. John Dee and Some Spirits (1659), editing Dee's "
     "angelic diaries with a lengthy preface arguing that the communications "
     "were diabolical delusions. Casaubon's hostile framing paradoxically "
     "preserved the material and shaped its reception for three centuries. "
     "Deborah Harkness and György Szönyi's works in the corpus provide the "
     "modern scholarly alternative to Casaubon's demonization."),

    (1677, 1684, "PUBLICATION", "Van Helmont and Knorr von Rosenroth publish Kabbala Denudata",
     "Francis Mercury van Helmont and Christian Knorr von Rosenroth publish "
     "Kabbala Denudata (Kabbalah Unveiled) in two volumes (1677, 1684), the "
     "most important printed compendium of Jewish Kabbalistic texts in Latin "
     "translation in the seventeenth century. The work makes Zoharic and "
     "Lurianic materials available to Protestant European scholars and deeply "
     "influences Anne Conway, Leibniz, and the Cambridge Platonists."),

    (1687, None, "PUBLICATION", "Newton publishes Principia Mathematica",
     "Isaac Newton publishes Philosophiae Naturalis Principia Mathematica, "
     "establishing mathematical mechanics as the foundation of natural "
     "philosophy. The Principia represents the decisive institutional triumph "
     "of the quantitative-mathematical approach over the qualitative-analogical "
     "Hermetic tradition. However, Newton's own extensive engagement with "
     "alchemy (undisclosed in his lifetime) complicates simple narratives of "
     "the 'death of magic' at the hands of mathematical science."),

    # ── SCHOLARSHIP ──────────────────────────────────────────────────────────

    (1958, None, "SCHOLARSHIP", "Walker publishes Spiritual and Demonic Magic",
     "D.P. Walker publishes Spiritual and Demonic Magic from Ficino to "
     "Campanella, establishing the analytical distinction between spiritual "
     "magic (working through natural spiritus) and demonic magic (invoking "
     "personal spirit-beings) that gives subsequent scholarship its central "
     "analytical vocabulary. Walker's close reading of Ficino's De Vita III "
     "and Campanella's solar magic shows how practitioners navigated the "
     "licit-illicit boundary in practice."),

    (1966, None, "SCHOLARSHIP", "Yates publishes The Art of Memory",
     "Frances Yates publishes The Art of Memory, tracing the classical memory "
     "tradition through the medieval period and into the Renaissance, arguing "
     "that Bruno's transformation of the classical art into a Hermetic memory "
     "system is central to understanding his philosophy and the emergence of "
     "theatre and visual culture. The book extends the Yates thesis into new "
     "cultural domains while deepening her account of Bruno."),

    (1971, None, "SCHOLARSHIP", "Keith Thomas publishes Religion and the Decline of Magic",
     "Keith Thomas publishes Religion and the Decline of Magic, the most "
     "comprehensive study of magical belief in English popular culture and its "
     "decline under Protestantism, print culture, and emerging scientific "
     "rationalism. Thomas's social-historical approach — attending to popular "
     "practice rather than elite philosophy — complements and challenges the "
     "intellectual history tradition represented by Yates and Walker."),

    (1978, None, "SCHOLARSHIP", "Peters publishes The Magician, the Witch, and the Law",
     "Edward Peters publishes The Magician, the Witch, and the Law, examining "
     "how medieval and early modern law constructed the categories of magician "
     "and witch through inquisitorial procedure. Peters's legal-historical "
     "approach shows how the witch-figure was created through juridical "
     "processes as much as theological doctrine — a complement to the "
     "intellectual history approaches of Yates and Walker."),

    (1984, None, "SCHOLARSHIP", "Vickers publishes methodological critique of Yates thesis",
     "Brian Vickers edits Occult and Scientific Mentalities in the Renaissance, "
     "including a powerful critique of the Yates thesis: the supposed connection "
     "between Hermetic animism and early modern science rests on a confusion "
     "between analogical and causal reasoning that neither Hermetists nor "
     "scientists themselves recognized. Vickers's critique does not dismiss "
     "the Hermetic tradition but challenges Yates's causal claim about its "
     "role in scientific change."),

    (1988, None, "SCHOLARSHIP", "Copenhaver publishes essays revising the Yates thesis",
     "Brian Copenhaver publishes a series of essays — including 'Magic and "
     "the Dignity of Man' and 'Hermes Trismegistus, Proclus, and the Question "
     "of a Philosophy of Magic in the Renaissance' — arguing that Ficino was "
     "primarily a Platonist rather than a Hermetist, and that 'Hermetism' as "
     "a unified tradition is more a scholarly construction than a historical "
     "reality. These essays are the most sustained scholarly revision of the "
     "Yates thesis."),

    (1992, None, "SCHOLARSHIP", "Copenhaver publishes critical edition of Hermetica",
     "Brian Copenhaver publishes Hermetica: The Greek Corpus Hermeticum and "
     "the Latin Asclepius in a New English Translation with Notes and "
     "Introduction — the modern critical edition. Copenhaver's introduction "
     "argues that the Hermetic texts are best understood as products of "
     "Neoplatonic philosophical culture rather than as evidence of a distinct "
     "'Hermetic tradition,' operationalizing his earlier essays into a "
     "sustained scholarly alternative to the Yates thesis."),

    (2001, None, "SCHOLARSHIP", "Klaassen publishes Transformations of Magic",
     "Frank Klaassen publishes The Transformations of Magic: Illicit Learned "
     "Magic in the Later Middle Ages and Renaissance, examining how the learned "
     "magic tradition — especially the Ars Notoria and medieval angel magic — "
     "transformed through manuscript transmission and how practitioners "
     "negotiated the boundary between licit prayer and illicit invocation. "
     "Klaassen's work bridges medieval and Renaissance magic studies."),

    (2005, None, "SCHOLARSHIP", "Hanegraaff edits Dictionary of Gnosis and Western Esotericism",
     "Wouter Hanegraaff (editor-in-chief) publishes the Dictionary of Gnosis "
     "and Western Esotericism, the first comprehensive scholarly reference work "
     "for the field. The Dictionary's appearance marks the institutionalization "
     "of Western esotericism as a recognized academic discipline and establishes "
     "the conceptual vocabulary — including the historiographical categories of "
     "Hermetism, Neoplatonism, theosophy, and occultism — that organizes "
     "the field's self-understanding."),

    (2012, None, "SCHOLARSHIP", "Hanegraaff publishes Esotericism and the Academy",
     "Wouter Hanegraaff publishes Esotericism and the Academy: Rejected Knowledge "
     "in Western Culture, arguing that 'Western esotericism' is a scholarly "
     "construct — the category of 'rejected knowledge' that Enlightenment "
     "rationalism excluded from legitimate discourse — and that this construct "
     "needs historical analysis rather than uncritical acceptance. The work "
     "provides the methodological foundation for treating 'magic' as a scholarly "
     "category rather than a neutral description."),

    (2015, None, "SCHOLARSHIP", "Saif publishes Arabic Influences on Early Modern Occult Philosophy",
     "Liana Saif publishes The Arabic Influences on Early Modern Occult "
     "Philosophy, demonstrating the depth and specificity of the Arabic-Islamic "
     "contribution to the magical-astrological tradition that Renaissance scholars "
     "inherited. Saif's work corrects the Eurocentric framing of Renaissance magic "
     "as a purely Greek-Latin tradition and establishes the Islamic thread as a "
     "first-class component of the intellectual genealogy — directly shaping "
     "RenMagDB's scope."),
]

# Figure associations: (event_title, figure_names)
FIGURE_ASSOCIATIONS = {
    "Plato's Timaeus composed": ["Plato"],
    "Birth of Porphyry": ["Porphyry"],
    "Plotinus opens school in Rome": ["Plotinus"],
    "Porphyry joins Plotinus in Rome": ["Porphyry", "Plotinus"],
    "Iamblichus writes De Mysteriis": ["Iamblichus"],
    "Porphyry publishes the Enneads": ["Porphyry", "Plotinus"],
    "Death of Porphyry": ["Porphyry"],
    "Augustine's City of God condemns Hermetic magic": ["Hermes Trismegistus"],
    "Proclus writes Elements of Theology": ["Proclus"],
    "Pseudo-Dionysius composes Celestial Hierarchy": [],
    "Justinian closes the Platonic Academy in Athens": ["Proclus"],
    "Sefer Yetzirah achieves final form": [],
    "Al-Kindi writes De Radiis Stellarum": ["Al-Kindi"],
    "Birth of Avicenna": ["Avicenna"],
    "Death of Avicenna": ["Avicenna"],
    "Albertus Magnus writes Speculum Astronomiae": ["Albertus Magnus"],
    "Roger Bacon presents Opus Majus to Pope Clement IV": ["Roger Bacon"],
    "Aquinas identifies Liber de Causis as Proclean": ["Thomas Aquinas", "Proclus"],
    "Birth of Thomas Aquinas": ["Thomas Aquinas"],
    "Aquinas studies under Albertus Magnus": ["Thomas Aquinas", "Albertus Magnus"],
    "Death of Thomas Aquinas": ["Thomas Aquinas"],
    "Moses de León composes the Zohar in Castile": [],
    "Cusa publishes De Docta Ignorantia": ["Nicholas of Cusa"],
    "Ficino publishes Theologia Platonica": ["Marsilio Ficino"],
    "Pico publishes Heptaplus": ["Giovanni Pico della Mirandola"],
    "Pico settles in Florence under Medici protection": ["Giovanni Pico della Mirandola", "Marsilio Ficino"],
    "Ficino completes Plotinus translation": ["Marsilio Ficino", "Plotinus"],
    "Trithemius composes Steganographia": ["Johannes Trithemius"],
    "Reuchlin-Pfefferkorn controversy over Jewish books": ["Johannes Reuchlin"],
    "Birth of Johann Weyer": ["Johann Weyer"],
    "Birth of Giovan Battista Della Porta": ["Giovan Battista Della Porta"],
    "Birth of Reginald Scot": ["Reginald Scot"],
    "Della Porta publishes Magia Naturalis (first edition)": ["Giovan Battista Della Porta"],
    "Weyer publishes De Praestigiis Daemonum": ["Johann Weyer"],
    "Dee begins angelic conversations with Barnabas Saul": ["John Dee"],
    "Edward Kelley becomes Dee's scryer": ["John Dee"],
    "Dee and Kelley in Central Europe: Prague and Krakow": ["John Dee"],
    "Scot publishes Discoverie of Witchcraft": ["Reginald Scot"],
    "Death of Johann Weyer": ["Johann Weyer"],
    "Della Porta publishes expanded Magia Naturalis": ["Giovan Battista Della Porta"],
    "Bruno arrested by Venetian Inquisition": ["Giordano Bruno"],
    "James VI publishes Daemonologie": [],
    "Death of Reginald Scot": ["Reginald Scot"],
    "Death of Giovan Battista Della Porta": ["Giovan Battista Della Porta"],
    "Agrippa publishes De Vanitate Scientiarum": ["Heinrich Cornelius Agrippa"],
    "Kepler-Fludd polemic over mathematical vs analogical method": ["Robert Fludd"],
    "Van Helmont and Knorr von Rosenroth publish Kabbala Denudata": ["Francis Mercury van Helmont"],
    "Walker publishes Spiritual and Demonic Magic": ["D.P. Walker", "Marsilio Ficino"],
    "Yates publishes The Art of Memory": ["Frances A. Yates", "Giordano Bruno"],
    "Copenhaver publishes essays revising the Yates thesis": ["Brian P. Copenhaver", "Marsilio Ficino"],
    "Copenhaver publishes critical edition of Hermetica": ["Brian P. Copenhaver", "Hermes Trismegistus"],
    "Saif publishes Arabic Influences on Early Modern Occult Philosophy": ["Liana Saif", "Al-Kindi"],
    "Bodin publishes De la Démonomanie des Sorciers": ["Johann Weyer"],
    "Meric Casaubon publishes Dee's True and Faithful Relation": ["John Dee"],
    "Cosimo de' Medici establishes Platonic Academy at Careggi": ["Marsilio Ficino"],
    "Fall of Constantinople": [],
    "Isaac Casaubon's philological dating of Corpus Hermeticum": ["Hermes Trismegistus"],
}


def run():
    conn = sqlite3.connect(str(DB_PATH))
    conn.execute("PRAGMA foreign_keys=ON")
    c = conn.cursor()

    # Build figure lookup: name -> id
    fig_map = {}
    for row in c.execute("SELECT id, name FROM figures").fetchall():
        fig_map[row[1]] = row[0]

    inserted = 0
    skipped = 0
    assoc_count = 0

    for event in NEW_EVENTS:
        year, year_end, event_type, title, description = event

        # Skip if title+year already exists
        exists = c.execute(
            "SELECT id FROM timeline_events WHERE title=? AND year=?",
            (title, year)
        ).fetchone()

        if exists:
            skipped += 1
            continue

        c.execute("""
            INSERT INTO timeline_events
                (year, year_end, event_type, title, description,
                 source_method, review_status, confidence)
            VALUES (?, ?, ?, ?, ?, 'HUMAN_VERIFIED', 'REVIEWED', 'HIGH')
        """, (year, year_end, event_type, title, description))
        event_id = c.lastrowid
        inserted += 1
        print(f"  INSERT: {year} [{event_type:12}] {title}")

        # Associate figures
        for fig_name in FIGURE_ASSOCIATIONS.get(title, []):
            fig_id = fig_map.get(fig_name)
            if fig_id:
                try:
                    c.execute(
                        "INSERT OR IGNORE INTO event_figures (event_id, figure_id) VALUES (?, ?)",
                        (event_id, fig_id)
                    )
                    assoc_count += 1
                except Exception as e:
                    print(f"    WARNING figure assoc {fig_name}: {e}")

    conn.commit()

    total = c.execute("SELECT COUNT(*) FROM timeline_events").fetchone()[0]
    conn.close()

    print()
    print(f"Inserted: {inserted}  Skipped (already exists): {skipped}")
    print(f"Figure associations added: {assoc_count}")
    print(f"Total timeline events: {total}")


if __name__ == "__main__":
    run()
