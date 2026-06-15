"""Seed concepts table — Batch 9: Music of Spheres, Occult Properties, Cunning Folk, Republic of Letters, Imagination."""

import sqlite3
import json
import sys
import io
from datetime import datetime

DB_PATH = "db/renmagic.db"

CONCEPTS = [
    {
        "slug": "music-of-the-spheres",
        "title": "Music of the Spheres",
        "category": "Cosmology and Natural Philosophy",
        "summary": "The Pythagorean and Neoplatonic doctrine that the planetary spheres move in mathematically harmonic ratios, producing an inaudible cosmic music that structures both the cosmos and the human soul; elaborated by Ficino into a theory of musical magic and by Kepler into a mathematical cosmology.",
        "related_figures": ["Marsilio Ficino", "Johannes Kepler", "Robert Fludd"],
        "related_concepts": ["neoplatonism", "astral-magic", "number-mysticism", "macrocosm-and-microcosm", "cosmic-sympathy"],
        "body": """## The Pythagorean Doctrine

The doctrine that the planets produce music in their movements—the *harmonia mundi* or "harmony of the world," *musica mundana* in Boethius's influential classification—derived from Pythagorean philosophy. Pythagoras (sixth century BCE) or his followers allegedly discovered that the fundamental musical intervals (octave, fifth, fourth) corresponded to simple numerical ratios (2:1, 3:2, 4:3), and inferred that similar ratios governed the distances and motions of the celestial bodies. The cosmos was therefore a musical instrument, its motions generating harmonious tones whose mathematical structure expressed divine reason.

The planetary music was not ordinarily audible to human beings: having grown up hearing it continuously, we were habituated to it just as inhabitants of a waterfall become unable to hear the water. Only exceptionally gifted souls—Pythagoras himself was said to have heard it—could perceive the cosmic music directly. But its effects were present everywhere in nature, particularly in the relationship between music and the human soul.

Plato's *Timaeus* incorporated Pythagorean number symbolism into its account of the World Soul, describing the Demiurge as constructing the soul's proportions from the same numerical ratios as the musical intervals. This Platonic version made the musical/mathematical structure of the cosmos the structure of the soul itself: the soul could resonate with cosmic harmonics because it was built from them.

## Ficino's Musical Magic

Marsilio Ficino developed the Pythagorean-Platonic doctrine of cosmic music into a practical theory of musical magic in *De vita* (1489). The human soul, built from the same proportions as the World Soul, was particularly susceptible to music: specific melodic modes, rhythmic patterns, and textual content could activate or strengthen the soul's participation in specific planetary influences. Sol-natured music—warm, expansive, joyful—could attract Solar *spiritus* and counteract Saturnine melancholy. Luna-natured music—flowing, gentle, meditative—could calm excessive agitation.

Ficino's musical practice was embedded in his broader astral magic: music was one of the most effective means of shaping the *spiritus* because it acted directly through the *spiritus animalis* in the ear and the *spiritus* that permeated the body, carrying the soul's movement directly into the practitioner's internal economy. His own practice of playing the lyre and singing Orphic hymns was understood as a form of astral magic as much as devotional activity.

## Kepler and Mathematical Harmony

Johannes Kepler's *Harmonices Mundi* ("Harmony of the World," 1619) represents the most mathematically sophisticated Renaissance version of the music-of-the-spheres doctrine. Kepler argued that the planetary orbits, while not circular (his first two laws had established elliptical orbits), exhibited harmonic relationships in their angular velocities at perihelion and aphelion—the ratio of a planet's fastest to slowest angular speed corresponded to a recognizable musical interval.

For Kepler, this was not merely metaphor but genuine mathematical fact: God had constructed the cosmos according to harmonic principles, and the astronomer's task was to discover these principles through careful observation and mathematical analysis. His third law (that the square of a planet's period is proportional to the cube of its mean orbital distance) was discovered as part of this search for cosmic harmonics, which gives it a double significance: it is simultaneously one of the most important laws of classical astronomy and a result of a Pythagorean-Neoplatonic search for mathematical beauty in the cosmos.

## Robert Fludd's Visual Harmonics

Robert Fludd's *Utriusque cosmi historia* (1617–21) presented the music of the spheres in an elaborate series of visual diagrams, the most famous of which shows the cosmos as a monochord (a single-stringed instrument) stretched between earth and the divine realm, with the planetary spheres arranged at positions corresponding to musical intervals. Fludd's visual argument was that the entire cosmos was structured by a single harmonic principle, and that this structure could be both discovered through mathematical analysis and grasped directly through aesthetic experience of the harmony.

Fludd's musical cosmology generated a famous controversy with Kepler, who objected to Fludd's use of the musical analogy as imprecise and aesthetically arbitrary. The controversy is historically significant as an early modern argument about the relationship between mathematical precision and symbolic or analogical reasoning in natural philosophy—a debate whose resolution (in Kepler's favor, broadly speaking) helped define the subsequent trajectory of mathematical science.

## Scholarly Significance

The music of the spheres illuminates the intersection of mathematics, aesthetics, cosmology, and magic in Renaissance thought. It shows how Pythagorean number mysticism could be simultaneously a rigorous mathematical claim (Kepler), a theory of magical operation (Ficino), and a symbolic-visual system (Fludd)—with the same underlying intuition generating very different intellectual projects. It also demonstrates how Renaissance natural philosophy was animated by aesthetic and spiritual commitments that modern science has largely bracketed without necessarily abandoning.
""",
    },
    {
        "slug": "occult-properties",
        "title": "Occult Properties",
        "category": "Magic Theory and Practice",
        "summary": "The category of hidden natural qualities—distinct from the 'manifest' qualities of heat, cold, moisture, and dryness—believed to produce effects through the specific nature of their subject rather than through elemental action; the foundational explanatory concept for natural magic and the target of mechanical philosophy's most sustained critique.",
        "related_figures": ["Marsilio Ficino", "Cornelius Agrippa", "Giovanni Battista della Porta", "Pietro Pomponazzi"],
        "related_concepts": ["natural-magic", "cosmic-sympathy", "talismans", "astral-magic", "spiritus-and-pneuma"],
        "body": """## Definition

Occult properties (*proprietates occultae* or *qualitates occultae*; also *virtutes occultae*, "hidden virtues") are the natural qualities of substances that act through the specific nature of the whole substance rather than through the elemental qualities of heat, cold, moisture, and dryness. "Occult" in this context means "hidden"—not in the sense of secret or forbidden but in the sense that these properties cannot be deduced from the manifest elemental composition of the substance; they must be discovered through experience.

The classical example is the magnet's attraction of iron: this cannot be explained through the magnet's hotness, coldness, moistness, or dryness, since these manifest qualities have nothing to do with attraction. The magnet's attractive power is therefore an occult property, rooted in the specific "total substance" (*tota substantia*) or "specific form" (*forma specifica*) of the magnet. Similarly, the *monarchia* (a specific plant) was said to cause the king snake to flee; the lodestone attracted iron but repelled garlic; rhubarb purged the bile though it was not warm and dry; certain stones prevented pregnancy or promoted childbirth.

## Scholastic Framework

The Aristotelian-scholastic tradition developed the concept of occult properties as a residual category for natural effects that resisted elemental explanation. Albertus Magnus discussed occult properties extensively in his commentaries on Aristotle and in his *De mineralibus*, providing a framework for understanding how stones, plants, and animals could have specific powers unexplained by their elemental constitution. Avicenna's *Canon of Medicine* included discussion of *tota substantia* effects in pharmacology, providing medical authority for the concept.

The framework was cautious: occult properties were natural properties, not supernatural ones, and their effects were in principle explicable through natural philosophy even if not through elemental qualities. But the explanatory framework was inevitably vague—if occult properties arose from the "specific form" of a substance, the form itself remained undefined, functioning as a placeholder for whatever explained the otherwise inexplicable effect.

## Natural Magic and Occult Properties

The tradition of natural magic, from the ancient *Kyranides* through Albertus Magnus and Porta to Agrippa, operated primarily through occult properties. Natural magic was the practical art of identifying, extracting, and deploying the hidden virtues of natural things for beneficial purposes. The herbalist who knew which plants had specific healing virtues, the jeweler who knew which stones could attract wealth or ward off disease, the natural magician who understood the correspondence of terrestrial substances with celestial powers—all were working with occult properties.

The key theoretical dispute about occult properties was whether they were genuinely natural (properties of the substances themselves, caused by celestial or formal principles but operating through entirely natural means) or whether they required supernatural assistance to work. The Thomistic position—that demons might be involved in operations apparently relying on occult properties—haunted the tradition throughout the Renaissance, and the elaborate defenses of natural magic as genuinely natural (Ficino, Agrippa, Porta) were all responses to this challenge.

## The Mechanical Philosophy's Challenge

The mechanical philosophy of Descartes, Gassendi, and their followers constituted the most fundamental challenge to the concept of occult properties in the seventeenth century. By insisting that all natural causation worked through matter in motion—through the impact and arrangement of particles of matter—mechanism made "specific form" and "total substance" causation unintelligible. There was no room in a mechanical universe for properties that depended on the particular nature of a substance rather than on its measurable physical properties (size, shape, motion of particles).

Robert Boyle's attack on "occult qualities" (*The Origin of Forms and Qualities*, 1666) argued that specific forms and total substance properties were not genuine explanations but verbal labels that postponed rather than provided understanding. The demand for explanations in terms of measurable mechanical properties effectively delegitimized the concept of occult properties as a scientific category.

Yet the challenge was not entirely clean: Newton's gravitational force, which acted at a distance through empty space without any contact mechanism, bore a suspicious resemblance to the occult action-at-a-distance properties that mechanism had dismissed. Newton was aware of this and sought throughout his career to explain gravity mechanically; his failure to do so left an ineliminable "occult" residue in the foundation of classical physics.

## Scholarly Significance

Occult properties are centrally important to the historiography of Renaissance magic as the explanatory concept that distinguished natural magic from mere superstition (on the practitioners' account) and from legitimate natural philosophy (on the mechanical philosophers' account). The history of occult properties is the history of a contested explanatory category that was productive for approximately fifteen centuries before being delegitimized—a history whose study illuminates both the character of Renaissance natural philosophy and the nature of the Scientific Revolution's methodological innovations.
""",
    },
    {
        "slug": "cunning-folk",
        "title": "Cunning Folk and Popular Magic",
        "category": "Social and Institutional Contexts",
        "summary": "The largely informal practitioners of practical magic in early modern Europe—healers, diviners, and charmers who served community needs for magical assistance with illness, theft, lost property, and relationship problems—distinguished from learned natural magicians above and from malefic witches below, representing the largest stratum of actual magical practice.",
        "related_figures": ["Keith Thomas"],
        "related_concepts": ["witchcraft", "natural-magic", "grimoires", "love-magic", "geomancy"],
        "body": """## Who Were the Cunning Folk?

"Cunning folk" (from Middle English *cunning*, "knowledge, skill") is the English term for the quasi-professional practitioners of beneficial magic who served community needs across early modern Europe. Similar figures appear under different names in other contexts: *saludadores* and *curanderos* in Spain, *benandanti* in Friuli (Carlo Ginzburg's famous case study), *strighe buone* ("good witches") in parts of Italy, *kluge Frauen* ("wise women") and *Wahrsager* ("truth-tellers") in German territories, and so on across European languages and regional traditions.

Keith Thomas's *Religion and the Decline of Magic* (1971) established the cunning folk as a major category for the social history of magic in England, estimating that every English village had access to at least one cunning person and that their services were sought across all social classes for assistance with illness, bewitchment, lost or stolen property, love problems, and identification of enemies. Their practices drew on a mixture of traditional herbal knowledge, folk charm traditions, astrological lore (often derived from cheap printed almanacs), and claimed supernatural powers of sight.

## Services and Techniques

The cunning person's repertoire of services was defined by community needs rather than by any theoretical system. Healing was the most common service: diagnosis and treatment of ailments attributed to supernatural causes (bewitchment, fairy action, ill-wishing) alongside herbal and physical treatments for naturally caused illness. Counter-magic against witchcraft was a closely related service: identifying who had bewitched a client and neutralizing the bewitchment through specific procedures.

Divination for lost or stolen property was another standard service, using a variety of techniques: the suspended key or sieve, the mirror or crystal, geomantic casting, or the urine flask. Love magic, as discussed in the relevant entry, was frequently sought from cunning folk. In some regions, cunning folk claimed to be able to identify the devil's marks on accused witches or to see the future through second sight—services that brought them into contact with the formal apparatus of witch prosecution.

The techniques employed were typically a mixture of orthodox Christian (invocation of the Trinity, use of prayer formulae, reference to saints) and heterodox elements (specific charms, herbs prepared at specific astrological times, procedures derived from the grimoire tradition in simplified or distorted form). The boundary between legitimate Christian prayer and illegitimate magical conjuration was often unclear in practice, and cunning folk regularly operated in this ambiguous zone.

## The Cunning Folk and the Learned Tradition

The relationship between cunning folk practice and the learned magical tradition of Ficino, Agrippa, and Porta was indirect and complex. Cunning folk typically lacked access to learned texts in Latin, though vernacular translations and simplified compilations sometimes reached literate practitioners. The cosmological framework of learned magic (planetary correspondences, Neoplatonic hierarchies, astrological theory) was present in distorted or simplified form in some cunning folk practice, particularly that of literate practitioners who had access to almanacs and vernacular magical handbooks.

More often, cunning folk operated with a different but parallel framework: they knew which herbs and charms worked for which conditions through practice and transmission, without necessarily understanding (or needing to understand) the learned theoretical explanation. The practical convergence between folk and learned magic—the use of sympathetic procedures, correspondences, verbal formulae, timing by the moon or stars—suggests that both traditions drew on a common substrate of pre-theoretical practical knowledge about what worked, which learned magic then rationalized and systematized.

## Prosecution and Social Position

The legal position of cunning folk was ambiguous throughout the early modern period. In England and most of continental Europe, beneficial magic was legally distinguishable from harmful sorcery, though the line in practice was often difficult to draw and shifted over time. Cunning folk who restricted themselves to healing, counter-magic, and divination could often operate relatively openly; those who also provided love magic, cursing services, or who fell under suspicion of maleficent practice were more vulnerable.

The relationship between cunning folk and the formal witch-trial apparatus was complex: cunning folk were sometimes called on to identify witches (their claimed second sight made them useful as expert witnesses), but they could also be accused of witchcraft themselves, particularly if a client died, a healing failed, or if their relationship with local authority became strained. The cunning folk occupied a precarious social position: valued for their services but vulnerable to the same prosecutorial apparatus that targeted malefic witches.

## Scholarly Significance

The cunning folk are important for the historiography of Renaissance magic because they represent the largest stratum of actual magical practice—the layer at which most people encountered magic in practice, rather than in treatises. Understanding what cunning folk actually did, and how their practice related to both elite learned magic above and to the demonic witchcraft of official prosecution below, is essential for a complete picture of the social reality of magic in early modern Europe. The social history of magic initiated by Thomas and Macfarlane and continued by subsequent scholars has substantially developed this dimension of the field.
""",
    },
    {
        "slug": "republic-of-letters",
        "title": "The Republic of Letters and the Circulation of Occult Knowledge",
        "category": "Social and Institutional Contexts",
        "summary": "The pan-European community of learned correspondents who exchanged manuscripts, books, and ideas across political and confessional boundaries, providing one of the primary channels through which magical and occult knowledge circulated among educated practitioners in the fifteenth through seventeenth centuries.",
        "related_figures": ["Cornelius Agrippa", "John Dee", "Johannes Trithemius", "Marsilio Ficino"],
        "related_concepts": ["printing-and-the-occult", "patronage-and-magic", "rosicrucianism", "natural-magic"],
        "body": """## The Republic of Letters

The *Respublica literaria* or "Republic of Letters" denotes the informal trans-European community of learned humanists, scientists, theologians, and philosophers who maintained contact through correspondence, book exchange, and occasional personal meetings throughout the early modern period. The term suggests a community defined by participation in learned culture rather than by political borders, religious affiliation, or social rank—though in practice it was predominantly male, predominantly elite, and predominantly (if not exclusively) Latin-literate.

For the circulation of magical and occult knowledge, the Republic of Letters served several important functions. It enabled the exchange of manuscripts before or instead of print publication, allowing sensitive texts (including magical works) to circulate among trusted correspondents without the risks of public printing. It provided networks of validation: a new magical or philosophical claim could be tested against the reactions of learned correspondents before being committed to print. And it created communities of shared interest that could sustain and develop occult philosophical programs over decades, providing the social infrastructure for long-term projects.

## Trithemius and Early Networks

Johannes Trithemius, abbot of Sponheim (1462–1516), was one of the most assiduous letter-writers of his generation and one of the central nodes in early sixteenth-century learned networks connecting German humanists, natural philosophers, and occult thinkers. His voluminous correspondence included exchanges with Agrippa, with the humanist Conrad Celtis and the Rhenish humanist circles, and with a wide range of correspondents across Germany and beyond.

Trithemius's position as an abbot gave him access to one of the best libraries in Germany (his collection at Sponheim eventually ran to over 2000 volumes, extraordinary for the period) and provided legitimacy for his interest in cryptography, natural philosophy, and what he called *steganography* (the art of secret writing, which included a magical dimension he deliberately concealed). His correspondence was a key channel through which knowledge of Neoplatonic philosophy, alchemical theory, and magical texts circulated in early sixteenth-century Germany.

## Agrippa's Networks

Cornelius Agrippa's career illustrates both the possibilities and the instabilities of the Republic of Letters for practitioners of magical philosophy. Agrippa maintained extensive correspondence across Europe, sending early versions of his *Occult Philosophy* to Trithemius for evaluation, maintaining contacts with learned circles in France, England, Spain, and Italy, and leveraging these networks for patronage, protection, and intellectual validation.

The circulation of the *Occult Philosophy* in manuscript before its publication in 1531 exemplifies how the Republic of Letters mediated between manuscript and print culture: the work reached a substantial educated audience for twenty years before print, accumulating reactions, suggestions, and endorsements (notably from Trithemius, whose letter praising the work was included in the published edition) that shaped both the text and its reception.

## Dee's International Networks

John Dee's career shows how the Republic of Letters could connect occult practitioners across confessional divides and national borders. Dee corresponded with and visited learned figures across Protestant Germany, Catholic Poland, and Bohemia during his continental travels (1583–89); his connections included the mathematician and natural philosopher Wilhelm IV of Hesse, the physician Leonhard Thurneisser, and various figures at the imperial court of Rudolf II. These networks facilitated the circulation of his published works, the sharing of manuscripts, and the patronage relationships that sustained his angelic project.

Dee's case also illustrates the limits of the Republic of Letters for occult practitioners: political and confessional tensions could override learned solidarity, and the suspicion of diabolical practice that attached to his angelic work made some potential correspondents reluctant to maintain visible connections.

## Scholarly Significance

The Republic of Letters as a framework for understanding the circulation of occult knowledge has been productively developed by scholars drawing on intellectual network analysis, book history, and correspondence studies. The tools of digital humanities—mapping correspondence networks, tracing manuscript and book provenance, identifying clusters of shared reading—are particularly well-suited to this kind of social history of knowledge. Work by scholars including Anthony Grafton, Ann Blair, and more recently focused studies of specific networks (Florike Egmond on natural history networks, Deborah Harkness on London's scientific community) has illuminated the social infrastructure of learned magical culture in ways that purely textual analysis of individual works cannot.
""",
    },
    {
        "slug": "imagination-as-magical-faculty",
        "title": "Imagination as Magical Faculty",
        "category": "Metaphysical Foundations",
        "summary": "The Renaissance philosophical account of the imagination (phantasia, imaginatio) as a faculty with genuine causal power operating through spiritus—capable of healing or harming both the imaginer's own body and others', and of accessing cosmic truths through inspired visionary states; a crucial bridge between medical theory, magical theory, and neo-Platonic epistemology.",
        "related_figures": ["Marsilio Ficino", "Cornelius Agrippa", "Pietro Pomponazzi", "Giordano Bruno"],
        "related_concepts": ["spiritus-and-pneuma", "natural-magic", "fascination-and-evil-eye", "art-of-memory", "cosmic-sympathy"],
        "body": """## The Faculty

The imagination (*phantasia* in Greek, *imaginatio* in Latin) is the faculty of the soul responsible for forming, storing, and manipulating images (*phantasmata* or *imagines*). In Aristotelian psychology, the imagination was intermediate between sense perception (which required the presence of the object) and intellect (which operated on universal concepts abstracted from images): it worked with images of absent or non-existent objects, enabling memory, anticipation, and creative thought.

Renaissance thinkers, drawing on the Aristotelian faculty psychology mediated through Avicenna's influential account, gave the imagination a substantially enhanced role. Avicenna had argued that a powerful imagination could impress itself on external matter—a claim elaborated in his discussion of prophetic knowledge and in his account of how the soul could affect the body during illness and health. This "active imagination" capable of external effects became a cornerstone of Renaissance magical theory.

## Spiritus and the Active Imagination

The mechanism connecting the Renaissance imagination to its alleged external effects was the *spiritus* theory. The imagination operated through *spiritus animalis* in the brain, creating configurations of refined vapor that corresponded to the images formed. When the imagination was strongly activated—by powerful emotion, by concentrated will, or by specific techniques (as in the art of memory)—it produced particularly charged configurations of *spiritus* that could:

1. Affect the body of the imaginer directly (explaining psychosomatic effects: imagining a frightening thing caused pallor; imagining warmth caused perspiration; imagining illness could produce illness)
2. Project outward through the eyes (explaining fascination and the evil eye)
3. Impress itself on the developing fetus (explaining maternal imagination effects: a pregnant woman who was frightened by a hare gave birth to a harelipped child)

Pietro Pomponazzi (*De incantationibus*, c. 1520) made the active imagination central to his naturalistic account of all apparently miraculous phenomena: sufficiently strong imagination, combined with receptive matter, could produce effects that appeared supernatural but were in fact natural. This was the most radical extension of the imagination's role—essentially eliminating any need for supernatural agency in the explanation of magical events.

## Ficino's Visionary Imagination

Ficino's account of imagination in the *Platonic Theology* and *De amore* gave it an additional epistemological role: in states of divine frenzy (*furor divinus*), the imagination could transcend its ordinary function of processing sensory images and receive higher impressions from the World Soul or even from the divine Intellect. The inspired poet, the religious visionary, and the prophetic dreamer all experienced states in which the imagination was elevated beyond its ordinary operation to receive cosmic truth.

This elevated imagination was continuous with the magical imagination: both operated through *spiritus*, both involved an openness to influences beyond ordinary sensory experience, and both presupposed the animistic cosmos in which soul and cosmos were in continuous communication. The inspired poet's imaginative vision and the natural magician's imaginative manipulation of *spiritus* were different modes of the same fundamental faculty.

## Bruno's Mnemonics and Imagination

Giordano Bruno's art of memory (discussed in the relevant entry) was premised on a theory of the imagination as capable of "stamping" the mind with cosmic images—images so charged with cosmic significance that the trained imagination became itself a microcosm, capable of moving through and operating on the macrocosm. For Bruno, the properly trained imagination was the instrument of genuine magical power: the sage whose imagination had been filled with the images of all cosmic powers was capable of moving those powers through the power of his own mental activity.

Whether this magical imagination was literal (the trained mind genuinely acquiring causal power over external events) or metaphorical (a philosophical account of the sage's comprehensive understanding of natural forces, enabling practically effective action) is debated. Bruno's language seems to claim the former, but the texts resist clean interpretation.

## Scholarly Assessment

The imagination as magical faculty has been studied primarily through the lens of spiritus theory (Walker, Copenhaver) and through the history of faculty psychology (Park, Keele). More recent scholarship, particularly Guido Giglioni's work on imagination in Renaissance natural philosophy, has examined the concept with close attention to specific Renaissance texts and their medical and philosophical sources. The imagination is significant as a point where medical theory (the *spiritus* account of psychosomatic phenomena), natural philosophy (the active imagination as a natural causal power), and magical theory (the imagination as instrument of magical operation) converge—making it impossible to separate these domains cleanly in Renaissance thought.
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
    print(f"\nBatch 9 done: {inserted} inserted, {skipped} skipped.")


if __name__ == "__main__":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
    main()
