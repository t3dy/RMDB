"""Seed batch 20: Magic Practice continued — Verbal Charms, Amulets, Suffumigations, Weapon Salve, Oneiromancy."""

import sqlite3
import sys
import io
import json
from datetime import datetime

DB_PATH = "db/renmagic.db"

CONCEPTS = [
    {
        "slug": "verbal-charms",
        "title": "Verbal Charms and Incantations: The Power of Spoken Word",
        "category": "Magic: Theory and Practice",
        "summary": "The tradition of spoken or written formulas — charms, spells, curses, blessings — used across all social levels for healing, protection, and harm, representing the most widespread and socially diffuse form of magical practice in Renaissance and early modern Europe.",
        "related_figures": ["Heinrich Cornelius Agrippa", "Reginald Scot"],
        "related_concepts": ["divine-names", "natural-magic", "cunning-folk", "love-magic", "grimoires", "learned-vs-popular-magic"],
        "body": """## Verbal Charms and Incantations: The Power of Spoken Word

Verbal charms and incantations — spoken or sung formulas, often combined with specific actions, objects, or timings, believed to produce physical or spiritual effects — represent the most socially widespread and culturally diffuse form of magical practice in Renaissance and early modern Europe. Unlike the elaborate ceremonial magic of learned practitioners or the systematic philosophy of natural magic, verbal charms required no specialized training, no expensive materials, and no access to books or schools: they were transmitted within families and communities, used by both men and women across the full social spectrum, and deployed for the full range of practical needs — healing illness, protecting against danger, recovering stolen goods, attracting love, harming enemies.

### The Structural Diversity of Charms

Verbal charms existed in an extraordinary variety of structural forms, from the extremely simple (a word or phrase repeated a fixed number of times) to the highly elaborate (long narrative or pseudo-narrative formulas invoking Christian imagery, biblical figures, and traditional healing lore). Several structural types recur across European traditions:

**Command formulas**: Direct commands addressed to the target of the charm (the illness, the wound, the evil spirit, the serpent): "I command you, worm, depart from this flesh." The command form presupposed a direct relationship of power between the speaker and the addressed entity, and required no intermediate spiritual agency.

**Narrative charms** (*Historiolae*): Short narrative formulas that described a mythological or biblical event analogous to the current situation, with the implicit or explicit claim that as the mythological event resolved, so the present situation would resolve. "Christ was born in Bethlehem, baptized in the Jordan; as the water stood still at his baptism, so stand still, blood." This type combined narrative precedent with analogical magic.

**Adjuration formulas**: Formulas that named and invoked higher spiritual powers (God, Christ, the Virgin, specific saints, angels) to authorize the charm's action. These were structurally similar to prayers but addressed to the charm's target rather than to God directly.

**Riddling or nonsense formulas**: Formulas whose power derived not from semantic content but from their sound, their strangeness, or their formal properties. *Abracadabra* — the most famous, inscribed on triangular amulets and used particularly against fever — falls into this category, whatever its etymological origin.

### Charms and Christian Practice

One of the most significant features of European verbal charm tradition was its pervasive integration with Christian materials. The vast majority of charms collected in early modern European records invoked God, Christ, the Virgin Mary, or specific saints; quoted or paraphrased biblical passages; and framed their action within a narrative of Christian miraculous intervention. This made charms simultaneously an expression of popular Christian devotion and a form of magical practice that the Church's authorities found ambiguous and often condemned.

The relationship between charms and prayers was explicitly theorized by both practitioners and critics. Practitioners often saw no distinction between a prayer for healing (which the Church explicitly authorized) and a charm for healing (which addressed the illness or its cause directly): both invoked Christian spiritual authority for a healing purpose. Church authorities drew the line differently: prayers directed to God, asking for divine healing in accordance with God's will, were legitimate; charms that claimed to work automatically through the correct performance of a verbal formula (regardless of the operator's spiritual state or God's will) were magical and potentially superstitious.

Reginald Scot's *Discoverie of Witchcraft* (1584) included extensive collections of charms as part of his skeptical project: by cataloguing the variety and absurdity of charm traditions, he hoped to demonstrate that belief in their efficacy was superstition rather than genuine experience. His collection is now a primary source for the charm tradition in sixteenth-century England.

### Transmission and Variation

Charm tradition was transmitted primarily through oral and manuscript channels rather than through print (although printed charm collections existed, particularly for use as amulets). The oral transmission meant that charms were highly variable: each retelling or transcription introduced modifications, substitutions, and adaptations to local circumstances. A charm transmitted through four generations might retain its structural type and some key phrases while varying substantially in detail.

This variability has made charms difficult to analyze as a "tradition" in the sense that intellectual historians use the term: there was no canonical text, no authoritative version, and no clear boundary between "genuine" tradition and individual innovation. The charm tradition was instead a repertoire of structural forms and conventional materials (divine names, narrative types, command phrases) from which individual practitioners assembled their own formulas, adapting them to specific situations and available materials.

### Learned Theories of Charm Efficacy

Learned natural philosophers who discussed the efficacy of verbal charms offered several theoretical accounts. Agrippa, drawing on Neoplatonic theories of language and the World Soul, argued that words possessed natural power derived from their relationship to the divine ideas they expressed: the correct word, spoken with conviction and at the appropriate celestial moment, could genuinely affect natural processes by aligning with the cosmic sympathies that connected all things.

The Ficinian theory of *spiritus* provided a more physiological account: spoken words were vibrations in the air that could enter the listener's body and affect their *spiritus* through resonance, in much the same way as music could alter the humoral balance. The physician-magician's authoritative voice, conveying the appropriate image and intention, could heal or harm through the physical medium of the spoken word operating on the patient's *spiritus*.

**See also:** Divine Names; Natural Magic; Cunning Folk and Popular Magic; Love Magic; Grimoires.
""",
    },
    {
        "slug": "amulets-and-talismans-practice",
        "title": "Amulets in Practice: Making, Wearing, and Using Protective Objects",
        "category": "Magic: Theory and Practice",
        "summary": "The practical tradition of creating, consecrating, and wearing physical objects charged with protective or beneficial magical power — distinct from the theoretical account of talismans as instruments of celestial influence — spanning popular domestic magic and learned ceremonial practice.",
        "related_figures": ["Heinrich Cornelius Agrippa", "Marsilio Ficino", "Paracelsus"],
        "related_concepts": ["talismans", "natural-magic", "divine-names", "practical-kabbalah", "verbal-charms", "learned-vs-popular-magic"],
        "body": """## Amulets in Practice: Making, Wearing, and Using Protective Objects

The practice of wearing, carrying, or placing physical objects believed to provide protection, healing, or magical power is among the most universal and ancient forms of magical practice in the historical record — and among the most socially diffuse and cross-culturally present in Renaissance and early modern Europe. The amulet (*amuletum* in Latin, *phylacterion* in Greek) was a physical object — inscribed, engraved, drawn, sewn, or otherwise prepared — that was believed to convey magical protection or benefit to its bearer through some form of inherent or conferred power. Closely related to the talisman (the theoretically oriented learned tradition of creating celestially charged objects), but socially much broader, amulets spanned the full spectrum from the Kabbalistic divine-name inscriptions of learned Jewish practice to the simple herb packets and knotted cords of village healing magic.

### Materials and Forms

Amulets were made from an extraordinarily wide range of materials, each chosen (in more sophisticated accounts) for its intrinsic natural properties or its celestial associations. Common materials included:

**Metals**: Gold (Solar, protective, purifying), silver (Lunar, feminine, related to water and silver crafts), iron (Martial, apotropaic against evil spirits — iron was widely believed to repel supernatural beings), lead (Saturnine, used in curse amulets rather than protective ones), copper (Venereal, associated with love and beauty).

**Stones**: Gemstones were extensively used in amulet making, each stone associated with a planet and carrying that planet's qualities. The bloodstone (*heliotrope*) was Solar and could staunch bleeding; the emerald was Venereal and promoted fidelity and healing; the sapphire was protective and granted wisdom. The magical properties of stones were catalogued in *lapidaries* (stone-medicine texts) from antiquity through the medieval and Renaissance periods.

**Written inscriptions**: The most specifically "magical" feature of learned amulets was the written content — divine names, biblical verses, planetary seals, magical characters — believed to carry the power of the words or symbols inscribed. Parchment was preferred over paper for important amulets (it was considered more durable and more appropriate for sacred content); the ink might be prepared from specific ingredients.

**Natural objects**: Herbs, roots, animal parts, and other natural objects carried in sachets or pouches constituted the simpler end of amulet practice. The herbs and other materials were chosen for their natural properties (healing, warming, protective) and their celestial associations.

### Consecration and Activation

In learned amulet-making theory, the physical object alone was insufficient: it required consecration — a ritual act that "charged" the object with the appropriate spiritual or celestial power — to become effective. The consecration procedures described in learned magical texts (Agrippa, the Solomonic grimoires, the *Picatrix*) involved:

- Choosing the appropriate astrological moment (when the relevant planet was in dignity and favorably positioned)
- Purifying the operator and the materials through fasting, prayer, or physical washing
- Performing the inscription of names, characters, and seals with appropriate implements and at the appropriate time
- Consecrating the completed object through prayer, fumigation with appropriate incense, and invocation of the relevant spiritual powers

This elaborate procedure was the learned elaboration of what in popular practice was a much simpler operation: the village charmer who made a protective herb pouch blessed it, perhaps spoke words over it, and handed it to the client without the elaborate astrological timing and ceremonial preparation of learned talisman-making.

### The Church and Amulets

The Church's attitude toward amulet practice was perpetually ambiguous. Ecclesiastical authorities condemned pagan or diabolically associated amulet practices while simultaneously authorizing practices that shared the same structural features: the wearing of the Agnus Dei (a wax disc blessed by the Pope, worn for protection), devotional medals of saints, images of the Virgin, the wearing of religious texts (*Tetragrammaton* amulets in the Jewish tradition paralleled by scriptural amulets among Christian populations). The line between a legitimate religious object worn for devotion and an illegitimate magical amulet worn for protection was theoretically clear but practically difficult to maintain.

The Council of Laodicea (364 CE) had already condemned clerics who made amulets; subsequent canons repeated similar condemnations. Yet popular practice continued relatively undisturbed, partly because the practical benefits of amulets (the placebo effect, the social function of providing concrete action in the face of illness or danger) were real and responded to genuine needs.

**See also:** Talismans; Natural Magic; Divine Names; Practical Kabbalah; Verbal Charms; Learned vs. Popular Magic.
""",
    },
    {
        "slug": "suffumigations",
        "title": "Suffumigations: Incense, Perfumes, and Aromatic Magic",
        "category": "Magic: Theory and Practice",
        "summary": "The magical and medical use of fumigations — burning aromatic substances to produce vapors that attracted, repelled, or communicated with spiritual beings, medicated the spirit, and established appropriate atmospheric conditions for magical operations — drawing on ancient temple practice, Galenic medicine, and Neoplatonic pneumatology.",
        "related_figures": ["Marsilio Ficino", "Heinrich Cornelius Agrippa", "Paracelsus"],
        "related_concepts": ["natural-magic", "talismans", "spiritus-and-pneuma", "planetary-spirits", "ceremonial-magic", "world-soul"],
        "body": """## Suffumigations: Incense, Perfumes, and Aromatic Magic

Suffumigation — the burning of aromatic substances to produce fragrant smoke used for magical, medical, or ritual purposes — was one of the most widely practiced and theoretically justified magical techniques in the Renaissance tradition. Rooted simultaneously in ancient temple practice (incense burned on altars to please the gods), Galenic medicine (aromatic vapors as therapeutic agents), Stoic pneumatology (scent as an extremely subtle material substance affecting the soul's vehicle), and Neoplatonic magic (aromatic substances as vehicles for celestial influence), suffumigation appeared at every level of Renaissance magical practice from the elaborate incense specifications of the *Picatrix* to the simple fumigating herbs of village healing practice.

### Theory: Aromatic Vapors and the Spiritus

The theoretical basis for the magical efficacy of suffumigations was provided primarily by the Neoplatonic-Ficinian account of *spiritus*. The *spiritus* — the subtle vehicle of the soul, the medium through which celestial influences operated in the body — was a vaporous, mobile substance susceptible to the same vaporous substances present in aromatic smells. Just as music (organized air vibration) could influence the *spiritus* through resonance, so aromatic vapors (extremely subtle material substances) could affect the *spiritus* through direct physical contact.

Each aromatic substance was associated with a specific planet: its smell, color, and chemical properties corresponded to the qualities of that planet, and its vapors therefore carried that planet's influence in condensed form. Burning the appropriate incense at the appropriate astrological moment attracted the corresponding celestial influence through the *spiritus mundi* and concentrated it in the ritual space, benefiting the practitioner whose *spiritus* was thereby imbued with the celestial quality.

Ficino's *De Vita III* specified incenses appropriate to each planet: for Solar influence (to counteract Saturnine melancholy), the appropriate incenses included frankincense, mastic, cinnamon, and other warm, bright, golden-colored aromatics; for Jovial influence, cedar and similar noble woods; for Lunar influence, camphor and other cool, white, moist aromatics.

### The Picatrix Tradition

The *Picatrix* provided the most elaborate systematic account of suffumigation in the Renaissance magical tradition. It specified incenses for each planet, each fixed star of influence, each of the 36 decans of the zodiac, and for operations involving specific spirits or spiritual beings. The *Picatrix* incense specifications typically combined multiple ingredients — roots, resins, woods, animal products — in proportions designed to produce a compound vapor that captured the full range of the target planet's qualities.

The *Picatrix* also described suffumigation as a technique for attracting planetary spirits into talismans and images: by burning the appropriate incense around the image while performing the appropriate invocations at the appropriate celestial moment, the magician created an aromatic "environment" in which the spirit was comfortable and could be drawn into the material object.

### Practical and Medical Uses

Beyond the ceremonial magical tradition, suffumigation had extensive practical and medical uses. Galenic medicine recognized fumigation as a therapeutic technique: aromatic vapors were used to treat conditions of the upper respiratory tract, to purify the air around sick patients, and to alter the humoral balance of the patient's body. The fumigation of rooms and clothing was widely used as a prophylactic against plague and other contagious illnesses — a practice that had genuine physical effects (some aromatic substances have genuine antimicrobial properties) embedded in a theoretical framework of miasmatic medicine (the belief that disease was spread through corrupted air).

Village healing practice used simpler fumigations — burning specific herbs around sick persons, animals, or buildings — without the elaborate astrological timing and planetary specification of learned magical practice. Juniper, rosemary, bay laurel, and similar aromatic herbs were commonly used for protective and purifying fumigations across much of Europe.

### Incense and Religious Practice

The magical tradition of suffumigation was never clearly separable from religious ritual. Incense burned on altars in ancient temples, incense in Jewish Temple worship, incense in Catholic liturgy — all shared the fundamental logic of aromatic vapor as a medium between human and divine, a means of communication across the boundary between the material and spiritual realms. The Catholic continued use of incense in the Mass (condemned by Protestant reformers as "papist" and practically magical) made the boundary between religious and magical fumigation impossible to maintain in practice.

**See also:** Natural Magic; Talismans; Spiritus and Pneuma; Planetary Spirits and Daemons; Ceremonial Magic; World Soul.
""",
    },
    {
        "slug": "weapon-salve",
        "title": "The Weapon Salve and Sympathetic Wound Treatment",
        "category": "Natural Magic and Natural Philosophy",
        "summary": "The celebrated Renaissance medical controversy over treating wounds by applying a salve to the weapon that caused them — rather than to the wound itself — as a test case for the theory of action at a distance and the power of sympathetic magic within natural philosophy.",
        "related_figures": ["Paracelsus", "Jan Baptist van Helmont", "Robert Fludd", "Francis Bacon"],
        "related_concepts": ["natural-magic", "paracelsianism", "cosmic-sympathy", "magic-and-medicine", "occult-properties", "doctrine-of-signatures"],
        "body": """## The Weapon Salve and Sympathetic Wound Treatment

The weapon salve (*unguentum armarium* in Latin, *Waffensalbe* in German) — a preparation applied to the weapon or instrument that caused a wound, or to something that had been in contact with the wound (a bandage, cloth, or even the blood itself), rather than directly to the wound — was one of the most famous and philosophically consequential medical controversies of the sixteenth and seventeenth centuries. Whether or not the weapon salve could actually heal wounds at a distance was not merely a question of practical medicine but a test case for the entire theory of sympathetic action at a distance on which natural magic was grounded, and it generated an extraordinary body of philosophical literature as practitioners, natural philosophers, and theologians debated whether it worked and, if so, by what mechanism.

### Paracelsus and the Mumia

The weapon salve was associated primarily with Paracelsus, who described it in several works and provided a theoretical account of why it should work. The Paracelsian theory invoked the concept of *Mumia* — a vital substance or force that permeated living bodies and could be transferred through contact. The *Mumia* of a wound was present not only in the wound itself but in the weapon that caused it (through contact), in the blood that flowed from it, and in anything that had been in contact with the wound. By applying a salve composed of specific ingredients to the weapon or blood-stained cloth, the physician could transmit the salve's healing virtues to the wound through the *Mumia* connection, healing at a distance through what Paracelsus understood as a genuine natural mechanism.

The standard recipe for the weapon salve was complex and varied between sources, but typically included materials of strong *Mumia* content: human fat (fat from a dead person, carrying vital force), moss growing on a human skull (*Usnea*, also known as "skull moss"), blood, and various aromatic and astrological ingredients. Some versions included the patient's own blood mixed with the salve applied to the weapon — creating the sympathetic connection through the patient's own *Mumia*.

### Van Helmont's Defense

Jan Baptist van Helmont (1580–1644) mounted the most sophisticated philosophical defense of the weapon salve in his *De Magnetica Vulnerum Curatione* ("On the Magnetic Cure of Wounds," 1621). Van Helmont argued that the weapon salve worked through a specific natural mechanism that he called "magnetic" — using the analogy of the lodestone's attraction of iron at a distance — rather than through anything supernatural or demonic. The human body generated a "magnetic" force field that extended beyond its physical boundaries; the *Mumia* transferred to the weapon or cloth maintained a connection with this field; and the salve applied to the weapon could therefore communicate its healing properties to the wound through this natural magnetic connection.

Van Helmont was careful to distinguish his account from both the Paracelsian *Mumia* theory (which he considered too vague) and from any suggestion of demonic agency (which would have made the weapon salve a form of forbidden magic). His account was intended to be a rigorous natural-philosophical theory of a genuine, if counterintuitive, natural phenomenon.

### Robert Fludd and the Magnetic Philosophy

Robert Fludd incorporated the weapon salve into his broader philosophy of nature in his *Medicina Catholica* and related works, treating it as a paradigmatic example of the sympathetic action at a distance that pervaded the natural world. For Fludd, the weapon salve demonstrated that matter was not simply inert extension but was pervaded by spiritual forces — the World Soul operating through the subtle spirit — that could maintain connections across spatial distance and act through them.

Fludd's account made the weapon salve a showcase for what he called the "magnetism" of all things: the attraction and repulsion operating between things through the medium of the World Soul's spirit. This magnetism was what natural magic operated through, and the weapon salve was simply one of its most striking and practically important applications.

### Theological Controversy and Skepticism

Not everyone was convinced. William Foster, an English clergyman, attacked the weapon salve in *Hoplocrisma-Spongus, or a Sponge to Wipe Away the Weapon-Salve* (1631), arguing that no natural mechanism could account for action at a distance without the involvement of demons, and that the weapon salve was therefore a form of demonic magic however its defenders described it. For Foster, the very claim that the salve worked without any physical contact between the remedy and the wound was an admission that the mechanism was supernatural — and therefore either miraculous (which God would not use for ordinary medical practice) or demonic.

Francis Bacon, characteristically, took a more empirical stance: in *Sylva Sylvarum* (published 1627), he discussed the weapon salve and sympathetic cure as phenomena worth investigating empirically, neither accepting nor rejecting their efficacy a priori. Bacon's empiricist approach — test the claim rather than reasoning from philosophical principles about whether it could work — prefigured the experimental attitude of the Royal Society.

**See also:** Natural Magic; Paracelsianism; Cosmic Sympathy; Magic and Medicine; Occult Properties; Doctrine of Signatures.
""",
    },
    {
        "slug": "oneiromancy",
        "title": "Oneiromancy: Dream Divination and the Prophetic Dream",
        "category": "Magic: Theory and Practice",
        "summary": "The practice and theory of dream divination — the belief that dreams could convey information about past, present, and future through divine, daemonic, or natural means — its classical and biblical foundations, and its role in Renaissance magical theory as a paradigmatic case of the imagination's receptivity to higher influences.",
        "related_figures": ["Marsilio Ficino", "Girolamo Cardano", "Paracelsus", "Heinrich Cornelius Agrippa"],
        "related_concepts": ["imagination-as-magical-faculty", "spiritus-and-pneuma", "scrying-and-crystal-gazing", "learned-astrology", "angelic-hierarchy", "subtle-body"],
        "body": """## Oneiromancy: Dream Divination and the Prophetic Dream

Dream divination — *oneiromancy* (from Greek *oneiros*, dream, and *manteia*, divination) — was one of the oldest and most universally practiced forms of divination in the ancient world and retained significant currency in the Renaissance as both a popular practice and a theoretically interesting problem for natural philosophy. The question of whether dreams could genuinely convey information about the future (or about hidden present realities), and if so, through what mechanism, engaged Aristotle, the Stoics, the Neoplatonists, and every major Renaissance natural philosopher who treated the magical and philosophical dimensions of sleep and dreaming.

### Classical Theory: Three Types of Prophetic Dream

The classical tradition distinguished several types of dream with different epistemological statuses. Macrobius's *Commentary on the Dream of Scipio* (c. 400 CE), the most influential ancient account in the medieval Latin West, classified dreams into five types:

1. **Somnium** (the enigmatic dream): A dream requiring interpretation because its meaning is veiled in metaphor or allegory.
2. **Visio** (the prophetic vision): A dream in which the future event is seen directly as it will happen.
3. **Oraculum** (the oracular dream): A dream in which a god, angel, or revered figure appears and gives direct instruction or information.
4. **Insomnium** (the nightmare or meaningless dream): A dream reflecting the physical and emotional state of the dreamer, with no prophetic significance.
5. **Visum** (the apparition): An apparition seen between sleep and waking, in the hypnagogic state.

Of these, the first three were significant for divination; the last two were physiological epiphenomena without divinatory import. The challenge for the interpreter was to determine which type any particular dream fell into.

Aristotle, characteristically skeptical of supernatural explanation, argued in *De Divinatione per Somnum* that prophetic dreams were most plausibly explained naturalistically: the dreaming person, free from the distractions of waking sensory experience, became sensitive to subtle physical signs that escaped waking attention, and the apparent prophecies were actually perceptions of natural physical processes (illness in the body not yet detectable by waking consciousness, subtle environmental changes) rather than genuinely future events.

### The Neoplatonic Account: Descent of the Soul

The Neoplatonists provided a richer account of prophetic dreams. In waking life, the soul's rational faculties were directed toward the sensible world and the practical demands of embodied existence, obscuring its connection to the higher world. In sleep, the rational faculties were inactive, and the soul (particularly through its *pneumatic vehicle*) was freed to receive impressions from the World Soul, from daemons, and even from the divine intellect. The prophetic dream was therefore a form of natural divination — not requiring supernatural intervention but drawing on the soul's inherent connection to the cosmic information network represented by the World Soul.

Iamblichus distinguished between "divine dreams" (sent by the gods and characteristically clear, authoritative, and accompanied by a distinctive quality of light or presence) and merely psychological dreams (produced by the soul's own activity in sleep, often fragmentary and confused). The divine dream was a form of waking theurgical experience in dream form — a genuine communication from a higher level of reality, not merely the soul's own processing of daily experience.

### Ficino and the Theory of Dream Physiology

Marsilio Ficino's account of dreams in *De Vita* and in his commentary on Plato's *Timaeus* integrated the Neoplatonic account with Galenic medicine and the theory of *spiritus*. During sleep, the *spiritus* — freed from the task of directing the body's waking activities — circulated more freely through the body and particularly concentrated in the brain and the *ventricles* (the cavities of the brain that Galenic anatomy associated with the faculties of imagination, reason, and memory). In this concentrated, purified state, the *spiritus* was more receptive to impressions from the World Soul and from celestial bodies, and the dreams it generated reflected these higher influences more clearly than waking imagination could.

This meant that the quality of prophetic dreaming was related to the quality of the dreamer's *spiritus*: the person with a refined, balanced *spiritus* (achieved through proper diet, exercise, the avoidance of melancholic foods, and the cultivation of philosophical reflection) would have clearer and more prophetically reliable dreams than the person with a crude, imbalanced *spiritus*.

### Agrippa's Systematic Account

Agrippa's *De Occulta Philosophia* II.60 provides a systematic taxonomy of prophetic dreams organized by their cause: some dreams come from the soul itself (reflecting its own powers and experiences), some from daemonic intervention (daemons being associated with the middle space between earth and heaven), some from divine illumination (direct communication from the divine intellect), and some from natural causes (the body's physical states reflected in the imagery of sleep). Each type required a different interpretive approach, and the interpreter's skill lay in distinguishing these types and applying the appropriate hermeneutic.

**See also:** Imagination as Magical Faculty; Spiritus and Pneuma; Scrying and Crystal Gazing; Learned Astrology; Angelic Hierarchy.
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
    print(f"\nBatch 20 done: {inserted} inserted, {skipped} skipped.")


if __name__ == "__main__":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
    main()
