"""Seed concepts table — Batch 8: Malleus Maleficarum, Geomancy, Sefirot, Prima Materia, Translation Movements."""

import sqlite3
import json
import sys
import io
from datetime import datetime

DB_PATH = "db/renmagic.db"

CONCEPTS = [
    {
        "slug": "malleus-maleficarum",
        "title": "Malleus Maleficarum",
        "category": "Demonology and Witchcraft",
        "summary": "The 'Hammer of Witches' (1486) by Heinrich Kramer, the most influential and notorious demonological treatise of the early modern period, which systematized witchcraft theory, justified torture, and provided the prosecutorial framework for the wave of witch trials that followed its publication.",
        "related_figures": ["Heinrich Kramer", "Johann Weyer", "Jean Bodin"],
        "related_concepts": ["witchcraft", "demonology", "demonic-pact", "gender-and-magic"],
        "body": """## The Text and Its Context

The *Malleus Maleficarum* ("Hammer of Witches"), published in 1486, was written primarily by Heinrich Kramer (Institoris), a Dominican inquisitor who had conducted witch trials in the Tyrol with results he found unsatisfactory—local authorities and clergy had resisted his procedures, and several accused persons had been freed. The text, nominally co-authored by Jakob Sprenger (though Sprenger's actual contribution is disputed by modern scholars), was intended partly to justify Kramer's controversial methods and partly to provide a comprehensive manual for the identification and prosecution of witches.

The *Malleus* was published with a papal bull, *Summis desiderantes affectibus* (1484), from Innocent VIII, which had authorized Kramer's inquisitorial activities in Germany. This association with papal authority gave the text considerable weight, though it was never formally adopted by the Church as official doctrine. Subsequent editions amplified the papal endorsement in the front matter, giving many readers the impression of a more official status than the text actually possessed.

## Structure and Content

The *Malleus* is organized in three parts. Part I addresses the question of whether witchcraft is real, arguing against skeptics that the devil's power, human complicity in it, and God's permission of it are all real and provable. Part II describes the specific activities of witches—their pact with the devil, their attendance at the sabbath, their capacity for harm (*maleficium*), their ability to harm men's sexual function (*ligature* or binding magic), and their power to generate illusions. Part III provides detailed judicial procedure for prosecuting witchcraft cases, including the use of torture to extract confessions and the forms of sentence.

The *Malleus*'s treatment of women is one of its most notorious features. Part I includes an extended argument for women's greater susceptibility to diabolical seduction, grounded in misogynist etymology (*femina* = *fides* + *minus*, "less faith"), moral psychology (women's greater credulity, inconstancy, and carnality), and physical constitution. This misogynist argument provided theological grounding for the disproportionate prosecution of women in witch trials, though it was not the only factor in the gendering of witchcraft prosecution.

## Influence and Limits

The *Malleus* was widely read and widely cited in the century after its publication, appearing in numerous editions and influencing both learned demonological treatises and practical witchcraft prosecution. But its influence was not uniform: some important demonologists (Bodin, Remy, de Lancre) engaged with it critically while accepting its fundamental framework; others (Weyer, Scot) challenged its claims systematically; and actual prosecutors often used it selectively, adapting its procedures to local legal customs rather than following it mechanically.

Modern scholarship has substantially complicated the older view of the *Malleus* as the single driving force behind the witch trials. Brian Levack, Lyndal Roper, and others have shown that the trials were driven by local dynamics—accusation patterns, community conflicts, zealous prosecutors, specific legal frameworks—that the *Malleus* influenced but did not determine. In some of the most intense prosecution areas (Scotland, the Trier region), the *Malleus* was not particularly central; in others, it provided the authoritative reference framework within which accusers, accused, and prosecutors all operated.

## Scholarly Assessment

The *Malleus* has been the subject of sustained feminist and gender-historical analysis, which has illuminated both its specific misogynist arguments and their role in structuring witch prosecution practice. Scholars including Lyndal Roper (*Witch Craze*, 2004) and Diane Purkiss (*The Witch in History*, 1996) have examined how the *Malleus*'s fantasies of female sexual and reproductive power—its particular obsession with malefic attacks on male sexual function and infant bodies—reflected specifically male anxieties about women's bodies rather than any transhistorical reality. The *Malleus* remains a central document for understanding both the witch trials and the broader culture of misogyny within which they operated.
""",
    },
    {
        "slug": "geomancy",
        "title": "Geomancy",
        "category": "Magic Theory and Practice",
        "summary": "The divinatory art of generating and interpreting sixteen figures formed by casting sand, soil, or dots and analyzing the resulting patterns according to an elaborate system of correspondence with planets, signs of the zodiac, and houses; one of the most widely practiced forms of divination in the medieval and Renaissance Islamic and European worlds.",
        "related_figures": ["Cornelius Agrippa"],
        "related_concepts": ["learned-astrology", "natural-magic", "grimoires"],
        "body": """## The Art and Its Method

Geomancy (from Greek *ge*, earth, + *manteia*, divination) is the divinatory art of generating binary figures through random processes involving earth or similar materials (casting seeds, sand, pebbles, or making dots in soil), organizing these figures into a complex of sixteen positions, and interpreting the resulting pattern through an elaborate system of correspondence with astrology.

The basic procedure generated sixteen "mothers" (the initial four figures derived from the random casting), which were combined through a series of mechanical operations to produce "daughters," "nephews," and finally two "witnesses" and a "judge." The sixteen fundamental figures (each a combination of four binary values) were named (*Via*, *Cauda Draconis*, *Puer*, *Fortuna Maior*, etc.) and assigned to planets, zodiacal signs, astrological houses, and elemental qualities. The geomancer's skill lay in interpreting this complex of assignments in relation to a specific question.

## Arabic Origins and European Transmission

Geomancy as practiced in medieval and Renaissance Europe was an Arabic import. The art was called *'ilm al-raml* ("science of sand") in Arabic, and its theoretical elaboration occurred primarily within the Arabic-Islamic intellectual tradition between the ninth and twelfth centuries. It reached the Latin West through twelfth and thirteenth-century translations, including works attributed to Hugo Sanctallensis and Gerard of Cremona, and became one of the standard divinatory arts taught in learned magical texts.

Its Arabic origin placed geomancy in an interesting position relative to other divinatory arts: unlike astrology, which derived from Greek sources (Ptolemy's *Tetrabiblos*), geomancy was explicitly Arabic in origin, making it a clearer example of the transmission of occult knowledge from Islamic to Christian culture. Liana Saif's work on Arabic influences in European occult philosophy has given geomancy new attention as a case study in the Arabic-European transmission of magical knowledge.

## Theoretical Status

Geomancy's theoretical status was disputed. Its defenders argued that it was a form of applied astrology: the random process of generating figures was not arbitrary but was guided by celestial influences operating on the practitioner at the moment of casting, so that the figures reflected the same celestial configuration that astrology would reveal more directly. On this account, geomancy was legitimate natural divination—a shortcut to astrological knowledge available to practitioners without full astronomical training.

Critics (including Pico della Mirandola in his anti-astrological polemic) argued that geomancy was even more dubious than judicial astrology: while astrology at least had a theoretical basis in celestial physics, the random process of generating geomantic figures had no coherent natural mechanism connecting it to the question asked. If the figures were not genuinely connected to the celestial configuration, their apparent meaning could only be demonic suggestion—meaning geomancy was unavoidably demonic divination.

## Practice and Social Context

Despite theoretical controversy, geomancy was one of the most widely practiced divinatory arts in early modern Europe. Its accessibility (it required no instruments, no tables, no Latin, and relatively little training compared to horoscopic astrology) made it available to a much wider social range of practitioners than astrological consultation. Popular geomantic manuals in vernacular languages circulated widely; cunning folk and traveling practitioners offered geomantic readings alongside other divinatory services; learned authors like Agrippa included geomancy in their systematic surveys of magical arts.

The range of questions addressed through geomancy covered the spectrum of early modern concerns: the prospects of proposed marriages, the recovery of lost or stolen property, the outcome of lawsuits, the safety of absent travelers, the advisability of business ventures. This practical orientation made geomancy primarily a service to clients seeking specific information about specific concerns rather than a philosophical or spiritual practice.
""",
    },
    {
        "slug": "sefirot",
        "title": "Sefirot",
        "category": "Kabbalah",
        "summary": "The ten divine emanations or attributes through which the infinite God (Ein Sof) manifests and creates in Kabbalistic theology—the foundational structure of Kabbalistic cosmology and theosophy, adapted by Christian Kabbalists to correlate with angelic hierarchies, Neoplatonic hypostases, and the persons of the Trinity.",
        "related_figures": ["Giovanni Pico della Mirandola", "Johannes Reuchlin", "Moses de León"],
        "related_concepts": ["kabbalah-and-christian-kabbalah", "emanation", "angelic-hierarchy", "neoplatonism", "ein-sof"],
        "body": """## The Ten Sefirot

The Sefirot (Hebrew singular *sefirah*, related to *sapphire* and possibly to *counting* or *telling*) are the ten divine attributes or powers through which the infinite, unknowable God (*Ein Sof*, "without end") communicates and creates. In the *Zohar* and subsequent Kabbalistic literature, the Sefirot are simultaneously aspects of the divine nature, the stages of divine creation, and the structure of cosmic reality—they are both how God is and how God creates and sustains everything that is.

The ten Sefirot in their standard enumeration (from highest to lowest) are:
1. **Keter** (Crown) — the divine will, closest to Ein Sof, sometimes understood as consciousness itself
2. **Chokhmah** (Wisdom) — the first flash of divine thought, pure potentiality
3. **Binah** (Understanding) — the divine womb, the mother that develops and differentiates
4. **Chesed** (Lovingkindness) — the principle of divine grace and expansive giving
5. **Gevurah** or **Din** (Judgment/Power) — the principle of divine limit and stern justice
6. **Tiferet** (Beauty) — the harmonizing center, the divine heart, often identified with the *Shekinah* or with the divine son
7. **Netzach** (Victory/Eternity) — divine desire and the source of artistic and natural beauty
8. **Hod** (Splendor) — divine majesty expressed in form and language
9. **Yesod** (Foundation) — the channel connecting upper and lower, often associated with the covenant
10. **Malkhut** (Kingdom) — the divine presence in the world, the *Shekinah*, the feminine receptive principle

These ten Sefirot are traditionally arranged in a pattern called the Etz Chayyim (Tree of Life), organized in three vertical columns (pillars of Mercy, Severity, and Balance) and connected by twenty-two paths corresponding to the letters of the Hebrew alphabet.

## The Sefirot as Theosophical Map

The Sefirot function in Kabbalistic thought as a map of the divine interior life and its expression in creation. The dynamics of the Sefirot—the interaction between Chesed and Gevurah, the harmonizing function of Tiferet, the grounding of Malkhut—constitute a theological account of how God relates to God's own nature and to creation. Kabbalistic prayer, practice, and contemplation aimed at understanding and participating in these divine dynamics, "rectifying" the Sefirot by performing the appropriate actions and intentions (*kavvanot*) that aligned human action with divine will.

The Lurianic innovation of *shevirat ha-kelim* (breaking of the vessels) introduced a tragic dimension: the original Sefirot could not contain the divine light and shattered, scattering divine sparks throughout creation. This made the Sefirot not only a map of divine perfection but a record of cosmic catastrophe requiring repair (*tikkun*).

## Christian Kabbalist Appropriations

Christian Kabbalists, beginning with Pico della Mirandola, appropriated the Sefirot for specifically Christian theological purposes. The most characteristic move was the identification of the Sefirot with the persons of the Trinity and with the angelic hierarchy: Keter corresponded to the Father, Chokhmah to the Son (as the divine Wisdom), and Binah to the Holy Spirit; below the divine Trinity, the remaining Sefirot corresponded to the nine orders of Pseudo-Dionysian angels.

This identification was attractive to Christian Kabbalists for several reasons. It allowed them to claim that the Sefirot "proved" the Trinity to Jews on the basis of their own tradition—that the internal structure of Jewish mysticism secretly contained Christian truth. It also allowed the angelic hierarchy to be grounded in the divine inner life rather than simply posited as cosmological furniture.

Jewish readers objected strenuously to this appropriation, recognizing that the Sefirot in their Kabbalistic context did not describe three divine persons in any sense recognizable as trinitarian theology. The Christian Kabbalist synthesis was creative but required systematic distortion of its Jewish sources.

## The Sefirot and Magic

In practical Kabbalistic tradition, the Sefirot provided the framework for a sophisticated magical practice: meditation on specific Sefirot, use of the divine names associated with each Sefirah, and performance of actions corresponding to the Sefirah's characteristic virtue could draw down divine blessing and rectify cosmic imbalances. Christian Kabbalists adapted this practical dimension: Agrippa's system of divine names, magical squares, and ritual seals incorporated Sephirotic associations, correlating Hebrew divine names (*YHVH*, *Elohim*, *El*, *Shaddai*, etc.) with the Sefirot and thereby with specific cosmic powers accessible through ritual.

The convergence of Sephirotic theosophy with Neoplatonic emanationism made the Sefirot particularly productive for Renaissance magical theory: they could be understood simultaneously as divine attributes (theology), cosmic principles (philosophy), and objects of magical address (practice), offering a unified framework for understanding and operating within the divine hierarchy.
""",
    },
    {
        "slug": "prima-materia",
        "title": "Prima Materia",
        "category": "Alchemy",
        "summary": "The primordial undifferentiated substance from which all things are made and to which the alchemist must first reduce the starting material before beginning the Great Work—simultaneously the most base and the most exalted of substances, identified with a vast range of materials in alchemical literature and carrying important spiritual and philosophical implications.",
        "related_figures": ["Paracelsus", "Newton"],
        "related_concepts": ["alchemy", "philosophers-stone", "great-work", "nigredo-albedo-rubedo", "emanation"],
        "body": """## The Concept

*Prima materia* (Latin, "first matter"; also called *materia prima*, *hyle*, *chaos*, *the unformed*, *the confused*) is the alchemical concept of the primordial, undifferentiated substrate from which all things are made and to which all things can in principle be reduced. It is simultaneously the lowest and the highest substance: lowest because it is without form, quality, or specific nature; highest because it is the source from which all specific natures emerge and the vehicle through which the philosopher's stone can be prepared.

The concept draws on Aristotelian prime matter (*hyle* in Greek, *materia prima* in Latin scholastic translations)—the purely potential substrate underlying all substantial change, which has no properties of its own but can receive any form. Aristotelian prime matter was a theoretical posit rather than something actually observable; similarly, alchemical *prima materia* was often described as something that could not be directly perceived in its pure state but had to be extracted from, or glimpsed in, specific natural substances.

## The Identification Problem

One of the most characteristic features of alchemical literature is the almost unlimited diversity of identifications proposed for the *prima materia*. Different alchemical authorities identified it with: lead (as the most base of metals, closest to formlessness); antimony (Basil Valentine's preferred starting material); sulfur (as the combustible principle present in all things); mercury (as the volatile, fluid principle); salt; common vitriol; dew; urine; human blood; semen; the material of the philosopher's stone itself (suggesting circularity); and many others.

This diversity of identification is not simply confusion. Alchemical texts often deliberately obscured the identity of the *prima materia* as a trade secret or as a test of the reader's understanding. Moreover, the concept itself implied that the *prima materia* could in principle be found anywhere—since all things were, at their deepest level, made of the same primordial stuff. The practitioner's task was to recognize which available material most fully expressed the *prima materia* in the accessible form most suitable for the Great Work.

## The Nigredo and First Operations

The first stage of the Great Work began with reducing the starting material to something approaching *prima materia*—a state of undifferentiated potential from which the Work could proceed. This first operation was typically called *putrefactio* (putrefaction) or *solutio* (solution), and its visual indicator was the *nigredo* (blackening): the material turned black, indicating that its previous forms had been dissolved and a state of maximal formlessness achieved.

The *nigredo* was simultaneously the most daunting and the most necessary stage: without achieving genuine dissolution of the starting material's forms, no genuine transformation was possible—one could only rearrange what was already there rather than achieving the fundamental transmutation of form that produced gold or the philosopher's stone. The practitioner who achieved the *nigredo* had, in the spiritual reading of the Work, achieved a similar dissolution of the ego's fixed forms—a kind of psychic death preparatory to rebirth.

## Spiritual and Philosophical Dimensions

The *prima materia* carried important spiritual and philosophical implications that distinguished alchemical thought from simple metallurgy. If all things shared a common primordial substrate, then the diversity of the natural world was a diversity of forms imposed on a single, undifferentiated stuff—an idea with profound cosmological implications aligning alchemy with Neoplatonic emanationism (all things emanating from the One) and with Stoic cosmic *pneuma* (a single substance differentiating into diverse forms).

The spiritual reading of the *prima materia* as the soul's own primordial nature—unformed, without fixed character, capable of receiving any form—made the alchemical reduction to *prima materia* a figure for the mystic's dissolution of ego and fixed identity preparatory to divine union. This spiritual reading does not replace the material reading but coexists with it: the best alchemical literature operates on both levels simultaneously, using the material *prima materia* as a real substance and as a figure for spiritual realities.

## Newton and the Active Principle

Isaac Newton's alchemical manuscripts show sustained engagement with the concept of *prima materia*, which he connected to his search for the "vegetable spirit" or "active principle" in matter. Newton was interested in identifying the substance that animated and activated the otherwise passive matter of mechanical philosophy, enabling the processes of growth, fermentation, and transmutation that mechanism could not explain. His alchemical reading of *prima materia* as the vehicle of this active principle connected his natural philosophical concerns with the alchemical tradition's deepest theoretical commitments.
""",
    },
    {
        "slug": "translation-movements",
        "title": "Translation Movements and the Transmission of Magical Knowledge",
        "category": "Social and Institutional Contexts",
        "summary": "The organized transmission of Greek and Arabic learning into the Latin West through systematic translation programs in the twelfth and fifteenth centuries, which delivered the philosophical and technical foundations of Renaissance natural magic, alchemy, astrology, and Kabbalistic philosophy to European scholars.",
        "related_figures": ["Marsilio Ficino", "Al-Kindi", "Avicenna", "Albertus Magnus"],
        "related_concepts": ["prisca-theologia", "hermetism", "learned-astrology", "alchemy", "natural-magic"],
        "body": """## The Twelfth-Century Translation Movement

The first major wave of translation that shaped the subsequent development of Western occult philosophy occurred in the twelfth century, centered primarily in Toledo, Spain—a city where Latin Christian, Arabic Muslim, and Jewish communities coexisted and collaborated in a period of unusual cultural interchange. Translators including Gerard of Cremona, Herman of Carinthia, John of Seville, and Adelard of Bath produced Latin versions of Arabic texts on astronomy, astrology, mathematics, medicine, and natural philosophy, including works by Aristotle, Ptolemy, al-Kindi, al-Farabi, Avicenna (Ibn Sina), and Averroes (Ibn Rushd).

For the history of magic and occult philosophy, the most significant translations of this period included:
- **Ptolemy's *Tetrabiblos***: The foundational text of learned Western astrology, transmitted through an Arabic version
- **Al-Kindi's *De radiis***: The theory of "rays" and celestial influence that provided the causal framework for astral magic
- **The *Picatrix*** (*Ghāyat al-Ḥakīm*): The comprehensive manual of astrological image magic and talismanic practice
- **Pseudo-Aristotelian works**: Including the *Secretum Secretorum* (a handbook of royal governance that included discussions of physiognomy, astrology, and alchemy) and works attributed to Aristotle on stones and natural magic
- **Avicenna's medical works**: Including the *Canon of Medicine*, which transmitted Arabic medical-philosophical accounts of the soul, imagination, and spiritual action

These translations provided the theoretical vocabulary and technical content for the subsequent development of Latin learned magic.

## The Fifteenth-Century Italian Renaissance

A second decisive translation moment occurred in the mid-fifteenth century in Florence, driven partly by the influx of Byzantine Greek scholars following the fall of Constantinople (1453) and partly by the Medici's deliberate patronage of humanist learning. Marsilio Ficino's translation programs under Cosimo and Lorenzo de' Medici produced Latin versions of:

- **The *Corpus Hermeticum*** (1463): The foundational text of Hermetic philosophy, translated from a Greek manuscript brought to Florence
- **Plato's complete works**: Providing access to the *Timaeus*, *Phaedrus*, *Republic*, and other works fundamental to Neoplatonic natural magic
- **Plotinus's *Enneads*** (1485): The foundational text of Neoplatonism, providing the metaphysical framework for Renaissance magical theory
- **Iamblichus's *De Mysteriis*** (1488): The foundational text of theurgy, making ancient ritual magical theory available in Latin for the first time
- **Proclus's *Elements of Theology* and *Platonic Theology***: Providing the systematic Neoplatonic hierarchiology that structured Agrippa's magical cosmos

These translations established the philosophical foundations for Ficino's own natural magic and for the entire subsequent tradition of Renaissance learned magic.

## Hebrew and Kabbalistic Transmission

A third transmission strand involved Hebrew sources and the Kabbalistic tradition. Pico della Mirandola's engagement with Kabbalism (from the 1480s) required Hebrew scholars as collaborators and teachers, most importantly Flavius Mithridates (who translated a substantial number of Kabbalistic texts into Latin for Pico). Johannes Reuchlin's *De arte cabalistica* (1517) provided the first systematic Latin introduction to Kabbalistic philosophy.

The Hebrew-Kabbalistic transmission differs from the Greek-Arabic transmission in that it was primarily mediated through personal relationships and manuscript translations rather than through organized translation programs or printed texts. The social dynamics of Jewish-Christian intellectual exchange were complex, shaped by the ambivalent legal and social position of Jewish communities in late medieval and Renaissance Europe, by occasional forced conversions that created hybrid identities, and by the practical needs of Christian humanists who wanted access to sources their education had not provided.

## Scholarly Significance

The translation movements are important for the historiography of Renaissance magic because they show that "Renaissance magic" was not a local European invention but the product of complex cross-cultural transmission over several centuries. The Neoplatonic framework that Ficino used to interpret natural magic came from Greece via Byzantine transmission; the astral magic he drew on came from the Arabic tradition via twelfth-century Toledo; the Kabbalistic material Pico integrated came from Jewish sources via a network of Hebrew scholars; the Hermetic texts came from Greco-Egyptian late antiquity via a Byzantine manuscript.

Liana Saif's research on Arabic influences in European occult philosophy has substantially advanced the scholarship on this transmission history, documenting specific texts and their Arabic antecedents with greater precision than earlier accounts. Her work challenges narratives that treat Renaissance magic as primarily a "recovery of classical antiquity" by showing how thoroughly Arabic mediation shaped what Europeans actually received and how they understood it.
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
    print(f"\nBatch 8 done: {inserted} inserted, {skipped} skipped.")


if __name__ == "__main__":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
    main()
