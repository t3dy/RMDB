"""Seed batch 21: Cosmology and science — Infinite Universe, Mechanical Philosophy, Active Principles, Sublunary/Superlunary, Death of Nature."""

import sqlite3
import sys
import io
import json
from datetime import datetime

DB_PATH = "db/renmagic.db"

CONCEPTS = [
    {
        "slug": "infinite-universe",
        "title": "The Infinite Universe: Bruno, Copernicus, and the New Cosmology",
        "category": "Astrology and Cosmology",
        "summary": "The radical transformation of cosmological thought in the sixteenth century — from the finite, spherically bounded Ptolemaic cosmos to Bruno's infinite universe of innumerable worlds — and its profound implications for astrological theory, natural magic, and the Renaissance understanding of humanity's place in creation.",
        "related_figures": ["Giordano Bruno", "Nicolaus Copernicus", "Galileo Galilei", "Thomas Digges"],
        "related_concepts": ["ptolemaic-cosmos", "copernican-revolution-and-magic", "world-soul", "neoplatonism", "disenchantment"],
        "body": """## The Infinite Universe: Bruno, Copernicus, and the New Cosmology

The transformation of cosmology in the sixteenth century — from the finite, geocentric, spherically bounded universe of Aristotle and Ptolemy to the potentially infinite universe adumbrated by Copernicus and proclaimed by Bruno — was among the most dramatic conceptual ruptures in the history of Western thought. The implications extended far beyond astronomy: the infinite universe threatened the entire hierarchical cosmology on which Renaissance natural magic was grounded, destabilized the special ontological status of the Earth and its human inhabitants, and required a wholesale reconsideration of how celestial influences operated on the sublunary world.

### The Ptolemaic Cosmos and Its Limits

The Ptolemaic cosmos was finite: it had an outer boundary, the sphere of the fixed stars, beyond which lay the Empyrean heaven — the dwelling of God and the blessed, motionless, eternal, outside of space and time. This finite universe was also thoroughly hierarchical: the Earth at the center was the heaviest, least perfect, most changeable element; the successive planetary spheres above it were composed of the perfectly circular-moving, incorruptible quintessence; and the divine realm beyond the stars was the source and ground of all cosmic order.

This finitude and hierarchy were not merely astronomical facts but cosmological and theological values. The Earth's central position was not a mark of honor but of lowness — the heavy dregs of creation had sunk to the center under gravity's compulsion, while the noble, quintessential heavens rose above. Human beings, between earth and heaven, were positioned at the cosmic intersection between the corruptible and the eternal. The scale of created being — from dust to divinity — was legible in the spatial structure of the universe.

### Copernicus and Heliocentrism

Nicolaus Copernicus's *De Revolutionibus Orbium Coelestium* (1543) proposed that the Sun, not the Earth, occupied the center of the planetary system, and that the Earth was one of the planets revolving around it. This proposal was initially received primarily as a mathematical device for simplifying astronomical calculation, and Copernicus himself (influenced by Neoplatonic solar theology) presented it in terms that emphasized the Sun's dignity as the light and life-giver of the cosmos, now properly placed at its center.

The full cosmological implications of Copernicism took decades to develop. If the Earth moved, there was no compelling reason why it should be the only planet to do so — the other planets presumably moved in their orbits for the same reasons the Earth did. And if the Earth was a planet, there was no compelling reason why the other planets should not be like the Earth — capable of supporting life and intelligence.

Thomas Digges's *A Perfit Description of the Caelestiall Orbes* (1576) was the first English exposition of Copernicus and the first European text to explicitly propose that the universe might be infinite — that the sphere of fixed stars was not a finite shell enclosing the cosmos but the near edge of an infinite space populated by innumerable stars at various distances.

### Bruno and the Infinite Universe

Giordano Bruno (1548–1600) transformed the mathematical hypothesis of an infinite stellar space into a philosophical and theological vision of incomparable audacity. In his Italian dialogues (*La Cena de le Ceneri*, *De la Causa, Principio et Uno*, *De l'Infinito, Universo e Mondi*, all 1584) and Latin poems (*De Immenso*, 1591), Bruno argued for an infinite universe containing infinitely many worlds, each potentially inhabited, revolving around their own suns.

Bruno's infinite universe was grounded in his understanding of divine infinity: an infinite God could only express himself fully in an infinite creation. The finite cosmos of the Ptolemaic tradition was, for Bruno, a philosophical insult to divine omnipotence — as if a God of infinite power would create a universe just big enough to fit in one set of concentric spheres. The infinite cosmos was the necessary expression of infinite divine creativity.

This argument had direct implications for natural magic. If the universe was infinite, the hierarchical structure of Ficinian natural magic — with its seven planetary spheres mediating between the divine and the earthly, each contributing its specific quality to the World Soul's economy — was no longer obviously valid. Where did Bruno's infinite cosmos leave the magical theory of celestial influences? Bruno's own magical system, presented in his mnemonic and magical works (*De Umbris Idearum*, *De Magia*, *Theses de Magia*), attempted to reconstruct a magical theory appropriate to the infinite cosmos, locating the unity and interconnection of all things not in the finite Ptolemaic hierarchy but in the immanent World Soul that pervaded the infinite universe.

### The Implications for Magic and Religion

The infinite universe destabilized several key supports of Renaissance magical theory:

1. **Unique terrestrial position**: If the Earth was not the center of the cosmos, the microcosm-macrocosm doctrine needed revision — was the human body still a replica of the whole cosmos if the cosmos had no determinate center?

2. **The sphere of fixed stars**: If the stars were not fixed to a single sphere but were scattered at various distances through infinite space, the astrological significance of the zodiacal signs (which were projections of the Sun's apparent path against the fixed star background) was complicated.

3. **Celestial influence mechanisms**: The theory of celestial influence had depended on the specific geometric relationship between the Earth (at the center) and the planetary spheres (at specific distances above). An infinite universe with no privileged center required a different theoretical account.

Bruno addressed some of these implications but did not resolve them — his magical system remained a creative but incomplete response to the cosmological revolution he had helped to initiate.

**See also:** Ptolemaic Cosmos; The Copernican Revolution and the Occult Sciences; World Soul; Neoplatonism; Disenchantment.
""",
    },
    {
        "slug": "mechanical-philosophy",
        "title": "The Mechanical Philosophy and the Death of Occult Qualities",
        "category": "Astrology and Cosmology",
        "summary": "The seventeenth-century natural-philosophical program — associated with Descartes, Gassendi, Boyle, and ultimately Newton — that sought to explain all natural phenomena through the motion and collision of material particles, explicitly excluding occult qualities, hidden causes, and the animist assumptions of Renaissance natural magic.",
        "related_figures": ["René Descartes", "Robert Boyle", "Pierre Gassendi", "Francis Bacon", "Isaac Newton"],
        "related_concepts": ["disenchantment", "magic-and-the-scientific-revolution", "occult-properties", "world-soul", "cambridge-platonists", "natural-magic"],
        "body": """## The Mechanical Philosophy and the Death of Occult Qualities

The mechanical philosophy — the program of explaining natural phenomena through the motion, size, shape, and arrangement of invisible material particles, excluding all appeal to occult (hidden) qualities, animist principles, or teleological causes — was the dominant intellectual achievement of the seventeenth century's "new science" and the most direct institutional and conceptual challenge to the entire tradition of Renaissance natural magic. Where natural magic had depended on the reality of occult properties (hidden sympathies and antipathies, celestial influences, the vital forces of the World Soul), the mechanical philosophy proposed to replace all such explanations with the transparent operations of matter and motion, in principle fully explicable in mathematical terms.

### The Problem of Occult Qualities

Renaissance natural philosophy had inherited from Aristotelian and Neoplatonic tradition the concept of "occult qualities" (*qualitates occultae*) — properties of things that, unlike the primary qualities of heat, cold, wetness, and dryness, were hidden from direct sensory observation but could be inferred from their effects. The magnet's attraction of iron was an occult quality; the healing power of a specific herb was an occult quality; the influence of the Moon on tides and on the female cycle was an occult quality. These hidden properties were the theoretical basis of natural magic: the natural magician was the person who knew and could manipulate the occult qualities of natural things.

For the new mechanical philosophers, "occult quality" was an explanatory fiction that concealed ignorance rather than describing a genuine natural phenomenon. To say that a magnet attracted iron because of its "occult attractive quality" was simply to rename the phenomenon without explaining it. The mechanical philosophy demanded genuine explanation — in terms of the size, shape, and motion of invisible particles — rather than the naming of hidden properties.

### Descartes and the Vortex World

René Descartes (1596–1650) provided the most systematic and philosophically ambitious version of the mechanical philosophy in his *Principia Philosophiae* (1644). Descartes divided all reality into two substances: *res cogitans* (thinking substance — minds and souls, which thought but did not occupy space) and *res extensa* (extended substance — matter, which occupied space but did not think). The physical world was exhaustively described by *res extensa* and its motion: there were no spiritual forces in matter, no occult qualities, no animist principles, no World Soul. The universe was a machine — an infinitely extended plenum of material particles in complex vortical motion.

Descartes's mechanism was so thoroughgoing that it explicitly excluded even God's ongoing involvement in physical processes (after the initial act of creation and the establishment of laws of motion, God was not needed as an ongoing cause). This radical immanentism — nature entirely sufficient unto itself — was actually more threatening to theistic natural magic than simple atheism would have been, because it denied the very principle (the ongoing presence of divine and spiritual forces in nature) that made natural magic possible.

### Boyle and the Corpuscular Philosophy

Robert Boyle (1627–1691) developed what he called the "corpuscular philosophy" — a less ambitious but more empirically grounded version of mechanism that avoided some of Descartes's more extravagant metaphysical commitments while maintaining the fundamental program of explaining natural phenomena through the properties of material corpuscles. Boyle's *The Sceptical Chymist* (1661) attacked both Paracelsian three-principle chemistry and Aristotelian four-element theory, arguing that neither provided genuine explanations of chemical phenomena and that both should be replaced by corpuscular explanations.

Boyle was not a wholesale opponent of spiritual reality — he was a devout Christian who wrote extensively on natural theology — but he was committed to keeping the category of "God's direct action" separate from the category of ordinary natural explanation. In the ordinary course of nature, mechanical causes were sufficient; the appeal to spiritual forces or occult qualities in ordinary natural philosophy was, for Boyle, a confusion of categories rather than genuine natural explanation.

### Newton's Complication

Isaac Newton's *Principia Mathematica* (1687) provided the most powerful synthesis of the new mechanical-mathematical approach to nature and simultaneously reintroduced something that looked disconcertingly like occult action at a distance: gravity, which acted between massive bodies across empty space without any apparent mechanical contact. Newton's gravity — a force that attracted bodies in proportion to their masses and inversely to the square of the distance between them — was described mathematically with extraordinary precision but remained physically inexplicable in strictly mechanical terms.

Newton himself was deeply troubled by this and in private searched extensively for a mechanical ether that might transmit gravitational force through contact. He was also, as his voluminous unpublished manuscripts show, deeply engaged with alchemical practice and thought, and his understanding of "active principles" in nature — principles that could produce effects without mechanical contact — drew on the tradition of natural magic as much as on the new mechanical philosophy. The "disenchantment" of the world associated with Newton's achievement was, in his own thinking, far from complete.

**See also:** Disenchantment; Magic and the Scientific Revolution; Occult Properties; World Soul; Cambridge Platonists; Natural Magic.
""",
    },
    {
        "slug": "active-principles",
        "title": "Active Principles in Nature: Between Magic and Mechanism",
        "category": "Astrology and Cosmology",
        "summary": "The concept of non-mechanical active forces in nature — vital spirits, magnetic forces, gravitational attraction, chemical ferments — that occupied the contested boundary between Renaissance occult philosophy and the new natural philosophy of the seventeenth century, resisting full reduction to mechanical explanation.",
        "related_figures": ["Isaac Newton", "Jan Baptist van Helmont", "Francis Glisson", "Henry More", "Robert Boyle"],
        "related_concepts": ["occult-properties", "mechanical-philosophy", "world-soul", "paracelsianism", "cambridge-platonists", "magic-and-the-scientific-revolution"],
        "body": """## Active Principles in Nature: Between Magic and Mechanism

The concept of "active principles" in nature — forces, spirits, or agencies that produced real physical effects without being reducible to the simple motion and collision of inert material particles — occupied a contested middle ground between Renaissance occult philosophy and the new mechanical natural philosophy of the seventeenth century. Neither fully "magical" (in the sense of requiring intelligent spiritual agency) nor fully "mechanical" (in the sense of being explicable through contact action of material bodies), active principles were claimed by both sides of the seventeenth-century natural philosophical debate as resources for their own programs: by the defenders of natural magic as evidence that occult forces were real and important, and by mechanists (including Newton) as modifications to strict mechanism that preserved the explanatory power of non-mechanical causation within an otherwise mechanical framework.

### The Problem

Strict mechanical philosophy held that all natural phenomena could be explained through the motion and contact of material particles. But several well-established natural phenomena resisted this explanation: magnetism (action at a distance through empty space), gravity (the same), chemical reactions (which produced heat, light, and new substances through processes apparently different from simple particle collision), fermentation (the apparently vital, internally directed process of organic transformation), and the phenomena studied by the Helmontian tradition (digestion, disease, healing).

These phenomena constituted what the historian of science Keith Hutchison has called "occult qualities" in the strict sense — properties that were real and causally effective but not explicable in terms of the primary mechanical qualities of size, shape, and motion. The question of whether these "occult" properties could be reduced to mechanical explanation or required a different ontological category was one of the central debates of seventeenth-century natural philosophy.

### Van Helmont and the Archeus

Jan Baptist van Helmont's concept of the *Archeus* — the internal directive principle of each living body, responsible for organizing its chemical processes, defending against illness, and directing growth and repair — was the most influential seventeenth-century articulation of an active principle in the Paracelsian tradition. The *Archeus* was not mechanical: it directed chemical processes toward specific ends (the preservation of the living body) in a way that inert matter following mechanical laws could not. It was not fully spiritual either: it operated through and with the body's chemistry, not independently of it.

Van Helmont's detailed experimental work (the willow-tree experiment demonstrating that water contributed to plant mass, the quantification of "gas" as a distinct aeriform substance) was combined with a vitalist theoretical framework that insisted on the reality of directive principles in living nature that went beyond mechanical explanation.

### Newton and Active Principles

Isaac Newton's private engagement with active principles in nature is one of the most historically significant examples of the persistence of the occult philosophical tradition within the new science. Newton's published *Opticks* (1704) concluded with a series of "Queries" that speculated about a subtle "active principle" in nature — an ether or spirit pervading all space — that was responsible for gravity, chemical reactions, the phenomena of life, and ultimately for God's ongoing involvement in the natural world.

In his unpublished manuscripts, Newton engaged extensively with alchemical theory, searching for the "vegetative spirit" or "vital agent" that he believed was responsible for the "vegetative actions" — growth, fermentation, generation — that he distinguished from the "mechanical actions" of ordinary matter in motion. This distinction between mechanical and vegetative actions, and Newton's conviction that the latter required an active principle beyond mechanism, shows that his relationship to the occult philosophical tradition was far more complex than the standard "Newton banished magic" narrative suggests.

Newton's biographer Richard Westfall characterized Newton's position as a synthesis of the mechanical and the occult: he used mathematical mechanics to describe the behavior of matter in bulk while positing an occult (hidden, non-mechanical) active principle to account for the phenomena that mechanics alone could not explain.

### Francis Glisson and Vital Matter

Francis Glisson (1597–1677), an English physician and anatomist, developed a theory of "vital matter" in his *Tractatus de Natura Substantiae Energeticae* (1672) that attributed perception, appetite, and motion to matter itself, not to an immaterial soul imposed on passive matter. Glisson's "hylozoism" (the doctrine that matter is inherently alive) was one of the most philosophically radical expressions of the active principle tradition: it relocated the animism of the Renaissance natural magic tradition within matter itself rather than in a separate spiritual realm.

Glisson's hylozoism was influenced by the Cambridge Platonist tradition (particularly Henry More and Ralph Cudworth) but moved in a direction opposite to theirs: where More and Cudworth insisted on the reality of an *immaterial* Spirit of Nature to explain the phenomena of life, Glisson proposed that matter itself, properly understood, had the properties previously attributed to spirit.

**See also:** Occult Properties; Mechanical Philosophy; World Soul; Paracelsianism; Cambridge Platonists; Magic and the Scientific Revolution.
""",
    },
    {
        "slug": "death-of-nature",
        "title": "The Death of Nature: Carolyn Merchant and the Gendering of the Scientific Revolution",
        "category": "Historiography and Methodology",
        "summary": "Carolyn Merchant's influential 1980 argument that the Scientific Revolution — by replacing the Renaissance image of nature as a living, gendered organism with the mechanical model of nature as inert matter — constituted a conceptual 'death of nature' with profound implications for the history of magic, ecology, and feminist theory.",
        "related_figures": ["Carolyn Merchant", "Francis Bacon", "René Descartes"],
        "related_concepts": ["disenchantment", "mechanical-philosophy", "magic-and-the-scientific-revolution", "world-soul", "natural-magic", "magic-and-gender"],
        "body": """## The Death of Nature: Carolyn Merchant and the Gendering of the Scientific Revolution

Carolyn Merchant's *The Death of Nature: Women, Ecology and the Scientific Revolution* (1980) is among the most influential and controversial works in the environmental history of science and the feminist history of natural philosophy. Merchant's central argument is that the Scientific Revolution of the sixteenth and seventeenth centuries — specifically the transition from the Renaissance organic worldview (nature as a living female organism) to the mechanical philosophy (nature as inert matter governed by mathematical laws) — constituted a profound cultural transformation whose consequences extended far beyond natural philosophy into gender relations, the treatment of the natural environment, and the social organization of knowledge production.

### The Organic Worldview

Merchant's starting point is the Renaissance identification of nature with a feminine, maternal, living organism. The Renaissance cosmos — drawing on Plato's *Timaeus* (with its World Soul animating the material body of the cosmos), Hermetic philosophy (with its doctrine of a living nature pervaded by divine force), Paracelsian medicine (with its animist account of natural forces), and the broader tradition of natural magic — was organized around the image of the Earth as a nurturing mother, nature as a living system of correspondences and sympathies, and matter as inherently alive and productive.

This image of nature as a living female body had normative implications: it set limits on what could be done to nature. Just as there were taboos against harming or defiling a living human body, the image of nature as a living mother created implicit (and sometimes explicit) constraints on the exploitation of natural resources. Mining, in particular, was associated in the early modern period with a kind of violation of the earth-mother's body — extracting the mineral "embryos" she was nurturing in her womb — and this image generated ambivalence about aggressive mining operations.

### Bacon and the Domination of Nature

Merchant's analysis focuses particularly on Francis Bacon (1561–1626) as the theorist of the new relationship between science and nature. Bacon's metaphors for natural inquiry — the scientist putting nature "on the rack" to extract her secrets, "binding" and "constraining" nature to "obey" human command — are, in Merchant's reading, explicitly gendered images of domination that figured the new natural philosophy as the conquest and control of a feminine nature.

Bacon's vision of a "masculine birth of time" (from the title of an unfinished work), his rhetoric of "entering and penetrating" nature's secrets, and his insistence on the practical mastery of nature as the goal of natural knowledge — these, for Merchant, constituted a new epistemic stance toward nature in which the normative constraints of the organic worldview were explicitly overridden. Nature was no longer a mother to be respected but a resource to be exploited.

The connections Merchant drew between Bacon's natural philosophy and the contemporary witch trials (in which nature's female "secrets" were violently extracted through the torture of women accused of magical knowledge) were controversial and have been criticized by historians who found the connection too direct and the historical evidence for Merchant's specific claims too thin. Nevertheless, her broader argument about the gendering of nature and natural knowledge resonated deeply with feminist and environmental historians.

### The Mechanical Philosophy as Disenchantment

Merchant's account of the mechanical philosophy extended Max Weber's concept of "disenchantment" in an explicitly gendered direction. Where Weber had described disenchantment in terms of the rationalization of the world (the replacement of enchanted, value-laden nature with mathematical-mechanical nature), Merchant argued that this rationalization was specifically a *gendering* operation: the feminine, living, enchanted nature of the Renaissance was replaced by a masculinized, inert, exploitable nature of the mechanists.

Descartes's *res extensa* — matter as pure extension, defined only by its mathematical properties — was the philosophical culmination of this disenchantment: nature stripped of all the qualities (life, spirit, feeling, purpose) that had made it a subject of respect and identification, reduced to an object of pure calculation and manipulation.

### Critical Responses

Merchant's thesis has been enormously influential in environmental history, feminist philosophy of science, and the history of natural magic, but it has also attracted substantial criticism. Historians of science have argued that her portrait of the Renaissance organic worldview is idealized, that Bacon's actual science was more varied and less misogynist than her selected quotations suggest, and that the transition from organic to mechanical philosophy was more gradual, more geographically varied, and more internally complex than the "death of nature" narrative implies.

Historians of magic have been more sympathetic, finding in Merchant's framework a useful analytical tool for understanding the relationship between the decline of natural magic and the rise of the new science, even if the specific mechanisms of transition were more complex than she acknowledged.

**See also:** Disenchantment; Mechanical Philosophy; Magic and the Scientific Revolution; World Soul; Natural Magic; Magic and Gender.
""",
    },
    {
        "slug": "continuity-rupture",
        "title": "Continuity vs. Rupture: The Scientific Revolution Debate",
        "category": "Historiography and Methodology",
        "summary": "The central historiographical debate about the Scientific Revolution — whether it represents a fundamental rupture with Renaissance and medieval natural philosophy or a continuity with it — and the specific role of occult philosophy and natural magic in that debate.",
        "related_figures": ["Frances Yates", "Alexandre Koyré", "Paolo Rossi", "Lawrence Principe"],
        "related_concepts": ["magic-and-the-scientific-revolution", "the-yates-thesis", "disenchantment", "mechanical-philosophy", "natural-magic", "western-esotericism-as-category"],
        "body": """## Continuity vs. Rupture: The Scientific Revolution Debate

The question of whether the "Scientific Revolution" — the transformation of natural philosophy in the sixteenth and seventeenth centuries associated with Copernicus, Galileo, Kepler, Descartes, Newton, and their contemporaries — represented a fundamental rupture with previous intellectual tradition or a development from it has been one of the most productive and contested debates in the history of science. Within this broader debate, the specific question of the relationship between Renaissance occult philosophy (natural magic, Hermeticism, alchemy, astrology) and the new natural philosophy has been particularly significant: how much did the new science owe to, emerge from, or react against the occult philosophical tradition?

### The Rupture Position: Koyré and the New Universe

Alexandre Koyré's influential essays and books — particularly *From the Closed World to the Infinite Universe* (1957) — argued for a fundamental conceptual rupture between the finite, qualitatively organized, teleologically structured universe of ancient and medieval natural philosophy and the infinite, mathematically homogeneous, mechanistically organized universe of the new science. For Koyré, the Scientific Revolution was precisely a revolution: a transformation of the deepest conceptual structures through which nature was understood, not a gradual accumulation of new empirical knowledge.

On Koyré's account, the occult philosophical tradition — with its qualitative sympathies, its animist natural forces, and its teleological natural magic — belonged to the old universe rather than the new. The new science was defined partly by its rejection of these categories: the replacement of occult qualities with mechanical explanation, the substitution of mathematical description for qualitative symbolism, and the abandonment of the "great chain of being" hierarchical cosmos for the infinite, isotropic space of the new astronomy.

### The Continuity Position: Yates and the Hermetic Hypothesis

Frances Yates's *Giordano Bruno and the Hermetic Tradition* (1964) proposed a striking continuity thesis: that the Hermetic tradition — specifically the Ficinian and Brunonian recovery of Hermetic philosophy and natural magic — played a positive and essential role in stimulating the mental changes that produced the Scientific Revolution. The magician who believed he could manipulate natural forces through his understanding of cosmic sympathies was psychologically and conceptually closer to the scientist who manipulated natural forces through experimental knowledge than was the contemplative medieval philosopher who observed but did not intervene.

Yates's specific claims were:
1. The Hermetic tradition's emphasis on active manipulation of nature (as opposed to medieval contemplative natural philosophy) created a new attitude of intervention in nature that was a precondition of experimental science.
2. The Copernican hypothesis was partly motivated by Hermetic solar theology: the Sun's central position in the cosmos reflected its divine status in Hermetic cosmological thought.
3. Galileo's mechanics and Newton's dynamics owed something (perhaps not directly traceable) to the magical tradition's interest in forces, sympathies, and natural manipulation.

Yates's hypothesis was enormously stimulating and generated a substantial research program, but it was also extensively critiqued. Historians of science showed that the specific historical connections she proposed (Hermetic influence on Copernicus, Galileo, Newton) were weaker than she claimed, and that the new science's *mechanism* — its insistence on mathematical-mechanical rather than animist-sympathetic explanation — was precisely the feature that distinguished it most sharply from natural magic.

### Recent Scholarship: Complexity and Context

The debate has evolved considerably since the 1960s–70s confrontation between Koyré's rupture and Yates's continuity. Recent scholarship tends toward a more complex picture:

1. **Newton's alchemy**: Betty Jo Dobbs's *The Foundations of Newton's Alchemy* (1975) and her subsequent work demonstrated that Newton's alchemical practice and theory were not a bizarre personal aberration but were integral to his natural philosophy, motivating his interest in active principles and informing his concept of gravitational force. This showed that the "new science" and the occult tradition were far more intertwined in the seventeenth century than either pure rupture or pure continuity would suggest.

2. **Chymistry and chemistry**: Lawrence Principe and William Newman's work (*Alchemy Tried in the Fire*, 2002; *Atoms and Alchemy*, 2006) has traced the continuities and discontinuities between alchemical theory and practice and the emergence of chemistry, arguing that many early "chemists" were continuous with the alchemical tradition in ways that previous scholarship had missed.

3. **Local and contextual studies**: Rather than a single "Scientific Revolution," recent historiography tends to emphasize multiple local transformations in different disciplines, countries, and institutional contexts, each with its own relationship to the occult tradition.

**See also:** Magic and the Scientific Revolution; The Yates Thesis; Disenchantment; Mechanical Philosophy; Natural Magic; Western Esotericism as a Scholarly Category.
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
    print(f"\nBatch 21 done: {inserted} inserted, {skipped} skipped.")


if __name__ == "__main__":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
    main()
