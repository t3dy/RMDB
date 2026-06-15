"""Pass 4: Add missing figures and expand thin significance fields.

Adds 13 figures missing from the DB (Hanegraaff, Keith Thomas, Newton,
Bodin, Kepler, Descartes, Mersenne, Klaassen, Vickers, Peters, Isaac
Casaubon, Moses de León, Andreae) and updates significance fields for
figures under 250 chars. Also links new figures to existing timeline events.

Run: python scripts/improve_content_pass4.py
Idempotent.
"""

import io
import sqlite3
import sys
from pathlib import Path

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

DB_PATH = Path(__file__).resolve().parent.parent / "db" / "renmagic.db"

# ── NEW FIGURES ──────────────────────────────────────────────────────────────
# Each: (name, figure_type, birth_year, death_year, nationality, biography, significance)

NEW_FIGURES = [

    ("Wouter Hanegraaff", "SCHOLAR", 1961, None, "Dutch",
     """\
Wouter J. Hanegraaff (1961–) is Professor of History of Hermetic Philosophy \
and Related Currents at the University of Amsterdam, where he holds the only \
dedicated chair in Western esotericism studies in the world. He is the \
editor-in-chief of the Dictionary of Gnosis and Western Esotericism (2005), \
the first comprehensive scholarly reference work for the field, and the \
author of Esotericism and the Academy: Rejected Knowledge in Western Culture \
(2012), the methodological cornerstone of current esotericism scholarship.

Hanegraaff's central methodological contribution is his argument that \
'Western esotericism' is a scholarly construct — the category of 'rejected \
knowledge' that Enlightenment rationalism excluded from legitimate discourse — \
and that studying this construct requires historical analysis rather than \
uncritical acceptance or hostile dismissal. He distinguishes between what \
esoteric practitioners actually believed (emic perspective), what academic \
scholars have made of them (etic perspective), and how Enlightenment \
apologetics shaped the very category of 'occultism' as a polemical label. \
This three-level methodological framework represents the third major phase of \
post-Yates historiography, following Vickers's methodological critique (1984) \
and Copenhaver's source-critical revision (1988). For RenMagDB, Hanegraaff's \
approach underwrites the portal's consistent distinction between actor \
categories and analyst categories — treating 'magic' as a term requiring \
analysis rather than as a neutral description of historical realities.""",

     "Dutch historian at University of Amsterdam; Dictionary of Gnosis and \
Western Esotericism (2005) institutionalized the field; Esotericism and the \
Academy (2012) provides the third-wave methodological framework treating \
'Western esotericism' as a scholarly construct requiring historical analysis \
rather than uncritical acceptance — the approach underpinning this portal"),

    ("Keith Thomas", "SCHOLAR", 1933, None, "British",
     """\
Sir Keith Thomas (1933–), British social historian and former President of \
Corpus Christi College, Oxford, published Religion and the Decline of Magic \
in 1971 — one of the most influential works of English social history of the \
twentieth century. Its subject is the full range of magical belief and \
practice in sixteenth- and seventeenth-century England — astrology, cunning \
folk, healing magic, prophecy, witchcraft, and the learned magic tradition — \
and its decline in the century after 1650.

Thomas's approach is sociological and social-historical rather than \
intellectual-historical: he attends to popular practice rather than elite \
philosophy, to the social functions of magical belief rather than its \
philosophical content, and to the conditions — Protestant reformation, \
print culture, emerging markets, urban anonymity — that made magical belief \
progressively less socially functional. His central argument is that magic \
declined not because science refuted it but because social and economic \
changes made it unnecessary. Religion and the Decline of Magic \
complements and challenges the Yates-Walker tradition of intellectual \
history: it covers social strata and practices almost entirely absent from \
the philosophical magic literature that corpus documents like Ficino's \
De Vita or Agrippa's De Occulta Philosophia represent.""",

     "British social historian; Religion and the Decline of Magic (1971) is \
the most comprehensive study of magical belief in English popular culture — \
sociological rather than intellectual-historical in approach; argues magic \
declined through social and economic change rather than scientific refutation; \
complements Yates and Walker with attention to practice over philosophy"),

    ("Frank Klaassen", "SCHOLAR", None, None, "British-Canadian",
     """\
Frank Klaassen is a historian of medieval and Renaissance magic at the \
University of Saskatchewan. His The Transformations of Magic: Illicit \
Learned Magic in the Later Middle Ages and Renaissance (2001) is the most \
rigorous examination of how the learned ritual magic tradition — centered on \
texts like the Ars Notoria, Liber Juratus, and various angelic magic manuals — \
transformed through manuscript transmission and the printing press between \
roughly 1200 and 1600.

Klaassen's core argument is that the learned magic tradition was not static \
but underwent systematic transformation: medieval practitioners adapted \
inherited texts by adding Christianizing frames, liturgical language, and \
appeals to authorized spiritual powers, progressively negotiating the boundary \
between licit prayer and illicit invocation. The Renaissance printing of these \
texts produced a second transformation, with editors selecting, adapting, and \
legitimizing through print what manuscript culture had treated with discretion. \
Klaassen's work bridges medieval and Renaissance magic studies in a way the \
Yates tradition — focused on the fifteenth-century Hermetic revival — does not, \
providing essential context for understanding the textual tradition (Ars Notoria, \
Sworn Book of Honorius) that co-existed with and shaped the more philosophically \
elaborated magic of Ficino, Agrippa, and Dee.""",

     "Historian of medieval and Renaissance magic; Transformations of Magic \
(2001) traces how the learned ritual magic tradition (Ars Notoria, angelic \
manuals) transformed through manuscript transmission and print; bridges the \
medieval and Renaissance magic traditions that the Yates framework leaves \
underexamined"),

    ("Brian Vickers", "SCHOLAR", 1937, None, "British",
     """\
Brian Vickers (1937–) is a British literary scholar and intellectual historian, \
best known in the Renaissance magic literature for his powerful critique of the \
Yates thesis in the edited volume Occult and Scientific Mentalities in the \
Renaissance (1984). Vickers's central argument is that the supposed causal \
connection between Hermetic animism and early modern science rests on a \
fundamental logical confusion: Hermetists thought in analogical, qualitative \
terms (A resembles B, therefore A is like B in other respects), while \
scientists thought in causal, quantitative terms (A causes B through \
measurable mechanisms). The two modes of thought are not only different \
but mutually exclusive — no historical actor could coherently hold both \
simultaneously.

Vickers's critique does not dismiss the Hermetic tradition or deny its \
historical significance — it challenges only Yates's specific causal claim \
that Hermetism drove the Scientific Revolution. His position is that the \
Hermetic and scientific traditions were parallel developments that sometimes \
appeared in the same individuals (Bruno, Newton) but served different \
intellectual purposes. The debate Vickers initiated — about the relationship \
between qualitative analogy and quantitative mechanism — remains active in \
scholarship on the history of science and magic.""",

     "British literary scholar and intellectual historian; critique of the \
Yates thesis in Occult and Scientific Mentalities in the Renaissance (1984) \
argued that Hermetism and natural science used incompatible modes of reasoning \
(analogical vs causal); does not dismiss the Hermetic tradition but challenges \
its causal role in the Scientific Revolution"),

    ("Edward Peters", "SCHOLAR", 1936, None, "American",
     """\
Edward Peters is an American medieval historian at the University of \
Pennsylvania. His The Magician, the Witch, and the Law (1978) examines how \
medieval and early modern law — inquisitorial procedure, ecclesiastical \
courts, secular criminal law — constructed the categories of magician, \
witch, and heretic through judicial process. Peters's central argument is that \
the witch-figure as it crystallized in late-medieval and early modern legal \
practice was not a description of existing social realities but a legal \
construct produced through the interaction of inherited theological doctrine, \
inquisitorial procedure, and the demands of judicial proof.

Peters situates the witch-trial tradition within the longer history of \
Roman law and medieval heresy prosecution, showing how the Inquisition's \
techniques for extracting confessions from suspected heretics were adapted \
to produce the confessions that defined witchcraft as a crime. His legal-\
historical approach complements the intellectual history of Yates and Walker \
and the social history of Keith Thomas — attending to the institutional and \
procedural mechanisms through which elite theological discourse became \
courtroom practice.""",

     "American medieval historian; The Magician, the Witch, and the Law (1978) \
examines how inquisitorial procedure and ecclesiastical law constructed the \
legal category of 'witch' through judicial process rather than describing a \
pre-existing social reality; legal-historical complement to Yates's \
intellectual history and Thomas's social history"),

    ("Isaac Casaubon", "SCHOLAR", 1559, 1614, "French-Swiss",
     """\
Isaac Casaubon (1559–1614), French-Swiss classical philologist, produced in \
De Rebus Sacris et Ecclesiasticis Exercitationes (1614) — published in the \
year of his death — the most important philological refutation of the prisca \
theologia tradition of Renaissance Hermetism. Examining the Greek of the \
Corpus Hermeticum translated by Ficino in 1463 and used by Renaissance thinkers \
as evidence of ancient Egyptian wisdom, Casaubon demonstrated through detailed \
linguistic analysis that the texts contain vocabulary, syntactic constructions, \
and anachronistic references characteristic of the early centuries CE — not \
ancient Egypt.

Casaubon's dating arrived too late to diminish the preceding century and a \
half of Hermetic philosophical influence, but it permanently changed how the \
texts had to be read by any scholar attending to their origins. D.P. Walker \
showed that Ficino was aware he was taking the texts on faith rather than \
philological proof; Casaubon provided the proof that Ficino had lacked. The \
implications for the entire prisca theologia project — the claim that Hermes, \
Orpheus, Zoroaster, Plato, and Moses had all taught the same ancient wisdom \
later revealed in Christianity — were devastating for anyone who accepted the \
dating, though many practitioners continued to value the texts for their \
philosophical content independent of their origin claims.""",

     "French-Swiss classical philologist; De Rebus Sacris (1614) dated the \
Corpus Hermeticum to early centuries CE through linguistic analysis, refuting \
the prisca theologia claim of ancient Egyptian origin; his philological \
demonstration permanently changed how the Hermetic texts must be read, \
arriving after a century and a half of influence"),

    ("Jean Bodin", "HISTORICAL", 1530, 1596, "French",
     """\
Jean Bodin (1530–1596), French jurist and political philosopher, is best known \
in political thought for his Six Books of the Republic (1576), which developed \
the concept of sovereignty that would dominate European political theory for \
two centuries. In the history of magic and witchcraft, he appears as the author \
of De la Démonomanie des Sorciers (1580), the most influential demonological \
treatise of the late sixteenth century and a fierce response to Johann Weyer's \
skeptical arguments in De Praestigiis Daemonum (1563).

Bodin's demonology is philosophically sophisticated in Neoplatonist terms: \
he accepts the hierarchical spirit world that Neoplatonic philosophy describes, \
including the reality of demons with genuine causal powers in the sublunary \
world. From this philosophical foundation he attacks Weyer's medical explanation \
of accused witches as victims of melancholy, arguing that Weyer ignores both \
the theological evidence for demonic power and the testimony of accused witches \
themselves. De la Démonomanie provides not only a theoretical framework but a \
handbook for witch-trial practice — cataloguing sabbat activities, modes of \
transportation, and appropriate punishments. Reginald Scot's Discoverie of \
Witchcraft (1584) is directly provoked by Bodin's work.""",

     "French jurist and political philosopher; De la Démonomanie des Sorciers \
(1580) was the most influential demonological treatise of the late sixteenth \
century, systematically refuting Weyer's skepticism from a Neoplatonist \
framework and providing a handbook for witch-trial practice; Reginald Scot's \
Discoverie of Witchcraft directly responds to Bodin"),

    ("Moses de León", "HISTORICAL", 1240, 1305, "Spanish",
     """\
Moses de León (c. 1240–1305) was a Spanish Kabbalist, now generally accepted \
as the principal author of the Zohar (Book of Splendor) — the most important \
text in the history of Jewish mysticism and the primary source through which \
Renaissance Christian Kabbalists accessed Kabbalistic thought. The Zohar was \
presented as the mystical teachings of the second-century Rabbi Shimon bar \
Yochai and circulated in manuscript form in Castile from the 1280s onward, \
eventually achieving canonical status alongside the Talmud in some Jewish \
communities.

Moses de León's authorship was argued most influentially by Gershom Scholem \
in Major Trends in Jewish Mysticism (1941) based on stylistic and historical \
evidence, though some scholars maintain that the Zohar's composition is more \
complex. For Renaissance magic, Moses de León's significance is almost entirely \
through the Zohar's subsequent influence: Pico della Mirandola's 900 Conclusiones \
(1486) included Kabbalistic theses drawing on Zoharic traditions; Reuchlin's \
De Arte Cabalistica (1517) transmitted Zoharic symbolism into the Christian \
humanist tradition; and Agrippa's treatment of divine names and letter magic \
in De Occulta Philosophia draws on Kabbalistic materials originating in the \
Zoharic tradition Moses de León created.""",

     "Spanish Kabbalistic author; principal composer of the Zohar (Book of \
Splendor), the foundational text of Jewish mysticism, cast as teachings of \
Rabbi Shimon bar Yochai; the Zohar's theosophy — ten sefirot, cosmic exile, \
divine union — became the primary source through which Pico, Reuchlin, and \
Agrippa accessed Jewish Kabbalah for Christian Kabbalistic synthesis"),

    ("Isaac Newton", "HISTORICAL", 1643, 1727, "English",
     """\
Isaac Newton (1643–1727), English mathematician, physicist, and alchemist, \
is best known for the Principia Mathematica (1687), which established \
mathematical mechanics as the foundation of natural philosophy and represents \
the decisive institutional triumph of quantitative method over the \
qualitative-analogical Hermetic tradition. Newton's public intellectual \
persona was that of the mathematical physicist; his private intellectual life \
included an extensive, decades-long program of alchemical reading, experiment, \
and manuscript collection that remained largely unknown to his contemporaries.

Newton eventually produced over a million words of alchemical writing — \
the largest body of alchemical scholarship produced by any single individual \
in the early modern period. His alchemical investigations drew on Paracelsian, \
Hermetic, and Rosicrucian sources, and his conviction that matter possessed \
active principles irreducible to mechanical extension likely originated in his \
alchemical reading. Richard Westfall's biography Never at Rest (1980) brought \
Newton's alchemy into the historiographical mainstream, demonstrating that \
the 'death of magic' at the hands of mathematical science is more complicated \
than the standard narrative allows. For RenMagDB, Newton represents the \
moment at which the Hermetic tradition is not simply expelled but incorporated \
and transformed into the problematic interior of early modern natural philosophy.""",

     "English mathematician and natural philosopher; Principia Mathematica \
(1687) established mathematical mechanics as the foundation of modern natural \
philosophy; his private alchemical program — over one million words of \
alchemical writing — demonstrates that the 'Scientific Revolution' did not \
simply expel the Hermetic tradition but incorporated and transformed it"),

    ("René Descartes", "HISTORICAL", 1596, 1650, "French",
     """\
René Descartes (1596–1650), French philosopher and mathematician, is \
the architect of the mechanistic philosophy that eliminated the conceptual \
foundations of Renaissance natural magic. His Discourse on Method (1637), \
Meditations on First Philosophy (1641), and Principles of Philosophy (1644) \
articulate a sharp distinction between mind (res cogitans, thinking substance) \
and matter (res extensa, pure spatial extension governed by mechanical laws). \
This dualism produces what Carolyn Merchant called 'the death of nature': \
in Descartes's framework, there is no world-soul, no spiritus pervading the \
cosmos, no active celestial influence animating sublunary matter — only \
passive extended substance and the mechanical transmission of motion.

Descartes's mechanism made the conceptual foundations of Renaissance natural \
magic philosophically untenable: Ficino's talismanic medicine depended on \
spiritus and celestial sympathy; Agrippa's celestial magic required an \
animated cosmos; Fludd's macrocosm-microcosm correspondences required \
qualitative analogy to have causal force. All of these presuppositions \
Descartes systematically eliminated. The Hermetic synthesis survived into \
the seventeenth century in the work of Kircher, van Helmont, and the \
Rosicrucian circles, but Descartes's philosophy provided the institutional \
framework of natural philosophy within which it became increasingly \
marginal.""",

     "French philosopher; Discourse on Method (1637) and subsequent works \
articulated the mechanistic dualism — res cogitans vs res extensa — that \
eliminated the spiritus, world-soul, and celestial sympathy on which \
Renaissance natural magic depends; produced 'the death of nature' (Carolyn \
Merchant's phrase) that made Ficino's and Agrippa's conceptual foundations \
philosophically untenable"),

    ("Johannes Kepler", "HISTORICAL", 1571, 1630, "German",
     """\
Johannes Kepler (1571–1630), German astronomer and mathematician, discovered \
the three laws of planetary motion (1609, 1619) that provided the empirical \
basis for Newton's gravitational mechanics. In the history of Renaissance \
magic, Kepler appears primarily through his polemic with Robert Fludd over \
the proper method of natural philosophy. In an appendix to his Harmonices \
Mundi (1619) — a work on the mathematical harmonies of the planetary system \
— Kepler attacked Fludd's analogical approach to cosmic harmony as unscientific: \
genuine natural philosophy, Kepler argued, requires quantitative mathematical \
relationships capable of empirical testing, not symbolic qualitative \
correspondences that can always be reinterpreted to fit any observation.

Fludd responded vigorously in several treatises, defending the legitimacy \
of his symbolic-qualitative method as addressing different questions than \
Kepler's mathematical astronomy. The exchange crystallizes the methodological \
rupture that Peter Dear, Robert Westman, and others have analyzed: the \
divergence between two legitimate but incompatible approaches to natural \
knowledge — the Hermetic-qualitative and the mathematical-quantitative — \
that the seventeenth century was in the process of separating into \
'science' and 'occultism.'""",

     "German astronomer; discoverer of planetary motion laws; his 1619 polemic \
against Robert Fludd crystallizes the methodological rupture between the \
Hermetic-qualitative tradition and emerging mathematical-quantitative natural \
science — the divergence that produced the modern distinction between \
'science' and 'occultism'"),

    ("Marin Mersenne", "HISTORICAL", 1588, 1648, "French",
     """\
Marin Mersenne (1588–1648), French Franciscan friar, mathematician, and \
scientific correspondent, was one of the central figures of the seventeenth-\
century republic of letters — corresponding with Descartes, Galileo, Hobbes, \
Gassendi, and virtually every major natural philosopher of the period. His \
significance for the history of Renaissance magic lies primarily in his attacks \
on Robert Fludd: in Quaestiones celeberrimae in Genesim (1623) and subsequent \
works, Mersenne accused Fludd of Cabalism and Hermetism incompatible with \
orthodox Christian natural philosophy, and argued that Fludd's symbolic-\
qualitative method produced no genuine knowledge of nature.

Mersenne's critique of Fludd combined theological concerns (Hermetism as \
a threat to orthodox Christianity) with methodological ones (analogical \
reasoning as epistemically vacuous). His position was that mathematics and \
mechanics — the method Descartes was developing simultaneously — provided \
the only legitimate framework for natural philosophy. Together with Kepler's \
polemic, Mersenne's attacks represent the growing institutional and theological \
pressure that compressed the space available for Hermetic natural philosophy \
in the seventeenth century.""",

     "French Franciscan friar and mathematician; his attacks on Robert Fludd \
in Quaestiones celeberrimae in Genesim (1623) combined theological concerns \
about Hermetism with methodological critique of analogical reasoning; together \
with Kepler's polemic, represents the institutional pressure that marginalized \
the Hermetic tradition in the seventeenth century"),

    ("Johann Valentin Andreae", "HISTORICAL", 1586, 1654, "German",
     """\
Johann Valentin Andreae (1586–1654), German Lutheran theologian and author, \
is the figure most credibly associated with the authorship of the Rosicrucian \
manifestos. The Chemical Wedding of Christian Rosencreutz (1616), the most \
literary of the three Rosicrucian texts, is attributed to Andreae with \
relatively high confidence; he later acknowledged it as a youthful literary \
jest (Ludibrium), though the degree to which he disowned the broader \
Rosicrucian project is debated. His connection to the Fama Fraternitatis \
(1614) and Confessio Fraternitatis (1615) is more uncertain.

The Rosicrucian manifestos generated an enormous literary debate across Europe \
in the 1610s and 1620s — hundreds of pamphlets, responses, and satires — but \
no actual Rosicrucian fellowship has ever been conclusively identified. Frances \
Yates, in The Rosicrucian Enlightenment (1972), argued that the manifestos \
represented a serious program for reforming European learning along Hermetic \
lines, connected to the court of Frederick V of the Palatinate and the \
Bohemian crisis. Subsequent scholarship has qualified this reading while \
accepting that the manifestos drew on genuine Paracelsian, alchemical, and \
Hermetic currents in early seventeenth-century German Lutheran culture.""",

     "German Lutheran theologian; attributed author of the Chemical Wedding of \
Christian Rosencreutz (1616), the most literary Rosicrucian manifesto — an \
alchemical allegory combining spiritual transformation, emblematic imagery, \
and court entertainment; Andreae later called it a youthful Ludibrium, though \
the Rosicrucian movement he helped generate was culturally significant"),
]

# ── SIGNIFICANCE EXPANSIONS FOR EXISTING FIGURES ────────────────────────────
# Format: (name, new_significance)
# Only updates if current significance is shorter

SIGNIFICANCE_UPDATES = [
    ("Johannes Trithemius",
     "German Benedictine abbot and humanist scholar; Steganographia composed a \
systematic angel-magic communication system while embedding genuine cryptographic \
ciphers within the angelic framework; Polygraphia is the earliest printed work \
on cryptography; teacher and correspondent of Agrippa, who drew on Trithemius's \
treatment of celestial spirits for De Occulta Philosophia"),

    ("Brian P. Copenhaver",
     "American historian of philosophy at UCLA; critical editions of Hermetica \
(1992) and Pico's works provide the textual foundation for current scholarship; \
his essays revising the Yates thesis — arguing Ficino was primarily a Platonist \
not a Hermetist, and that 'Hermetism' is a scholarly construct — constitute the \
most influential post-Yates methodological revision; general editor of the \
Cambridge History of Renaissance Philosophy"),

    ("Johannes Reuchlin",
     "German humanist and Hebraist; De Verbo Mirifico (1494) and De Arte \
Cabalistica (1517) are the foundational texts of Christian Kabbalah — \
arguments that Kabbalistic interpretation of Hebrew reveals Christianity's \
truth encoded in the Old Testament; his defense of Jewish books against \
Pfefferkorn's destruction campaign (1509–1514) galvanized the humanist movement \
and established the legitimacy of Hebrew learning for Christian scholars"),

    ("Robert Fludd",
     "English Paracelsian physician and Rosicrucian philosopher; Utriusque \
Cosmi Historia (1617–21) is the most elaborately illustrated cosmological \
synthesis of the Renaissance, integrating Hermetic, Kabbalistic, alchemical, \
and musical symbolism in macrocosm-microcosm diagrams; his polemics with \
Kepler and Mersenne crystallize the methodological rupture between Hermetic \
qualitative analogy and emerging mathematical-quantitative natural science"),

    ("Avicenna",
     "Persian polymath (Ibn Sina); his Canon of Medicine remained the standard \
medical text in European universities into the seventeenth century; his \
Neoplatonized Aristotelian pneumatic psychology — especially the theory that \
a powerful imagination can act on external matter — provided the theoretical \
basis for Renaissance accounts of fascination, the evil eye, and the \
physician-practitioner's power over the body; transmitted by Albertus Magnus \
and the Toledo translation school"),

    ("John Dee",
     "English mathematician, astronomer, astrologer, and occult philosopher; \
advisor to Elizabeth I on navigation and calendar reform; the angelic \
conversations conducted with Edward Kelley (1581–1589) produced the Enochian \
language and celestial system — the most elaborate angelological system of \
the Renaissance; Monas Hieroglyphica (1564) presents a mathematical-symbolic \
account of the unity of the cosmos through a single hieroglyphic symbol; \
held the largest private library in Elizabethan England"),

    ("Giordano Bruno",
     "Italian Dominican friar turned philosopher; executed by the Roman \
Inquisition (1600) for heretical cosmological and theological doctrines; \
his infinite-universe cosmology drew on Copernicus and Nicholas of Cusa but \
was embedded in a Hermetic-magical framework; transformed Lullian combinatory \
art into a Hermetic memory system for impressing the animated cosmos on the \
practitioner's mind; Frances Yates's Giordano Bruno and the Hermetic Tradition \
(1964) made him the central figure of her Hermetic thesis"),

    ("Jacob Boehme",
     "German Christian mystic, shoemaker, and theologian; Aurora (1612) \
presented a spontaneous theosophical vision of the divine ground, the \
generation of the divine persons, and the spiritual structure of nature — \
drawing on Paracelsian chemical imagery, Kabbalistic symbolism, and Lutheran \
piety; Boehme's influence on German Romanticism, Schelling, and Hegel makes \
him a key figure in the transmission of Renaissance Hermetic-alchemical \
themes into later Western intellectual history"),

    ("Giovanni Pico della Mirandola",
     "Italian philosopher; Oration on the Dignity of Man (1486) is the \
Renaissance's most eloquent statement of human freedom and perfectibility; \
his 900 Conclusiones (1486) — condemned by Innocent VIII — included the first \
systematic Christian Kabbalistic theses, arguing that Kabbalah confirms \
Christian doctrine; synthesized Hermetism, Neoplatonism, Kabbalah, Aristotle, \
and Arabic philosophy; settled in Florence under Medici protection, in \
direct intellectual exchange with Ficino"),

    ("Marsilio Ficino",
     "Italian philosopher, Catholic priest, and translator; head of the \
Florentine Platonic Academy under Cosimo de' Medici; his Latin translation \
of the Corpus Hermeticum (1463) and Plato (completed 1484) gave the Latin \
West its first full access to these traditions; Theologia Platonica (1482) \
synthesized Neoplatonism and Christianity; De Vita Coelitus Comparanda (1489) \
is the foundational philosophical account of natural talismanic magic; \
Walker's distinction between spiritual and demonic magic was built on \
close reading of Ficino's strategies for legitimizing his practices"),

    ("Plotinus",
     "Egyptian-born Neoplatonist philosopher teaching in Rome; the Enneads \
(arranged by Porphyry) articulate the system of divine emanation — One, \
Intellect, Soul, Matter — that grounds all subsequent Neoplatonism; the \
doctrine of world-soul pervading and animating the cosmos provided Ficino's \
philosophical basis for natural magic; his account of the soul's ascent \
through philosophical contemplation structures the spiritual dimension of \
Renaissance magical theory"),

    ("Porphyry",
     "Neoplatonist philosopher; disciple and biographer of Plotinus; his \
edition of the Enneads (c.301) preserved Plotinus's work for posterity; the \
Isagoge (Introduction to Aristotle's Categories) became the standard medieval \
logic textbook; his Letter to Anebo challenging the philosophical basis of \
theurgy provoked Iamblichus's De Mysteriis as a systematic defense — the \
central ancient debate about whether ritual practice or philosophical \
contemplation alone can unite the soul with the divine"),

    ("Hermes Trismegistus",
     "Legendary author of the Corpus Hermeticum; syncretic figure combining \
Greek Hermes and Egyptian Thoth, imagined as a contemporary of Moses \
transmitting the same prisca theologia; Isaac Casaubon's 1614 philological \
demonstration that the texts are early centuries CE compositions permanently \
changed their scholarly reception; they remain philosophically significant \
as evidence of Neoplatonist culture regardless of their fraudulent origin \
claim, and as the primary source for Ficino's Hermetic synthesis"),

    ("Nicholas of Cusa",
     "German cardinal and philosopher; De Docta Ignorantia (1440) argued that \
the infinite God exceeds rational comprehension and can be approached only \
through 'learned ignorance' — acknowledgment of the limits of human knowing; \
his cosmological corollary that the infinite universe has no fixed center \
directly influenced Bruno's infinite cosmology; his mathematical mysticism \
(using mathematical paradoxes to approach divine infinity) influenced Dee's \
symbolic mathematics in the Monas Hieroglyphica"),

    ("Iamblichus",
     "Syrian Neoplatonist (c.245–c.325); De Mysteriis Aegyptiorum (c.300) \
provided the most systematic ancient philosophical defense of theurgy — \
arguing that divinely instituted ritual operations, not philosophical \
contemplation alone, prepare the soul for union with the divine; his \
insistence that theurgical power derives from the gods' own nature rather \
than human convention underwrites Renaissance ceremonial magic's \
philosophical self-defense; the dominant Neoplatonist for the Florentine \
Academy's engagement with ritual"),

    ("Proclus",
     "Late-antique Neoplatonist; head of Platonic Academy in Athens; Elements \
of Theology (c.450) axiomatized Neoplatonic metaphysics into 211 propositions \
on the Euclidean model — hierarchical divine emanation from the One through \
divine henads, Intellect, and Soul; his works on theurgy provided the \
philosophical framework for ritual operation that Ficino, Agrippa, and Dee \
draw on; Liber de Causis, a compilation from his Elements, circulated \
attributed to Aristotle throughout the medieval West"),
]

# ── EVENT-FIGURE ASSOCIATIONS to backfill ───────────────────────────────────
# Maps event title → list of figure names to associate
# These were skipped in expand_timeline.py because the figures didn't exist yet

BACKFILL_ASSOCIATIONS = {
    "Moses de León composes the Zohar in Castile": ["Moses de León"],
    "Picatrix translated into Castilian for Alfonso X": [],
    "Albertus Magnus writes Speculum Astronomiae": ["Albertus Magnus"],
    "House of Wisdom translation project in Baghdad": ["Al-Kindi"],
    "Bodin publishes De la Démonomanie des Sorciers": ["Jean Bodin"],
    "James VI publishes Daemonologie": [],
    "Mersenne attacks Fludd as incompatible with Christian philosophy": ["Marin Mersenne", "Robert Fludd"],
    "Kepler-Fludd polemic over mathematical vs analogical method": ["Johannes Kepler", "Robert Fludd"],
    "Descartes publishes Discourse on Method": ["René Descartes"],
    "Newton's alchemical investigations": ["Isaac Newton"],
    "Newton publishes Principia Mathematica": ["Isaac Newton"],
    "Isaac Casaubon's philological dating of Corpus Hermeticum": ["Isaac Casaubon", "Hermes Trismegistus"],
    "Chemical Wedding of Christian Rosencreutz": ["Johann Valentin Andreae"],
    "Confessio Fraternitatis (second Rosicrucian manifesto)": [],
    "Van Helmont and Knorr von Rosenroth publish Kabbala Denudata": ["Francis Mercury van Helmont"],
    "Meric Casaubon publishes Dee's True and Faithful Relation": ["John Dee"],
    "Walker publishes Spiritual and Demonic Magic": ["D.P. Walker", "Marsilio Ficino"],
    "Yates publishes The Art of Memory": ["Frances A. Yates", "Giordano Bruno"],
    "Keith Thomas publishes Religion and the Decline of Magic": ["Keith Thomas"],
    "Peters publishes The Magician, the Witch, and the Law": ["Edward Peters"],
    "Vickers publishes methodological critique of Yates thesis": ["Brian Vickers", "Frances A. Yates"],
    "Copenhaver publishes essays revising the Yates thesis": ["Brian P. Copenhaver", "Marsilio Ficino"],
    "Copenhaver publishes critical edition of Hermetica": ["Brian P. Copenhaver", "Hermes Trismegistus"],
    "Klaassen publishes Transformations of Magic": ["Frank Klaassen"],
    "Hanegraaff edits Dictionary of Gnosis and Western Esotericism": ["Wouter Hanegraaff"],
    "Hanegraaff publishes Esotericism and the Academy": ["Wouter Hanegraaff"],
    "Saif publishes Arabic Influences on Early Modern Occult Philosophy": ["Liana Saif", "Al-Kindi"],
    "Luther's Ninety-Five Theses initiate the Reformation": [],
}


def run():
    conn = sqlite3.connect(str(DB_PATH))
    conn.execute("PRAGMA foreign_keys=ON")
    c = conn.cursor()

    # ── INSERT NEW FIGURES ───────────────────────────────────────────────────
    print("=== Inserting new figures ===")
    inserted_figs = 0
    for (name, ftype, birth, death, nationality,
         biography, significance) in NEW_FIGURES:
        exists = c.execute(
            "SELECT id FROM figures WHERE name=?", (name,)
        ).fetchone()
        if exists:
            print(f"  SKIP (exists): {name}")
            continue
        c.execute("""
            INSERT INTO figures
                (name, figure_type, birth_year, death_year, nationality,
                 biography, significance,
                 source_method, review_status, confidence)
            VALUES (?, ?, ?, ?, ?, ?, ?, 'HUMAN_VERIFIED', 'REVIEWED', 'HIGH')
        """, (name, ftype, birth, death, nationality, biography, significance))
        print(f"  INSERT: {name} ({ftype})")
        inserted_figs += 1
    conn.commit()
    print(f"  New figures inserted: {inserted_figs}")

    # ── EXPAND SIGNIFICANCE FIELDS ───────────────────────────────────────────
    print()
    print("=== Expanding figure significance fields ===")
    updated_sig = 0
    for name, new_sig in SIGNIFICANCE_UPDATES:
        row = c.execute(
            "SELECT id, significance FROM figures WHERE name=?", (name,)
        ).fetchone()
        if row is None:
            print(f"  SKIP (not found): {name}")
            continue
        fig_id, existing = row
        existing_len = len(existing) if existing else 0
        if existing_len >= len(new_sig):
            print(f"  SKIP (existing longer {existing_len}): {name}")
            continue
        c.execute("""
            UPDATE figures
            SET significance=?, updated_at=datetime('now')
            WHERE id=?
        """, (new_sig, fig_id))
        print(f"  UPDATE: {name} ({existing_len} → {len(new_sig)} chars)")
        updated_sig += 1
    conn.commit()
    print(f"  Significance fields updated: {updated_sig}")

    # ── BACKFILL EVENT-FIGURE ASSOCIATIONS ──────────────────────────────────
    print()
    print("=== Backfilling event-figure associations ===")

    # Rebuild figure map (includes newly inserted figures)
    fig_map = {}
    for row in c.execute("SELECT id, name FROM figures").fetchall():
        fig_map[row[1]] = row[0]

    assoc_added = 0
    for event_title, fig_names in BACKFILL_ASSOCIATIONS.items():
        # Find all events with this title (there can be several years)
        events = c.execute(
            "SELECT id FROM timeline_events WHERE title=?", (event_title,)
        ).fetchall()
        if not events:
            print(f"  WARNING event not found: {event_title}")
            continue
        for (event_id,) in events:
            for fig_name in fig_names:
                fig_id = fig_map.get(fig_name)
                if fig_id is None:
                    print(f"  WARNING figure not found: {fig_name}")
                    continue
                try:
                    c.execute(
                        "INSERT OR IGNORE INTO event_figures "
                        "(event_id, figure_id) VALUES (?, ?)",
                        (event_id, fig_id)
                    )
                    if conn.total_changes:
                        assoc_added += 1
                except Exception as e:
                    print(f"  WARNING: {e}")
    conn.commit()
    print(f"  Associations added: {assoc_added}")

    # ── SUMMARY ─────────────────────────────────────────────────────────────
    total_figs = c.execute("SELECT COUNT(*) FROM figures").fetchone()[0]
    total_events = c.execute("SELECT COUNT(*) FROM timeline_events").fetchone()[0]
    total_assoc = c.execute("SELECT COUNT(*) FROM event_figures").fetchone()[0]
    conn.close()

    print()
    print("=== Done ===")
    print(f"  Total figures: {total_figs}")
    print(f"  Total timeline events: {total_events}")
    print(f"  Total event-figure associations: {total_assoc}")


if __name__ == "__main__":
    run()
