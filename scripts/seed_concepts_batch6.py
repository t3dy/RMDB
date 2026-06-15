"""Seed concepts table — Batch 6: Paracelsianism, Gnosis, Chain of Being, Printing, Disenchantment."""

import sqlite3
import json
import sys
import io
from datetime import datetime

DB_PATH = "db/renmagic.db"

CONCEPTS = [
    {
        "slug": "paracelsianism",
        "title": "Paracelsianism",
        "category": "Rosicrucian and Later Traditions",
        "summary": "The intellectual movement inspired by the writings of Paracelsus (Theophrastus Bombastus von Hohenheim, 1493–1541), developing his chemical medicine, alchemical natural philosophy, and theosophical cosmology into an influential and contested alternative to Galenism that shaped late sixteenth and seventeenth-century medicine, natural philosophy, and esotericism.",
        "related_figures": ["Paracelsus", "Heinrich Khunrath", "Robert Fludd", "Joan Baptista van Helmont"],
        "related_concepts": ["alchemy", "spiritus-and-pneuma", "macrocosm-and-microcosm", "rosicrucianism", "signatures"],
        "body": """## Paracelsus and the Paracelsian Reform

Paracelsianism designates the diffuse but influential movement inspired by the writings of Theophrastus Bombastus von Hohenheim, called Paracelsus (1493–1541), a Swiss-German physician, alchemist, and religious thinker whose work constituted one of the most radical challenges to Galenic medical authority in the Renaissance. Paracelsus's program combined chemical medicine (the use of mineral and metallic remedies prepared alchemically), a new theory of disease (diseases as specific entities caused by specific agents, rather than humoral imbalance), and a comprehensive natural philosophy grounding medicine in a theosophical cosmology that drew on Neoplatonism, Kabbalah, and his own idiosyncratic speculations.

Paracelsus himself published relatively little during his lifetime; the vast body of Paracelsian texts was compiled, edited, and partly fabricated by his followers in the decades after his death. This textual situation—a corpus assembled posthumously from manuscripts of uncertain authenticity—complicates the distinction between "Paracelsus" and "Paracelsianism": much of what passed as Paracelsian doctrine in the later sixteenth century reflected the interests and additions of his editors and followers rather than Paracelsus himself.

## The Tria Prima and Chemical Medicine

The theoretical core of Paracelsian medicine was the doctrine of the *tria prima*: the three principles of sulphur, mercury, and salt that constituted all material things. Paracelsus replaced the Galenic four humors (blood, phlegm, yellow bile, black bile) and four elements (earth, water, fire, air) with this chemical triad, derived from alchemical theory. Sulphur was the combustible principle (the soul of things); mercury was the volatile, fluid principle (the spirit of things); salt was the fixed, solid principle (the body of things).

Disease, on this account, resulted from the disorder or excess of one of the three principles in a specific organ or the body as a whole. Treatment required chemical remedies—minerals, metals, and their compounds prepared alchemically—that could address the specific disturbed principle directly. This was a revolutionary claim: rather than adjusting diet, bloodletting, and herbal remedies to rebalance the humors, the Paracelsian physician applied chemical specifics, including antimony, arsenic, mercury compounds, and sulfuric preparations, to treat specific diseases.

The practical successes of Paracelsian chemical medicine—particularly its treatments for syphilis (which Galenic medicine handled poorly) and some infectious diseases—gave it a genuine empirical basis, even though many of its theoretical claims were speculative. The tension between Paracelsian chemical practice and Galenic theoretical framework was one of the major intellectual fault lines of late sixteenth and early seventeenth-century medicine.

## Paracelsian Natural Philosophy

Beyond medicine, Paracelsianism encompassed a comprehensive natural philosophy that drew on the macrocosm/microcosm analogy, the doctrine of signatures, and an animated conception of nature. Paracelsus's doctrine of *signatures* (*signatura rerum*) held that natural objects bore visible signs of their hidden medicinal virtues: the walnut's lobed shape mirrored the brain and therefore indicated its usefulness for cerebral ailments; the yellow of saffron indicated its affinity for bile and jaundice. This analogical method of discovering therapeutic virtues drew on the same cosmological framework as astral magic but applied it to morphological rather than celestial correspondences.

Paracelsian nature was thoroughly animated: every natural object contained its own spirit (*archaeus*), an internal life-principle that directed its processes. The *archaeus* of each organ governed that organ's specific functions; the *archaeus mundi* (world spirit) governed the cosmos. Disease resulted from the disruption of the local *archaeus* by external *archei* (disease-causing agents) or by toxic influences. This animistic cosmology aligned Paracelsianism with the broader tradition of Renaissance natural magic and Hermetic philosophy.

## The Paracelsian Controversy

Paracelsian medicine was fiercely contested by Galenic medical authorities throughout the later sixteenth century. The controversy was not merely academic: it involved professional boundaries, institutional power (who controlled university medical education), patient safety (Paracelsian remedies were genuinely dangerous in unskilled hands), and cosmological commitments (the Paracelsian animated cosmos versus the Galenic qualitative-humoral framework).

The controversy played out differently in different European contexts. In Germany and Central Europe, Paracelsianism found institutional support in some Protestant courts (the association with Luther-style reform against scholastic authority was culturally potent). In France, the Paris medical faculty was strongly anti-Paracelsian through the late sixteenth century. In England, Paracelsianism influenced the Cambridge-educated physician and natural philosopher Helmont, whose later work extended Paracelsian chemistry in important directions.

Joan Baptista van Helmont (1580–1644) transformed Paracelsianism in significant ways, introducing the concept of *gas* (from Greek *chaos*) for aeriform substances, conducting quantitative experiments (the willow tree experiment on plant growth), and developing a more systematic chemical pneumatology. Helmont's work represents a crucial transitional figure between Paracelsian chemical philosophy and the chemical revolution of Boyle and Lavoisier.

## Paracelsianism and Esotericism

In the later sixteenth and early seventeenth centuries, Paracelsianism merged with other currents of learned esotericism—Hermeticism, Kabbalah, alchemy, Rosicrucianism—to produce the distinctive "Christian Theosophy" of figures like Heinrich Khunrath, Robert Fludd, and Jakob Böhme. This synthesis drew on Paracelsus's theosophical cosmology (his account of the divine creative process and the spiritual dimensions of natural phenomena) to develop a comprehensive religious philosophy in which alchemy, natural philosophy, and Christian spirituality were inseparable.

Jakob Böhme (1575–1624), a shoemaker in Görlitz who experienced visionary illuminations and wrote a series of theosophical works of extraordinary complexity, drew explicitly on Paracelsian concepts (the tria prima, the spiritual fire) in developing his account of the divine nature and its self-revelation through creation. Böhme's influence on subsequent German mysticism and Romantic philosophy makes him one of the most significant transmitters of Paracelsian ideas into the modern period.
""",
    },
    {
        "slug": "gnosis-and-gnosticism",
        "title": "Gnosis and Gnosticism",
        "category": "Hermetic Tradition",
        "summary": "Ancient religious and philosophical currents centering on salvific knowledge (gnosis) of the divine and the soul's true origin, often involving cosmic dualism and the devaluation of the material world; important background for Hermetic texts and for the scholarly category of Western esotericism, but requiring careful distinction from later appropriations.",
        "related_figures": ["Wouter Hanegraaff", "Marsilio Ficino"],
        "related_concepts": ["hermetism", "neoplatonism", "emanation", "western-esotericism-as-category"],
        "body": """## Defining Terms

"Gnosis" (Greek, "knowledge") in its technical religious-historical sense designates a specific type of salvific knowledge: direct, experiential acquaintance with the divine, the soul's true nature, and its origin in and return to a transcendent realm, distinguished from rational knowledge (*episteme*) and from faith (*pistis*). "Gnosticism" is the modern scholarly term for a cluster of ancient religious movements—active primarily in the second and third centuries CE—that centered on gnosis as the means of salvation and typically combined cosmological dualism (a distinction between a transcendent true God and an inferior or evil creator deity, the Demiurge) with narratives of the soul's fall into matter and its potential return to the divine pleroma.

Both terms are contested. "Gnosticism" as a category was constructed by modern scholarship (primarily by Hans Jonas's *Gnosis und spätantiker Geist*, 1934, and its English development *The Gnostic Religion*, 1958), and some contemporary scholars have argued for its abandonment or radical revision (Michael Williams, *Rethinking "Gnosticism"*, 1996; Karen King, *What Is Gnosticism?*, 2003). The argument is that "Gnosticism" groups together movements that differed substantially in texts, cosmology, ritual, and self-understanding under a category imposed by later scholarship rather than recognized by historical actors.

For the history of Renaissance magic, "Gnosticism" in the strict historical sense is less directly relevant than the broader concept of *gnosis* as an orientation toward knowledge—the aspiration toward direct experiential knowledge of divine reality that appears in Hermetic texts, Neoplatonic philosophy, and various forms of Christian mysticism. The Hermetic texts in particular are best understood as oriented toward gnosis in this broad sense, and the Gnostic background (in the sense of the Hellenistic religious pluralism within which both Gnosticism and Hermetism emerged) illuminates their content.

## Gnostic Cosmology and its Relevance

The distinctive cosmological feature of Gnostic systems was cosmic dualism: a radical distinction between the transcendent, unknowable true God and the inferior divine being (variously called Demiurge, Ialdabaoth, or Yaldabaoth) who created the material world in ignorance or malevolence. Material creation was not the work of the highest God but of a lesser being who mistakenly believed himself supreme; the divine sparks trapped in human souls were exiles from the true divine realm, awaiting liberation through gnosis.

This cosmological dualism contrasted with Neoplatonic emanationism, which held that material reality was the lowest but not evil product of a single divine principle. The Hermetic texts occupy an intermediate position: some (*Corpus Hermeticum* I, *Asclepius*) describe the Demiurge in broadly Platonic terms as a subordinate but legitimate divine craftsman; others appear more dualist in their treatment of matter and the body. This variety reflects the pluralist Hellenistic-Egyptian environment in which both Hermetism and various Gnostic movements emerged.

Renaissance readers of the Hermetic texts generally did not engage with Gnosticism as a specific movement (they lacked access to most Gnostic texts, the Nag Hammadi library being undiscovered until 1945). But they were aware, through Irenaeus, Epiphanius, and other patristic heresiologists, that ancient "heresies" had involved Gnostic-type dualism, and they were cautious about readings of Hermetic texts that implied too radical a devaluation of matter. Ficino's integration of Hermetism with Neoplatonism served partly to domesticate potentially dualist Hermetic tendencies within a framework that affirmed the goodness of creation.

## Gnosis and the Esoteric Tradition

Wouter Hanegraaff's work on Hermetism has emphasized the centrality of gnosis—in the broad sense of transformative, experiential knowledge of the divine—to the original Hermetic texts and to the Western esoteric tradition more broadly. On this account, the distinguishing feature of esoteric traditions is not their specific metaphysical doctrines but their orientation toward gnosis: direct, transforming knowledge of ultimate reality rather than merely rational or propositional knowledge about it.

This formulation allows Hanegraaff to connect diverse traditions (Hermetism, Kabbalah, alchemy, Neoplatonism) without reducing them to a single doctrine, while identifying what they share: an epistemological orientation toward experiential transformation and a soteriology centered on knowledge rather than faith or works. It also explains their "marginal" status in Western culture: gnosis-oriented traditions have been consistently marginalized by religious institutions centered on faith and sacrament (Christianity) and by intellectual institutions centered on rational demonstration (philosophy, science), not because they are intellectually inferior but because they pursue a different kind of knowing.

## Gnosticism in Modern Reception

The modern Western rediscovery of Gnostic texts (the Berlin Codex, 1896; the Nag Hammadi library, 1945) and their scholarly edition has made authentic Gnostic texts available for the first time in Western modernity. Carl Jung's engagement with Gnosticism as a parallel to his psychological theory of individuation gave Gnostic ideas a significant twentieth-century reception outside strictly historical scholarship. Hans Jonas's philosophical interpretation of Gnosticism as an "existentialist" response to the anxiety of alienation in a vast, indifferent cosmos proved enormously influential in the mid-twentieth century.

Contemporary scholars of Western esotericism have been cautious about anachronistic projections of modern interests onto ancient Gnostic materials. The Renaissance had no direct access to Gnostic texts in the modern sense; what it received was Hermetism, various Neoplatonic materials, and filtered representations of ancient "heresies" through patristic sources. Using "Gnosticism" as a category for Renaissance esotericism requires careful qualification about which specific features are actually present in Renaissance texts rather than assumed from the modern Gnostic category.
""",
    },
    {
        "slug": "chain-of-being",
        "title": "The Chain of Being",
        "category": "Metaphysical Foundations",
        "summary": "The ancient and Renaissance metaphysical principle that all of reality constitutes a continuous hierarchy from God through angels, humanity, animals, plants, and minerals—without gaps—providing the ontological scaffolding for theories of magical correspondence, astrological influence, and the human being's special mediating position.",
        "related_figures": ["Marsilio Ficino", "Pico della Mirandola", "Plotinus", "Pseudo-Dionysius the Areopagite"],
        "related_concepts": ["neoplatonism", "emanation", "macrocosm-and-microcosm", "angelic-hierarchy", "cosmic-sympathy"],
        "body": """## The Principle

The "great chain of being" (the phrase was popularized by Arthur Lovejoy's influential intellectual history *The Great Chain of Being*, 1936) designates the metaphysical principle that reality constitutes a single continuous hierarchy extending from the divine source down through all levels of existence to the most elementary material beings—without gaps, without redundancy, with each possible level of being actually occupied. Lovejoy identified three constitutive principles: *plenitude* (every possible form of being exists), *continuity* (no gaps in the hierarchy), and *gradation* (beings are arranged in an ordered succession of degrees of perfection).

The principle had ancient roots in Plato's *Timaeus* (the Demiurge creates all possible forms), in Aristotle's biological taxonomy (organisms arranged in a scale of increasing complexity), and most elaborately in Neoplatonism (the hierarchy of emanated levels from the One through Intellect, Soul, and Nature to Matter). Medieval Christian cosmology, particularly as filtered through Pseudo-Dionysius and Aquinas, transformed this into the hierarchical cosmos familiar to Renaissance readers: God at the top; then the nine orders of angels in three triads; then the incorruptible celestial spheres and their intelligences; then the four elements and the corruptible sublunary realm; within the sublunary, humanity at the top, followed by animals, plants, and minerals.

## The Human Position

The chain of being had particular implications for understanding the human position in the cosmos. Humanity occupied a unique "middle" position: above the animals (through rational soul) but below the angels (through embodiment); participating in both the spiritual and material realms; capable of ascent toward the divine or descent toward the animal. Pico della Mirandola's *Oration on the Dignity of Man* (1486) made this special position the centerpiece of a humanist anthropology: humanity alone had no fixed place in the hierarchy but could freely choose to ascend or descend, becoming godlike through philosophy or bestial through vice.

This middle position gave humanity a special role in Renaissance cosmological speculation. As the junction-point between spirit and matter, the human soul was the knot of the cosmos (*nodus mundi*)—the being in whom all levels of reality were united and through whom communication between levels was possible. This meant that the human magician, properly trained, was uniquely positioned to mediate between cosmic levels: to draw astral influences downward through knowledge of correspondences, to direct natural forces through informed manipulation of material sympathies, and to ascend toward divine union through philosophical and theurgic practice.

## Magic and the Hierarchy

The chain of being was not merely an abstract metaphysical principle but a practical framework for magical theory. The magical practitioner's task was to understand the hierarchical structure of reality and to use that understanding to direct influences across levels. Astral magic worked downward through the hierarchy: planetary influences flowed from the celestial to the terrestrial through the medium of *spiritus*, and knowledge of the chain of correspondences enabled the practitioner to channel these influences beneficially. Theurgic magic worked upward: by ascending through the hierarchy—from material sympathies to celestial contemplation to angelic mediation—the practitioner could access divine power and return to the divine source.

The hierarchy also structured the theory of occult properties. Every natural thing had its "home" level in the hierarchy and derived its specific properties from its participation in the beings above it. Gold participated most fully in Solar virtue; lead was most "Saturnine"; plants, stones, and animals each corresponded to specific levels and powers within the celestial hierarchy. The practitioner who understood where each thing stood in the chain could understand and manipulate its specific virtues.

## Challenges to the Chain

The chain of being came under pressure from several directions in the seventeenth century. The Copernican revolution relocated the earth from the center of the cosmos, disrupting the hierarchical spatial arrangement within which the chain was traditionally figured (with the divine above and matter below). The discovery of new species in the Americas—animals and plants without counterparts in European experience—challenged the principle of plenitude as previously understood. The mechanical philosophy, by treating all material things as composed of the same undifferentiated particles, undermined the hierarchical gradation of ontological levels that gave the chain its metaphysical force.

These challenges did not immediately destroy chain-of-being thinking; the principle remained influential in natural history (the *scala naturae* or scale of nature in biological taxonomy), in philosophy (Leibniz's principle of continuity), and in theology (the argument from design, which inferred God's existence from the ordered perfection of natural creation) well into the eighteenth century. But its role as the organizing framework of magical theory effectively ended with the decline of Neoplatonic cosmology.

## Lovejoy and His Critics

Arthur Lovejoy's *The Great Chain of Being* (1936), which traced the principle from Plato to the early nineteenth century, was enormously influential in establishing the concept as a central category of intellectual history. Subsequent critics have argued that Lovejoy's analysis was too focused on the logical structure of the principle at the expense of its historical contexts of use, that it imposed more unity on a diverse tradition than the evidence warranted, and that it undervalued the transformations the principle underwent in different periods and frameworks. These criticisms are valid but should not obscure the genuine importance of hierarchical metaphysics in organizing Renaissance cosmological, magical, and theological thinking.
""",
    },
    {
        "slug": "printing-and-the-occult",
        "title": "Printing and the Occult Sciences",
        "category": "Social and Institutional Contexts",
        "summary": "The complex relationship between the invention of printing (c. 1450) and the circulation of magical and occult knowledge: print both widened access to learned magical texts and created new problems of control, authentication, and audience, transforming the social conditions under which Renaissance magic was produced and consumed.",
        "related_figures": ["Cornelius Agrippa", "Marsilio Ficino", "Johannes Trithemius", "Giovanni Battista della Porta"],
        "related_concepts": ["grimoires", "natural-magic", "patronage-and-magic", "republic-of-letters", "censorship-and-the-index"],
        "body": """## Print and the Transformation of Magical Knowledge

The invention of the printing press by Johannes Gutenberg around 1450 transformed the conditions of production and circulation of all forms of learned knowledge, including magic and the occult sciences. Before printing, occult texts circulated in manuscript: produced laboriously by hand, expensive, limited in circulation, typically confined to educated clerical and court environments. After printing, texts could be produced in hundreds or thousands of copies, distributed across Europe, and read by a vastly larger and more socially diverse audience.

This transformation was not uniformly positive for the learned magical tradition. Print widened access but also reduced control: a text that circulated in fifty manuscripts could be tracked, recalled, and suppressed relatively easily; a text printed in five hundred copies was effectively beyond recall. Print also transformed the economics of magical knowledge: what had been a rare and expensive manuscript became a cheap commodity available to readers of modest means.

## The Ambivalence of the Magical Tradition toward Print

The magical tradition's relationship to print was ambivalent from the outset. Trithemius, one of the most important early commentators on the new medium, was deeply suspicious of it: his *De laude scriptorum* (1492) argued that manuscripts were superior to printed books for preserving sacred and learned knowledge, partly because they required the labor and care of trained scribes, and partly because their restricted circulation kept sensitive knowledge from reaching inappropriate readers. Trithemius himself, however, used print for his major published works, and the paradox of his *Steganographia* (a magical-cryptographic text) circulating in manuscript for over a century while his other works were printed illustrates the complex calculation practitioners made about what to print and what to withhold.

Cornelius Agrippa's *Three Books of Occult Philosophy* provides another case study. Written in a version around 1510, the work circulated in manuscript for over twenty years before its publication in 1531. The decision to publish was shaped by multiple considerations: the need to establish priority, the desire for reputation, the availability of a suitable publisher (Agrippa eventually found a printer in Cologne), and the calculation that the work's philosophical apparatus would protect it against condemnation. The publication was followed almost immediately by the *De incertitudine* (1530) and by the condemnation of several passages by Louvain theologians—illustrating the risks of print visibility.

## Print and the Democratization of Magical Knowledge

One of the most significant effects of printing on magical knowledge was the widening of access to learned occult texts beyond the clerical and aristocratic elite. Agrippa's *Occult Philosophy*, Porta's *Magia Naturalis*, and similar works reached a readership that included merchants, apothecaries, surgeons, and other educated but non-elite readers who would previously have had no access to such material. This wider circulation contributed to the dissemination of learned magical concepts into popular culture—a process whose dynamics have been examined by historians including Eamon (*Science and the Secrets of Nature*, 1994) and Keith Thomas.

At the same time, print created new forms of vulgarization and distortion. Cheap printed almanacs, herbals, and "books of secrets" brought truncated versions of learned magical theory to mass audiences, often stripped of the philosophical context that gave them their coherence in learned usage. The distinction that educated practitioners drew between their philosophically grounded natural magic and vulgar popular magic became harder to maintain when both circulated in the same medium—print—and were sometimes sold by the same booksellers.

## Censorship and the Index

The Catholic Church's response to print's challenge to doctrinal control included the development of the *Index Librorum Prohibitorum* (Index of Prohibited Books), first published under Paul IV in 1559. The Index regulated the circulation of magical and occult texts, though inconsistently: some works were prohibited outright (Agrippa's *Occult Philosophy* appeared on early versions of the Index), while others were permitted in expurgated editions. Protestant authorities developed their own censorship mechanisms, though they generally focused on religious rather than magical content.

The practical effect of censorship on the circulation of magical texts was limited. Prohibited books circulated through informal networks (learned friends, traveling merchants, sympathetic printers in less controlled jurisdictions), and the Index itself sometimes functioned as an advertisement—contemporaries noted that prohibiting a book could increase demand for it. Nevertheless, the existence of censorship shaped what was printed and how it was framed: magical writers became increasingly careful about the philosophical framing of their work, seeking to distinguish it clearly from what the censors targeted.

## Digital Humanities and the Print Record

Recent digital humanities projects—particularly the comprehensive cataloguing of early modern printed books in databases like the *English Short Title Catalogue* and *Universal Short Title Catalogue*—have made it possible to study the print record of magical texts quantitatively. Research on print runs, publisher networks, ownership marks (ex libris, marginal annotations), and geographic distribution of surviving copies has begun to illuminate the actual patterns of circulation of magical knowledge in ways that qualitative analysis of individual texts could not.

This quantitative dimension reveals, for example, that some works associated with the learned magical tradition (Agrippa, Porta) went through dozens of editions across multiple languages and were clearly commercial successes, while other equally sophisticated works had very limited print runs and confined circulation. Understanding this differential demands attention to the market dynamics of early modern book production alongside the intellectual content of the texts.
""",
    },
    {
        "slug": "disenchantment",
        "title": "Disenchantment",
        "category": "Historiographic Concepts",
        "summary": "Max Weber's concept of the progressive elimination of magical thinking from modern Western culture through rationalization and the rise of scientific naturalism; a foundational narrative in the historiography of Renaissance magic that subsequent scholars have extensively complicated and challenged.",
        "related_figures": ["Keith Thomas", "Wouter Hanegraaff", "Frances Yates"],
        "related_concepts": ["western-esotericism-as-category", "the-yates-thesis", "natural-magic", "mechanical-philosophy", "rejected-knowledge"],
        "body": """## Weber's Concept

Max Weber's concept of *Entzauberung* ("disenchantment of the world," sometimes translated as "demystification") designates the progressive rationalization of Western culture through which magical, religious, and animistic understandings of natural reality were displaced by scientific naturalism—by the view that the world operates through impersonal causal laws accessible to rational investigation, without the intervention of supernatural beings, divine purposes, or magical forces. Weber introduced the concept in his lecture "Science as a Vocation" (1917/19) and elaborated it across his sociological writings on the relationship between religion, economics, and modernity.

For Weber, disenchantment was not simply the triumph of knowledge over ignorance but a complex cultural process with both gains and losses. The gains included the rational mastery of nature through science and technology, bureaucratic efficiency, and the demystification of inherited authorities. The losses included the diminishment of meaning: a disenchanted world was one from which transcendent purpose, cosmic significance, and magical efficacy had been expelled, leaving a "rationalized" cosmos that was technically masterable but existentially empty.

## Keith Thomas and English Disenchantment

Keith Thomas's *Religion and the Decline of Magic* (1971) applied something like a Weberian framework to the specific history of magic in early modern England. Thomas argued that the decline of magical practices—astrology, cunning craft, divination, healing magic—was driven by the combined effects of Protestantism (which stripped the Church of its quasi-magical sacramental functions and thereby forced individuals to rely on alternative means of dealing with misfortune), the rise of scientific naturalism (which provided alternative causal explanations for events previously attributed to supernatural agency), and the development of institutional mechanisms (insurance, medicine, government) that reduced the social need for magical solutions to practical problems.

Thomas's account has been enormously influential but also extensively criticized. Critics have argued that his functionalist explanation reduces magic to a response to unmet social needs, neglecting its intrinsic cultural meaning; that his narrative of "decline" imposes a teleological arc that distorts the actual historical pattern; that his evidence is primarily English and may not generalize to other European contexts; and that he underestimates the persistence of magical thinking in post-Reformation culture.

## Disenchantment and Renaissance Magic

For the historiography of Renaissance magic specifically, the disenchantment narrative creates characteristic distortions. If one begins with the assumption that disenchantment is the direction of history, then Renaissance magic appears primarily as a survival of pre-modern thinking destined for displacement rather than as a coherent intellectual tradition engaging seriously with the problems of its time. This framing makes it difficult to explain why intelligent, educated people in the sixteenth and seventeenth centuries took magic seriously—the question becomes "why hadn't disenchantment happened yet?" rather than "what made this tradition compelling on its own terms?"

Wouter Hanegraaff's work has been particularly important in challenging disenchantment narratives as applied to Western esotericism. Hanegraaff argues (*Esotericism and the Academy*, 2012) that "disenchantment" is not a neutral description of historical change but a normative narrative that maps neatly onto the self-understanding of Enlightenment rationalism—including the specific process by which Enlightenment institutions (universities, scientific academies, Protestant churches) excluded "occult" traditions as "rejected knowledge." To adopt the disenchantment narrative is implicitly to endorse the perspective of those who did the excluding.

## Re-enchantment and Its Critics

The sociological concept of "re-enchantment" has been used to describe various twentieth and twenty-first century phenomena—New Age spirituality, neo-paganism, the persistence of astrology, the revival of interest in Western esotericism—understood as cultural responses to the "loss" associated with disenchantment. This framing assumes that disenchantment actually occurred, that its losses are genuinely felt, and that re-enchantment movements constitute authentic or pseudo-authentic responses to them.

Historians of magic have generally been skeptical of this narrative, both because it assumes a cleaner disenchantment than actually occurred (magical practices never disappeared from Western culture but changed their forms and contexts) and because it treats "re-enchantment" as a cultural return when what is actually happening is the construction of new traditions that draw selectively on earlier materials in new configurations.

## Scholarly Alternatives

Alternatives to the disenchantment narrative have emphasized different dimensions of the historical change. Jason Josephson-Storm's *The Myth of Disenchantment* (2017) argued that the major theorists of disenchantment (Weber, Freud, Durkheim) were themselves deeply engaged with magic and the occult, and that "disenchantment" was always more programmatic aspiration than empirical description. Alexandra Walsham's work on post-Reformation England showed the persistence and transformation of sacred and magical practices well into the supposedly "disenchanted" early modern period.

These revisions suggest that the historiographically productive question is not "when did disenchantment occur?" but rather "what specific changes in the cultural status, institutional location, and social function of magical practices occurred in specific contexts, and why?" This more granular question allows for the complexity of actual historical change without imposing the teleological narrative of Weber's disenchantment thesis.
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
    print(f"\nBatch 6 done: {inserted} inserted, {skipped} skipped.")


if __name__ == "__main__":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
    main()
