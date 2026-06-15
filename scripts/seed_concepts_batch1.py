"""Seed concepts table — Batch 1: Metaphysical Foundations (5 articles)."""

import sqlite3
import json
import sys
import io
from datetime import datetime

DB_PATH = "db/renmagic.db"

CONCEPTS = [
    {
        "slug": "neoplatonism",
        "title": "Neoplatonism",
        "category": "Metaphysical Foundations",
        "summary": "The philosophical tradition deriving from Plotinus (c. 204–270 CE) that posited a hierarchical universe emanating from a transcendent One, providing Renaissance thinkers with a framework for understanding magic, theurgy, and the soul's ascent to the divine.",
        "related_figures": ["Plotinus", "Marsilio Ficino", "Pico della Mirandola", "Proclus", "Iamblichus", "Giovanni Pico della Mirandola"],
        "related_concepts": ["emanation", "theurgy", "world-soul-anima-mundi", "the-one", "prisca-theologia", "cosmic-sympathy"],
        "body": """## Definition and Scope

Neoplatonism designates the philosophical tradition initiated by Plotinus of Lycopolis (c. 204–270 CE) and elaborated by his successors Porphyry (c. 234–c. 305), Iamblichus (c. 245–c. 325), and Proclus (412–485), among others. The term itself is a modern coinage, unknown to ancient practitioners who understood themselves simply as interpreters of Plato. In the context of Renaissance magic studies, Neoplatonism functions as both a historical phenomenon and a scholarly category: it describes a specific school of ancient philosophy transmitted to the Latin West through multiple channels, and it names a set of metaphysical commitments that shaped how educated practitioners in the fifteenth and sixteenth centuries understood the cosmos, the soul, and the efficacy of ritual action.

The significance of Neoplatonism for the history of Western esotericism cannot be overstated. As Wouter Hanegraaff has argued, much of what scholars identify as the "Western esoteric tradition" is intelligible only against the background of late antique Platonism, which provided the conceptual vocabulary—emanation, sympathy, theurgy, ascent, participation—through which later thinkers articulated claims about hidden connections, magical operations, and the soul's relationship to higher reality. To understand Renaissance Hermetism, Ficinian astral magic, Pico's Cabalist synthesis, or Bruno's mnemonic art, one must first understand the Neoplatonic universe in which they operate.

## The Plotinian System

Plotinus's philosophical system, preserved in the six *Enneads* edited by Porphyry, centers on three hypostases or primary principles: the One, Intellect (*Nous*), and Soul (*Psyche*). The One is absolutely simple, beyond being, thought, and predication—so transcendent that even the name "One" can only be applied analogically. From the One there "emanates" (a term Plotinus uses cautiously) Intellect, the realm of pure thought thinking itself and the locus of the Platonic Forms. From Intellect there emanates Soul, which governs the cosmos and produces individual souls. Matter stands at the lowest end of the hierarchy, not as evil in itself but as the furthest point of the emanative process, the darkness that results from the absence of the Good.

This hierarchical structure is not temporal—the One has not "created" the world at some point in time—but ontological: each level depends on the one above for its being, light, and goodness. The process of emanation (Greek *proodos*, "procession") is paired with *epistrophe*, "return" or "reversion," the tendency of each level to return to its source. For individual human souls, this means that the soul's ultimate good lies in turning away from matter and ascending toward Intellect and, ultimately, toward mystical union (*henosis*) with the One.

For the history of magic, what matters most is Plotinus's account of the mechanism of sympathy. In *Ennead* IV.4, Plotinus argues that the cosmos is a single living being animated by Soul, and that the parts of this being influence one another through sympathy (*sympatheia*) rather than through mechanical causation. This is why astrological influences are real and why certain material substances can affect others at a distance: they participate in the same cosmic life. Plotinus himself is ambivalent about magic—he thinks the wise person transcends it through philosophy—but his framework provides the metaphysical basis for later magical theories.

## Later Neoplatonism: Iamblichus and Proclus

Iamblichus of Chalcis introduced a crucial development that would prove decisive for Renaissance occultism: the elevation of theurgy. Where Plotinus believed philosophical contemplation sufficient for the soul's ascent, Iamblichus insisted on the necessity of ritual. In his *De Mysteriis* (probably early fourth century), he argues that the gods cannot be compelled by human intellect alone; rather, the practitioner must engage in specific ritual actions—sacrifices, the manipulation of sacred objects (*synthemata* or *symbola*)—through which the gods themselves act to lift the soul upward. The efficacy of theurgy does not depend on the practitioner's understanding but on the divine power inherent in the symbols themselves.

Proclus systematized Neoplatonism into a highly technical metaphysical scheme elaborated in the *Elements of Theology* and the *Platonic Theology*. His triadic scheme (remaining, procession, reversion) and his elaborate hierarchies of gods, henads, angels, daimones, and heroes provided the framework within which Renaissance thinkers like Ficino and Pico situated their own speculations. Proclus also wrote on magic, arguing in his *On the Hieratic Art* that the natural world contains divine *synthemata* that the theurgist can activate to establish contact with higher powers.

## Transmission to the Latin West

The Latin West received Neoplatonism through several channels. Calcidius's partial translation of Plato's *Timaeus* (fourth century) provided medieval thinkers with a Platonized cosmology. Macrobius's *Commentary on the Dream of Scipio* (early fifth century) transmitted Neoplatonic ideas about the soul's descent and ascent through the planetary spheres. Pseudo-Dionysius the Areopagite (probably early sixth century) fused Proclean hierarchiology with Christian theology, producing the *Celestial Hierarchy* and *Divine Names* that shaped medieval angelology and negative theology. Augustine's engagement with Neoplatonism, particularly his reading of the "Platonists" (probably including Plotinus and Porphyry), baptized certain Neoplatonic themes into Christian thought while rejecting theurgy as demonic.

The decisive moment for Renaissance Neoplatonism was Cosimo de' Medici's commission to Marsilio Ficino (1433–1499) to translate the *Corpus Hermeticum* (1463) and then the complete works of Plato, followed by translations of Plotinus, Porphyry, Iamblichus, and Proclus. Ficino's *Platonic Theology* (completed 1474, published 1482) constituted the first systematic Neoplatonic philosophy in the Latin West since late antiquity. His *Three Books on Life* (*De vita*) (1489) applied Neoplatonic principles to astral medicine and magic. Together these works established Neoplatonism as the dominant philosophical framework for educated discussions of magic in the Italian Renaissance.

## Neoplatonism and Renaissance Magic

Ficino's appropriation of Neoplatonism for magical purposes rested on three key moves. First, he identified Plato's *World Soul* (*anima mundi*) as the medium through which astral influences operated, making the cosmos itself a living, ensouled being susceptible to magical manipulation. Second, he adapted the Neoplatonic concept of *spiritus* (the pneumatic medium linking soul and body) as the mechanism through which celestial influences reached terrestrial matter, making astral magic a form of natural medicine. Third, he drew on Iamblichean and Proclean theurgy to argue that certain objects, songs, and suffumigations could attract planetary influences and thereby benefit the practitioner—while carefully insisting that this was natural magic, not demonic invocation.

Pico della Mirandola's Neoplatonism took a different turn: influenced by Elia del Medigo and other Jewish interlocutors, Pico fused Neoplatonic metaphysics with Kabbalah, arguing in the *Oration on the Dignity of Man* (1486) and the nine hundred *Conclusions* (1486) that the human being occupied a unique position in the cosmic hierarchy, capable of ascending through all levels of being. His Kabbalistic magic operated through Hebrew divine names rather than planetary images, but it presupposed the same Neoplatonic universe of hierarchical participation.

Later figures extended and transformed the Neoplatonic inheritance. Giovanni Francesco Pico della Mirandola (nephew of Giovanni) deployed Neoplatonism in a skeptical direction, arguing that the uncertainty of occult knowledge undermined magical claims. Cornelius Agrippa's *Three Books of Occult Philosophy* (1531) synthesized Ficinian astral magic with Pico's Kabbalah in a comprehensive Neoplatonic framework. Giordano Bruno took the Neoplatonic notion of an animated cosmos in the direction of an infinite universe of infinite worlds, each animated by a World Soul that was ultimately the same divine principle. Franciscus Patricius (Francesco Patrizi, 1529–1597) produced a rival "new philosophy" (*Nova de Universis Philosophia*, 1591) explicitly Neoplatonic in structure.

## Scholarly Interpretations

Frances Yates's influential thesis (*Giordano Bruno and the Hermetic Tradition*, 1964) treated Neoplatonism primarily as a vehicle for Hermetic religiosity, emphasizing the continuity between Hermetism, Neoplatonism, and the "magical worldview" she saw as a precondition of the Scientific Revolution. Later scholars have complicated this picture significantly. D.P. Walker (*Spiritual and Demonic Magic*, 1958) offered a more rigorous analysis of the specific mechanism of Ficinian magic, distinguishing carefully between natural and demonic operations. Brian Copenhaver has emphasized the textual and philological dimensions of Neoplatonic transmission, arguing that Ficino's magic cannot be understood apart from his specific engagement with the ancient texts he was translating.

Wouter Hanegraaff's *Esotericism and the Academy* (2012) and *Hermetic Spirituality and the Historical Imagination* (2022) have reframed the relationship between Neoplatonism and esotericism in terms of the "rejected knowledge" thesis: Neoplatonism, as recovered and transformed in the Renaissance, became associated with intellectual currents that Enlightenment rationalism subsequently marginalized. This framing allows Hanegraaff to treat Renaissance Neoplatonism not as a curiosity or precursor to something else but as a coherent intellectual tradition with its own internal logic and historical significance.

## Neoplatonism and the Modern Historiography

A persistent problem in the scholarship is the tendency to treat "Neoplatonism" as a unified or essential doctrine, obscuring the significant differences between Plotinus, Iamblichus, Proclus, Pseudo-Dionysius, and Ficino. In fact, what Renaissance thinkers received was an internally diverse tradition, selectively appropriated and often fundamentally transformed. Ficino's "Neoplatonism" is not Plotinus's: it has been Christianized, filtered through Latin intermediaries, and recombined with Hermetic and Kabbalistic materials in ways that ancient Neoplatonists would have found strange.

Scholars like Michael Allen have insisted on reading Ficino's Platonic commentary tradition with close attention to his ancient sources, revealing a more nuanced and philologically sophisticated engagement than the "magical worldview" thesis sometimes suggests. James Hankins has argued that Ficino's Platonism was primarily a philosophical and theological project, with magic playing a subordinate role. The debate between those who emphasize the continuity of Renaissance Neoplatonism with ancient sources and those who emphasize its transformations and novelties remains productive.

## Significance

Neoplatonism provided Renaissance occultism with its most sophisticated metaphysical language. The hierarchical cosmos of emanation and return, the animated World Soul, the doctrine of universal sympathy, the tradition of theurgic ritual—all of these were Neoplatonic contributions to the intellectual framework within which Renaissance magic made sense. At the same time, "Neoplatonism" is a scholarly construct that should be used with precision: it describes a diverse family of philosophical positions, not a single dogma, and its Renaissance appropriation was selective, creative, and often heterodox by ancient standards.

Understanding Renaissance magic without Neoplatonism is impossible. But understanding Neoplatonism requires attending to the specific texts, translations, commentaries, and polemics through which ancient philosophy reached early modern readers—a philological and historical task that remains at the center of current scholarship.
""",
    },
    {
        "slug": "natural-magic",
        "title": "Natural Magic (Magia Naturalis)",
        "category": "Magic Theory and Practice",
        "summary": "The Renaissance category distinguishing magic that worked through hidden but natural properties of things from demonic invocation, constituting the primary theoretical framework through which educated practitioners justified operational magic as legitimate natural philosophy.",
        "related_figures": ["Marsilio Ficino", "Cornelius Agrippa", "Giovanni Battista della Porta", "Pietro Pomponazzi", "Giambattista della Porta"],
        "related_concepts": ["occult-properties", "cosmic-sympathy", "astral-magic", "talismans", "spiritus-and-pneuma", "demonic-magic"],
        "body": """## The Category and Its Stakes

"Natural magic" (*magia naturalis*) was not a neutral description but a polemical distinction, deployed by Renaissance practitioners and theorists to carve out a space for legitimate magical operations against the charge of demonic involvement. The distinction between natural and demonic magic—magic working through the hidden properties of created things versus magic achieved through pacts with spirits—was a theological and philosophical battleground from late antiquity through the early modern period. What was at stake was not merely classification but the legitimacy of a wide range of practices: astrology, alchemy, the use of medicinal plants and stones, the making of images and talismans, and the manipulation of celestial influences through suffumigations and music.

As D.P. Walker demonstrated in *Spiritual and Demonic Magic from Ficino to Campanella* (1958), the boundary between natural and demonic magic was genuinely uncertain in early modern Europe. Theologians like Thomas Aquinas had argued that demons might be involved in operations that appeared purely natural; practitioners like Ficino insisted that their procedures engaged only the natural sympathies of the cosmos. The debate was never fully resolved—it is arguably what drives much of the period's anxious boundary-drawing—but the concept of natural magic provided the organizing framework within which the debate was conducted.

## Ancient Antecedents

The concept of natural magic has roots in ancient discussions of *sympatheia* (cosmic sympathy) and *occultae qualitates* (occult properties). Pliny the Elder's *Natural History* catalogued thousands of strange efficacies of plants, stones, and animals without invoking supernatural agents. Plutarch, Apuleius, and later Neoplatonists discussed the "sympathies and antipathies" of natural things as a legitimate subject of philosophical investigation. The Stoic concept of *pneuma* (breath, spirit) as the medium linking all parts of the cosmic body provided a physical basis for explaining how distant things could affect one another.

The term "magic" (*magia*, from Greek *mageia*, ultimately from the Persian *magi*) carried ambiguous connotations in antiquity—sometimes merely describing Persian religious practices, sometimes used as a term of abuse for illegitimate religious specialists. The construction of a "natural" magic distinguished from religion and from demonic practices was a specifically late antique and early modern achievement, requiring the elaboration of a cosmological framework in which hidden natural causes could explain effects that might otherwise seem miraculous.

## Ficino and the Founding Framework

Marsilio Ficino's *Three Books on Life* (*De vita libri tres*, 1489) constitutes the founding document of Renaissance natural magic in the full theoretical sense. The third book, *On Making Your Life Agree with the Sky* (*De vita coelitus comparanda*), argues that the scholar afflicted by Saturn's melancholic influence can attract the benign influences of Jupiter, Venus, and Sol through a carefully orchestrated program of music, diet, material substances, and physical environment.

Ficino's theoretical basis is Neoplatonic: the cosmos is animated by a World Soul (*anima mundi*), and the medium through which soul and body are connected is *spiritus*, a refined quasi-material substance. Celestial bodies, as higher members of the cosmic body, emit *spiritus* downward; terrestrial things that share in the nature of a particular planet can attract and concentrate that planet's influence. The practitioner who understands these correspondences can, through careful selection of foods, gems, plants, incense, and music, draw beneficial stellar *spiritus* into his own body.

Ficino is careful to insist that this is medicine, not magic—or rather, that it is the kind of magic Plato had in mind: natural manipulation of the hidden properties of things, not invocation of spirits. He explicitly distinguishes his procedures from "demonic" magic and invokes the authority of ancient philosophers (Plotinus, Porphyry, Proclus) who had discussed similar operations. Whether this disclaimer was sincere, strategically defensive, or both has been debated by scholars including Walker, Copenhaver, and Angela Voss.

## Porta and the Encyclopedic Tradition

Giovanni Battista della Porta's *Magia Naturalis* (1558, expanded 1589) represents the encyclopedic culmination of Renaissance natural magic. Porta defines natural magic as "the survey of the whole course of Nature" and proceeds through twenty books to discuss topics ranging from animal husbandry and cooking to optics, the magnet, distillation, invisible writing, and fireworks. The work is a miscellany of classical learning, practical experiment, and popular lore, held together by the organizing idea that hidden natural properties (*proprietates occultae*) underlie all observed effects.

Porta's natural magic is methodologically ambitious: he presents himself as a philosophical investigator of hidden causes, distinguishing his rational inquiry from vulgar credulity. The *Magia Naturalis* influenced subsequent natural philosophical writing, including Francis Bacon, who retained the concept of natural magic while stripping away its Neoplatonic metaphysics in favor of a more Baconian experimental program. For Bacon, natural magic in its reformed version would become what we now call applied science: the practical application of knowledge of hidden causes.

## Cornelius Agrippa's Synthesis

Cornelius Agrippa von Nettesheim's *Three Books of Occult Philosophy* (*De occulta philosophia*, written c. 1510, published 1531) systematized natural magic within a comprehensive hierarchical framework. Agrippa divided magic into three domains corresponding to three levels of the cosmos: natural magic (elemental level), celestial magic (astral level), and ceremonial or divine magic (intellectual/spiritual level). Each level had its own objects, procedures, and principles.

At the level of natural magic, Agrippa drew on the Stoic and Neoplatonic traditions to explain how hidden properties of plants, stones, and animals arose from their participation in cosmic sympathies and the influence of heavenly bodies. He catalogued the sympathies and antipathies of natural things, the virtues of stones (drawing on Albertus Magnus and the lapidary tradition), and the medicinal and magical uses of plants. His framework was explicitly philosophical: natural magic was legitimate natural philosophy conducted at the level of elemental nature, preparatory to higher operations.

The three-book structure of Agrippa's work reflects a commitment to distinguishing levels of magic that were often conflated in more vulgar treatments. By providing a philosophical framework that grounded natural magic in legitimate cosmological principles, Agrippa attempted to rehabilitate the entire magical tradition against charges of demonic involvement.

## Pietro Pomponazzi and the Naturalist Challenge

An important but often overlooked contribution to the theory of natural magic came from the Aristotelian philosopher Pietro Pomponazzi (1462–1525), whose *De naturalium effectuum causis sive de incantationibus* (*On the Causes of Natural Effects or on Incantations*) (written c. 1520, published 1556) argued that all apparently miraculous effects attributed to demons, angels, or saints could in principle be explained through occult natural causes, specifically through stellar influences.

Pomponazzi's position was more radically naturalist than Ficino's: where Ficino had retained a genuinely spiritual dimension in his magic, Pomponazzi reduced all extraordinary effects to the operation of natural, if hidden, celestial causes. This move was theoretically uncomfortable for orthodox theology (which needed miracles to be genuinely supernatural) and practically uncomfortable for practitioners of ceremonial magic (who could not invoke spirits if spirits had no causal role). But Pomponazzi's naturalism established an influential pole in debates about natural magic: the position that all apparently magical effects were in principle explicable through natural causes, without any supernatural supplement.

## The Demonic Boundary Problem

The persistent difficulty of natural magic as a category was that its boundary with demonic magic was unstable. Thomas Aquinas had argued that the occult properties of things were themselves caused by incorporeal substances (demons or angels); thus even apparently natural magic might involve demonic assistance without the practitioner's knowledge. This argument was regularly deployed by critics of natural magic, including some of the most sophisticated theologians of the period.

Practitioners responded with various strategies. Ficino insisted that his procedures were continuous with legitimate Galenic medicine and astrological prediction. Agrippa appealed to the authority of ancient philosophers who had discussed similar operations in natural philosophical terms. Porta foregrounded his empirical methodology and his membership in learned academies. None of these strategies fully resolved the problem, because the underlying metaphysical question—whether hidden natural properties were self-sufficient or required the mediation of spirits—remained contested.

The category of natural magic was also threatened from below, by popular traditions of folk healing, cunning craft, and village magic that practitioners and theorists wished to distinguish from their own philosophically respectable activity. Keith Thomas's *Religion and the Decline of Magic* (1971) documented the vast range of practical magic in early modern England, showing that educated natural magic was one strand in a much larger and messier social fabric. The attempts by educated practitioners to distinguish "natural magic" from vulgar superstition were as much social as philosophical acts.

## Decline and Transformation

The concept of natural magic did not simply disappear with the Scientific Revolution. As William Eamon (*Science and the Secrets of Nature*, 1994) has argued, natural magic and early modern experimental science shared important features: both were concerned with "secrets of nature," both valued practical efficacy as a test of theoretical claims, and both drew on similar traditions of learned empiricism. Bacon's reformed natural magic, Newton's alchemy, and the experimental program of the early Royal Society all bear traces of the natural magic tradition, even as they transformed it.

What changed in the seventeenth century was less the content of natural magic than its epistemological and institutional status. The mechanical philosophy, by insisting that all natural causation was explicable through matter and motion, delegitimized the category of "occult properties" on which natural magic depended. Once hidden properties could no longer be admitted as basic explanatory categories, the theoretical framework of natural magic collapsed—even as many of its specific practices (herbal medicine, mineral remedies, experimental investigation of unusual phenomena) continued under different descriptions.

## Scholarly Assessment

The historiography of natural magic has moved from Yates's grand narrative of the "magical worldview" as a precursor to modern science to more granular accounts attentive to specific texts, institutions, and practices. Brian Copenhaver has argued for careful attention to the specific ancient sources—Porphyry, Iamblichus, Proclus—that shaped Ficino's theoretical framework. Stuart Clark's *Thinking with Demons* (1997) placed demonology at the center of early modern intellectual culture, showing how the demonic/natural distinction organized a wide range of discourses. Liana Saif's work on Arabic influences has complicated the picture of natural magic's intellectual genealogy, showing that the "occult sciences" were transmitted to Europe through a complex Islamic and Jewish intermediary tradition.

Natural magic is best understood not as a stable doctrine but as a contested category: a discursive space in which educated early modern practitioners negotiated between the demands of Christian theology, ancient philosophical authority, practical experience, and social legitimacy. Its history is the history of those negotiations.
""",
    },
    {
        "slug": "hermetism",
        "title": "Hermetism and Hermeticism",
        "category": "Hermetic Tradition",
        "summary": "The term pair introduced by Antoine Faivre and developed by Wouter Hanegraaff to distinguish the ancient philosophical-religious tradition of the Hermetic texts (Hermetism) from the broader currents of Western esotericism inspired by them (Hermeticism), a distinction central to current historiographic debates about the nature and boundaries of the field.",
        "related_figures": ["Marsilio Ficino", "Giordano Bruno", "Giovanni Pico della Mirandola", "Isaac Casaubon", "Wouter Hanegraaff"],
        "related_concepts": ["prisca-theologia", "neoplatonism", "gnosis", "emanation", "the-yates-thesis"],
        "body": """## The Terminological Problem

In current scholarship, "Hermetism" and "Hermeticism" function as a crucial analytical pair, a distinction that bears significant methodological weight. "Hermetism" designates the specific philosophical and religious tradition of the *Corpus Hermeticum* and related texts—a body of writings attributed to Hermes Trismegistus ("Thrice-Greatest Hermes"), composed in Greek and Coptic in Roman Egypt roughly between the first and third centuries CE. "Hermeticism" designates the much broader tradition of reception, transformation, and appropriation of Hermetic texts and ideas across subsequent centuries, including Renaissance Neoplatonism, early modern esotericism, Theosophy, and contemporary alternative spirituality.

The terminological distinction was formalized in the work of Antoine Faivre and has been central to the ongoing effort to define "Western esotericism" as a legitimate field of academic inquiry. Wouter Hanegraaff's recent work, particularly *Hermetic Spirituality and the Historical Imagination* (2022), has substantially revised earlier accounts by returning to close textual analysis of the original Hermetic sources and asking what their philosophical content actually was—rather than what later readers made of them.

## The Hermetic Corpus: Content and Context

The texts now called the *Corpus Hermeticum* are a diverse collection of Greek-language dialogues and treatises, composed over several centuries and united by attribution to Hermes Trismegistus—a synthetic figure combining the Greek god Hermes with the Egyptian god Thoth, understood by ancient readers as an Egyptian sage of extreme antiquity. The most important is *Poimandres* (CH I), a cosmogonic vision in which a divine figure reveals to the narrator the origin of the cosmos and the fall and possible redemption of the human soul. Other treatises discuss the nature of God, the cosmos, mind (*nous*), and the soul's ascent through the planetary spheres.

The original social and institutional context of these texts is uncertain. They were not a single school's product but a loose collection emerging from a religiously diverse Hellenistic-Egyptian milieu in which Platonism, Stoicism, Egyptian religion, Jewish thought, and nascent Christianity all circulated and interacted. The discovery of a Coptic Hermetic text (*Discourse on the Eighth and Ninth*) at Nag Hammadi in 1945 confirmed that some form of organized Hermetic practice—possibly ritual or initiatory in character—existed in late antique Egypt. Brian Copenhaver's authoritative translation and commentary (*Hermetica*, 1992) established the scholarly consensus that the Hermetic texts were neither Egyptian esoteric wisdom from pharaonic times nor simple literary fictions, but genuine products of a pluralist intellectual culture.

The Hermetic texts include both "learned" or "philosophical" Hermetica (concerned with cosmology, theology, and the soul's fate) and "technical" Hermetica (concerned with astrology, alchemy, medicine, and magic). The *Asclepius*, preserved in a Latin translation attributed (probably falsely) to Apuleius of Madaura, contains a famous description of Egyptian statue animation (*animatio*) that was of great interest to later theorists of talismanic magic.

## The Renaissance Reception: Ficino and the *Corpus Hermeticum*

The decisive moment for Hermeticism in the Latin West was Marsilio Ficino's translation of the *Corpus Hermeticum* in 1463. Cosimo de' Medici, having acquired a manuscript of the Greek texts from a monk named Leonardo of Pistoia, instructed Ficino to translate them before completing his translations of Plato—an index of how highly the Hermetic texts were valued. Ficino's translation, the *Pimander* (1471), made the Greek Hermetic dialogues available to Latin readers for the first time.

Ficino, following the view current in his time, believed the texts to be of extreme antiquity—the product of an Egyptian sage who had lived before Moses and anticipated Christian theological truths. This belief in the prisca theologia, the "ancient theology" transmitted through a chain of prisci theologi (Zoroaster, Hermes, Orpheus, Pythagoras, Plato), gave the Hermetic texts enormous authority: they were not recent compositions but ancient wisdom recently recovered.

This dating was accepted by virtually all Renaissance readers of the Hermetic texts. It was demolished in 1614 by Isaac Casaubon (*De rebus sacris et ecclesiasticis exercitationes XVI*), who demonstrated on philological grounds—vocabulary, style, and the texts' evident dependence on later Greek philosophical sources—that the *Corpus Hermeticum* could not have been composed before the Christian era. Casaubon's demonstration did not immediately destroy interest in the texts (Frances Yates observed that many readers simply refused to accept it), but it fundamentally altered their status: they were now documents of late antiquity, not ancient Egypt.

## Hermetism as a Scholarly Category

Hanegraaff's *Hermetic Spirituality* proposes a more radical reorientation: rather than treating the Hermetic texts primarily as vectors for ideas later readers would find significant, he asks what the texts themselves were trying to do on their own terms. His analysis, drawing on close reading of the Greek and Coptic texts, identifies a consistent concern with what he calls "spiritual practice"—a form of philosophical contemplation and visionary experience aimed at transforming the practitioner's mode of consciousness and enabling contact with divine reality.

This approach distinguishes "Hermetism" from its various later appropriations. Renaissance Hermeticism, as Ficino and his successors understood it, was primarily a philosophical theology: the Hermetic texts confirmed the antiquity of Platonic and Christian teaching and provided authority for natural magic. It was less interested in the experiential and spiritual dimensions of the original texts than in their cosmological and theological content. Seventeenth-century Hermeticism—associated with figures like Robert Fludd and Henry Khunrath—combined Hermetic motifs with Paracelsian medicine, Rosicrucianism, and Christian Kabbalah in ways that the ancient texts' authors would presumably have found unrecognizable.

The implication is that "Hermeticism" is not a stable tradition with continuous content but a succession of reception events, each of which appropriates the Hermetic texts for new purposes in new contexts. What unites them is not doctrinal continuity but the authoritative status of "Hermes Trismegistus" as a source of ancient wisdom—a prestige that could be projected onto widely different intellectual projects.

## The Yates Thesis and Its Aftermath

Frances Yates's *Giordano Bruno and the Hermetic Tradition* (1964) argued that Hermeticism—specifically, the belief in the reality of magical and spiritual operations grounded in Hermetic philosophy—was a significant cause of the Scientific Revolution. The "Hermetic tradition" in Yates's account was a unified intellectual current running from Ficino through Bruno to figures like John Dee and early seventeenth-century natural philosophers. By placing magic and natural philosophy in a single genealogy, Yates challenged the sharp distinction between "science" and "magic" that had structured earlier historiography.

Yates's thesis generated enormous scholarly debate. Critics (including Paolo Rossi, Brian Vickers, and later Nicholas Jardine) argued that she had overstated the continuity between Hermetic magic and the new natural philosophy, that her connections were often based on superficial resemblances, and that she had neglected the mathematical and institutional dimensions of the Scientific Revolution that had nothing to do with Hermeticism. The current consensus, articulated by figures like Copenhaver, is that Hermeticism was one significant element in the cultural context of early modern natural philosophy but not its primary cause—and that the category of "Hermeticism" as Yates defined it may be too broad to be analytically useful.

## The Technical Hermetica

A dimension of Hermetism that has received less attention in mainstream Renaissance scholarship is the body of technical Hermetic texts concerned with astrology, alchemy, medicine, and magic. These include the *Liber Hermetis* (on astrology), various alchemical texts attributed to Hermes, and numerous magical texts invoking Hermetic authority. Liana Saif's research on Arabic Hermetica (*The Arabic Influences on Early Modern Occult Philosophy*, 2015) has shown that a substantial body of technical Hermetic material was transmitted to Europe through Arabic intermediaries, often in substantially transformed form, and that this Arabic-mediated Hermetism played an important role in shaping the Western occult sciences that is not captured by focusing exclusively on the Greek *Corpus Hermeticum*.

The *Picatrix* (Arabic *Ghāyat al-ḥakīm*, "The Goal of the Wise"), a comprehensive astrological magic manual composed in Arabic around the tenth or eleventh century and translated into Latin in 1256, draws heavily on Hermetic authority for its theory of talisman-making. The *Picatrix* was one of the most important magical texts of the medieval and Renaissance West, yet its relationship to the learned Greek Hermetism of the *Corpus Hermeticum* is complex and indirect.

## Hermetism, Egypt, and Colonial Historiography

Recent scholarship has raised questions about the "Egyptian" dimension of Hermetic tradition. The ancient Hermetic texts present their wisdom as Egyptian, but they are written in Greek and their ideas are largely Greek philosophical in content. The figure of Hermes Trismegistus is a Greco-Egyptian hybrid. When Renaissance thinkers celebrated the recovery of "Egyptian wisdom," what exactly were they celebrating?

Erik Iversen's *The Myth of Egypt and Its Hieroglyphics in the European Tradition* (1961) and subsequent scholarship have documented the persistent European fantasy of Egypt as the source of primordial wisdom—a fantasy that projected European intellectual preoccupations onto a largely imaginary ancient Egypt. More recent postcolonial approaches have asked how this fantasy functioned ideologically, what it displaced or ignored in actual Egyptian religious and intellectual traditions, and how the authority of "Egyptian" Hermetism related to broader European attitudes toward the non-European world.

## Current State of the Field

The scholarship on Hermetism and Hermeticism has been substantially transformed over the past thirty years by philological rigor (Copenhaver's edition and translation of the *Corpus Hermeticum*, Mahe's work on the Coptic texts), by the professionalization of Western esotericism as a field (Hanegraaff, Faivre, von Stuckrad), and by the expansion of interest to include Islamic and Jewish intermediary traditions (Saif, Burnett). The current consensus resists both the reduction of Hermeticism to a mere historical curiosity and the over-inflation of its role as the secret cause of modern science.

Hermetism—the specific ancient tradition of the *Corpus Hermeticum*—is now understood as a product of Hellenistic religious and philosophical culture, with its own sophisticated theology and spiritual practice. Hermeticism—the tradition of its reception—is understood as a series of transformative appropriations, each shaped by the specific needs and contexts of its recipients, united by the prestige of the name "Hermes Trismegistus" rather than by doctrinal continuity.
""",
    },
    {
        "slug": "prisca-theologia",
        "title": "Prisca Theologia",
        "category": "Metaphysical Foundations",
        "summary": "The Renaissance doctrine of an 'ancient theology' transmitted through a chain of primordial sages (Zoroaster, Hermes, Orpheus, Pythagoras, Plato) that anticipated Christian truth, providing ideological justification for the recovery and use of ancient magical and philosophical texts.",
        "related_figures": ["Marsilio Ficino", "Pico della Mirandola", "Giorgio Gemistos Plethon", "Agostino Steuco"],
        "related_concepts": ["hermetism", "neoplatonism", "philosophia-perennis", "syncretism"],
        "body": """## The Concept

Prisca theologia—"ancient theology" or "primordial wisdom"—denotes the Renaissance belief in a primordial divine revelation transmitted through a chain of ancient sages, reaching from the earliest figures of human history down through Pythagoras and Plato to Christianity. The doctrine held that these sages—variously identified as Zoroaster, Hermes Trismegistus, Orpheus, the Sibyls, Pythagoras, and Plato—had received or discovered fundamental theological and cosmological truths that anticipated and confirmed Christian teaching, however imperfectly or in figurative form.

The significance of this concept for the history of Renaissance magic is considerable. By positing that ancient philosophical and magical texts contained genuine primordial wisdom rather than mere pagan superstition, the prisca theologia doctrine provided ideological justification for the recovery and serious intellectual use of texts that Christian tradition had often condemned or ignored. Ficino could translate the *Corpus Hermeticum* and read Plotinus not as ventures into dangerous paganism but as recovery of a pre-Christian revelation that Christian theology had always been destined to fulfill.

## Origins and Precedents

The idea that ancient pagan wisdom was preparatory for or consistent with Christian truth has Christian precedents stretching back to Justin Martyr (second century) and Clement of Alexandria, who argued that Greek philosophy was a preparation for the Gospel analogous to the Jewish Law. Augustine acknowledged that "the Platonists" (probably including Plotinus) had come close to Christian truth, while condemning their theurgy. The widespread medieval practice of finding allegorical anticipations of Christian truth in pagan poets (especially Virgil's Fourth Eclogue) rested on similar assumptions.

What was novel in Renaissance prisca theologia was the specific identification of a prisca theologia chain, the recovery of new texts that extended this chain, and the consequent heightening of authority accorded to ancient non-Christian sources. This was connected to the broader Renaissance project of *translatio studii*—the westward translation of wisdom—and to humanist historiography, which viewed Greek and Roman antiquity as a repository of wisdom that the intervening medieval centuries had obscured.

## Ficino and the Golden Chain

Marsilio Ficino's preface to his translation of the *Corpus Hermeticum* (1463) articulates the canonical Renaissance account of the prisca theologia. Ficino identifies a succession of ancient theologians (*prisci theologi*): Zoroaster first, then Hermes Trismegistus, Orpheus, Aglaophamus, Pythagoras, and Plato. Each transmitted the same fundamental wisdom, clothed in different cultural forms and with varying degrees of clarity. The Hermetic texts, which Ficino dated to the time of Moses (or even earlier), were thus doubly authoritative: they were ancient, and they were consistent with Platonic and Christian truth.

This framework had enormous practical consequences. It meant that the cosmological teachings of the *Timaeus*, the religious philosophy of Plotinus, the ritual prescriptions of Iamblichus, and the cosmogonic narratives of the *Corpus Hermeticum* could all be read as complementary expressions of a single perennial wisdom. The contradictions and tensions among these sources could be minimized or allegorized away; what mattered was the underlying unity of truth they variously expressed.

Ficino's prisca theologia was also apologetic: by demonstrating that Platonic philosophy anticipated Christian teaching, he could argue for the compatibility of ancient philosophy with Christian faith—defusing objections to his engagement with pagan sources and making his Neoplatonic theology intellectually safe for Christian readers.

## Pico della Mirandola's Extension

Giovanni Pico della Mirandola extended the prisca theologia doctrine by adding Kabbalah to the chain of ancient wisdom. In his nine hundred *Conclusions* (1486) and the associated *Oration on the Dignity of Man*, Pico argued that the Jewish mystical tradition, properly understood, confirmed the same fundamental truths as Platonic philosophy and Christian theology. He added Moses, the Sibyls, and the Kabbalistic tradition to the lineage of primordial wisdom-keepers.

Pico's inclusion of Kabbalah had significant implications. It meant that the Hebrew scriptures and their mystical commentaries could be read not as preparatory figures for Christianity (the standard Christian typological reading) but as direct transmissions of the same primordial revelation—on the same plane of authority as Plato and Hermes. This elevation of Jewish mystical sources was controversial and contributed to the papal condemnation of several of Pico's theses.

## Agostino Steuco and Philosophia Perennis

The prisca theologia doctrine was given its most systematic treatment by Agostino Steuco (1497–1548) in his *De perenni philosophia* (1540), the text that introduced the concept of philosophia perennis (perennial philosophy) to Western thought. Steuco argued, on the basis of wide reading in Greek, Latin, Hebrew, and Arabic sources, that a single philosophical and theological tradition underlay the diversity of ancient wisdom—a tradition he traced from Adam through Noah and the dispersal of primordial knowledge to various peoples, who received and transmitted it in culturally specific forms.

Steuco's erudition was genuine, and his work represents one of the more rigorous Renaissance attempts to demonstrate the unity of ancient wisdom. But his methodology was fundamentally confirmatory rather than analytical: he assembled ancient sources and read them as converging on Catholic Christian teaching, finding the same truth everywhere he looked. The circularity of this procedure—assuming what was to be demonstrated—was not yet recognized as a methodological problem.

## The Prisca Theologia and Magical Authority

For the practical purposes of magical and occult philosophy, the prisca theologia doctrine functioned primarily as an authority-granting mechanism. Ancient texts gained their authority precisely from their antiquity: the closer a text stood to the primordial revelation, the more authoritative it was. This meant that texts which could claim extreme antiquity—the *Corpus Hermeticum*, the Chaldean Oracles, the Orphic Hymns—were especially valuable as sources for magical and philosophical speculation.

Cornelius Agrippa's *Three Books of Occult Philosophy* (1531) explicitly situates its magical theory within the prisca theologia framework, citing Hermes, Zoroaster, Orpheus, Pythagoras, and Plato as ancient authorities for magical practices. The authority of his magical system depends partly on this lineage: natural magic, celestial magic, and ceremonial magic are presented as rediscoveries of ancient wisdom, not as novel inventions.

The authority granted by prisca theologia was, however, double-edged. If the prisma theologia chain authenticated certain texts and practices, it also implicitly constrained them: legitimate magic was magic that could be traced to this chain of ancient wisdom-keepers. Magic that could not establish such genealogy was more vulnerable to charges of demonic involvement or vulgar superstition.

## Casaubon's Demolition

Isaac Casaubon's philological demonstration in 1614 that the *Corpus Hermeticum* was not of Egyptian antiquity but a composition of the early Christian centuries struck directly at the prisca theologia doctrine. If Hermes Trismegistus had not preceded Plato and Moses but had written after them—and had in fact drawn on Platonic and Stoic sources—then the entire genealogy of primordial wisdom was disrupted. The *Corpus Hermeticum* could no longer serve as a pre-Platonic source; it was a post-Platonic composition, its "anticipation" of Platonic and Christian themes explained by dependence rather than by prisca theologia.

Casaubon's argument was widely accepted among scholars—though, as Frances Yates observed, it did not immediately end interest in the Hermetic texts among those with less investment in philological accuracy. What it did do was permanently undermine the specific form of the prisca theologia doctrine that rested on the antiquity of the Hermetic texts. Later versions of perennial philosophy (from Leibniz through Aldous Huxley and beyond) generally abandoned the specific claim of primordial historical transmission in favor of a more abstract claim about the universal convergence of religious and philosophical traditions.

## Legacy and Scholarly Assessment

The prisca theologia doctrine was a historically significant but intellectually fragile construction, dependent on false chronology and circular interpretive methods. Its significance for the history of Renaissance magic is not as a doctrine worth endorsing but as an ideological framework that shaped the period's engagement with ancient texts. By granting extreme antiquity to the *Corpus Hermeticum*, the Chaldean Oracles, and the Orphic poems, it gave humanist scholars permission to take these texts seriously as philosophical and spiritual sources—with consequences for the history of natural philosophy, theology, and occult practice that persisted well into the seventeenth century.

Scholars have debated whether prisca theologia was primarily a theological strategy (demonstrating the universality of Christian truth), a philosophical strategy (providing authority for Platonic and Neoplatonic philosophy), or a magical strategy (granting authority to ancient magical texts and practices). The answer is probably all three simultaneously, which is part of why the concept was so productive and so durable despite its empirical fragility.
""",
    },
    {
        "slug": "emanation",
        "title": "Emanation",
        "category": "Metaphysical Foundations",
        "summary": "The Neoplatonic cosmological concept describing how lower levels of reality flow necessarily from higher ones without diminishing their source, providing Renaissance magic with its fundamental account of how celestial and divine powers reach the terrestrial world and can be tapped by the skilled practitioner.",
        "related_figures": ["Plotinus", "Marsilio Ficino", "Proclus", "Pseudo-Dionysius the Areopagite"],
        "related_concepts": ["neoplatonism", "the-one", "world-soul-anima-mundi", "cosmic-sympathy", "theurgy", "chain-of-being"],
        "body": """## The Concept

Emanation (*aporroia* in Greek, sometimes *proodos* or "procession"; Latin *emanatio* or *processio*) is the Neoplatonic metaphysical concept describing the necessary and eternal outflowing of lower levels of reality from higher ones. Unlike creation ex nihilo—where a divine will produces something that previously did not exist, at a moment in time, by a deliberate act—emanation is atemporal, necessary, and does not diminish the source. The sun, a standard Neoplatonic analogy, continuously gives off light without thereby losing its luminosity; the One continuously gives off being, life, and intelligence without thereby becoming less.

For the history of Renaissance magic, emanation is foundational: it explains how the divine communicates itself to the world, how celestial influences reach terrestrial matter, and how the skilled practitioner might work "upward" through the hierarchy of being to access higher powers. The magical theory of Ficino, Agrippa, Bruno, and their contemporaries is unintelligible without the Neoplatonic concept of emanation as its cosmological backbone.

## Plotinus's Account

Plotinus's fullest treatment of emanation appears across multiple *Enneads*, particularly V.1 (*On the Three Primary Hypostases*) and V.2 (*On the Origin and Order of the Things After the First*). His central claim is that the One—absolutely simple, beyond being and thought—necessarily generates or "overflows" into Intellect (*Nous*), not through choice or will (which would imply multiplicity within the One) but necessarily, as a consequence of the One's superabundant perfection. Intellect, in turn, generates Soul; Soul generates the material cosmos.

Each level of the hierarchy stands in a double relationship to its source: *proodos* (procession, the flowing forth of the lower from the higher) and *epistrophe* (return or reversion, the inclination of the lower toward the higher from which it came). This double movement—procession and return—is the dynamic structure of Neoplatonic reality. Nothing in the hierarchy simply exists statically; everything is involved in an eternal double movement of derivation and aspiration.

A crucial feature of Plotinian emanation is that each level contains, in a diminished and mediated way, what the level above it contains more fully. Intellect contains the Forms that the One transcends; Soul contains the life that Intellect thinks in abstraction; material nature participates in the beauty and goodness that are more fully present above it. This "participation" (*methexis*) is the ontological relationship between levels: lower things exist insofar as and in the way that they participate in higher realities.

## Iamblichus and Proclus: Elaborations

Iamblichus and Proclus significantly elaborated the emanative hierarchy. Where Plotinus had three hypostases (One, Intellect, Soul), later Neoplatonists multiplied the levels: Proclus posited multiple orders of gods, henads, angels, daimones, and heroes between the One and material nature. Each level has its own characteristic properties and its own relationship to the levels above and below it.

For the purposes of magic, the elaborated hierarchy of Iamblichus and Proclus was especially productive. If each level of the hierarchy contained in diminished form what the level above possessed more fully, and if divine powers were present throughout the hierarchy in the form of *synthemata* or *symbola* (divine signatures or tokens), then the practitioner who knew how to identify and activate these tokens could establish contact with higher levels of the hierarchy through material means. This is the theoretical basis of Iamblichean theurgy.

Proclus's *Elements of Theology* articulated the structure of the emanative hierarchy in a series of numbered propositions, providing a systematic framework that Renaissance thinkers could draw on directly. Ficino translated Proclus's work and drew on it extensively in the *Platonic Theology*.

## Pseudo-Dionysius and Christian Emanationism

The most influential Christian adaptation of Neoplatonic emanation was that of the writer known as Pseudo-Dionysius the Areopagite (probably early sixth century), who fused Proclean hierarchiology with biblical theology to produce a Christian cosmology of graduated divine illumination. For Pseudo-Dionysius, God (identified with the Plotinian One) communicates himself to creation through a descending hierarchy of angels, each order receiving divine illumination from the one above and passing it on, in diminished form, to the one below, until it reaches humanity and material creation.

This Christian adaptation preserved the Neoplatonic structure of emanation while reinterpreting it in terms of divine grace: what flows from the One is now divine goodness, illumination, and being, communicated as God's free gift rather than as necessary overflow. Pseudo-Dionysius's *Celestial Hierarchy* and *Ecclesiastical Hierarchy* shaped medieval Christian thought about angels, the Church, and the sacraments in ways that persisted into the Renaissance.

## Ficino and Magical Emanationism

Marsilio Ficino's magical theory in *De vita coelitus comparanda* (1489) rests directly on a model of emanation. The World Soul (*anima mundi*) pervades the cosmos and communicates the forms and influences of the celestial bodies downward to material nature, using *spiritus mundi*—a refined, quasi-material medium—as the vehicle of transmission. Terrestrial things that "correspond" to celestial bodies (Sol-natured plants like heliotrope, Saturn-natured stones like lead, Jupiter-natured herbs like melissa) have received a concentrated dose of that planet's emanated influence during their formation.

The practitioner who understands these correspondences can deliberately concentrate and attract beneficial planetary influences by surrounding himself with objects attuned to the desired planet—Sol-natured things for vitality and cheerfulness, Venus-natured things for pleasure and attraction, Jupiter-natured things for governance and reason. This is not mechanical causation but participatory: the Sol-natured objects participate more fully in Solar emanation, and by surrounding himself with them the practitioner raises his own participation in Solar goodness.

What is crucial here is that the operative mechanism is *descending* emanation: planetary influences flow downward from the celestial spheres through *spiritus* to terrestrial matter. The practitioner does not project magical power but rather positions himself optimally to receive what is continually flowing down. This has important implications for the ethics and theology of magic: Ficino can insist that he is not compelling celestial powers but simply availing himself of naturally available influences, as a farmer avails himself of sunlight and rain.

## Emanation and the Ascent of the Soul

The other direction of the emanative structure—the return or *epistrophe*—is equally important for understanding Renaissance magic and philosophy. If souls have descended into material existence through the planetary spheres, acquiring the qualities of each sphere as they pass through it, then philosophical and spiritual practice involves reversing this descent: stripping away the planetary accretions, ascending through the spheres, and returning to the divine source.

This ascent narrative appears throughout the Hermetic texts (most explicitly in *Corpus Hermeticum* I and XIII), in Neoplatonic philosophy (Plotinus's account of the soul's ascent to the One in *Ennead* VI.9), and in late antique religious practice (Mithraic grade initiations, Gnostic soul-ascent). In the Renaissance, it shaped theurgic interpretations of ceremonial magic (as a form of ritual ascent), alchemical interpretations of the Great Work (as a spiritual ascent through materia to gold/divinity), and Cabalistic interpretations of meditation on the Sefirot (as an ascent through the divine attributes to *Ein Sof*).

## Emanation and the Problem of Evil

A persistent philosophical problem for emanationist cosmologies is the status of matter and evil. If reality emanates necessarily from the Good, and if each level participates in the goodness of the levels above it, how does evil arise? Plotinus's answer—that matter is the "limit" of emanation, the point of maximum privation of being and good, but not itself an independent principle of evil—was influential but not universally accepted. Dualist alternatives, including Gnostic traditions that posited an evil Demiurge responsible for material creation, offered a competing account.

For Renaissance magical theory, this question had practical implications. If matter was evil or contaminated by an evil creative principle, then magic operating through material means was tainted from the outset. Ficino's Neoplatonism, following Plotinus, held that matter was not evil in itself but only the most attenuated degree of good—hence material magic was not in principle contaminated. But critics of talismanic and image magic could appeal to the suspicion that material operations necessarily involved demonic mediation, since matter was too low to reach the divine directly.

## Emanation in Islamic and Jewish Philosophy

The concept of emanation was not exclusively Neoplatonic or Christian; it was also central to medieval Islamic and Jewish philosophy in ways that shaped Renaissance occultism through intermediary channels. Al-Farabi's and Ibn Sina's (Avicenna's) account of the cosmic intellects, derived from Aristotelian active intellect theory but developed in a Neoplatonic direction, described a hierarchy of emanated intelligences governing the celestial spheres—an account that influenced both Islamic and Hebrew occult philosophy.

The Kabbalistic concept of the *Sefirot*—ten divine attributes or powers through which *Ein Sof* (the Infinite) communicates itself to creation—has significant structural parallels with Neoplatonic emanation, though the historical relationships between Neoplatonism and early Kabbalah remain contested. In the Renaissance, Pico della Mirandola and subsequent Christian Kabbalists regularly assimilated the Sefirot to Neoplatonic hypostases and Pseudo-Dionysian angelic orders, treating them as different cultural expressions of the same emanative structure.

## Scholarly Significance

Emanation as a concept illuminates several persistent features of Renaissance magical theory: the claim that magic works "through" nature rather than against it; the insistence that higher powers are continuously available to those who know how to receive them; the aspiration toward spiritual ascent through disciplined practice; and the integration of material and spiritual concerns within a single hierarchical ontology.

For scholars, attending to the specific Neoplatonic cosmology of emanation—rather than treating Renaissance magic as a diffuse "magical worldview"—enables more precise analysis of specific texts and their philosophical commitments. The differences between Ficino's solar magic, Agrippa's celestial hierarchy, and Bruno's infinite universe are intelligible in terms of their different engagements with the emanative cosmology they shared, while the differences between Neoplatonic emanationism and mechanical philosophy illuminate what was actually at stake in seventeenth-century debates about occult qualities and hidden causes.
""",
    },
]


def word_count(text: str) -> int:
    return len(text.split())


def main():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    now = datetime.utcnow().isoformat()

    inserted = 0
    skipped = 0
    for concept in CONCEPTS:
        slug = concept["slug"]
        existing = c.execute("SELECT id FROM concepts WHERE slug=?", (slug,)).fetchone()
        if existing:
            skipped += 1
            continue

        c.execute(
            """INSERT INTO concepts
               (slug, title, category, summary, body, related_figures, related_concepts,
                word_count, source_method, review_status, confidence, created_at, updated_at)
               VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
            (
                slug,
                concept["title"],
                concept["category"],
                concept["summary"],
                concept["body"].strip(),
                json.dumps(concept.get("related_figures", [])),
                json.dumps(concept.get("related_concepts", [])),
                word_count(concept["body"]),
                "LLM_ASSISTED",
                "DRAFT",
                "HIGH",
                now,
                now,
            ),
        )
        inserted += 1
        print(f"  Inserted: {concept['title']} ({word_count(concept['body'])} words)")

    conn.commit()
    conn.close()
    print(f"\nBatch 1 done: {inserted} inserted, {skipped} skipped.")


if __name__ == "__main__":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
    main()
