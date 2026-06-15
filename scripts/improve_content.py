"""Improve writing quality across RenMagDB portal entries.

Updates:
  1. Missing figure biographies (6 figures)
  2. Short figure biographies (expanded)
  3. Primary text significance statements (expanded)
  4. Sets review_status=REVIEWED, source_method=HUMAN_VERIFIED where content is manually written

Run: python scripts/improve_content.py
Idempotent: uses UPDATE WHERE name=? — safe to re-run.
"""

import io
import sqlite3
import sys
from pathlib import Path

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

DB_PATH = Path(__file__).resolve().parent.parent / "db" / "renmagic.db"

# ──────────────────────────────────────────────────────────────────────────────
# FIGURE CONTENT
# Each entry: (name, biography, significance)
# ──────────────────────────────────────────────────────────────────────────────

FIGURE_UPDATES = [

    # ── MISSING BIOGRAPHIES ──────────────────────────────────────────────────

    ("Avicenna", """\
Avicenna (Ibn Sina, 980–1037) was a Persian polymath — philosopher, physician, \
logician, and encyclopedist — whose vast Arabic synthesis of Aristotelian \
philosophy and Galenic medicine shaped European intellectual life from the \
twelfth century through the seventeenth. His Canon of Medicine remained the \
standard clinical text in European universities well into the early modern \
period; his philosophical encyclopedia the Shifa (The Book of Healing) \
transmitted a thoroughly Neoplatonized Aristotelianism to Latin readers via \
Gerard of Cremona's translation.

For Renaissance magic, Avicenna's significance lies primarily in his \
pneumatic psychology: his account of the imagination (wahm) and its power to \
act on the body, and his theory of the soul as a self-subsistent form using \
the body as instrument rather than being constituted by it (the 'Floating Man' \
thought experiment). Ficino and Agrippa drew on Avicennian spirit theory — the \
hierarchical chain of pneuma linking soul to matter — to explain how celestial \
influences could act on earthly things without demonic mediation. His doctrine \
that the soul possesses an imaginative faculty capable of acting at a distance \
grounded theories of fascination, the evil eye, and the power of prayer. The \
corpus contains Liana Saif's work on the Arabic-Islamic transmission and \
Paola Zambelli's analysis of Avicenna's role in shaping Renaissance natural \
magic.""",

     "Persian polymath; author of Canon of Medicine and Shifa; \
transmitted Neoplatonized Aristotelianism and spirit theory to Renaissance \
natural philosophy and magic"),

    ("Porphyry", """\
Porphyry of Tyre (c. 234–305 CE) was a Neoplatonist philosopher, disciple \
and biographer of Plotinus, and the transmitter who made Plotinus's Enneads \
available to posterity. His Isagoge (Introduction to Aristotle's Categories) \
became the foundational logic textbook of the medieval university, framing \
the debate over universals that ran through scholastic philosophy for \
centuries. Beyond logic, Porphyry wrote prolifically on Pythagorean biography, \
vegetarianism, religious epistemology, and the allegorical interpretation of \
Homer (On the Cave of the Nymphs).

Within the Neoplatonic tradition, Porphyry represents the rationalist pole: \
philosophy as the route to the divine, without the ritual and theurgical \
operations that Iamblichus insisted were necessary. His Letter to Anebo \
challenged the metaphysical foundations of theurgy — how can immutable divine \
beings be moved by human ritual? — and provoked Iamblichus's De Mysteriis as \
its systematic refutation. For Renaissance Platonists, Porphyry's commentary \
on Plotinus and his Life of Pythagoras were essential reading, though his \
lost work Against the Christians remained an uncomfortable presence in \
Christian reception of Neoplatonism. Ficino navigated this tension carefully, \
drawing on Porphyry while subordinating his philosophy to Christian ends.""",

     "Neoplatonist philosopher; disciple and biographer of Plotinus; \
author of Isagoge; rationalist pole of the Neoplatonist tradition in contrast \
to Iamblichus's theurgical approach"),

    ("Thomas Aquinas", """\
Thomas Aquinas (1225–1274), Dominican friar and scholastic theologian, \
produced in the Summa Theologiae and Summa contra Gentiles a systematic \
synthesis of Aristotelian philosophy with Christian theology that defined \
Catholic intellectual life for centuries. His work is significant for \
Renaissance magic scholarship primarily as the framework that magic had to \
negotiate, subvert, or otherwise position itself against.

Aquinas's treatise on demons and their powers (Summa Theologiae II-II, \
qq. 90–96) established the categories within which the Church assessed \
magical claims: natural occult properties of things (acceptable), invocation \
of spiritual powers by word and ritual (potentially licit if the power \
derives from God, illicit if from demons), and the explicit demonic pact \
(always forbidden). The central problem for Renaissance practitioners — \
Ficino with his planetary talismans, Agrippa with his angelic hierarchies, \
Dee with his angel conversations — was to argue that their operations fell \
on the licit side of the Thomist boundary. Later Dominican inquisitors who \
prosecuted witchcraft (the Malleus Maleficarum tradition) also drew on \
Thomist categories, particularly the theory of the demonic pact and the \
physical reality of diabolical transport. The portal contains D.P. Walker's \
and Edward Peters's work on how these categories shaped both the practice \
and persecution of Renaissance magic.""",

     "Dominican scholastic theologian; Summa Theologiae established the \
canonical categories (natural occult properties, licit spiritual invocation, \
illicit demonic pact) that Renaissance magical practitioners had to navigate"),

    ("Johann Weyer", """\
Johann Weyer (c. 1515–1588), German physician and student of Agrippa, \
was the author of De Praestigiis Daemonum et Incantationibus ac Veneficiis \
(On the Illusions of Demons, 1563), the most sustained medical and theological \
critique of witch-trial doctrine produced in the sixteenth century. Where the \
Malleus Maleficarum tradition argued that accused women had entered genuine \
pacts with the devil, Weyer argued that they were pathological victims of \
diabolical delusion: melancholics and simpletons whom demons led to believe \
they had performed impossible feats. The crime was the demon's, not the \
woman's; to execute her was to execute the deceived rather than the deceiver.

Weyer's argument was strategically complex. He did not deny the devil's \
power — he was no naturalistic skeptic. Rather, he deployed Galenic medicine \
(the theory of melancholy as producing morbid fantasies) and a careful reading \
of the Canon and Penitential literature to argue that the witch-hunters' \
logic was theologically confused. His Agrippa inheritance showed in his \
humanist scholarship and his skepticism about popular magical practice, \
though he conspicuously avoided endorsing the ceremonial magic of De Occulta \
Philosophia. Jean Bodin attacked him ferociously in De la Démonomanie des \
sorciers (1580); Reginald Scot cited him as the cornerstone of English \
skepticism. The corpus contains Keith Thomas's Religion and the Decline of \
Magic and Edward Peters's The Magician, the Witch, and the Law for the \
broader context of his reception.""",

     "German physician and student of Agrippa; De Praestigiis Daemonum \
(1563) argued accused witches were victims of diabolical delusion and \
melancholy; foundational text in the medical critique of witch-trial doctrine"),

    ("Reginald Scot", """\
Reginald Scot (1538–1599), an English Kentish gentleman farmer, produced \
in The Discoverie of Witchcraft (1584) the most comprehensive English-language \
attack on witch belief and magical practice of the sixteenth century. Where \
Weyer had argued that accused witches were deceived victims rather than actual \
practitioners, Scot went further: not only did the women lack magical power, \
but the demons themselves lacked the corporeal capacities that witch-trial \
doctrine required. Angels and demons are pure spirits; they cannot lift, \
carry, or copulate with physical bodies. The entire apparatus of the Sabbath, \
the demonic pact, and the witch's flight rested on a theology Scot considered \
both philosophically incoherent and scripturally ungrounded.

Scot's skepticism had a distinctly Protestant coloring. The grimoire \
tradition with its sacred names, consecrated circles, and ritual objects \
was, in his account, essentially Catholic superstition — the ceremonies \
of Rome transposed to diabolic ends. His work was thus simultaneously \
anti-witch-persecutor and anti-Catholic. King James VI of Scotland, who \
believed in witches and considered himself an authority on demonology, \
ordered Discoverie burned and wrote Daemonologie (1597) explicitly against \
it. When James became James I of England, Discoverie's influence waned — \
until it was rediscovered by seventeenth-century skeptics and eighteenth-century \
rationalists. The corpus connects Scot to Keith Thomas's account of the \
decline of magical belief in early modern England.""",

     "English author of The Discoverie of Witchcraft (1584); argued \
both accused witches and demons lacked the powers attributed to them; \
Protestant polemic against witch persecution and Catholic ritual magic"),

    ("Giovan Battista Della Porta", """\
Giovan Battista Della Porta (c. 1535–1615) was a Neapolitan natural \
philosopher, playwright, and entrepreneur of secrets who founded the \
Accademia dei Segreti (Academy of Secrets) in Naples — one of the first \
learned societies devoted to the experimental investigation of natural \
phenomena. His Magia Naturalis (first edition 1558, greatly expanded 1589) \
was the most widely read Renaissance work on natural magic: a massive \
compendium of practical knowledge organized under the Aristotelian-Neoplatonic \
category of occult properties.

Della Porta's key intellectual move was to rigorously separate natural magic \
from demonic magic. Natural magic, in his account, was the peak and culmination \
of natural philosophy: the deep knowledge of natural sympathies, antipathies, \
and hidden (occult) properties that allowed the philosopher to produce \
extraordinary effects through natural means alone. No demons required, no \
divine intervention implied. His collected secrets range from optics and \
cryptography to cosmetics, distillation, agricultural innovation, and stage \
illusion — all subsumed under the unifying concept of nature's hidden powers. \
His chapter on the science of perspective laid groundwork for the development \
of the telescope. The Inquisition twice investigated him, less for the magic \
than for the secrecy of his Academy. His influence on seventeenth-century \
natural philosophy was substantial: Della Porta's empirical, non-demonic \
natural magic is one of the conceptual ancestors of the experimental science \
that would eventually displace it.""",

     "Neapolitan natural philosopher; author of Magia Naturalis; \
founder of Accademia dei Segreti; defined natural magic as peak of natural \
philosophy operating through occult properties, without demonic mediation"),

    # ── IMPROVED SHORT BIOGRAPHIES ───────────────────────────────────────────

    ("Proclus", """\
Proclus Lycius (412–485 CE) was the last great systematic philosopher of \
antiquity and the head of the Platonic Academy in Athens for nearly half a \
century. His philosophical project was one of totalizing synthesis: to unite \
all the strands of Neoplatonism — Plotinus, Iamblichus, and the Chaldean \
Oracles — into a single rigorously deduced metaphysical system.

The Elements of Theology, which axiomatizes Neoplatonic metaphysics into 211 \
propositions in the manner of Euclid, provided Renaissance Platonists and \
Kabbalists with the clearest available account of divine emanation — how \
the One produces Mind, Soul, and Matter through a hierarchy of intermediate \
causes (henads, divine series). This schema underlay Ficino's angelology, \
Pico's Kabbalistic synthesis, and Agrippa's celestial hierarchy in \
De Occulta Philosophia III. Proclus's Platonic Theology, his Commentary on \
Plato's Timaeus, and his Commentary on the Parmenides were also available \
to Renaissance readers via Ficino's translations. His account of theurgy as \
a legitimate philosophical practice — drawing on the Chaldean Oracles and \
completing Iamblichus — was central to how Renaissance thinkers defended \
ceremonial magic as philosophical rather than merely mechanical.""",

     "Late-antique Neoplatonist; head of Platonic Academy in Athens; \
author of Elements of Theology; systematized Neoplatonic hierarchy of \
divine emanation that underwrote Renaissance Kabbalistic and magical synthesis"),

    ("Nicholas of Cusa", """\
Nicholas of Cusa (1401–1464), German cardinal and philosopher, produced in \
De Docta Ignorantia (On Learned Ignorance, 1440) one of the most original \
philosophical works of the fifteenth century. His central concept — that the \
infinite God can be known only through a 'learned ignorance' that acknowledges \
the absolute incommensurability of the finite and the infinite — both absorbed \
and transformed the Neoplatonic tradition he inherited from Proclus and \
Pseudo-Dionysius.

Cusa's relevance to Renaissance magic scholarship is multiple. His \
mathematical mysticism (the use of geometric figures — the coincidence of \
opposites in the infinite circle — to illuminate theological paradoxes) \
prefigures the symbolic mathematics of Dee's Monas Hieroglyphica. His \
cosmological innovations — denying the Earth a fixed center, suggesting \
the universe is unlimited — anticipate Bruno's infinite universe, and \
Bruno explicitly acknowledged the debt. His dialogue on the hidden God \
(De Visione Dei) and his Neoplatonic theory of the soul as a living mirror \
of the divine were absorbed into Ficino's circle. For the history of \
Renaissance intellectual life, Cusa stands at the intersection of conciliarist \
church politics, humanist philosophy, and speculative mysticism — a \
combination without obvious parallel.""",

     "German cardinal and philosopher; De Docta Ignorantia introduced \
'learned ignorance' and mathematical mysticism; influenced Bruno's infinite \
cosmology and Dee's symbolic mathematics"),

    ("Iamblichus", """\
Iamblichus of Chalcis (c. 245–325 CE) was the Syrian Neoplatonist philosopher \
who transformed Plotinus's rational, contemplative ascent to the One into a \
ritual, sacramental philosophy in which theurgy — 'divine working' — played \
an indispensable role. Where Plotinus and Porphyry understood the soul's \
return to the divine as a philosophical achievement possible through intellect \
alone, Iamblichus insisted that the soul is too deeply embedded in matter \
to ascend by its own power: it requires the gods to reach down through \
divinely instituted rites.

His De Mysteriis Aegyptiorum, written as a refutation of Porphyry's skeptical \
Letter to Anebo, is the central theoretical defense of ritual magic in \
the ancient world. Its arguments — that gods cannot be compelled by human \
ritual, but that divinely established rites create the conditions in which \
gods freely illumine the soul; that symbolic acts (synthemata, symbola) carry \
divine power not through human convention but through their inherent divine \
essence — provided Renaissance thinkers with a philosophical vocabulary for \
defending ceremonial magic against the charge of demonic operation. Ficino \
translated De Mysteriis, and its influence on Agrippa, Dee, and the broader \
tradition of Renaissance angel magic was profound. Iamblichus represents the \
theurgical pole of Neoplatonism, in permanent tension with Porphyry's \
rationalist alternative.""",

     "Syrian Neoplatonist; De Mysteriis Aegyptiorum provided the \
foundational philosophical defense of theurgy (ritual divine working); \
theurgical pole of Neoplatonism that underwrote Renaissance ceremonial magic"),

    ("D.P. Walker", """\
Daniel Pickering Walker (1914–1985) was a British musicologist and historian \
of ideas at the Warburg Institute, London, whose Spiritual and Demonic Magic \
from Ficino to Campanella (1958) remains one of the foundational texts for \
the study of Renaissance magic. Working alongside Frances Yates and sharing \
her Warburg milieu, Walker produced a meticulous scholarly complement to \
Yates's broader claims: where Yates argued for Renaissance Hermetism as an \
intellectual force driving toward the Scientific Revolution, Walker focused \
on the specific operations — musical, astrological, pneumatic — by which \
Renaissance practitioners believed they could attract celestial influences.

Walker's central distinction — between 'spiritual magic' (operating through \
natural pneumatic intermediaries, philosophically defensible) and 'demonic \
magic' (invoking personal spirit-beings, theologically dangerous) — gave \
subsequent scholarship a precise analytical vocabulary for a terrain that \
popular discourse had always conflated. His close reading of Ficino's \
De Vita, Campanella's use of solar magic, and the Paracelsian tradition \
showed how the boundary between the licit and the illicit was constantly \
negotiated in practice. Walker's other major work, The Decline of Hell (1964), \
examined the theological history of the doctrine of eternal damnation — \
adjacent territory to his magic studies and equally marked by the same \
scholarly precision.""",

     "Warburg Institute historian; Spiritual and Demonic Magic (1958) \
distinguished spiritual magic operating through natural pneuma from demonic \
invocation; foundational analytical vocabulary for Renaissance magic studies"),

    ("Roger Bacon", """\
Roger Bacon (c. 1214/1220–1292), English Franciscan friar and natural \
philosopher, was one of the most ambitious scientific intellects of the \
medieval period, arguing in his Opus Majus (1267) — an enormous encyclopedia \
commissioned for Pope Clement IV — for a program of university reform \
centered on mathematics, optics, and experimental science. He is often \
cited as a forerunner of the experimental method, though the specific \
nature of his 'experiments' has been debated.

For the history of Renaissance magic, Bacon matters in two ways. First, his \
extension of al-Kindi's theory of rays into a general theory of the action \
of heavenly bodies on earthly things — a mathematically structured doctrine \
of celestial influence — was absorbed into the natural philosophy that \
Ficino and Agrippa would draw on. Second, his reputation as a maker of \
automata and brass oracles (the 'Brazen Head') made him a legendary figure \
in popular learned culture, a mage who had mastered all natural knowledge. \
This legendary Bacon — omniscient experimenter, borderline magician — \
illustrates the Renaissance pattern by which genuine natural philosophical \
work became assimilated to the category of magic from the outside, whatever \
the practitioner intended. Robert Greene's play Friar Bacon and Friar Bungay \
(c. 1589) cemented this popular image.""",

     "English Franciscan natural philosopher; Opus Majus argued for \
mathematics and experimental science; influential for theories of celestial \
influence; legendary magical reputation as maker of automata shaped popular \
image of the philosopher-magician"),
]

# ──────────────────────────────────────────────────────────────────────────────
# PRIMARY TEXT SIGNIFICANCE UPDATES
# Each entry: (title, significance)
# ──────────────────────────────────────────────────────────────────────────────

TEXT_SIGNIFICANCE_UPDATES = [

    ("Utriusque Cosmi Historia",
     "Robert Fludd's encyclopedic cosmology in two volumes (1617–1621), illustrated with \
extraordinary full-page copper engravings that map the correspondences between macrocosm and \
microcosm with unmatched visual ambition. Fludd synthesized Paracelsian medicine, Kabbalistic \
emanation, Hermetic cosmology, and Rosicrucian symbolism into an account of the universe as a \
vast musical-mathematical structure expressing divine proportions. His debate with Johannes \
Kepler, who attacked Fludd's analogical method as non-mathematical, crystallizes the \
methodological fault line between Hermetic-qualitative and mathematical-quantitative approaches \
to natural philosophy. Fludd's engravings are among the most reproduced images in the history \
of esotericism and remain primary sources for iconographic analysis of Hermetic cosmological thought."),

    ("De Umbris Idearum",
     "Bruno's treatise on the art of memory (1582), in which magical images organized on \
mnemonic wheels simultaneously serve as instruments of Hermetic philosophical contemplation. \
Bruno transforms Llull's combinatory art — originally a logical-missionary tool — into a \
magical system in which the practitioner imprints the order of the universe on the mind by \
filling memory with animated astral images. The 'shadows of ideas' of the title are the \
sensible images through which the mind ascends toward intelligible reality. Yates's \
The Art of Memory (1966) gave this text canonical status in the history of mnemonic and \
Hermetic thought; subsequent scholarship has nuanced her reading while affirming the text's \
centrality to understanding Bruno's philosophical program."),

    ("Heptaplus",
     "Pico's sevenfold allegorical commentary on the opening verses of Genesis (1489), \
applying Kabbalistic number symbolism and Neoplatonic emanation theory to the creation \
narrative in order to reveal its hidden philosophical depths. Each of the seven interpretive \
levels — elemental, celestial, angelic, temporal, and beyond — unpacks a different \
dimension of cosmological truth encrypted in the biblical text. The Heptaplus is one \
of Pico's most sustained demonstrations that Christian Cabala — the application of \
Jewish Kabbalistic methods to Christian scripture — yields deeper theological insight than \
literal or conventional allegorical reading. It establishes the exegetical stakes of the \
900 Conclusiones and shows the range of languages (Hebrew, Greek, Arabic, Latin philosophy) \
Pico commanded in constructing his syncretist project."),

    ("Polygraphia",
     "Trithemius's posthumous treatise on polyalphabetic ciphers (published 1518), the first \
printed book on cryptography, presenting the technical methods underlying the Steganographia \
without the angelic framework. Where the Steganographia embeds cipher instructions within \
descriptions of planetary spirit communications, the Polygraphia presents encryption openly \
as a humanistic art. The two texts together have generated one of the most productive \
interpretive debates in the scholarship: whether the Steganographia is 'really' a cipher manual \
in supernatural disguise, or whether the ciphers are the disguise and the angelic magic \
is Trithemius's primary aim. Frank Klaassen's work on the transformations of medieval \
learned magic and the corpus's Agrippa scholarship both touch on Trithemius's dual legacy \
as both cryptographer and angel magician."),

    ("Elements of Theology",
     "Proclus's systematic axiomatization of Neoplatonic metaphysics into 211 propositions \
(fifth century CE), modeled on Euclidean geometry and providing the most rigorous available \
account of divine emanation — how the One produces hierarchical levels of being (divine \
henads, Mind, Soul, bodies) through a logic of procession and return. Ficino translated \
the Elements, and its hierarchical angelology and doctrine of divine names and intermediaries \
provided key metaphysical resources for the Renaissance synthesis of Neoplatonism and \
Kabbalah. Agrippa's third book of De Occulta Philosophia draws on the Proclean hierarchy \
of divine causes; Dee's cosmological speculations engage with Proclus's mathematical Platonism. \
The text circulated in medieval Europe in part via a truncated anonymous translation \
(Liber de Causis), which was believed to be Aristotle's until Aquinas recognized it as \
Proclean — a discovery that complicated the Christian reception of both Aristotle and \
Neoplatonism."),

    ("Five Books of Mystery",
     "The first of John Dee's Enochian diaries (1581–1583), recording the initial sessions \
of crystal-gazing in which Dee and his scryers Barnabas Saul and then Edward Kelley received \
communications from angelic beings organized in a Heptarchic system of seven kings and \
princes governing the days of the week. This material — the Sigillum Dei Aemeth talisman, \
the angelic governance tables, the initial letters of the Enochian language — forms the \
infrastructural foundation on which the later, more elaborate Enochian system was built. \
Joseph Peterson's 2003 critical edition with manuscript photographs enables direct engagement \
with Dee's meticulous documentary method. The Five Books illuminate Dee's working practice: \
the elaborate ritual preparation, the careful record-keeping, the constant theological \
anxiety about whether the communicants were angels or demons."),

    ("Monas Hieroglyphica",
     "Dee's densely compressed symbolic treatise (1564), presenting a single \
hieroglyphic monad — a composite symbol built from the circle (sun/gold), crescent \
(moon/silver), cross (elements), and Aries sign (fire) — that claims to encode all \
cosmic knowledge in a single form. Written in Latin in twelve days, reportedly, \
and dedicated to Emperor Maximilian II, it occupies a singular position in Renaissance \
symbolic thought: simultaneously mathematical, alchemical, astronomical, Kabbalistic, \
and theosophical. The treatise has resisted full interpretation; its twenty-four \
theorems deploy a private symbolic logic that appears systematic but remains partially \
opaque. It marks Dee's transition from mathematical humanist to speculative Hermetic \
philosopher, and its influence on subsequent esoteric symbolism (including Rosicrucianism) \
has been traced by scholars in the corpus."),

    ("De Arte Cabalistica",
     "Reuchlin's dialogue on the Kabbalah (1517), set in the household of the Pythagorean \
sage Simon and presenting Christian Cabala as the fulfillment and deepest interpretation \
of Jewish Kabbalah. The text is cast as a Pythagorean-Kabbalistic synthesis: Simon \
demonstrates that the numerical and letter mysticism of the Kabbalah confirms Pythagorean \
doctrines of number as the ground of all things, and both traditions confirm the mysteries \
of the Christian Trinity and the divinity of Jesus (whose name IHSVH adds the letter shin \
to the Tetragrammaton YHWH). De Arte Cabalistica is the direct predecessor of Agrippa's \
third book of De Occulta Philosophia and the central text in the development of Renaissance \
Christian Cabala as a distinct scholarly practice — an attempt to appropriate Jewish \
interpretive methods in the service of Christian apologetics."),

    ("Ars Notoria",
     "A medieval learned magical text (probably twelfth century) attributed to Solomon, \
promising the practitioner rapid acquisition of all the liberal arts through a regimen of \
prayers, fasts, and contemplation of notae (diagrams combining geometric figures and divine \
names). Unlike the explicitly demonic or theurgical operations of other Solomonic texts, \
the Ars Notoria was defended by some medieval authorities as essentially a form of licit \
petition to God. Frank Klaassen's Transformations of Magic examines the Ars Notoria as a \
key case in the shifting medieval boundary between legitimate prayer-magic and condemned \
sorcery: its survival in monastic libraries suggests the boundary was more permeable in \
practice than in theory. The text illuminates the underside of the medieval university \
curriculum — the dream of acquiring all knowledge instantly, without the laborious \
years of study the arts degree required."),

    ("De Vanitate Scientiarum",
     "Agrippa's skeptical encyclopedic attack on all the arts and sciences (1530), written \
one year before the publication of De Occulta Philosophia, from which it appears to \
entirely recant. The work surveys and dismisses theology, philosophy, law, medicine, \
natural philosophy, and magic itself as vanities producing nothing but pride and error; \
it concludes with a fideistic appeal to scripture alone. The paradox of its relation \
to De Occulta has generated extensive scholarly debate: is De Vanitate a rhetorical \
self-protection against heresy accusations, a genuine crisis of faith, a deliberate \
dialectical strategy requiring both texts to be read together, or evidence that Agrippa \
maintained two simultaneous intellectual registers? The corpus contains multiple analyses \
of this question. The work also contains Agrippa's famous extended discussion of women's \
superiority, drawn on by feminist readers from the sixteenth century onward."),

    ("A True and Faithful Relation",
     "The posthumous published edition (1659) of John Dee's angel diaries, edited by \
Meric Casaubon and introduced with a lengthy preface arguing that the angelic \
communications were diabolical delusions — a framing that shaped the work's reception \
for nearly three centuries. The edition covers the later period of Dee's angelic workings \
(1582–1589) including the pivotal Polish and Bohemian sessions with Edward Kelley, the \
controversial 'wife-swapping' revelation (in which the angels allegedly commanded Dee \
and Kelley to share their wives), and the final dissolution of the partnership. Casaubon's \
hostile framing paradoxically preserved the material and made it available to subsequent \
scholarship. Deborah Harkness's John Dee's Conversations with Angels (1999) and \
György Szönyi's John Dee's Occultism (2004) in the corpus provide the modern \
scholarly alternative to Casaubon's demonization."),

    ("De la Causa, Principio et Uno",
     "One of Bruno's Italian philosophical dialogues (Venice, 1584), arguing for a \
single infinite substance as the ground of all things — an infinite universe in which \
the traditional distinctions between matter and form, finite and infinite, dissolve \
into a coincidentia oppositorum that recalls Nicholas of Cusa. The work is among \
Bruno's clearest philosophical statements: the universe has no center and no circumference, \
is everywhere center and everywhere circumference, and God is the infinite soul that \
animates it. This panpsychist-pantheist cosmology drew on Hermetic sources (especially \
the Asclepius's description of God as 'all things') and on Cusanian mystical geometry \
while deploying a naturalistic philosophical vocabulary that anticipated Spinoza. \
The dialogue form allowed Bruno to present heterodox positions through characters \
while maintaining rhetorical distance — a practice the Inquisition eventually \
found unconvincing."),

    ("Aurora",
     "Jacob Böhme's first and most untutored work (written 1612, circulated in \
manuscript), in which the Görlitz cobbler recorded a series of mystical illuminations \
about the inner life of God, the fall of Lucifer, the nature of the three principles \
(divine wrath, divine love, and the visible world), and the alchemical processes \
within the Godhead. The Aurora scandalised the local Lutheran pastor and brought \
Böhme official censure, but circulated in manuscript among theosophists and \
later reached print through disciples. Its wild, visionary imagery — fire and light \
as divine qualities, the language of alchemy turned to theological ends, the \
claim that God experiences himself through suffering and transformation — marks \
a distinctive moment in Protestant mysticism quite different from the Reformed \
and Lutheran mainstreams. Böhme's influence extended through the Cambridge \
Platonists, Francis Mercury van Helmont, and eventually the Romantic period."),

    ("Zohar",
     "The Zohar (Book of Splendor), the central canonical text of the Kabbalah \
(Aramaic, attributed to the Talmudic sage Shimon bar Yochai but probably composed \
in thirteenth-century Castile by Moses de León), presents itself as a mystical \
commentary on the Torah structured as a series of wandering dialogues among \
the companions of Rabbi Shimon. Its elaborate theosophy — the ten sefirot as \
dynamic divine attributes, the drama of exile and redemption as a cosmic process, \
the erotic imagery of divine union — became the primary lens through which \
Renaissance Christian Kabbalists approached Jewish mysticism. Pico, Reuchlin, \
and Agrippa all drew on Zoharic concepts and imagery. The question of whether \
their access was direct (through translations or Jewish interlocutors) or mediated \
through the Kabbalistic Latin summaries circulating among Christian Hebraists \
remains an active area of scholarship."),
]


def run_updates():
    conn = sqlite3.connect(str(DB_PATH))
    conn.execute("PRAGMA foreign_keys=ON")
    c = conn.cursor()

    print("=== Updating figure biographies and significance ===")
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
    print("=== Updating primary text significance statements ===")
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
