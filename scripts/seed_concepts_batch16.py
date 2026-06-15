"""Seed batch 16: Astrology concepts — Ptolemaic Cosmos, Celestial Spheres, Planetary Hours, Natal Astrology, Election Astrology."""

import sqlite3
import sys
import io
import json
from datetime import datetime

DB_PATH = "db/renmagic.db"

CONCEPTS = [
    {
        "slug": "ptolemaic-cosmos",
        "title": "The Ptolemaic Cosmos: Structure of the Astrological Universe",
        "category": "Astrology and Cosmology",
        "summary": "The geocentric cosmological model deriving from Ptolemy's Almagest — concentric crystalline spheres carrying the planets around the Earth — that provided the physical framework for Renaissance astrology, magic, and the theory of celestial influence.",
        "related_figures": ["Ptolemy", "Marsilio Ficino", "Giordano Bruno", "Nicolaus Copernicus"],
        "related_concepts": ["learned-astrology", "celestial-spheres", "music-of-the-spheres", "planetary-spirits", "copernican-revolution-and-magic", "world-soul"],
        "body": """## The Ptolemaic Cosmos: Structure of the Astrological Universe

The Ptolemaic cosmos — the geocentric universe of concentric crystalline spheres carrying the planets and stars in their courses around the central, stationary Earth — was the physical framework within which Renaissance astrology, natural magic, and the theory of celestial influence operated. Named for the Alexandrian astronomer and mathematician Claudius Ptolemy (c. 100–170 CE), whose *Almagest* (in Arabic, from Greek *Megale Syntaxis*, "Great Composition") and *Tetrabiblos* provided the twin foundations of astronomical and astrological theory, the Ptolemaic cosmos was accepted as the correct account of the universe's structure by virtually all European intellectuals from the twelfth century through the early seventeenth, and remained the operative cosmological model of practical astrology even longer.

### Structure of the Ptolemaic Universe

The Ptolemaic universe was organized concentrically around the Earth, with successive spheres — each carrying a planet — nested inside each other like the layers of an onion:

1. **The Moon** (closest to Earth, fastest-moving)
2. **Mercury**
3. **Venus**
4. **The Sun**
5. **Mars**
6. **Jupiter**
7. **Saturn** (outermost planet visible to the naked eye)
8. **The Sphere of Fixed Stars** (*firmamentum*)
9. **The Primum Mobile** (First Mover) — the outermost moving sphere, which imparted its diurnal (daily) rotation to all the spheres below

Beyond the Primum Mobile lay the Empyrean — the divine dwelling, motionless and eternal, identified in Christian Aristotelian cosmology with Heaven and the presence of God.

The spheres were understood as crystalline (later descriptions sometimes specified *quinta essentia* — quintessence, the fifth and most perfect element, not found below the Moon) and perfectly transparent; their rotation carried the planets embedded in them through the heavens. The elaborations required to account for the apparent complexity of planetary motion (retrograde motion, variations in apparent size and speed) were handled through the technical devices of epicycles, deferents, and equants that Ptolemy developed in the *Almagest*.

### The Sublunary and Superlunary Worlds

One of the most cosmologically and magically significant features of the Ptolemaic cosmos was its sharp division between the sublunary world (below the Moon) and the superlunary world (above the Moon). In the Aristotelian physics that provided the background theory:

- **Sublunary world**: Composed of the four elements (earth, water, fire, air), characterized by change, generation and corruption, growth and decay. This is the world of birth and death, of the material processes studied by natural philosophy and medicine.

- **Superlunary world**: Composed of quintessence (the fifth element), characterized by perfect circular motion (neither generation nor corruption), incorruptible and eternal. The planets and stars were perfect, unchanging spheres of quintessence moving in perfect circles.

This division had crucial implications for the theory of astrological influence. Celestial bodies, being quintessential and perfect, could influence the sublunary world (where they were the ultimate causes of all natural change) but could not themselves be changed by sublunary causes. The influence flowed one way: from above to below, from the perfect and unchanging to the imperfect and mutable.

The mechanism of this influence was light and motion: planetary light (including invisible light beyond the visible spectrum, what Renaissance authors called "occult qualities" of celestial influence) penetrated the sublunary atmosphere and affected the qualities of things born and growing under particular planetary configurations. This was a respectable natural-philosophical mechanism, not magic in the pejorative sense: it was simply the nature of the physical universe that celestial bodies influenced sublunary things.

### Medieval Elaborations: Angels and Intelligences

The Aristotelian cosmos required a mechanism to account for the constant rotation of the celestial spheres. Aristotle himself had proposed an Unmoved Mover as the ultimate cause of celestial motion. Medieval Christian interpreters identified the separate intelligences that Aristotle had assigned to each sphere (as proximate movers) with the angels of the Christian tradition. Each planet was moved by an angelic intelligence assigned to it — a doctrine that fused Aristotelian cosmology with the Pseudo-Dionysian angelic hierarchy.

This angelic population of the Ptolemaic cosmos had significant implications for astrology and magic. The planetary influence that astrologers catalogued was not merely a physical effect of rotating quintessential matter but the operation of intelligent spiritual beings — the planetary angels — who governed their respective spheres and communicated their qualities to the sublunary world through the medium of light. Natural magic that worked through celestial correspondences was therefore, at least implicitly, working through the operations of these celestial intelligences.

Marsilio Ficino's *De Vita III* exploited this implication: the planet-soul (whether understood as the Plotinian World Soul expressing itself through the planetary sphere or as the Christianized angelic intelligence governing the sphere) was the real agent of astrological influence, and attracting astrological influence through the natural sympathies catalogued in *De Vita* was a form of communication with this intelligence.

### The Copernican Challenge and Its Delay

Nicolaus Copernicus's *De Revolutionibus Orbium Coelestium* (1543) proposed the heliocentric hypothesis — that the Sun, not the Earth, was at the center of the universe, and that the Earth was one of the planets revolving around it. This proposal had profound implications for both the cosmological framework and the astrological-magical theory built on it.

However, the practical impact of Copernicus on either astronomy or astrology was relatively slow. Practical astronomers who needed to calculate planetary positions for astrological or navigational purposes found the Ptolemaic system perfectly adequate (indeed, Copernicus's own system, without the later simplification provided by Kepler's elliptical orbits, was hardly simpler than the Ptolemaic). Most astrologers continued to use geocentric computation tables well into the seventeenth century, and the qualitative theory of planetary influences remained unchanged by heliocentric computation.

The deeper philosophical challenge was more acute: if the Earth moved (and was therefore not a fixed, central, unique body), and if there was no clear boundary between the sublunary and superlunary worlds, then the entire framework of the Aristotelian cosmos — including the division of elements, the mechanism of celestial influence, and the special status of Earth and its human inhabitants — was threatened. Giordano Bruno, who embraced the Copernican hypothesis and extended it into an infinite universe with infinitely many worlds, showed how radical the implications could be.

**See also:** Learned Astrology; Celestial Spheres; Music of the Spheres; Planetary Spirits and Daemons; The Copernican Revolution and the Occult Sciences.
""",
    },
    {
        "slug": "celestial-spheres",
        "title": "Celestial Spheres: The Architecture of Planetary Influence",
        "category": "Astrology and Cosmology",
        "summary": "The concentric rotating spheres of the Ptolemaic cosmos, each carrying a planet and transmitting its distinctive quality to the sublunary world — the physical infrastructure through which astrology claimed to operate and the site of the soul's ascent and descent in Neoplatonic and Hermetic cosmology.",
        "related_figures": ["Ptolemy", "Marsilio Ficino", "Pseudo-Dionysius the Areopagite", "Robert Fludd"],
        "related_concepts": ["ptolemaic-cosmos", "learned-astrology", "music-of-the-spheres", "planetary-spirits", "angelic-hierarchy", "hermetic-cosmology"],
        "body": """## Celestial Spheres: The Architecture of Planetary Influence

The celestial spheres of the Ptolemaic cosmos — the seven concentric rotating shells carrying the Moon, Mercury, Venus, Sun, Mars, Jupiter, and Saturn, enclosed by the sphere of fixed stars and the outermost Primum Mobile — constituted the physical architecture through which astrological influence was thought to operate, through which the planets' qualities were transmitted to the sublunary world, and through which the soul descended at birth and ascended at death in Neoplatonic and Hermetic cosmological mythology. They were not merely a technical astronomical hypothesis but a cosmological vision that integrated physics, theology, music, medicine, and magic into a single unified account of the universe.

### The Physics of the Spheres

The Aristotelian-Ptolemaic physics of the spheres was elaborated through multiple centuries of commentary and synthesis. Each sphere was understood as a perfectly transparent crystalline body, consisting of the fifth element (quintessence) that was lighter than all four sublunary elements and naturally moved in perfect circles. The spheres were nested concentrically, each perfectly fitting within the next, with no gap or empty space between them.

The motion of each sphere was maintained by a separate unmoved mover or separate intelligence (in Christian interpretation, an angel). The outermost sphere, the Primum Mobile, moved with the diurnal (daily) rotation — east to west, completing one revolution in approximately 24 hours — and imparted this rotation to all the spheres below. Each planetary sphere also had its own characteristic motion — slower for the outer planets (Saturn required about 29 years to complete its zodiacal circuit), faster for the inner planets (the Moon completed its circuit in about 28 days).

The interaction between the spheres was a significant technical problem: if each sphere was a rigid, perfectly fitting crystalline shell, how could the inner spheres rotate independently of the outer? The standard solution (deriving from Aristotle and elaborated by medieval commentators) was that the inner spheres were "driven" by contact with the outer ones through some form of physical interaction, or that each sphere's independent motion was superimposed on the overall diurnal rotation through the operation of its particular intelligence.

### Quality Transmission: How the Spheres Influenced Earth

The mechanism by which the celestial spheres influenced the sublunary world was central to the theory of astrology and natural magic. The basic mechanism was light: planetary bodies emitted light (both visible and invisible) that penetrated the sublunary atmosphere and affected the qualities of things exposed to it. But "light" in this context was understood very broadly: it included not just visible electromagnetic radiation but any form of "ray" or "influence" that a celestial body could emit.

The qualities transmitted by each planet were systematically catalogued:

- **Moon**: Moisture, change, growth and diminution, the feminine, the imagination, dreams, the tide, madness (*luna*, moon, being the root of *lunacy*)
- **Mercury**: Speech, intellect, commerce, speed, versatility, the arts of communication, androgyny
- **Venus**: Love, beauty, pleasure, fertility, harmony, the feminine (in a different register from the Moon)
- **Sun**: Life, heat, royalty, intellect, gold, glory, the masculine principle par excellence
- **Mars**: Aggression, heat and dryness, iron, conflict, courage, passion
- **Jupiter**: Justice, beneficence, expansion, wisdom, prosperity, law
- **Saturn**: Melancholy, coldness and dryness, lead, age, death, contemplation, limitation

These quality-associations were not arbitrary: they derived from a combination of mythological tradition (the planets were identified with the Olympian gods), astronomical observation (Saturn, the slowest and most distant planet, was associated with age and delay; Mars, the reddish planet, with fire and conflict), and philosophical theory (the planets being further from or closer to the Sun were associated with qualities of greater or lesser warmth and dryness).

### The Spheres and the Soul's Journey

In Neoplatonic and Hermetic cosmology, the celestial spheres were not merely the infrastructure of astrological influence but the route of the soul's descent into matter and its potential ascent back to the divine. As Macrobius's *Commentary on the Dream of Scipio* (influential throughout the medieval period) described it, the soul descending from the divine realm to take up residence in a body passed through each of the celestial spheres in turn, acquiring at each sphere a portion of that sphere's characteristic quality: from Saturn, the capacity for reasoning and understanding; from Jupiter, the power of action; from Mars, the courageous spirit; from the Sun, sense-perception and imagination; from Venus, the impulse of desire; from Mercury, the arts of speech; from the Moon, the capacity for natural growth.

At birth (the moment of descent below the lunar sphere into the sublunary world), these acquired qualities were permanently "stamped" on the soul's subtle body by the particular planetary configuration at that moment — which is why the birth chart could reveal the soul's fundamental constitution: the chart mapped the moment of the soul's final passage into sublunary existence.

At death, the reverse process occurred: the soul rose back through the spheres, shedding at each sphere the quality it had acquired in descent, until it arrived purified above the planetary spheres at the fixed-star heaven. This ascent-through-the-spheres schema was the cosmological framework within which the goals of Hermetic practice — the Poimandres ascent, the Mithraic grades, the Enochian Aethyrs — made sense.

### Musical Harmony of the Spheres

The celestial spheres were intimately connected with the Pythagorean-Platonic tradition of the music of the spheres (*musica mundana*): the claim that the proportional relationships between the spheres' sizes and speeds of rotation generated cosmic musical harmonies analogous to the harmonies of musical intervals. Plato's *Timaeus* described the World Soul as constructed from numerical ratios that generate the musical scale; Cicero's *Dream of Scipio* (as commented by Macrobius) described the music generated by the celestial spheres as "the greatest and sweetest harmony" inaudible to human ears only because we have always heard it from birth.

Boethius (*De Institutione Musica*, c. 500 CE) systematized the doctrine of *musica mundana* alongside *musica humana* (the harmony of the human body) and *musica instrumentalis* (the music produced by instruments) as the three types of music studied by the educated person. This tripartite scheme made the celestial spheres the ultimate referent of musical harmony, and musical practice on earth a participation (however imperfect) in cosmic order.

Robert Fludd's elaborate cosmological diagrams — particularly the famous cosmic monochord showing God reaching down to tune the string of the universe — visualized this Pythagorean-Hermetic synthesis of spherical cosmology and musical harmony in its most baroque form.

**See also:** Ptolemaic Cosmos; Learned Astrology; Music of the Spheres; Planetary Spirits and Daemons; Angelic Hierarchy; Hermetic Cosmology.
""",
    },
    {
        "slug": "natal-astrology",
        "title": "Natal Astrology: The Birth Chart and the Human Individual",
        "category": "Astrology and Cosmology",
        "summary": "The astrological practice of casting a horoscope for the moment of a person's birth, interpreting the planetary configuration as revealing the individual's character, fate, and the arc of their life — the most socially widespread and philosophically elaborated branch of astrology in the Renaissance.",
        "related_figures": ["Ptolemy", "Marsilio Ficino", "Giovanni Pico della Mirandola", "Girolamo Cardano"],
        "related_concepts": ["learned-astrology", "ptolemaic-cosmos", "celestial-spheres", "planetary-spirits", "macrocosm-and-microcosm", "fate-and-free-will"],
        "body": """## Natal Astrology: The Birth Chart and the Human Individual

Natal astrology (*genethlialogia*, from Greek *genethle*, "birth") — the practice of casting and interpreting a horoscope for the moment of a person's birth — was the most intellectually elaborate, socially prestigious, and philosophically controversial branch of astrological practice in the Renaissance. Distinguished from mundane astrology (which predicted collective events — wars, epidemics, the rise and fall of kingdoms) and from elective astrology (which identified auspicious times for beginning specific undertakings), natal astrology focused on the individual: on the particular configuration of planets at the moment of an individual's entry into the sublunary world, and on what that configuration revealed about the person's temperament, capacities, likely diseases, relationships, and the general arc of their life.

### The Technical Basis

A natal chart (*horoscope* from Greek *horoskopos*, "hour-watcher") was a representation of the sky at the moment of a person's birth, showing the positions of the Sun, Moon, and five visible planets (Mercury, Venus, Mars, Jupiter, Saturn) in relation to the twelve signs of the zodiac and the twelve "houses" — divisions of the sky based on the local horizon and meridian at the birth-time and birth-place.

The twelve zodiacal signs (Aries through Pisces) were bands of the ecliptic, the apparent path of the Sun through the year, each associated with particular qualities (cardinal/fixed/mutable, fire/earth/air/water signs) and with a ruling planet. The positions of the planets in these signs qualified the planetary influences: a planet in its "domicile" (the sign it ruled) was strong; a planet in its "detriment" (the sign opposite its domicile) was weak; planets in "exaltation" (their position of greatest dignity) were especially powerful.

The twelve "houses" were spatial divisions of the sky based on the horizon and meridian, rotating with the Earth's diurnal motion and thus different at every moment. Each house was associated with a department of human life:
- **House 1 (Ascendant)**: The self, appearance, health, beginning of life
- **House 2**: Possessions, wealth
- **House 3**: Siblings, short journeys, communication
- **House 4 (IC, Imum Coeli)**: Parents, home, origins, end of life
- **House 5**: Children, pleasures, creativity
- **House 6**: Illness, service, work
- **House 7 (Descendant)**: Marriage, partnerships, open enemies
- **House 8**: Death, inheritance, transformation
- **House 9**: Religion, philosophy, long journeys, higher education
- **House 10 (MC, Medium Coeli)**: Career, reputation, public life
- **House 11**: Friends, groups, hopes
- **House 12**: Hidden enemies, prisons, isolation, self-undoing

### Philosophical Foundations

The philosophical justification for natal astrology in the Renaissance was provided primarily by the macrocosm-microcosm doctrine and by the theory of celestial influence. If the human being is a microcosm replicating the structure of the macrocosm, and if the moment of birth (or more precisely, the moment of the soul's arrival in the sublunary world) is when the celestial configuration permanently stamps its qualities on the newly formed individual, then the natal chart is a map of the individual's cosmological constitution — the particular combination of macrocosmic forces that define the individual's nature.

This justification was not universally accepted even among those who accepted astrology's general validity. The most sophisticated Renaissance challenge to natal astrology came from Giovanni Pico della Mirandola's *Disputationes Adversus Astrologiam Divinatricem* (written in the 1490s, published posthumously 1496), which attacked the theoretical and empirical foundations of natal astrology without denying the general physical theory of celestial influence. Pico's arguments included: the impossibility of determining the exact moment of birth (a few seconds' difference in the time of birth would alter the chart significantly); the irrelevance of the zodiacal signs (which were the astrologers' projection onto the fixed stars rather than physical realities); and the empirical failures of astrological prediction (twins born at the same moment under the same chart had different fates).

### Ficino and the Saturnine Temperament

Marsilio Ficino's famous analysis of his own natal chart — in which he identified himself as a Saturnine type (Saturn conjunct the Ascendant in Aquarius, with Mars in the same house) — illustrates the sophisticated Renaissance use of natal astrology for self-understanding. Ficino understood his melancholic temperament (cold, dry, prone to depression and physical illness) as astrologically determined, but also as the mark of philosophical and intellectual depth: Saturn was the planet of contemplation, and the Saturnine temperament, while dangerous to health, was also the signature of philosophical genius.

This reading drew on the pseudo-Aristotelian *Problemata* XXX.1 — a text asking why all outstanding men in philosophy, politics, poetry, and the arts were melancholic — which Ficino synthesized with the Neoplatonic theory that Saturn's coldness and slowness corresponded to the contemplative withdrawal from sensory engagement that philosophical practice required. The melancholic scholar, afflicted by his own Saturnine nature, could mitigate the worst physical effects through the use of Jovian and Solar counter-influences (specific foods, colors, music, smells, activities associated with Jupiter and the Sun) while preserving the contemplative depth that his saturnine constitution provided.

Ficino's self-analysis established a pattern followed by many subsequent Renaissance intellectuals: the interpretation of one's natal chart as a resource for self-understanding and as a guide to the appropriate philosophical and medical regimen for managing one's particular constitution.

### Cardano and Predictive Natal Astrology

Girolamo Cardano (1501–1576) — mathematician, physician, philosopher, and autobiographer — pushed natal astrology in a more predictive direction. His *Libelli Quinque* (1547) and *Geniturarum Exempla* (1554) collected natal charts of famous persons (including Petrarch, Erasmus, Luther, and Jesus Christ) with retrospective interpretations that claimed to explain their careers, characters, and deaths through astrological analysis.

Cardano's most notorious astrological venture was his casting of the horoscope of the young Edward VI of England (1552), in which he predicted the king would live to at least 55 years. Edward died of tuberculosis in 1553, at age 15 — a spectacular predictive failure that illustrated the empirical vulnerability of natal astrology and that its critics (including Pico's followers) did not allow to pass unremarked.

Cardano's autobiographical *De Vita Propria* contains extensive reflection on his own natal chart and its significance for understanding his unusual life. His was one of the most self-analytically sophisticated deployments of natal astrology in the Renaissance.

**See also:** Learned Astrology; Ptolemaic Cosmos; Celestial Spheres; Macrocosm and Microcosm; Planetary Spirits and Daemons.
""",
    },
    {
        "slug": "election-astrology",
        "title": "Electional and Interrogatory Astrology: Timing Magic and Divine",
        "category": "Astrology and Cosmology",
        "summary": "The astrological practice of identifying auspicious or inauspicious moments for undertaking specific actions (electional astrology) or of deriving answers to specific questions from the horoscope of the moment of asking (horary/interrogatory astrology) — the most operationally magical applications of astrological theory.",
        "related_figures": ["Ptolemy", "Marsilio Ficino", "Heinrich Cornelius Agrippa"],
        "related_concepts": ["learned-astrology", "ptolemaic-cosmos", "talismans", "natural-magic", "natal-astrology", "planetary-spirits"],
        "body": """## Electional and Interrogatory Astrology: Timing Magic and Divine

Of the four main branches of judicial astrology recognized in the classical and medieval tradition — natal (concerning the individual at birth), mundane (concerning collective entities and events), electional (concerning the choice of auspicious times for actions), and interrogatory or horary (concerning answers to specific questions) — the latter two had the most immediate practical connection to magical operations. Electional astrology provided the technique for identifying astrologically optimal moments for performing magical operations, constructing talismans, beginning undertakings, or taking medicines; interrogatory astrology (also known as horary astrology) claimed to answer specific questions from the horoscope of the moment of asking. Together, these branches made astrology not merely a diagnostic or predictive science but an operational tool for manipulating the timing of human action.

### Electional Astrology: The Art of Choosing Moments

The fundamental principle of electional astrology was the same as that of natal astrology but applied prospectively rather than retrospectively: just as the planetary configuration at the moment of birth shaped the individual's constitution and fate, so the planetary configuration at the moment of beginning any undertaking — planting a crop, launching a ship, beginning a medical treatment, marrying, starting a battle, constructing a talisman — shaped the outcome of that undertaking. By choosing the moment to act, the practitioner could ensure that the beginning was fortified by favorable planetary influence and that unfavorable influences were minimized or avoided.

The practical technique of electional astrology involved identifying, for any proposed undertaking, the relevant astrological significators (the planets, signs, and houses particularly associated with that type of activity) and choosing a time when those significators were strong and well-aspected. For medical treatment, the physician would elect a moment when the Moon was well-placed and not afflicted by malefic planets, when the relevant planetary ruler of the illness was weakened, and when the planet associated with the remedy being used was strengthened. For constructing a talisman of a particular planet, the talisman should be made when that planet was angular (on the Ascendant, MC, Descendant, or IC), in its dignity, and receiving favorable aspects from benefic planets.

Marsilio Ficino's *De Vita III* is essentially an extended guide to electional astrology applied to the specific problem of the melancholic scholar: how to use astrological timing to attract Jovian and Solar influences and mitigate Saturnine ones. The recommendations about specific foods, colors, smells, music, and activities associated with each planet are embedded in an electional framework: they should be used especially when the relevant planet is in a favorable position in the sky.

### Magical Timing and Talisman Construction

The connection between electional astrology and talisman magic was particularly close and was recognized as such by both practitioners and critics. A talisman — an engraved image designed to attract and concentrate the influence of a specific planet or star — would only work effectively if it was created at a moment when that planet or star was in a position of maximum strength. The image had to be created at the auspicious moment to "capture" the celestial influence in the material; if the timing was wrong, the celestial power would not be available for inscription.

This meant that the talisman-maker had to be skilled in electional astrology: they needed to calculate in advance when the relevant celestial body would be optimally positioned, prepare all materials in advance so that the actual engraving or inscription could be performed at exactly the right moment (sometimes a window of only a few minutes), and perform the inscription swiftly and without error. The *Picatrix* provided detailed instructions for this procedure for each of the planets, the 28 lunar mansions, and the 36 decans (10° divisions of the zodiac), making electional astrology for talisman construction a highly technical skill.

### Interrogatory (Horary) Astrology

The most philosophically remarkable branch of practical astrology was interrogatory or horary astrology: the practice of casting a horoscope for the moment when a question was put to the astrologer, and reading from that horoscope an answer to the question. If a client came to ask whether their stolen goods would be recovered, whether a sick person would live or die, whether a proposed business venture would succeed, or whether a love interest reciprocated their feelings, the horary astrologer would note the exact time of the question, calculate the planetary positions at that moment, and read the answer from the chart.

The theoretical justification for horary astrology was subtle: the moment when a question arose in the mind (or when it was put to the astrologer) was taken to be a kind of "birth" of the question, and just as the natal chart revealed the nature of a person born at that moment, the horary chart revealed the nature of the question and its probable resolution. Underlying this was the assumption that nothing happens by chance — that the moment when a question arose was determined by the same celestial influences that determined the events the question was about, so that the chart of the question and the chart of the outcome were, in some deep sense, the same chart.

This reasoning seemed circular to critics: if the moment of the question was itself determined by celestial factors, then casting the chart of that moment merely read back the celestial determination, rather than providing independent information about the future. Defenders replied that precisely this circular relationship justified horary astrology: the cosmos was a unified system in which the same celestial influences that shaped events also shaped the timing of questions about those events.

**See also:** Learned Astrology; Ptolemaic Cosmos; Talismans; Natural Magic; Natal Astrology.
""",
    },
    {
        "slug": "planetary-dignities",
        "title": "Planetary Dignities and Debilities: The Grammar of Astrological Strength",
        "category": "Astrology and Cosmology",
        "summary": "The technical system of essential dignities — domicile, exaltation, triplicity, term, and face — by which Renaissance astrology evaluated the strength or weakness of a planet in a given zodiacal position, providing the fine-grained grammar that made astrological interpretation and magical timing possible.",
        "related_figures": ["Ptolemy", "Marsilio Ficino", "Heinrich Cornelius Agrippa", "Girolamo Cardano"],
        "related_concepts": ["learned-astrology", "ptolemaic-cosmos", "natal-astrology", "election-astrology", "talismans"],
        "body": """## Planetary Dignities and Debilities: The Grammar of Astrological Strength

The system of planetary dignities (*dignitates*) — the technical scheme by which each degree of the zodiac was assigned to a planet as its "domain" in varying degrees of strength and specificity — was the grammatical foundation of Renaissance astrological practice. Without a reliable method for evaluating the relative strength or weakness of a planet in any given zodiacal position, the astrologer could not assess whether a planet's influence was being expressed powerfully or feebly, benevolently or destructively. The dignity system provided this evaluative grammar, and mastery of it was the technical prerequisite for competent astrological interpretation, talisman construction, and elective timing.

### The Essential Dignities

Classical and medieval astrology distinguished five levels of essential dignity (and their corresponding debilities):

**1. Domicile (and Detriment)**
Each planet was assigned one or two zodiacal signs as its "home" — the sign in which it expressed its nature most purely and powerfully. The seven traditional planets ruled twelve signs between them:
- Sun: Leo; Moon: Cancer
- Mercury: Gemini and Virgo; Venus: Taurus and Libra
- Mars: Aries and Scorpio; Jupiter: Sagittarius and Pisces; Saturn: Capricorn and Aquarius

A planet in its domicile was like a person in their own house — comfortable, in full possession of their faculties, and able to act freely. A planet in the sign opposite its domicile (its "detriment") was like a guest unwelcome in someone else's house — uncomfortable and unable to act effectively. The Sun in Leo was powerfully expressive; the Sun in Aquarius (Leo's opposite) was in detriment.

**2. Exaltation (and Fall)**
Each planet had a single sign of exaltation — the sign in which it performed at its highest potential, even beyond what its domicile allowed. Traditional exaltations:
- Sun: Aries; Moon: Taurus; Mercury: Virgo
- Venus: Pisces; Mars: Capricorn; Jupiter: Cancer; Saturn: Libra

A planet in its exaltation was like a visiting dignitary in a foreign country — honored, treated with extraordinary respect, and performing at their absolute best. The opposite sign was the planet's "fall" — where it was disgraced and enfeebled.

**3. Triplicity**
The twelve signs were divided into four triplicities of three signs each (the fire triplicity: Aries/Leo/Sagittarius; earth: Taurus/Virgo/Capricorn; air: Gemini/Libra/Aquarius; water: Cancer/Scorpio/Pisces). Each triplicity had day and night rulers (and sometimes a participating ruler), varying between traditions. Triplicity rulership was a weaker dignity than domicile or exaltation but still significant in evaluating planetary strength.

**4. Term (Bound)**
Each sign was divided into five "terms" of varying degrees (totaling 30 degrees per sign), each ruled by one of the five non-luminary planets (Mercury, Venus, Mars, Jupiter, Saturn). Terms were the weakest of the major dignities but provided fine-grained qualification of planetary influence at the degree level.

**5. Face (Decan)**
Each sign was divided into three faces of 10 degrees each, each ruled by a planet in a specific sequence. Faces were the weakest major dignity, providing the least qualification to a planet's expression.

### Accidental Dignities

Beyond the essential dignities (which depended solely on zodiacal position), astrology also recognized "accidental dignities" that strengthened or weakened a planet's expression based on its position in the chart rather than the zodiac:

- **Angular houses**: A planet on the Ascendant, MC, Descendant, or IC was powerfully placed, regardless of its zodiacal sign
- **Speed**: A planet moving faster than its average speed was stronger than one moving slowly or stationally
- **Direction**: A planet in direct motion was stronger than one in retrograde
- **Combustion**: A planet within 8.5 degrees of the Sun was "combust" — burned up by the Sun's rays and severely weakened (the Moon "conjunct the Sun" was new, and functionally blind)

### The Dignity System in Magical Practice

For Renaissance magical timing and talisman construction, the dignity system was operationally essential. Ficino's instructions for attracting Solar, Jovian, or Venereal influences required knowing not only when those planets were above the horizon but when they were in positions of essential dignity — when the Sun was in Leo or Aries, when Jupiter was in Sagittarius or Cancer — so that the influence available for attraction was at maximum strength.

The *Picatrix*'s detailed instructions for talisman construction specified that the relevant planet must be in its domicile or exaltation, free from combustion, not in a debilitated sign, angular, and making no unfavorable aspects to malefic planets. Meeting all these conditions simultaneously might require waiting weeks or even months for the right moment — which explained why talisman construction was considered a highly skilled and time-consuming operation.

Agrippa's tables in *De Occulta Philosophia* systematized these correspondences into reference charts that a practitioner could consult for any magical operation, providing the technical basis for astrologically timed magic in a convenient and accessible form.

**See also:** Learned Astrology; Natal Astrology; Electional Astrology; Talismans; Ptolemaic Cosmos.
""",
    },
]


def main():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    inserted = 0
    skipped = 0
    for concept in CONCEPTS:
        existing = c.execute(
            "SELECT id FROM concepts WHERE slug = ?", (concept["slug"],)
        ).fetchone()
        if existing:
            print(f"  Skipped (exists): {concept['title']}")
            skipped += 1
            continue

        now = datetime.utcnow().isoformat()
        word_count = len(concept["body"].split())

        c.execute(
            """INSERT INTO concepts
               (slug, title, category, summary, body,
                related_figures, related_concepts,
                word_count, source_method, review_status, confidence,
                created_at, updated_at)
               VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)""",
            (
                concept["slug"],
                concept["title"],
                concept["category"],
                concept["summary"],
                concept["body"],
                json.dumps(concept.get("related_figures", [])),
                json.dumps(concept.get("related_concepts", [])),
                word_count,
                "LLM_ASSISTED",
                "DRAFT",
                "HIGH",
                now,
                now,
            ),
        )
        print(f"  Inserted: {concept['title']} ({word_count} words)")
        inserted += 1

    conn.commit()
    conn.close()
    print(f"\nBatch 16 done: {inserted} inserted, {skipped} skipped.")


if __name__ == "__main__":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
    main()
