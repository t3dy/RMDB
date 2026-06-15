"""Seed concepts table — Batch 5: Demonology, Astrology, Rosicrucianism, Art of Memory, Angelology."""

import sqlite3
import json
import sys
import io
from datetime import datetime

DB_PATH = "db/renmagic.db"

CONCEPTS = [
    {
        "slug": "demonology",
        "title": "Demonology",
        "category": "Demonology and Witchcraft",
        "summary": "The systematic study of demons—their nature, hierarchy, powers, and relationship to human beings—a central preoccupation of early modern theology, natural philosophy, and legal thought that structured debates about magic, witchcraft, and the boundaries of legitimate religious practice.",
        "related_figures": ["Jean Bodin", "Johann Weyer", "Heinrich Kramer", "Reginald Scot", "Cornelius Agrippa"],
        "related_concepts": ["witchcraft", "demonic-magic", "demonic-pact", "angelic-hierarchy", "natural-magic"],
        "body": """## The Scope of Demonology

Demonology—the systematic investigation of demons, their nature, capacities, and activities—was not a fringe preoccupation in early modern Europe but a central concern of academic theology, natural philosophy, medicine, and law. As Stuart Clark argued in *Thinking with Demons* (1997), demonology was embedded in the fundamental conceptual structures of early modern thought: its categories and assumptions organized discussions of causation, epistemology, politics, and religious practice far beyond the specific question of what demons could do.

Demons, in the Christian theological tradition inherited and elaborated by Renaissance thinkers, were fallen angels: spiritual beings of great intelligence and power who had rebelled against God and were now engaged in the deception and destruction of humanity. Their existence was scripturally attested, theologically established, and philosophically explicable within the Neoplatonic cosmological framework. They inhabited the sublunary air (following a tradition derived from Neoplatonic daimonology), had access to the secrets of nature exceeding human knowledge, and could manipulate the material world through their understanding of natural causes—but they could not perform genuine miracles, which were God's exclusive prerogative.

## Philosophical Foundations

The Christian demonological tradition drew on several distinct philosophical sources. The Neoplatonic tradition, particularly Apuleius of Madaura's *De deo Socratis* and later Neoplatonic authors, described intermediate beings (*daimones*) inhabiting the air between earth and heaven, capable of both helping and harming humans. Augustine's appropriation of this tradition in *City of God* (Books VIII–X) retained the ontology of intermediate beings while reinterpreting all such beings as either good angels (serving God's purposes) or demons (deceptive and malevolent fallen angels). This Augustinian synthesis established the theological framework within which all subsequent demonology operated.

Aquinas systematized the theological account of demons in the *Summa Theologiae*, establishing their nature (immaterial intellects with no material body), their powers (ability to move matter and affect human imagination through local motion, but not to create matter or compel the will), and their limitations (inability to foreknow contingent futures, inability to perform genuine miracles). This Thomistic account provided the intellectual framework within which the more spectacular claims of Renaissance demonology were evaluated and contested.

## The Question of Demonic Power

The central practical question of Renaissance demonology was what demons could actually do, and therefore what forms of magic could be explained without recourse to demonic assistance. Aquinas had established that demons could cause apparent but not genuine change in matter (they could rearrange atoms but not create new substances), could afflict the imagination and produce false sensory impressions, and could know natural facts unknown to humans (but not genuine contingent futures or the secrets of divine providence).

Pietro Pomponazzi's *De incantationibus* (written c. 1520) tested the limits of this framework by arguing that all apparently demonic effects could be explained through occult natural causes (specifically, stellar influences)—making demons causally redundant in natural philosophy. This radical naturalism was theologically uncomfortable (it threatened to explain away miraculous phenomena attributed to demons and thereby, by symmetry, those attributed to God), but it established a powerful naturalist pole in the debate about what demons could and could not do.

Johann Weyer's *De praestigiis daemonum* (1563) deployed demonological expertise in a skeptical direction regarding witchcraft: Weyer argued that demons were real and powerful, but that accused witches were typically deluded melancholic women whose "confessions" of sabbath attendance and maleficent magic reflected demonic deception of their imaginations rather than actual events. This sophisticated position—accepting the reality of demons while denying the reality of most witchcraft confessions—influenced subsequent debates considerably, though it was strenuously rejected by witch-trial advocates like Jean Bodin.

## Jean Bodin and Maximalist Demonology

Jean Bodin's *De la démonomanie des sorciers* (1580) represents the most intellectually ambitious case for robust demonic activity and for vigorous persecution of witches. Bodin drew on his vast learning (he was one of the most erudite men of his generation, author of the landmark political theory text *Six Books of the Republic*) to argue that witchcraft was real, that the sabbath was a genuine event rather than a delusion, and that the testimony of accused witches was generally reliable evidence of actual pacts with the devil.

Bodin's demonology was also politically significant: he connected the spread of witchcraft to the breakdown of social and political order, arguing that tolerance of witches was politically dangerous. His use of political theory in the service of demonological argument exemplifies Stuart Clark's point that demonology was not an isolated domain but was integrated into the broader intellectual culture of the period.

## Demonology and Natural Magic

Demonology was structurally intertwined with natural magic through the persistent question of whether magic was "natural" (operating through hidden but genuine natural causes) or "demonic" (operating through the power of demons, whether explicitly invoked or tacitly assisted). The impossibility of clearly answering this question in specific cases was a source of persistent anxiety for both practitioners and critics of magic.

Thomas Aquinas had argued that demons could be implicitly involved in magical operations that appeared natural—that the occult properties attributed to plants and stones might in fact be operative only through demonic enhancement. This argument meant that no clear empirical test could distinguish natural from demonic magic: apparent natural efficacy was always potentially demonic deception. The practitioner's only recourse was to insist on the philosophical coherence of his natural framework, as Ficino, Agrippa, and Porta all attempted.

## The Decline of Demonology

The intellectual decline of demonology in the later seventeenth and eighteenth centuries was a complex process that reflected multiple contributing factors. The mechanical philosophy made demonic intervention in natural processes theoretically incoherent (in a mechanical universe, demons could not operate without observable material disturbance). Legal skepticism about the reliability of witchcraft confessions obtained under torture accumulated through painful experience of the trial process. Broader cultural shifts toward natural explanation and away from providential-demonic frameworks gradually reduced the plausibility of demonic causation as a standard explanatory resource.

But demonology did not disappear smoothly. As Keith Thomas showed, belief in witchcraft and demonological frameworks persisted in popular culture well into the eighteenth and nineteenth centuries; what changed was its status in elite intellectual culture, not its prevalence more broadly. The "decline" of demonology was a cultural and institutional process, not simply the replacement of superstition by science.
""",
    },
    {
        "slug": "learned-astrology",
        "title": "Learned Astrology",
        "category": "Astrology",
        "summary": "The systematic art of predicting and interpreting the influences of celestial bodies on terrestrial events and human lives, an established component of the medieval and Renaissance university curriculum and a central pillar of the learned magical-philosophical worldview, whose eventual marginalization as 'pseudo-science' reflects contested early modern debates rather than self-evident intellectual progress.",
        "related_figures": ["Marsilio Ficino", "Pico della Mirandola", "Cornelius Agrippa", "Johannes Kepler", "Ptolemy"],
        "related_concepts": ["astral-magic", "cosmic-sympathy", "macrocosm-and-microcosm", "ptolemaic-cosmos", "natural-magic"],
        "body": """## Astrology as Learned Practice

Astrology—the systematic study of celestial influences on terrestrial events and human affairs—occupied a complex and contested but by no means marginal position in Renaissance intellectual culture. It was taught in Italian universities as part of the medical curriculum (physicians needed astrological knowledge to diagnose and treat disease), patronized by popes and princes (Julius II and Paul III both employed court astrologers), embedded in agricultural and medical almanacs read by literate people across Europe, and the subject of serious philosophical debate among the most sophisticated thinkers of the period.

The term "astrology" covered a diverse range of practices and theoretical commitments. *Judicial astrology*—the use of planetary positions to forecast events and interpret human fates—was distinguished from *natural astrology*, which studied celestial influences on weather, tides, agriculture, and health without making specific individual predictions. *Natal astrology* calculated a person's fate from the positions of planets at the moment of birth; *horary astrology* answered specific questions from the planetary positions at the moment of asking; *mundane astrology* predicted political and historical events from celestial configurations; *electoral astrology* chose auspicious times for undertaking important activities.

## Ptolemaic Foundations

Western learned astrology derived primarily from Claudius Ptolemy's *Tetrabiblos* (second century CE), one of the most influential scientific texts in the Western tradition. Ptolemy provided a systematic account of how celestial bodies exerted physical influences on terrestrial nature through their heat, moisture, and other qualities, operating through the medium of light and the celestial "air." He offered a fundamentally naturalistic account: astrology worked through physical causation, not through divine providence or spiritual beings.

This naturalistic framework was crucial for astrology's academic legitimacy. Ptolemy's astrology was not divination (reading arbitrary signs to infer divine intentions) but natural philosophy (identifying physical causes and their effects). The planets influenced human bodies and minds through the same physical mechanisms that caused weather changes and seasonal variation—the astrologer was simply extending natural philosophical reasoning to human affairs.

## Arabic Elaborations and Medieval Transmission

Arabic astronomers and astrologers substantially elaborated the Ptolemaic tradition, adding technical refinements (more complex theories of planetary aspects, lots, and horoscope interpretation) and philosophical integration with Aristotelian and Neoplatonic thought. Abu Ma'shar's *Introductorium Maius* (ninth century), translated into Latin in the twelfth century, became the standard introduction to learned astrology in the Latin West. Al-Kindi's *De radiis* provided a theoretical framework for astrological influence in terms of the radiation of "rays" from celestial bodies—a framework applicable not only to astrology but to magic more generally.

The medieval university incorporated astrology primarily through the medical curriculum. Physicians were expected to cast horoscopes, determine auspicious times for treatments, and use astrological knowledge to diagnose diseases and predict their course. Major universities (Bologna, Padua, Paris) had chairs in astrology or in the combined *astronomia-astrologia* that covered both observational and predictive celestial knowledge.

## Pico's Critique and Its Limits

Giovanni Pico della Mirandola's *Disputationes adversus astrologiam divinatricem* (written c. 1493, published 1496, posthumously) constitutes the most thoroughgoing Renaissance critique of judicial astrology. Pico argued across twelve books that astrology was empirically unreliable, theoretically incoherent, and theologically dangerous. His empirical arguments pointed to cases where astrological predictions failed, to the problem of twins (who share a natal horoscope but may have very different fates), and to the impossibility of measuring the exact moment of birth with sufficient precision. His theoretical arguments attacked the physical basis of planetary influence, challenging whether planets could have the specific qualities attributed to them. His theological arguments insisted that divine providence and human free will were incompatible with the deterministic claims of natal astrology.

Pico's critique was enormously influential in subsequent debates but did not end serious astrological practice. Defenders of astrology (including Luca Gaurico and others) responded to his arguments point by point; practitioners modified their claims to exclude deterministic fate-assignment while retaining the milder claim that planetary influences inclined rather than compelled; and the philosophical and medical applications of astrology continued to be taught and practiced throughout the sixteenth century and well into the seventeenth.

## Kepler's Reformed Astrology

Johannes Kepler presents a fascinating case of a mathematician of the highest ability who rejected traditional judicial astrology while retaining something like a reformed astrological philosophy. Kepler argued against Ptolemaic astrology that there was no physical basis for the traditional qualities of planets, no mechanism for the zodiac signs to have any influence (they were merely arbitrary divisions of the ecliptic), and no evidence for the specific predictions of horoscopic astrology. At the same time, he believed that celestial harmonies—specifically, the harmonic relationships between planetary positions—had genuine influence on terrestrial processes and human souls.

Kepler's "reformed astrology" replaced the Ptolemaic qualitative framework with a Pythagorean-Neoplatonic harmonic framework: celestial influence worked through mathematical harmony rather than physical qualities. This replacement preserved his commitment to genuine celestial influence while rejecting the specific theoretical apparatus of traditional astrology. The result was philosophically interesting but practically unworkable: it was impossible to generate specific predictions from harmonic relationships alone.

## The Social Context of Astrological Practice

Astrology was not merely a theoretical debate but a widespread social practice with specific institutional contexts. Court astrologers advised rulers on the timing of military campaigns, political decisions, and marriages. Medical astrologers diagnosed patients and prescribed treatment schedules. Popular almanacs provided astrological weather forecasts and health advice for literate laypeople. Urban practitioners offered natal horoscopes and horary consultations for a fee.

The social range of astrological practice extended from the court astrologers of major European princes (whose mistakes could have serious consequences, including imprisonment) to the itinerant practitioners selling penny almanacs at fairs. The same intellectual tradition that produced Ficino's Neoplatonic astrology in *De vita* also produced the cheap almanac predictions that Keith Thomas documented for early modern England. Understanding the relationship between these levels—how elite astrological theory filtered into popular practice, and how popular practice shaped elite theory—remains an important area of social history of knowledge.

## Astrology's Decline and Transformation

The decline of judicial astrology from its position as a learned discipline is usually dated to the late seventeenth and early eighteenth centuries, when it lost its place in university curricula, was increasingly regarded as incompatible with mechanical natural philosophy, and faced sustained empirical criticism (the failure of specific predictions, the incompatibility of heliocentric astronomy with geocentric horoscopic theory). But this decline was gradual and uneven: astrological almanacs continued to sell widely throughout the eighteenth century, and elite astrological consultation persisted longer than its academic marginalization might suggest.

What changed was not primarily the empirical record (astrological predictions had always mixed hits and misses) but the epistemological and cultural framework within which astrological claims were evaluated. When celestial influence through physical qualities in a geocentric cosmos ceased to be the default cosmological framework, astrology's theoretical basis evaporated. The question was no longer whether specific predictions were accurate but whether the entire causal framework was coherent—and by the late seventeenth century, the dominant answer among educated Europeans was that it was not.
""",
    },
    {
        "slug": "rosicrucianism",
        "title": "Rosicrucianism",
        "category": "Rosicrucian and Later Traditions",
        "summary": "The movement launched by the anonymous publication of the Rosicrucian manifestos (1614–1616), announcing the existence of a secret brotherhood of enlightened Christian reformers possessing the secrets of alchemy and natural philosophy; a cultural phenomenon that generated enormous response despite the brotherhood's probable non-existence, shaping the development of seventeenth-century esotericism.",
        "related_figures": ["Johann Valentin Andreae", "Robert Fludd", "Michael Maier", "Francis Bacon"],
        "related_concepts": ["alchemy", "christian-theosophy", "printing-and-the-occult", "patronage-and-magic", "kabbalah-and-christian-kabbalah"],
        "body": """## The Rosicrucian Manifestos

The Rosicrucian movement originated with the publication of three texts in rapid succession: the *Fama Fraternitatis* (1614), the *Confessio Fraternitatis* (1615), and the *Chymical Wedding of Christian Rosenkreutz* (1616). These texts announced the existence of a secret brotherhood—the Order of the Rosy Cross or Fraternity of the Rosicrucians—founded by a mysterious figure named Christian Rosenkreutz (C.R.C.), whose tomb had allegedly just been rediscovered after 120 years of concealment.

The *Fama* narrated C.R.C.'s travels through the Islamic world (Arabia, Egypt, Morocco), where he learned the occult sciences from Arab and Eastern sages, and his subsequent establishment of a four-man brotherhood dedicated to healing the sick for free, wearing no distinctive dress, and meeting once yearly. The *Confessio* elaborated the brotherhood's religious and philosophical principles, emphasizing a reformed Christian piety compatible with Protestant theology (the texts were anti-Catholic) and a programme of universal learning based on alchemy and natural philosophy. The *Chymical Wedding* presented an elaborate allegorical narrative of C.R.C.'s attendance at a mysterious royal wedding, involving alchemical processes, hermetic symbolism, and initiatory trials.

## The Non-Existent Brotherhood

The Rosicrucian manifestos generated an extraordinary cultural response: between 1614 and 1620, over two hundred texts were published in response, claiming to have contacted the brotherhood, appealing for admission, attacking the brotherhood as demonic, or attempting to expose it as fraudulent. The brotherhood itself never responded to any of these appeals. Contemporary and subsequent investigation has found no evidence that the Rosicrucian Order actually existed as described.

The most plausible account of the manifestos' authorship attributes the *Fama* and *Confessio* to a circle associated with the Lutheran theologian and writer Johann Valentin Andreae (1586–1654), and identifies the *Chymical Wedding* as Andreae's own early work, later somewhat embarrassingly incorporated into the phenomenon he had helped create. Andreae later claimed the manifestos were a *ludibrium* (jest or literary game)—a claim that may reflect genuine ambivalence about the project's reception rather than simple dishonesty about its purpose.

## The Rosicrucian Response and Its Significance

The enormous response to the Rosicrucian manifestos reflects the particular cultural moment of the early seventeenth century. The period was one of intense millenarian expectation (the early years of the seventeenth century saw widespread predictions of imminent religious and political transformation), of acute anxiety about the state of Christendom (the Wars of Religion had divided Europe, and the Thirty Years' War was about to devastate it), and of genuine excitement about the possibilities of natural philosophical reform (Bacon's *Advancement of Learning* appeared in 1605).

The manifestos addressed all of these concerns simultaneously: they promised a secret reformation of learning and religion, claimed to possess the secrets of alchemy and Paracelsian medicine that could transform human well-being, and framed these promises in a Protestant Christian theological context that distinguished the Rosicrucian programme from both Catholic corruption and atheistic naturalism. They were, in short, the perfect cultural object for a particular moment—which is why they generated such an enormous response.

Robert Fludd defended the Rosicrucians against their critics in *Apologia Compendiaria Fraternitatem de Rosea Cruce* (1616), though he may not have had any actual contact with the brotherhood. Michael Maier wrote and published several works in dialogue with Rosicrucian themes, including *Silentium Post Clamores* (1617) and *Themis Aurea* (1618). Their serious engagement with a movement whose central institution may have been fictitious illustrates how the manifestos functioned primarily as a literary and cultural phenomenon rather than an organizational one.

## Rosicrucian Ideas and Their Legacy

Despite the probable non-existence of the brotherhood, the Rosicrucian manifestos crystallized a specific combination of ideas that proved enormously influential: the union of Paracelsian medicine and alchemy with Hermetic-Neoplatonic philosophy and Protestant Christian piety; the idea of a small group of enlightened reformers working secretly for universal benefit; the vision of natural philosophical and spiritual knowledge as inherently connected; and the claim that this comprehensive wisdom was available through initiation into a brotherhood possessing ancient secrets.

These ideas shaped subsequent esoteric movements: Freemasonry incorporated Rosicrucian themes in the eighteenth century; the Hermetic Order of the Golden Dawn in the nineteenth century claimed Rosicrucian roots; and numerous subsequent esoteric orders have invoked the Rosicrucian name and tradition. The historical Rosicrucian manifestos of 1614–16 thus inaugurated a tradition of organizations claiming secret Rosicrucian descent whose relationship to any actual historical succession is entirely fictional—but whose cultural vitality has been remarkable.

## Scholarly Assessment

The Rosicrucian manifestos were treated by Frances Yates (*The Rosicrucian Enlightenment*, 1972) as part of her broader thesis about the Hermetic-magical tradition's role in the Scientific Revolution: she connected the Rosicrucian moment to the scientific societies of the later seventeenth century (particularly the early Royal Society) through the figure of Samuel Hartlib and a proposed Rosicrucian network around the Elector Palatine Frederick V. Subsequent scholarship has found Yates's specific connections difficult to sustain, but her insight that the Rosicrucian moment was a significant cultural crystallization of the tensions between esoteric and emerging scientific culture remains influential.

Carlos Gilly's archival work on the Rosicrucian documents and their reception has substantially advanced the scholarly understanding of the phenomenon's specific intellectual and political context, providing a more nuanced picture than Yates's grand narrative. The Rosicrucian episode remains one of the most fascinating examples in European cultural history of how a literary fiction can generate an enormous real historical effect.
""",
    },
    {
        "slug": "art-of-memory",
        "title": "The Art of Memory",
        "category": "Magic Theory and Practice",
        "summary": "The ancient mnemonic technique of placing images in imagined architectural spaces, elaborated in the Renaissance as a potentially magical or philosophical art capable of structuring the mind's relationship to the entire cosmos; Frances Yates's study of it illuminated the intersection of rhetoric, philosophy, and occult practice.",
        "related_figures": ["Giordano Bruno", "Giulio Camillo", "Ramon Llull", "Cornelius Agrippa", "Frances Yates"],
        "related_concepts": ["neoplatonism", "the-yates-thesis", "hermetism", "macrocosm-and-microcosm", "number-mysticism"],
        "body": """## The Classical Art

The *ars memorativa* (art of memory) was a classical rhetorical technique for memorizing large amounts of material by mentally placing images (imagines) representing the items to be remembered in specific locations (loci) within imagined architectural spaces—typically, the rooms of a familiar building traversed in a fixed order. When one wished to recall the material, one mentally "walked" through the building, encountering each image in its place. The technique was described in the anonymous *Rhetorica ad Herennium* (first century BCE, attributed to Cicero), Cicero's own *De oratore*, and Quintilian's *Institutio oratoria*.

The art of memory was primarily a practical technique for orators who needed to deliver long speeches without notes. The images chosen for memory-work were typically striking, emotionally charged, or bizarre—the technique recognized that the unusual and vivid was more memorable than the ordinary. This requirement for powerful, affect-laden images was to prove significant when the art was appropriated for magical and philosophical purposes.

## Medieval Transformation

The medieval tradition transformed the classical art in two significant ways. First, Thomas Aquinas and other scholastics moralized the technique, recommending it as a tool for memorizing moral and theological content, and specifying that the images should be ordered around the categories of virtues and vices. Second, Ramon Llull (c. 1232–1316) developed a related but distinct combinatorial art (*ars combinatoria*), using rotating concentric wheels with letters and concepts to generate all possible combinations of divine attributes and to demonstrate Christian theological truths. Llull's art was not strictly mnemonic but rather a method for discovering truth through systematic combination—a precursor to later combinatorial logic.

Both transformations are significant for the Renaissance: the moralized classical art provided the background for humanist treatments of memory as a moral-philosophical discipline, while the Lullian combinatorial art provided the model for Bruno's more elaborate memory systems.

## Giulio Camillo's Theatre of Memory

Giulio Camillo Delminio (c. 1480–1544) constructed a physical "Memory Theatre"—a wooden structure, apparently built at least in part—designed to contain images representing all of human knowledge organized according to a Hermetic-Neoplatonic cosmological scheme. The theatre was arranged in a semicircle with seven gangways (corresponding to the seven planets) and seven tiers (corresponding to the seven Sephiroth of Kabbalah or to Hermetic cosmological principles), each location containing a box with images and inscriptions summarizing the knowledge belonging to that cosmic category.

Camillo's theatre was a kind of physical encyclopedia organized not alphabetically or by subject but cosmologically: by standing in the theatre and "reading" its images, one would comprehend the structure of the cosmos and the place of all human knowledge within it. This was simultaneously a mnemonic device (organizing knowledge for recall), a philosophical instrument (demonstrating the cosmic structure of knowledge), and arguably a magical object (embodying the correspondences between cosmic levels in physical space).

## Giordano Bruno and the Magical Memory

Giordano Bruno's numerous works on the art of memory—*De umbris idearum* (1582), *Cantus Circaeus* (1582), *De imaginum, signorum et idearum compositione* (1591), and others—developed the most philosophically elaborate and explicitly magical version of the art in the Renaissance. Frances Yates's *The Art of Memory* (1966) is the foundational modern study, arguing that Bruno transformed the classical art into a magical tool: by loading memory locations with images corresponding to the Hermetic cosmic powers (drawn from Hermetic sources like the *Decans* of the zodiac), the practitioner could attain a mind that was itself a microcosm of the cosmic order—a mind "stamped with" the images of all reality, and thereby capable of magical power.

Yates's reading of Bruno has been influential but also contested. She interpreted Bruno's memory art primarily in terms of his Hermeticism—as an attempt to achieve the Hermetic sage's mastery of the cosmos through internal representation. Subsequent scholars (including Hilary Gatti and Michele Ciliberto) have emphasized Bruno's Neoplatonic and cosmological commitments over his Hermeticism, and have questioned whether "magical" is the right term for what Bruno was doing with memory. The art of memory in Bruno was at minimum a philosophical technique for organizing the mind's relationship to a necessarily infinite universe of infinite worlds—whether that organization had magical efficacy in any strict sense remains debated.

## Memory, Magic, and the Imagination

The connection between the art of memory and magic runs through the concept of *imagination* (*phantasia* or *imaginatio*) as a quasi-material power. In the Neoplatonic and medical traditions drawing on *spiritus* theory, the imagination operated through *spiritus animalis* in the brain, creating images that could affect the body directly and project outward through the eye to affect others. Memory images, on this account, were not merely cognitive but quasi-material: they were configurations of *spiritus* in the brain, with genuine causal power.

This gave the art of memory a potentially magical dimension: if the images one placed in memory locations had the right cosmic charge—if they corresponded to and participated in the relevant cosmic powers—then the memory-trained mind became a kind of talisman, a concentrated focus of cosmic power. The practitioner who had perfectly internalized the images of all cosmic powers would thereby have those powers available for practical use. This is the implication that Yates drew out in Bruno, and while its historical accuracy is disputed, it illustrates how magical and philosophical concerns could be integrated within a single technical practice.

## Significance

The art of memory has attracted attention from historians of ideas and intellectual culture partly because of Yates's influential studies, and partly because it stands at the intersection of several major concerns: the relationship between language and thought, between representation and reality, between memory and knowledge, and between technique and magic. As a practical art, it was used by orators, preachers, lawyers, and scholars throughout the period. As a philosophical and potentially magical art, it was the subject of elaborate speculation about the mind's capacity to mirror and participate in the cosmic order.
""",
    },
    {
        "slug": "angelic-hierarchy",
        "title": "Angelic Hierarchy",
        "category": "Angelology",
        "summary": "The elaborate taxonomy of angelic beings—divided into orders or choirs from Seraphim to Angels—derived primarily from Pseudo-Dionysius the Areopagite and Aquinas, which provided Renaissance magical practitioners with a map of the spiritual hierarchy through which divine power descended and toward which magical and theurgic operations could be directed.",
        "related_figures": ["Pseudo-Dionysius the Areopagite", "Cornelius Agrippa", "John Dee", "Giovanni Pico della Mirandola"],
        "related_concepts": ["theurgy", "neoplatonism", "emanation", "kabbalah-and-christian-kabbalah", "planetary-spirits", "natural-magic"],
        "body": """## Pseudo-Dionysius and the Standard Account

The canonical account of the celestial hierarchy in the Latin West derived primarily from the works attributed to Dionysius the Areopagite (Acts 17:34), in fact composed by an anonymous Christian Neoplatonist of the early sixth century whose identity remains unknown. Pseudo-Dionysius's *Celestial Hierarchy* and *Ecclesiastical Hierarchy*, translated into Latin by John Scottus Eriugena in the ninth century and widely read throughout the medieval period, divided the angelic realm into three triads:

**First Hierarchy** (closest to God): Seraphim, Cherubim, Thrones
**Second Hierarchy**: Dominions, Virtues, Powers
**Third Hierarchy** (governing the lower cosmos): Principalities, Archangels, Angels

Each order received divine illumination from the order above it, purified and transmitted it appropriately to the order below, and performed specific cosmic functions. The Seraphim burned with divine love; the Cherubim possessed divine knowledge; the Thrones were seats of divine judgment. The Principalities governed nations; the Archangels communicated divine messages to humanity; the Angels (lowest order) were the immediate messengers and guardians of individual humans.

This hierarchical account drew directly on Proclus's Neoplatonic hierarchiology, translated into Christian theological terms: the Plotinian One became the Christian God; the Neoplatonic levels of gods and daimones became the angelic orders. The result was a cosmology in which divine power descended through graded levels of spiritual being, each appropriate to a specific cosmic function, and in which human beings could potentially approach the divine through this hierarchy with appropriate mediation.

## Aquinas and Scholastic Angelology

Thomas Aquinas elaborated the Pseudo-Dionysian hierarchy within the framework of Aristotelian metaphysics, providing systematic answers to questions about angelic nature that Pseudo-Dionysius had left unresolved. Angels were immaterial intelligences, each constituting its own species (since immaterial beings could not be individuated by matter). They knew through innate ideas implanted by God rather than through abstraction from sense experience. They moved instantaneously through space without being in the intermediate locations. They could affect bodies through local motion but could not directly compel human wills.

Aquinas's angelology served important functions in Renaissance magical theory. It established the ontological status of intermediate spiritual beings (neither purely material nor purely divine), provided a framework for the powers and limitations of such beings that could be applied to discussion of both angels and demons, and integrated the celestial hierarchy into the Aristotelian cosmological framework that governed natural philosophical discussion.

## Angelic Hierarchy in Renaissance Magic

For Renaissance magical practitioners, the angelic hierarchy provided a map of the spiritual territory that magical operations navigated. Agrippa's *Three Books of Occult Philosophy* correlated the Pseudo-Dionysian hierarchy with the planetary spheres (the third hierarchy governing the sublunary and planetary realms), with Hebrew divine and angelic names from the Kabbalistic tradition, and with the magical squares and seals that enabled planetary invocation. Each planetary sphere was governed by an angel of a specific order; addressing that angel through its name and seal was the means of harnessing that planet's influence.

The Kabbalistic tradition provided parallel resources. The Sefirot of Kabbalah could be correlated with angelic orders: Keter corresponded to the Seraphim, Chokhmah to the Cherubim, and so on down the Tree of Life. Christian Kabbalists like Pico della Mirandola and Agrippa performed these correlations explicitly, creating a synthetic map in which Hebrew angelic names, Greek-derived Pseudo-Dionysian categories, and Arabic-derived planetary spirits were organized into a single hierarchical scheme.

## John Dee's Angelology

John Dee's angelic conversations developed a distinctive angelology through direct "revelation." The angelic beings who communicated through Edward Kelley's scrying gave themselves names, ranks, and specific powers, providing what Dee understood as an authoritative account of the celestial hierarchy above—and in some ways different from—the standard Pseudo-Dionysian taxonomy. The Enochian system included governors of the four elements, princes of the four quarters of the earth, and a complex hierarchy of rulers organized around the mysterious "Aires" or Aethers, thirty concentric zones of angelic governance above the earth.

Dee's angelic system was not a simple derivative of the established tradition but a creative elaboration, drawing on elements of the Pseudo-Dionysian hierarchy, the Kabbalistic Sephirotic scheme, the planetary spirit tradition, and the prophetic-apocalyptic tradition of angelic revelation. Whether it represented genuine revelation, creative imagination, Edward Kelley's manipulation, or some complex combination of all three has been debated by historians from Dee's own time to the present.

## Angelic Hierarchy and Ritual Practice

The practical dimension of angelic hierarchy in Renaissance magic was the development of specific ritual procedures for addressing specific angelic beings: their names (often derived from Hebrew divine names by systematic processes), their seals or sigils (derived from magic squares or other procedures), and the appropriate conditions (planetary hour, day of the week, material correspondences) for their invocation. The grimoire tradition preserved extensive catalogues of angelic and demonic names, organized by planetary association, function, and rank—providing practitioners with the information needed to address the right being for specific purposes.

This practical angelology existed in tension with orthodox Christian theology, which insisted that appropriate angelic contact was mediated through prayer and the Church's sacramental system, not through ritual invocation. The distinctions that practitioners drew—between prayer (addressed to God and acceptable to angels) and invocation (addressed to spiritual beings and potentially demonic)—were never fully convincing to orthodox critics, who maintained that any ritual address to spiritual beings outside the sacramental framework was by definition demonic.

## Scholarly Significance

The angelic hierarchy is important for the history of Renaissance magic as the spiritual topology within which magical operations were situated. Understanding what practitioners believed about angels—their nature, powers, hierarchy, and addressability—is essential for understanding how they understood their own practice. The standard academic contrast between "rational" natural philosophy and "superstitious" magic often misses this dimension: for educated Renaissance practitioners, the angelic hierarchy was as much a part of cosmological reality as the planetary spheres or the four elements, and magical operations directed toward angelic beings were in principle as rationally coherent as operations directed toward material substances.
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
    print(f"\nBatch 5 done: {inserted} inserted, {skipped} skipped.")


if __name__ == "__main__":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
    main()
