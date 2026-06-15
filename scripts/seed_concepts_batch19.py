"""Seed batch 19: Rosicrucian/Theosophical — Christian Theosophy, Cambridge Platonists, Signatures, Elemental Spirits, Subtle Body."""

import sqlite3
import sys
import io
import json
from datetime import datetime

DB_PATH = "db/renmagic.db"

CONCEPTS = [
    {
        "slug": "christian-theosophy",
        "title": "Christian Theosophy: Divine Wisdom and Mystical Speculation",
        "category": "Esotericism and Mysticism",
        "summary": "The current within Protestant mysticism — associated above all with Jacob Böhme — that sought a direct experiential knowledge of God and the divine mysteries through visionary experience, combining Lutheran pietism with Neoplatonic, Kabbalistic, and Paracelsian elements into a distinctive tradition of mystical natural philosophy.",
        "related_figures": ["Jacob Boehme", "Robert Fludd", "Valentin Weigel", "Johann Georg Gichtel"],
        "related_concepts": ["rosicrucianism", "paracelsianism", "gnosis-and-gnosticism", "disenchantment", "lurianic-kabbalah", "western-esotericism-as-category"],
        "body": """## Christian Theosophy: Divine Wisdom and Mystical Speculation

Christian theosophy (*theosophia*, divine wisdom) designates a current of Protestant mystical speculation that emerged primarily in Germany in the late sixteenth and early seventeenth centuries and is associated above all with the Silesian shoemaker-mystic Jacob Böhme (1575–1624). Distinct from both the established Protestant theological tradition and from Ficinian Neoplatonism (though drawing on both), Christian theosophy sought an experiential knowledge (*theosophia*, wisdom of God, as opposed to mere *theologia*, discourse about God) grounded in direct visionary illumination and expressed through a distinctive symbolism that combined Lutheran religious experience with Paracelsian natural philosophy, Kabbalistic theosophy, and medieval German mysticism.

### Jacob Böhme and the Aurora

Jacob Böhme's first book, *Aurora* (written 1612, circulated in manuscript, not published until 1634), was the founding document of German Christian theosophy. Böhme had a visionary experience in 1600 in which he saw, or seemed to see, the inner structure of the spiritual-natural world revealed through the refraction of light in a pewter dish. Out of this experience grew a sustained attempt to describe the hidden ground of reality — the structure of God, nature, and the human soul — in language that was simultaneously mystical and natural-philosophical.

Böhme's system, worked out over more than a dozen subsequent books (*Forty Questions on the Soul*, *Mysterium Magnum*, *Aurora*, *Clavis*, etc.), is dense, non-systematic, and expressed in a highly idiosyncratic German that has always challenged translators. Its central vision is of a divine ground (*Ungrund*, "groundless ground" or abyss) that is analogous to the Kabbalistic *Ein Sof* — the absolutely undifferentiated divine infinity before God "becomes" anything. From this *Ungrund*, the divine self-disclosure proceeds through a series of internal divine acts that Böhme describes using the imagery of fire, light, and darkness.

Böhme's description of the divine nature as involving an internal conflict between the dark principle (will, desire, contraction) and the light principle (love, expansive outpouring) was one of the most controversial aspects of his thought. Critics accused him of Manicheanism (making evil co-eternal with God); defenders argued that Böhme was describing the internal dialectic of the divine self-disclosure rather than a cosmic dualism, and that this description illuminated aspects of experience — particularly the experience of suffering and spiritual crisis — that conventional theology left unexplained.

### Paracelsian and Kabbalistic Elements

Böhme's theosophy was deeply indebted to Paracelsian natural philosophy, which had circulated widely in the German-speaking world since the mid-sixteenth century. Böhme adopted Paracelsus's three principles (Sulfur, Mercury, Salt), his concept of a living spirit pervading nature, and his medical-cosmological view of the world as a system of correspondences between inner and outer, above and below. But where Paracelsus's framework remained primarily natural-philosophical and medical, Böhme gave these Paracelsian concepts a thoroughgoing mystical-theological interpretation: the three principles were not merely natural but divine realities expressing the inner structure of God as God disclosed himself in nature.

Böhme's knowledge of Kabbalah was mediated and incomplete — he probably did not read Hebrew and his access to Kabbalistic material was through secondary sources and the Christian Kabbalistic tradition — but Kabbalistic themes are clearly present in his system: the *Ungrund* as Ein Sof, the birth of light from darkness paralleling the *tzimtzum* and the emanation of the *Sefirot*, the concept of a cosmic fall and repair (*tikkun*). Later scholars (particularly Gershom Scholem) noted the structural parallels between Böhme's theosophy and Lurianic Kabbalah, though the question of direct influence remains debated.

### The Theosophical Tradition after Böhme

Böhme's influence spread through a network of correspondents and disciples in Germany, the Netherlands, and England during the seventeenth century. Johann Georg Gichtel (1638–1710) edited the first collected edition of Böhme's works and developed Böhme's ideas in a direction of spiritual interiority, developing the concept of the subtle body and its centers (the Tinktur, which he saw as analogous to the Kabbalistic Adam Kadmon, the Primordial Human) as a framework for understanding spiritual development.

In England, Böhme's works were translated in the 1640s–1660s and became a significant influence on radical Protestant sects (Quakers, Familists, antinomian groups) who found in Böhme's emphasis on direct spiritual illumination a support for their own critiques of institutional religion. The Cambridge Platonists (Henry More, Ralph Cudworth) engaged critically with Böhme, finding him intellectually fascinating but spiritually dangerous.

Gottfried Wilhelm Leibniz (1646–1716) read Böhme and was influenced by his dynamic conception of substance (the *monad* may owe something to Böhme's theosophical conception of the divine point or *Quell*). Hegel's dialectical philosophy (the dialectic of the Idea as it unfolds through contradiction) has been read as a secularized version of Böhmean theosophy.

**See also:** Rosicrucianism; Paracelsianism; Gnosis and Gnosticism; Lurianic Kabbalah; Western Esotericism as a Scholarly Category.
""",
    },
    {
        "slug": "cambridge-platonists",
        "title": "Cambridge Platonists: Christian Neoplatonism in Seventeenth-Century England",
        "category": "Esotericism and Mysticism",
        "summary": "The group of English philosophers centered at Cambridge in the mid-seventeenth century — including Henry More, Ralph Cudworth, Benjamin Whichcote, and John Smith — who sought to reconcile Christian faith with Neoplatonic philosophy, defending the reality of spirit against Cartesian mechanism and Hobbesian materialism.",
        "related_figures": ["Henry More", "Ralph Cudworth", "Benjamin Whichcote", "John Smith"],
        "related_concepts": ["neoplatonism", "disenchantment", "magic-and-the-scientific-revolution", "world-soul", "christian-theosophy", "western-esotericism-as-category"],
        "body": """## Cambridge Platonists: Christian Neoplatonism in Seventeenth-Century England

The Cambridge Platonists — a loose group of English philosophers, theologians, and preachers based primarily at Cambridge University in the middle decades of the seventeenth century — represent one of the most intellectually sophisticated defenses of Neoplatonic philosophy within the context of Protestant Christianity, and one of the last significant moments at which the conceptual vocabulary of the Renaissance esoteric tradition (World Soul, spiritual substance, the hierarchy of being) was deployed within the mainstream of English intellectual life. Associated primarily with Benjamin Whichcote (1609–1683), Henry More (1614–1687), Ralph Cudworth (1617–1688), John Smith (1618–1652), and Nathaniel Culverwell (1619–1651), the Cambridge Platonists responded to the twin threats of Hobbesian materialism and Calvinist theological determinism by developing a philosophy that insisted on the reality and priority of spiritual substance over material nature.

### Intellectual Context: Mechanism vs. Spirit

The Cambridge Platonists developed their philosophical positions in response to the dominant intellectual challenges of their era. Thomas Hobbes's *Leviathan* (1651) presented a comprehensive philosophical materialism in which all reality, including the human mind and soul, was ultimately material; there were no incorporeal substances, no real spiritual beings, and the soul was mortal. This materialist program threatened both the intellectual foundations of Christian theology and the moral framework of English society (since Hobbes's political philosophy was grounded in his materialism).

At the same time, René Descartes's mechanical philosophy divided reality into two substances — extended matter (*res extensa*) and thinking substance (*res cogitans*) — with no obvious mechanism for interaction between them, and described the material world as a machine governed entirely by mathematical-mechanical laws. For the Cambridge Platonists, this left the material world devoid of life, soul, and purpose — a universe in which God was at best a remote clockmaker who had wound up the machine at the beginning but played no ongoing role in its operations.

Against both Hobbesian monistic materialism and Cartesian dualistic mechanism, the Cambridge Platonists insisted on the priority of mind and spirit over matter, the real existence of immaterial substances, and the ongoing activity of God and spiritual principles in the natural world.

### Henry More and the "Spirit of Nature"

Henry More was the Cambridge Platonist most directly engaged with the question of magical and occult philosophy. His *Antidote Against Atheism* (1653), *The Immortality of the Soul* (1659), and *Enchiridion Metaphysicum* (1671) developed a Neoplatonic metaphysics explicitly designed to refute materialism and to defend the reality of spirit.

More's most original contribution to the debate was his concept of the *hylarchic principle* or *Spirit of Nature* — an immaterial but causally active principle that pervaded the material world and was responsible for all the phenomena that mechanical philosophy struggled to explain: the apparently purposive growth of organisms, the mysterious attraction of magnets, the apparently non-mechanical operation of gravity. More explicitly positioned this Spirit of Nature as a philosophical reconstruction of the ancient World Soul (Anima Mundi) and identified its existence with the anti-mechanist tradition running from Plato through the Neoplatonists to the Renaissance natural magicians.

More engaged directly with occult philosophy: he was deeply read in the Hermetic tradition, the Kabbalistic material available in Latin translation, and the works of Jan Baptist van Helmont and Jacob Böhme. He was also one of the most serious collectors and investigators of reports of supernatural phenomena — apparitions, poltergeists, and demonic possession — understanding these as empirical evidence for the reality of spiritual substances against materialist denial.

### Ralph Cudworth and the True Intellectual System

Ralph Cudworth's massive *The True Intellectual System of the Universe* (1678) was the most philosophically ambitious work produced by the Cambridge Platonists: a comprehensive refutation of atheistic materialism through a systematic account of the history of philosophy. Cudworth traced the history of materialism and idealism from ancient Greece to his own day, arguing that the Platonic tradition represented the authentic philosophical wisdom while Epicurean atomism (the ancient form of materialism) had always been a minor and philosophically deficient tradition.

Cudworth's discussion of the World Soul, of the relationship between divine and natural causation, and of the hierarchy of being drew extensively on ancient and Renaissance Neoplatonic sources. His concept of "plastic nature" — an immaterial but non-conscious principle immanent in matter that organized material processes according to intelligible ends — paralleled More's Spirit of Nature and represented a sophisticated attempt to maintain a spiritually animated natural world without collapsing back into either Stoic materialism or occult magical animism.

### Legacy for the History of Magic

The Cambridge Platonists represent an important transitional moment in the history of Renaissance magical philosophy: they were the last major philosophical school to seriously defend the conceptual vocabulary of the World Soul, the hierarchy of spiritual beings, and the reality of supernatural agency within the mainstream of English intellectual culture. Their engagement with Hermetic and Kabbalistic sources, their defense of spiritual causation against mechanical materialism, and their investigation of "supernatural" phenomena positioned them as the final representatives of a tradition stretching back to Ficino.

After the Cambridge Platonists, the defense of the World Soul and related concepts was relegated primarily to explicitly esoteric or heterodox traditions — Rosicrucianism, the various theosophical movements, and eventually Romantic Naturphilosophie — rather than being part of mainstream philosophical theology.

**See also:** Neoplatonism; World Soul; Disenchantment; Magic and the Scientific Revolution; Christian Theosophy.
""",
    },
    {
        "slug": "doctrine-of-signatures",
        "title": "The Doctrine of Signatures: Nature's Hieroglyphics",
        "category": "Natural Magic and Natural Philosophy",
        "summary": "The belief — associated particularly with Paracelsus but with much older roots — that plants, minerals, and other natural objects displayed visible signs (signatures) indicating their therapeutic or magical uses, making the natural world a text legible to the trained observer.",
        "related_figures": ["Paracelsus", "Giambattista della Porta", "Jacob Boehme", "Robert Fludd"],
        "related_concepts": ["natural-magic", "paracelsianism", "as-above-so-below", "macrocosm-and-microcosm", "occult-properties", "magic-and-medicine"],
        "body": """## The Doctrine of Signatures: Nature's Hieroglyphics

The doctrine of signatures (*Signaturenlehre*) holds that plants, minerals, and other natural objects bear visible markings, shapes, or other sensible qualities that indicate their therapeutic or magical uses — that God or nature has inscribed the function of each thing on its outward appearance, making the natural world a legible text for the observer trained to read it. The yellow color of saffron indicates its efficacy in treating jaundice; the shape of the walnut, resembling a human brain within its skull-like shell, indicates its efficacy in treating brain ailments; the spotted leaves of the lungwort (*Pulmonaria officinalis*) indicate its utility in pulmonary complaints. The doctrine is associated particularly with Paracelsus, who systematized and advocated it most influentially, but its roots are much older and its presence in the intellectual tradition much broader.

### Ancient and Medieval Roots

The doctrine of signatures was not invented by Paracelsus but was present, in varying degrees of systematization, throughout ancient and medieval natural medicine. The *Dioscorides* (first century CE), the foundational ancient herbal that remained authoritative throughout the medieval period, contained numerous entries where a plant's sensory properties were taken as indicators of its therapeutic virtues. The nettles' sting suggested their heating properties; the aconite's resemblance to a hood or helmet (*aconitum* from Greek *akonition*, "dart", used for poisoning arrows) indicated its dangerous nature.

Medieval herbals expanded on these connections, often in terms of the Galenic humoral system: the color, taste, smell, and texture of plants were taken as indicators of their elemental qualities (hot, cold, wet, dry) and thus of their humoral effects on the body. This "quality-based" reading of natural signs was not identical to the Paracelsian doctrine of signatures (which was less focused on Galenic qualities and more on specific correspondences between plant form and bodily organ) but prepared the ground for it.

### Paracelsus and the Systematization of Signatures

Paracelsus developed the doctrine of signatures most explicitly in his *Paragranum* (1530) and in scattered passages of his medical writings. For Paracelsus, the signature of a plant or mineral was not merely a convenient memory aid for the herbalist but a genuine ontological sign — a mark inscribed by God (or by the Archaeus of the plant itself) on the plant's exterior that expressed the plant's inner virtue and its proper relationship to the corresponding organ or ailment in the human body.

The Paracelsian doctrine operated within the broader framework of the macrocosm-microcosm analogy and the principle of cosmic sympathy: since the human body was a microcosm replicating the structure of the greater world, the organs of the body corresponded to specific natural things (plants, minerals, planets, stars). The plant that bore the signature of the liver (the yellowish-green color of *Chelidonium majus*, for example) was related by genuine correspondence to the liver in the body, and its healing efficacy for liver complaints was grounded in this correspondence rather than being merely empirical.

This made the doctrine of signatures both a hermeneutical theory (how to read nature as a text) and a therapeutic theory (how to find medicines): the physician who could read the signatures of natural things had direct access to the divine pharmacy inscribed in the natural world, without needing to rely solely on the empirical traditions of Galenic medicine.

### Giambattista della Porta and Natural Magic

Giambattista della Porta's *Magia Naturalis* (1558, expanded 1589) incorporated the doctrine of signatures into the broader framework of natural magic, presenting it as part of the science of sympathies and antipathies by which the natural magician could work. Della Porta gave numerous examples of signatory correspondence: the scorpion's tail, given in medicine, could heal scorpion stings; plants resembling serpents could treat snakebite; the mandrake's human-shaped root indicated its connection to human physiology.

Della Porta was more skeptical than Paracelsus of the ontological depth of the doctrine — he sometimes presented signatory correspondences as empirical regularities to be tested rather than as metaphysical necessities — but he incorporated them as one tool among many in the natural magician's repertoire.

### Jacob Böhme and Cosmic Language

Jacob Böhme's *Signatura Rerum* ("The Signature of All Things," 1621) gave the doctrine its most mystical and philosophically ambitious formulation. For Böhme, signatures were not merely practical indicators of therapeutic virtues but manifestations of the divine Word (*Logos*) inscribed in the natural world — the language in which God had spoken creation into being, visible to those with eyes to see. Every natural thing, from the smallest herb to the largest mountain, bore the signature of the divine quality that was its deepest essence, and the philosopher or mystic who learned to read these signatures was reading the divine Word written in the book of nature.

Böhme's *Signatura Rerum* was enormously influential in the German Pietist tradition, in English Romanticism (where it influenced William Law and William Blake), and in the broader tradition of what Hanegraaff calls "enchanted" natural philosophy — the conviction that the natural world is a spiritually meaningful text rather than a mechanically indifferent system of forces.

### The Decline of the Doctrine

The doctrine of signatures was attacked from the mid-seventeenth century onward by critics who argued that the correspondences it claimed to find were imaginary rather than real: the liver-shaped leaf did not have genuine therapeutic effect on the liver; the "brain" shape of the walnut was a product of the observer's imagination rather than an objective feature. The rise of controlled experiment as the criterion of therapeutic validity — exemplified in Robert Boyle's experimental program — gradually displaced the interpretive method of signature-reading with empirical testing of medicinal effects.

**See also:** Natural Magic; Paracelsianism; As Above, So Below; Macrocosm and Microcosm; Occult Properties; Magic and Medicine.
""",
    },
    {
        "slug": "elemental-spirits",
        "title": "Elemental Spirits: Gnomes, Sylphs, Undines, and Salamanders",
        "category": "Natural Magic and Natural Philosophy",
        "summary": "The tradition, systematized by Paracelsus, of invisible beings inhabiting the four elements — earth, air, water, and fire — distinct from angels and demons, constituting a third category of spiritual being in the natural world and providing the theoretical basis for elemental magic.",
        "related_figures": ["Paracelsus", "Heinrich Cornelius Agrippa", "Robert Fludd"],
        "related_concepts": ["natural-magic", "paracelsianism", "angelic-hierarchy", "demonology", "world-soul", "four-worlds"],
        "body": """## Elemental Spirits: Gnomes, Sylphs, Undines, and Salamanders

The doctrine of elemental spirits — invisible beings inhabiting the four elements, distinct from both angels (who inhabit the empyrean heaven) and demons (fallen angels) — represents one of the most creative contributions of Paracelsian natural philosophy to the Western magical tradition. Where medieval Christianity had populated the spiritual world primarily with angels and demons, Paracelsus introduced a third category of spiritual being: natural spirits that inhabited the four elements as their proper environment, possessed a quasi-material body suited to that element, and constituted a kind of "natural" spiritual life below the level of the angelic hierarchy.

### The Paracelsian System

Paracelsus described the elemental spirits in his *Liber de Nymphis, Sylphis, Pygmaeis et Salamandris* ("On the Nymphs, Sylphs, Pygmies, and Salamanders," written c. 1530–35, published posthumously 1566):

- **Gnomes** (*Pygmei*, later also *Gnomi*): Beings of the earth element, inhabiting the solid ground, mines, and underground caverns. Gnomes moved through earth as easily as humans moved through air; they were associated with hidden mineral wealth, with the secrets of the underground, and with the alchemical processes occurring in the earth's interior.

- **Sylphs** (*Sylvestres* or *Sylphi*): Beings of the air element, inhabiting the atmosphere. Their bodies were composed of air-like substance, allowing them to move freely through the atmosphere. They were associated with wind, weather, and the aerial realm between earth and heaven.

- **Undines** (*Nymphae* or *Undinae*): Beings of the water element, inhabiting rivers, lakes, seas, and underground water sources. They were associated with the hidden life of water and with the alchemical dimension of dissolution and purification.

- **Salamanders** (*Salamandri*): Beings of the fire element, inhabiting flames and the fiery principle within all matter. The salamander (the real animal) was believed in folklore to be able to survive fire unharmed, and Paracelsus took this as evidence that fire had its appropriate spiritual inhabitant.

Paracelsus was careful to distinguish elemental spirits from both demons and angels. They were not fallen angels (demons) and thus not inherently malevolent; they were not holy angels and thus not objects of devotion. They were natural beings — part of the created order — whose nature was determined by their elemental constitution. They could be encountered, communicated with, and potentially enlisted in natural magical operations, but they required different approaches than the angelic invocations of ceremonial magic or the demonic conjurations of grimoire magic.

### Classical and Medieval Antecedents

While Paracelsus systematized the doctrine of elemental spirits into its most influential form, the idea had deep antecedents in classical and medieval thought. Ancient discussions of *daimones* (intermediate beings between gods and humans) included nature spirits associated with specific natural locations and phenomena: the *nymphs* of water sources, the *satyrs* and *fauns* of forests, the *dryads* of trees. These classical nature-spirit traditions persisted in modified forms throughout the medieval period, sometimes assimilated to demonic categories (forest spirits as minor demons), sometimes surviving in a more ambiguous folkloric form.

Medieval traditions of the *fée* (fairy) in French literature and the analogous traditions of elves and dwarves in Germanic and Scandinavian culture constituted a parallel popular tradition of nature spirits with partly overlapping characteristics. Paracelsus probably drew on these popular traditions as well as on classical and medical-alchemical sources in constructing his systematic account.

### The Elemental Spirits in Ceremonial Magic

The Paracelsian elemental spirit doctrine was incorporated into ceremonial magic in the seventeenth century, above all through the Rosicrucian tradition. The Rosicrucian manifestos of 1614–15 drew on Paracelsian natural philosophy extensively, and subsequent Rosicrucian-influenced magical traditions (including the Hermetic Order of the Golden Dawn) developed the elemental spirit doctrine into a systematic framework for elemental magic.

In the Golden Dawn's system (which became foundational for modern Western magic), the four elemental spirits were associated with the four magical implements (the wand for fire/salamanders, the cup for water/undines, the dagger for air/sylphs, the pentacle for earth/gnomes), with the four quarters of the magic circle, and with the four angelic guardians of the elemental quarters (Michael for fire, Gabriel for water, Raphael for air, Uriel for earth). This systematic integration of elemental spirits into the ceremonial framework gave them a stable symbolic position in Western magical practice.

### Alexander Pope and Literary Sylphs

The most culturally significant deployment of the elemental spirit tradition outside the explicitly magical context was Alexander Pope's mock-heroic poem *The Rape of the Lock* (1712, 1714), which populated its satire of aristocratic social life with sylphs borrowed from the Rosicrucian tradition. Pope's sylphs — invisible guardian spirits who protect the heroine Belinda's chastity and honor — were presented in a spirit of ironic play with the Rosicrucian tradition but also reflected genuine familiarity with that tradition's content. The poem's popularity gave the sylph in particular a permanent place in English literary culture.

**See also:** Natural Magic; Paracelsianism; Angelic Hierarchy; Demonology; World Soul.
""",
    },
    {
        "slug": "subtle-body",
        "title": "The Subtle Body: Spirit, Vehicle, and the Inner Anatomy of Magic",
        "category": "Natural Magic and Natural Philosophy",
        "summary": "The tradition of a semi-material, luminous vehicle of the soul — pneuma, astral body, or vehicle — that mediates between the soul and the physical body, serves as the organ of magical and imaginal operation, and constitutes the inner anatomy within which visionary and magical experience occurs.",
        "related_figures": ["Marsilio Ficino", "Paracelsus", "Robert Fludd", "Henry More", "Giordano Bruno"],
        "related_concepts": ["spiritus-and-pneuma", "imagination-as-magical-faculty", "neoplatonism", "world-soul", "scrying-and-crystal-gazing", "fascination-and-evil-eye"],
        "body": """## The Subtle Body: Spirit, Vehicle, and the Inner Anatomy of Magic

The concept of the subtle body — a semi-material luminous vehicle of the soul, intermediate between the spiritual soul proper and the gross physical body — is one of the most widespread and persistent ideas in the history of magic and mysticism. Appearing under various names (*pneuma*, astral body, ethereal vehicle, spirit, ochema, *spiritus*) in ancient Neoplatonic philosophy, Stoic pneumatology, Hermetic cosmology, Paracelsian medicine, and Renaissance natural magic, the subtle body provided the theoretical infrastructure for understanding how the soul operated in and through the body, how magical influence was transmitted, how the imagination could physically affect both the practitioner's own body and external objects and persons, and how visionary and out-of-body experiences were possible.

### The Philosophical Background: Pneuma and Vehicle

The concept derives from several converging ancient traditions:

**Stoic pneuma**: In Stoic natural philosophy, *pneuma* (breath or spirit) was a rarefied material substance pervading all things and constituting the animating principle of the cosmos and of living beings. The human soul was an especially refined *pneuma*, distinguishable in grade from the coarser *pneuma* of animals and plants. The Stoic *pneuma* was genuinely material (if very subtle material), not immaterial, and this gave it causal power in the physical world that a purely immaterial soul would have lacked.

**Neoplatonic ochema-pneuma**: The Neoplatonists developed the concept of the *ochema* ("vehicle," *ókhēma*) as the luminous chariot or container in which the soul descended from the divine realm into material embodiment. Proclus distinguished between the highest vehicles of the soul (given by the Demiurge, eternal and luminous) and lower pneumatic vehicles acquired during the soul's descent through the planetary spheres. The soul thus arrived in its human body wearing multiple vehicles: the highest ethereal vehicle of divine origin, and the successive pneumatic vehicles accumulated in the planetary descent, which constituted the "astral body" in the Renaissance sense.

### Ficino and Spiritus in Renaissance Magic

Marsilio Ficino's *De Vita* (1489) made the concept of spiritus — understood as the body's most subtle, mobile, and luminous dimension, the vehicle of the soul within the body — central to his theory of natural magic. The *spiritus* was the organ through which stellar influences operated: it was composed of a very subtle material substance analogous to the *spiritus mundi* (the spirit of the world that pervaded the cosmos), and it was therefore susceptible to the same stellar influences that acted on the *spiritus mundi*.

This made the scholar's *spiritus* both his vulnerability (to Saturnine melancholy and physical depletion) and his magical instrument: by cultivating the *spiritus* through the proper foods, music, smells, and activities, the scholar could make it a better conductor of Solar and Jovial influences, achieving both physical health and philosophical excellence. The talisman, on this account, worked because it concentrated stellar influence in a material object whose *spiritus* was specially prepared through astrological timing and appropriate material composition.

The imagination was, for Ficino, the primary faculty of the subtle body: it was through the imagination (operating in and through the spiritus) that images from the external world were received, stored, and projected, and that the influence of mental states on the physical body was mediated. The powerful imagination of the *fascinator* (the person with the evil eye) worked by projecting a concentrated flux of spiritus laden with malevolent imaginal content through the eyes into the eyes and spiritus of the victim.

### Paracelsus and the Sideral Body

Paracelsus introduced a distinctive terminology for the subtle body: the *sidereus* (sideral or astral body, derived from the Latin *sidus*, star) was the stellar or elemental body of the human being, the vehicle acquired during the soul's descent through the planetary spheres. This sideral body was the seat of the imagination, dreams, and magical operations: it was through the sideral body that the practitioner could act at a distance, project their influence on others, and receive influences from the stars.

Paracelsus's concept of the *Mumia* — a subtle vital force or essence that could be transmitted from one body to another and that served as the medium of magical healing at a distance — is related to the subtle body concept: it was the Mumia of the wound that the sympathetic weapon salve (applied to the weapon rather than the wound) could reach and heal.

### Henry More and Extension of the Spirit

Henry More's *The Immortality of the Soul* (1659) provided a seventeenth-century philosophical defense of the subtle body concept in terms designed to refute both Hobbesian materialism and Cartesian dualism. More argued that the soul was not *res cogitans* in Descartes's sense (a purely thinking, non-extended substance) but a substance that was both immaterial and *extended* — it occupied space without being matter. The soul's "spissitude" (density or fineness) could vary, making it compatible with material nature at its most subtle levels while remaining genuinely immaterial.

More's concept of a spiritual substance that was extended but not material provided a philosophical framework for understanding how the soul could act on and through the body, and implicitly for how subtle body phenomena (visions, magical operations at a distance, the experience of spiritual beings) were possible. His work constitutes one of the last serious philosophical defenses of the subtle body concept within the mainstream of English intellectual culture.

**See also:** Spiritus and Pneuma; Imagination as Magical Faculty; Neoplatonism; World Soul; Scrying and Crystal Gazing; Fascination and the Evil Eye.
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
    print(f"\nBatch 19 done: {inserted} inserted, {skipped} skipped.")


if __name__ == "__main__":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
    main()
