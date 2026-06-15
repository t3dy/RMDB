"""Seed concepts table — Batch 10: Quintessence, Gematria, Magic and Medicine, Enochian, Copernican Revolution."""

import sqlite3
import json
import sys
import io
from datetime import datetime

DB_PATH = "db/renmagic.db"

CONCEPTS = [
    {
        "slug": "quintessence",
        "title": "Quintessence",
        "category": "Cosmology and Natural Philosophy",
        "summary": "The 'fifth element' or 'aether' posited by Aristotle as the substance of the celestial bodies, incorruptible and eternally in circular motion; adapted by Renaissance alchemists and natural magicians as the refined extract of any substance from which its specific virtue could be concentrated and extracted for medical or magical use.",
        "related_figures": ["Marsilio Ficino", "Paracelsus", "Cornelius Agrippa"],
        "related_concepts": ["alchemy", "spiritus-and-pneuma", "astral-magic", "natural-magic", "prima-materia"],
        "body": """## The Aristotelian Fifth Element

In Aristotle's cosmology, the four terrestrial elements (earth, water, fire, air) were subject to generation and corruption—they could combine, transform, and dissolve. The celestial bodies (sun, moon, planets, fixed stars) were made of a different, fifth substance (*pempton soma* in Greek, later *quinta essentia* in Latin) that was incorruptible, neither hot nor cold nor moist nor dry, and moved naturally in eternal circles. This fifth element explained why celestial bodies did not age, decay, or change in nature—they were made of an entirely different kind of stuff from everything below the lunar sphere.

Medieval natural philosophers called this substance the "fifth essence" (*quinta essentia*) and associated it with the Stoic *pneuma* and with the luminous, refined substance sometimes identified as *lux* (light). The question of whether it was identical with *spiritus* or *pneuma*—the refined substance connecting soul to body in Galenic medicine and Stoic cosmology—was answered differently by different thinkers, but the overlap was significant: all these concepts described a substance intermediate between gross matter and pure spirit, associated with vital activity and celestial influence.

## Alchemical Quintessence

In alchemical theory, the concept of quintessence was adapted to refer to the most refined extract of any natural substance—the concentrated essence that carried the substance's specific virtue most powerfully. The alchemist could, through distillation and other refining processes, extract the "quintessence" of a plant, mineral, or animal substance—separating the vital, active virtue from the gross elemental matter in which it was embedded and producing a concentrated preparation of exceptional potency.

This alchemical quintessence was not the same as Aristotle's celestial fifth element, though the terminology deliberately invoked the Aristotelian framework. Rather, it was the most refined, subtle, and volatile fraction of any natural substance—obtained through repeated distillation—that carried the substance's occult properties in their most concentrated and accessible form. Paracelsus made the extraction of quintessences central to his pharmaceutical program: alchemically prepared *arcana* (specific remedies) were powerful precisely because they had been refined to their quintessential virtue, separating the active healing principle from the inert gross matter.

## Ficino's Spiritus and the Celestial Quintessence

Marsilio Ficino's natural magic theory drew explicitly on the concept of quintessence as the substance linking the terrestrial and celestial realms. In *De vita* (1489), Ficino argued that certain substances—particularly wine, aromatic preparations, gold, and gems—contained a proportion of quintessential *spiritus* that was effectively a portion of the celestial substance, enabling them to act as conduits for planetary influences. The distilled essences of aromatic plants (particularly those associated with specific planets) could be used in suffumigations that concentrated planetary *spiritus* in the practitioner's immediate environment.

Ficino's concept of quintessential *spiritus* provided the mechanism linking the theory of cosmic sympathy (planets affect terrestrial things through their shared quintessential nature) to the practice of astral magic (concentrating planetary influence through quintessence-rich substances). It also explained why certain substances were particularly effective magical media: they contained more of the quintessential *spiritus* that carried celestial virtue than their gross elemental composition would suggest.

## The Decline of Quintessential Thinking

The concept of celestial quintessence was fatally undermined by the new astronomy. If the celestial bodies were not made of a special incorruptible substance but were physically similar to terrestrial matter (subject to the same laws of motion, as Newton's gravitational theory implied), then the theoretical basis for quintessential distinctions between celestial and terrestrial matter disappeared. By the late seventeenth century, the concept of quintessence as a natural philosophical category had become intellectually untenable, surviving primarily in alchemical and popular usage detached from its original cosmological framework.

The word "quintessential" survives in modern English in the sense of "most perfectly representative" or "most concentrated"—a linguistic trace of the alchemical and natural magical tradition in which the quintessence of a substance was its perfect, concentrated essence. This semantic residue illustrates how concepts can persist in language after their original theoretical context has dissolved.
""",
    },
    {
        "slug": "gematria-and-letter-mysticism",
        "title": "Gematria and Letter Mysticism",
        "category": "Kabbalah",
        "summary": "The Kabbalistic practices of assigning numerical values to Hebrew letters and deriving hidden meanings from numerical equivalences between words and phrases—one of the most characteristic techniques of both Jewish Kabbalah and Christian Kabbalah, and a source for the magical sigil generation central to Renaissance ceremonial magic.",
        "related_figures": ["Giovanni Pico della Mirandola", "Cornelius Agrippa", "Johannes Reuchlin"],
        "related_concepts": ["kabbalah-and-christian-kabbalah", "sefirot", "magic-squares", "divine-names", "natural-magic"],
        "body": """## The Techniques

Jewish tradition developed three main techniques for finding hidden meaning through the manipulation of Hebrew letters and their numerical values:

**Gematria**: Each Hebrew letter has a numerical value (Alef=1, Bet=2, ..., Yod=10, Kaf=20, ..., Kuf=100, ..., Tav=400). Words and phrases can be compared by summing their letters: if two words share the same numerical value, they are in some sense equivalent and can illuminate one another's meaning. The most famous example is the word *Ahava* (love, = 13) and *Echad* (one, = 13): their equivalence reveals that love and unity are fundamentally connected. The name of God's angel *Metatron* (= 314) was equated with *Shaddai* (= 314), identifying Metatron as the one through whom God's power was manifested.

**Notarikon**: The initial or final letters of words in a biblical phrase are taken as abbreviations, spelling out a hidden phrase; or conversely, the letters of a single word are treated as initials spelling out a longer phrase. This technique was used to find abbreviated divine teachings compressed into apparently simple words.

**Temurah**: Letters are systematically substituted for one another according to specific cipher tables (the most famous being *Atbash*, in which Alef substitutes for Tav, Bet for Shin, etc., reversing the alphabet). By applying temurah, hidden names and meanings within the sacred text could be revealed.

## Theological Basis

The theological basis for letter mysticism in Jewish tradition was the doctrine that Hebrew is the divine language—the language God used to create the world ("God said, 'Let there be light'"), the language in which Torah was revealed, and the language whose letters carry genuine divine power. The thirty-two "paths of wisdom" of the *Sefer Yetzirah* (an early Kabbalistic text on creation), consisting of the ten Sefirot and the twenty-two letters of the Hebrew alphabet, provided the framework within which the creative power of letters was theorized.

If the letters were the instruments of divine creation, then manipulating letters—discovering their hidden equivalences, combinations, and permutations—was a form of engaging with the structure of reality itself. The practitioner who knew the hidden letter-combinations (*tzerufim*) that God had used in creation could potentially replicate or redirect creative divine power—the theoretical basis for the creation of the Golem through letter manipulation.

## Christian Kabbalist Appropriation

Christian Kabbalists appropriated gematria and letter mysticism with enthusiasm, finding in Hebrew letter-number equivalences confirmation of Christian doctrines and a source for magical procedures. Pico della Mirandola's ninety-eight "Kabbalistic conclusions" drew heavily on gematria, arguing that specific Hebrew letter-number values confirmed the Trinity, the divine sonship of Christ, and the structure of the angelic hierarchy.

Cornelius Agrippa's integration of gematria with magic squares (as discussed in the relevant entry) was particularly productive: by converting the letters of angelic names to numbers using the Hebrew numeral system and plotting these numbers through the appropriate planetary magic square, the practitioner could generate geometrical figures (sigils) that served as the signatures or seals of specific angelic beings. This procedure gave the apparently arbitrary graphic symbols of ritual magic a pseudo-mathematical derivation from the divine names—lending them a kind of occult rationality.

## Broader Letter Mysticism

Beyond the specific techniques of gematria, notarikon, and temurah, the broader tradition of letter mysticism held that the twenty-two Hebrew letters, as the instruments of divine creation, were present in some sense in all created things—that every natural object expressed, in its form and properties, the creative letter-power from which it had been generated. This idea was elaborated in the doctrine of *Signa Naturae* or "signatures of nature" (associated particularly with Paracelsus and Jacob Böhme): nature itself was a divine text whose letters could be read by the properly trained eye.

This convergence of Jewish letter mysticism with the doctrine of natural signatures exemplifies the synthetic character of Renaissance Kabbalah: by connecting a specifically Jewish technique with a broadly held natural philosophical doctrine, Christian Kabbalists created frameworks that could operate across confessional and traditional boundaries, drawing Jewish, Christian, and natural philosophical resources into a single synthetic system.
""",
    },
    {
        "slug": "magic-and-medicine",
        "title": "Magic and Medicine",
        "category": "Social and Institutional Contexts",
        "summary": "The complex and historically varying relationship between learned medicine and the occult sciences in Renaissance Europe—both overlapping in theory (through the spiritus framework, astrological medicine, and Paracelsian chemistry) and in tension institutionally, as the medical profession sought to define legitimate practice against magical alternatives.",
        "related_figures": ["Marsilio Ficino", "Paracelsus", "Pietro Pomponazzi", "Joan Baptista van Helmont"],
        "related_concepts": ["spiritus-and-pneuma", "natural-magic", "paracelsianism", "astral-magic", "macrocosm-and-microcosm"],
        "body": """## The Theoretical Overlap

In the Renaissance, medicine and magic were not neatly separable domains but overlapping fields that shared theoretical frameworks, contested practices, and ambiguous practitioners. Both drew on the same natural philosophical vocabulary: the four humors and four elements of Galenic medicine, the *spiritus* theory connecting soul and body, the astrological framework of celestial influence on human health, and the doctrine of occult properties in natural substances. A learned physician who advised patients on astrological timing for bloodletting, prescribed mineral and plant remedies according to their occult virtues, and made use of *spiritus*-based accounts of how medicines acted was employing the same conceptual apparatus as a natural magician—the difference lay in therapeutic goal and institutional context, not in fundamental theory.

Marsilio Ficino's *Three Books on Life* (1489) explicitly positioned itself as medical advice, framing its astral magic as a form of therapeutic care for the scholarly body: the scholar's Saturnine constitution required Solar and Jovial medicine, delivered through the appropriate use of musical, dietary, and material means. Whether Ficino's procedures were medicine or magic was a question Ficino himself recognized as difficult, and his careful insistence on natural mechanism reflects awareness of the boundary's instability.

## Astrological Medicine

The most institutionally established overlap between medicine and the occult sciences was astrological medicine. University medical curricula in Renaissance Italy required students to study astrology alongside anatomy, Galenic theory, and pharmacology: the physician needed to cast horoscopes, understand the effects of planetary conjunctions on disease prognosis, and time therapeutic interventions (bloodletting, purging, medication) according to the lunar phase and planetary hours.

This integration was not peripheral but central: major medical textbooks (including works by the highly regarded Girolamo Cardano) integrated astrological considerations throughout their clinical discussions. Medical astrology operated on the basis of the macrocosm/microcosm analogy—each planet governed specific organs and humors, and celestial configurations affected these organs' function—providing a systematic framework for understanding why diseases appeared at particular times and why some patients recovered while others did not.

## Paracelsian Chemical Medicine

The Paracelsian movement of the late sixteenth and seventeenth centuries intensified the overlap between medicine and magic by introducing a specifically chemical and theosophical dimension. Paracelsian medicine replaced Galenic humoral theory with a chemical framework (the *tria prima* of sulphur, mercury, and salt) and therapeutic program (alchemically prepared mineral and metallic remedies), while grounding this chemistry in a cosmological and theological account of nature that drew on Hermetic, Neoplatonic, and magical traditions.

From the perspective of Galenic medicine, Paracelsian chemical remedies were dangerously close to poisons (many Paracelsian specifics—antimony, arsenic, mercury compounds—were highly toxic in careless use), while the theoretical justification (alchemical principles, cosmic signatures, divine light in nature) was uncomfortably close to magical rather than medical reasoning. The controversy between Galenists and Paracelsians in the later sixteenth century was partly a dispute about the proper relationship between medicine and the occult sciences.

## Institutional Tensions

The medical profession's institutional development in the Renaissance—through guild organization, university faculties, and royal licensing—created formal boundary-maintenance mechanisms that excluded practitioners of magical healing. The London College of Physicians (founded 1518) prosecuted unlicensed practitioners including cunning folk, wise women, and Paracelsian chemical practitioners, partly on grounds of intellectual illegitimacy (they lacked university training) and partly on grounds of dangerous practice.

These institutional exclusions were not simply about competence but about the definition of legitimate medical theory: learned medicine required a specific theoretical framework (Galenic humoral theory, classical pharmacology, astrological medicine within limits), and practitioners who substituted occult or magical frameworks for this classical learning were by definition outside the professional pale. The boundaries were contested throughout the period, and the eventual triumph of a more thoroughly naturalistic medicine required institutional as well as intellectual transformation.

## Scholarly Significance

The history of medicine and magic in the Renaissance is important because it shows how the supposed opposition between rational medicine and magical healing was historically constructed rather than given. What counted as legitimate medicine versus illegitimate magic was determined as much by institutional power, professional interest, and confessional politics as by any self-evident difference in therapeutic efficacy or theoretical coherence. Studies by historians including Andrew Wear, Harold Cook, and Katharine Park have illuminated this dimension, showing how the boundaries of legitimate medical practice were drawn and maintained through social processes as well as intellectual argument.
""",
    },
    {
        "slug": "enochian-system",
        "title": "The Enochian System",
        "category": "Angelology",
        "summary": "The elaborate angelic language, cosmological map, and system of ritual invocations received by John Dee and Edward Kelley through scrying sessions from 1582 to 1589, claiming to be the original language of angels and of Adam before the Fall, and providing a systematic framework for angelic communication and apocalyptic prophecy.",
        "related_figures": ["John Dee", "Edward Kelley"],
        "related_concepts": ["scrying-and-crystal-gazing", "angelic-hierarchy", "grimoires", "kabbalah-and-christian-kabbalah", "divine-names"],
        "body": """## Origins and Reception

The Enochian system is the elaborate body of angelic teaching received by John Dee (1527–1608/09) and his scryer Edward Kelley (1555–1597) through a series of scrying sessions conducted primarily between 1582 and 1589, first in England and then on the Continent (Poland and Bohemia). Dee recorded these sessions meticulously in a series of notebooks, now partly preserved at the British Library and the Bodleian, which document the progressive revelation of an angelic language, a cosmological map of the celestial hierarchy, a set of ritual calls or invocations in the angelic language, and a series of prophetic messages about the imminent transformation of world religion.

The system was named "Enochian" by later commentators after the biblical Enoch (Genesis 5:24, "Enoch walked with God, and he was not; for God took him"), the antediluvian patriarch who was said to have been taken by God without dying and to have received divine secrets—the name implying that Dee and Kelley were recovering the angelic knowledge that Enoch had originally received. The angels themselves called the language they delivered *Angelical* or the language of *Enoch*.

## The Angelic Language

The most striking element of the Enochian system is the elaborate language delivered through Kelley's scrying: an apparently complete language with its own alphabet (the Enochian or *Angelical* script), vocabulary, grammar, and syntax, presented as the original language spoken by God and the angels and by Adam before the Fall. The angels delivered the language in reverse order (the Lord's Prayer in Enochian was given backwards, letter by letter) to prevent its power from inadvertently manifesting during transmission—a procedure that itself implied genuine concern about the language's causal efficacy.

Whether the Enochian language is a genuine natural language with consistent grammatical structure or an inspired artifact of Kelley's unconscious invention has been the subject of both scholarly and amateur analysis. Linguists have found partial but not complete grammatical consistency, which neither confirms nor refutes the hypothesis of genuine supernatural origin—or of sophisticated conscious or unconscious linguistic creativity.

## The Cosmological Map

Alongside the language, the angelic communications delivered a detailed cosmological map: the Enochian system distinguished thirty Aethyrs or Aires (concentric zones of the celestial realm), each governed by specific angelic rulers; four Watchtowers governing the four directions; and a complex hierarchy of governors, seniors, and angelic officers whose names, sigils, and powers were specified in detail. This hierarchy bore some relationship to conventional Renaissance angelology (the four elements, the four cardinal directions, hierarchical governance) but differed substantially in its specific structure and nomenclature from both Pseudo-Dionysian and Agrippa-derived traditions.

Dee understood this cosmological map as authoritative divine revelation—an accurate account of the celestial hierarchy that superseded earlier, fallible human accounts. His aspiration, evident in the diaries, was to use this authoritative knowledge to purify Christian religion and enable a universal religious reform under the patronage of Elizabeth I and subsequently of Rudolf II.

## The Forty-Eight Calls

The forty-eight Calls (also known as Keys or Claves Angelicae) constitute the ritual dimension of the Enochian system: verbal invocations in the Enochian language that addressed specific levels of the Aethyrs and their governors. The Calls were delivered to Dee and Kelley incrementally, and they represent the most practically oriented element of the system—the means by which the practitioner could formally address the angelic beings of the hierarchy.

The angelic instructions provided specific contexts for using the Calls, including invocations of the Watchtower angels for elemental operations, approaches to the Aethyr governors for prophetic revelation, and a general cosmological framework within which all invocations were situated. The system thus combined a comprehensive angelic cosmology with a practical ritual program—an integration characteristic of the theurgic tradition from Iamblichus through Agrippa.

## Later Influence

The Enochian system had limited influence in Dee's own time—the complexity of the material and its unpublished state (the diaries remained in manuscript) prevented wide dissemination. Its major later influence came through the work of seventeenth-century occultists (particularly Elias Ashmole, who acquired Dee's diaries) and more substantially through the Hermetic Order of the Golden Dawn in the late nineteenth century, which incorporated an adapted version of the Enochian system into its initiation rituals and magical practice. This Golden Dawn Enochian became a major current in twentieth-century Western ceremonial magic, ensuring that Dee and Kelley's original material remained actively used by magical practitioners.

Scholarly analysis of the Enochian material has been substantially advanced by Deborah Harkness (*John Dee's Conversations with Angels*, 1999), György Szőnyi (*John Dee's Occultism*, 2004), and the critical edition and translation of the diaries by Joseph Peterson and others, making the primary sources accessible for systematic historical study for the first time.
""",
    },
    {
        "slug": "copernican-revolution-and-magic",
        "title": "The Copernican Revolution and the Occult Sciences",
        "category": "Cosmology and Natural Philosophy",
        "summary": "The complex and contested impact of Copernican heliocentric astronomy on the cosmological frameworks that sustained Renaissance astrology, talismanic magic, and Neoplatonic natural philosophy—neither immediately destructive nor simply irrelevant, but requiring new conceptual resources that practitioners and critics worked out across the sixteenth and seventeenth centuries.",
        "related_figures": ["Giordano Bruno", "Johannes Kepler", "Marsilio Ficino", "Cornelius Agrippa"],
        "related_concepts": ["learned-astrology", "neoplatonism", "macrocosm-and-microcosm", "magic-and-the-scientific-revolution", "ptolemaic-cosmos"],
        "body": """## The Heliocentric Challenge

Nicolaus Copernicus's *De revolutionibus orbium coelestium* (1543) proposed that the sun rather than the earth occupied the center of the cosmos, with the earth moving around it annually and rotating on its own axis diurnally. This "Copernican revolution" (the phrase was Kant's, much later) had profound implications for the cosmological frameworks on which Renaissance astrology, natural magic, and Neoplatonic philosophy depended—though these implications were worked out gradually and unevenly over more than a century.

The most immediate challenge was to astrological theory: if the earth moved rather than the sun and planets, then the entire apparatus of horoscopic astrology—based on the apparent positions of celestial bodies as seen from a stationary earth—required reinterpretation. Did astral influence still operate the same way if the "movement" of the planets was partly an artifact of the earth's own motion? Were the houses of the horoscope still meaningful if the earth was no longer at the center of the universe?

## Giordano Bruno and the Infinite Cosmos

Giordano Bruno's embrace of Copernican cosmology—and his extension of it into an infinite universe of infinite worlds—represents one of the most dramatic responses to the heliocentric challenge from within the natural magic tradition. Bruno's *De l'infinito universo et mondi* (1584) argued for an infinite universe with no center at all: every world had its own "center" relative to its inhabitants, and the sun was merely the "world" of our local system, not the center of everything.

Bruno's infinite cosmos created problems for traditional hierarchical cosmology (how could there be a single cosmic hierarchy if the universe had no center and no boundary?) but also liberated Neoplatonic natural magic from its dependence on the old Ptolemaic framework. If the World Soul animated an infinite universe rather than a bounded geocentric one, the scope of natural magical sympathy was correspondingly infinite—a feature that Bruno found philosophically exciting rather than threatening.

## Kepler's Compromise

Kepler's response to the Copernican challenge in astrology exemplifies the creative adaptation that characterized the best Renaissance thinking about these issues. Kepler explicitly rejected the traditional framework of horoscopic astrology (the zodiac signs and houses) as arbitrary constructions with no physical basis, while insisting on the genuine reality of planetary aspects—the mathematical angles between planetary positions as seen from the earth.

On Kepler's account, the human soul was attuned to harmonic ratios by virtue of its creation by a God who had created the world according to geometry. When the planets formed harmonic angles (120° trine, 60° sextile, 90° square, 180° opposition), the resulting configuration resonated with the soul's own harmonic structure, producing real effects on human mood and disposition. This reformed astrology was both Copernican (the earth moved) and anti-traditional (no signs, no houses, no traditional planetary dignities), but it preserved the core astrological claim that celestial configurations genuinely affected human beings.

## The Slow Undermining of Magical Cosmology

The Copernican revolution did not immediately destroy the cosmological framework supporting Renaissance magic. Throughout the later sixteenth century, most practicing astrologers continued to use Ptolemaic geocentric models for astrological calculation, since the heliocentric and geocentric models produced mathematically equivalent predictions of planetary positions. The philosophical implications of heliocentrism for the interpretation of astrological influence were debated but did not immediately destabilize practice.

What did gradually undermine the magical cosmology was the combination of heliocentrism with other developments: the infinite universe of Bruno, which dissolved the hierarchical distinction between celestial and terrestrial; the new physics of Galileo and Descartes, which insisted on the same laws of motion governing both celestial and terrestrial bodies; and Newton's gravitation, which provided a unified quantitative account of celestial motion that left no room for the animating intelligences and sympathetic *spiritus* that had been the mechanisms of magical action.

## Scholarly Significance

The Copernican revolution and the occult sciences is a topic that illustrates the complexity of the relationship between "magic" and "science" in the early modern period: the same astronomical development that eventually undermined the framework of Renaissance magic was also embraced by one of the most committed natural magicians of the age (Bruno) and contributed to one of the most mathematically sophisticated defenses of astrological theory (Kepler). The outcome—a new natural philosophy that made "occult" cosmology untenable—was not predictable from the Copernican premise alone but required the entire sequence of developments from Copernicus through Newton.
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
    print(f"\nBatch 10 done: {inserted} inserted, {skipped} skipped.")


if __name__ == "__main__":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
    main()
