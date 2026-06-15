"""Seed concepts table — Batch 7: Fascination, Scrying, Necromancy, Sci Rev and Magic, Love Magic."""

import sqlite3
import json
import sys
import io
from datetime import datetime

DB_PATH = "db/renmagic.db"

CONCEPTS = [
    {
        "slug": "fascination-and-evil-eye",
        "title": "Fascination and the Evil Eye",
        "category": "Magic Theory and Practice",
        "summary": "The belief that certain persons could cause harm through their gaze or envious attention, explained in Renaissance magical theory through the spiritus theory of visual projection; one of the most widely attested forms of magical belief across European and Mediterranean cultures, debated by philosophers from Plutarch to Ficino and Agrippa.",
        "related_figures": ["Marsilio Ficino", "Cornelius Agrippa", "Giovanni Battista della Porta"],
        "related_concepts": ["spiritus-and-pneuma", "natural-magic", "cosmic-sympathy", "imagination"],
        "body": """## The Phenomenon

Fascination (*fascinatio* in Latin; *baskania* in Greek; *mal d'occhio*, *ayin ha-ra*, *mauvais oeil* in vernacular traditions) is the capacity attributed to certain persons—typically those with strong envy, malevolent intent, or specific physical characteristics—to harm others, particularly children and livestock, through direct gaze or mere proximity. The evil eye was one of the most geographically widespread and culturally persistent forms of magical belief in Mediterranean and European history, attested in ancient Mesopotamia, Egypt, Greece, Rome, the Islamic world, and throughout Christian Europe, persisting in popular practice well beyond the early modern period.

In the Renaissance, fascination was not merely a folk belief but a topic of serious philosophical and medical debate. The question was not whether fascination occurred—virtually all educated people accepted that it did—but how it worked. Was it a purely natural process (operating through the hidden properties of visual *spiritus*)? Did it require demonic assistance? Could it be involuntary, occurring without the fascinator's conscious intent? What was the relationship between the evil eye and the more deliberate practices of image magic and love magic?

## The Spiritus Theory

The dominant Renaissance philosophical account of fascination drew on the *spiritus* theory of vision. Ancient and medieval optics debated whether vision occurred through an "intromissive" process (rays entering the eye from the object) or an "extromissive" process (rays issuing from the eye toward the object). Fascination made most sense on an extromissive account: the gaze of the envious person projected contaminated *spiritus* outward through the eye, entering the body of the victim and disturbing their own *spiritus*.

Marsilio Ficino offered the most philosophically elaborate account of fascination in his *De vita* (1489) and in his commentary on Plato's *Symposium* (*De amore*, 1469). Following the extromissive optics of Neoplatonic tradition, Ficino argued that the eye continuously emitted *spiritus* charged with the qualities of the soul it expressed—warm and vivifying in the healthy, compassionate person; cold, dry, and venomous in the envious or melancholic. When an envious person directed their gaze at a child or beautiful young person, the venomous *spiritus* entered the victim's body and corrupted their own *spiritus*, producing illness or worse.

Ficino's account made fascination simultaneously a medical phenomenon (a disruption of *spiritus*), a psychological phenomenon (an expression of character through vision), and a magical phenomenon (genuine harm caused at a distance through hidden natural properties). This integration of medical, psychological, and magical dimensions exemplifies how Renaissance natural magic theory united domains that modern thought tends to separate.

## Cornelius Agrippa on Fascination

Agrippa's treatment of fascination in *Three Books of Occult Philosophy* (Book I, chapter 50) is more systematically philosophical than Ficino's. Agrippa draws on Plutarch's *Symposiacs* (VII.5, *On the Evil Eye*) and on Neoplatonic accounts of visual *spiritus* to explain how strongly directed imagination and envy can project harmful influences through the eyes. He notes that certain animals (the basilisk, the catoblepas) were famous for killing with their gaze—evidence that the capacity was a genuine natural property, not mere superstition.

Agrippa also discusses the involuntary dimension of fascination: certain persons with diseased or abnormally configured eyes could fascinate without intention, their visual *spiritus* being naturally harmful through constitution rather than through deliberate malevolence. This involuntary version was particularly difficult for the theological account of fascination-as-demonic-pact, since it removed the element of conscious choice that made the pact framework applicable.

## Apotropaic Practices

The widespread belief in fascination generated a corresponding repertoire of apotropaic (protective) practices—ways of deflecting, absorbing, or neutralizing the evil eye's influence. Amulets, particularly phallic amulets (*fascina*, cognate with *fascinatio*), were worn by children in ancient Rome to deflect the evil eye; similar apotropaic objects appear across Mediterranean cultures. Verbal formulae, spitting, specific gestures (the *mano cornuta* or *mano fica*), and the wearing of red thread or specific stones (coral was commonly recommended) were employed as defenses.

Learned magical theory provided more elaborate defenses: understanding the mechanism of fascination enabled the practitioner to counteract it through sympathetic means. If fascination worked through *spiritus*, then strengthening the victim's own *spiritus* through Solar and Jovial influences, maintaining physical health and emotional equanimity, and avoiding exposure to fascinating gaze in vulnerable states (illness, infancy, strong emotion) all provided natural protection.

## Fascination and Gender

The evil eye was often but not exclusively gendered female. Old women past menopause were frequently identified as particularly dangerous fascinators in European popular belief, partly because their retained menstrual fluid (which could not be expelled) was thought to produce venomous qualities that their gaze expressed. This gendering of fascination intersected with broader early modern anxieties about older women's bodies and their alleged capacity for harm—anxieties that also fed into witchcraft accusations.

But the evil eye was also attributed to men of strong passion (jealousy, lust, anger) and to certain professions (teachers, praise-givers, executioners). The Talmudic tradition of *ayin ha-ra* focused on the dangerous power of admiration and public attention, explaining why lavish praise could harm its object: the concentrated attention it represented projected harmful *spiritus* onto the one praised. This attentional rather than purely envy-based account of the evil eye was integrated into some Renaissance philosophical treatments.

## Scholarly Significance

Fascination is important for the historiography of Renaissance magic because it shows how the spiritus theory could generate specific causal accounts of apparently magical phenomena, grounding them in natural philosophy without requiring recourse to demons. It also illustrates the problem of the natural/demonic boundary: physicians, natural philosophers, and theologians could all agree that fascination occurred while disagreeing sharply about whether it required demonic involvement.

The evil eye also shows the persistence and cultural breadth of magical belief: it was shared across social classes, educational levels, and religious communities (Christian, Jewish, and Islamic traditions all included robust evil-eye beliefs), suggesting that it addressed genuine human anxieties about envy, vulnerability, and the power of malevolent attention that could not be adequately handled by any of the official frameworks of religion, medicine, or law.
""",
    },
    {
        "slug": "scrying-and-crystal-gazing",
        "title": "Scrying and Crystal Gazing",
        "category": "Magic Theory and Practice",
        "summary": "The practice of inducing visionary states through gazing into reflective surfaces—crystals, mirrors, water, polished metals—in order to obtain information from spiritual beings or access otherwise hidden knowledge; one of the oldest and most persistent forms of divination, elevated by John Dee into a systematic angelic communication system.",
        "related_figures": ["John Dee", "Edward Kelley", "Cornelius Agrippa"],
        "related_concepts": ["angelic-hierarchy", "grimoires", "natural-magic", "art-of-memory", "demonology"],
        "body": """## The Practice

Scrying (from Middle English *descry*, "to descry, perceive") denotes the use of a reflective, transparent, or dark surface as a focus for visionary experience—typically the perception of images, lights, figures, or written messages that provide information about hidden or remote events, the future, or the spiritual realm. The surfaces used historically include crystal balls or beryl stones (*speculum*, *crystallum*), mirrors, pools of water, polished metal, ink, oil, blood, and dark glass. The practitioner either gazes into the surface alone or uses a scryer (a person with particular sensitivity) as an intermediary whose visions are reported and interpreted.

Scrying was one of the oldest and most persistent forms of divination in Mediterranean and European culture, attested in ancient Mesopotamia (the use of water, oil, and bowls for divination), in Greek and Roman practice (lecanomancy, hydromancy), and throughout medieval and early modern Europe. The *Key of Solomon* and other grimoires included instructions for preparing and consecrating scrying devices, and the practice was widespread enough to generate specific legal and theological discussion of its legitimacy.

## Natural and Demonic Explanations

The philosophical explanation of scrying was contested along predictable lines. Natural accounts argued that the reflective surface served as a focus for the imagination, enabling the concentration of *spiritus animalis* in ways that produced genuine visionary experiences without supernatural assistance. On this account, scrying was essentially a technique for activating the imagination's natural capacity to access information through the World Soul—analogous to prophetic dreams, which were widely accepted as genuine natural phenomena.

Theological accounts were more suspicious: the information apparently received through scrying could only come from spirits, and unspecified spirit communication was demonic by definition. The *Malleus Maleficarum* (1486) categorized scrying explicitly as demonic practice; inquisitorial manuals treated crystal gazing as evidence of spirit invocation. The specific content of scryed visions—who appeared, what they said, what form they took—was key evidence in evaluating whether demonic involvement was present.

## John Dee and the Angelic Conversations

The most extensively documented Renaissance scrying practice is John Dee's series of angelic conversations, conducted with the scryer Edward Kelley (and briefly others) between 1582 and 1589. Dee himself could not scry effectively; Kelley gazed into a polished obsidian mirror (a showstone, or "shew-stone") and reported the figures, speech, and writings that appeared to him. Dee recorded everything meticulously in his "spiritual diaries," which survive in substantial part and have been published and studied by scholars including Deborah Harkness, Nicholas Clulee, and György Szőnyi.

Dee understood the conversations not as divination but as angelic revelation: the beings communicating through Kelley were God's own angels, providing guidance for Dee's prophetic and reforming mission. The elaborate Enochian system—the angelic language, the forty-nine Calls or Keys, the cosmological system of Aethyrs and governors—was received incrementally through the scrying sessions, Kelley reporting in real-time while Dee recorded and asked clarifying questions.

The practice raises complex questions about the nature of the experience, the reliability of Kelley as intermediary, and the relationship between Dee's theological expectations and the content of what was "received." Scholars have debated whether Kelley's reports were genuine visionary experience, deliberate fraud, unconscious dramatization of material from his own reading, or some complex combination. The question is complicated by Dee's own unshakable conviction in the authenticity of the communications and by Kelley's later recantation of several key elements.

## Technical Preparations

Both learned magical texts and practical manuals provided detailed instructions for preparing scrying devices. Crystal balls or beryl spheres had to be consecrated through specific ritual procedures: blessed in the name of God and the angels, exposed to specific planetary influences, and often kept in a specially prepared setting (a frame of virgin wax, a holder of silver engraved with angelic names). The scryer had to be in a state of ritual purity, having fasted, prayed, and avoided sexual activity; the session took place in a purified space at an astrologically appropriate time.

Agrippa's *Three Books of Occult Philosophy* discusses the natural basis of divinatory vision in crystalline and reflective surfaces, arguing that the polished surface focuses the visual *spiritus* in a way that enables the imagination to perceive subtle spiritual realities normally inaccessible to ordinary vision. He cites the authority of Ptolemy for the principle that certain surfaces can reveal hidden things, and grounds the practice in the Neoplatonic framework of cosmic sympathy and spiritual perception.

## Scholarly Significance

Scrying is significant for the historiography of Renaissance magic as one of the clearest cases where the natural/demonic boundary was practically inoperative: the practice was simultaneously defended as natural and condemned as demonic, with neither side able to demonstrate conclusively which it was. The Dee diaries in particular have become a major resource for understanding how educated Renaissance practitioners understood spirit communication and how they negotiated the boundary between revelation and imagination, between genuine angelic contact and self-deception or fraud.
""",
    },
    {
        "slug": "necromancy",
        "title": "Necromancy",
        "category": "Magic Theory and Practice",
        "summary": "The art of communicating with or raising the dead to obtain knowledge or power—one of the most condemned forms of magic in Christian tradition, technically distinguished from demonic magic in learned discourse but associated in practice with the broader category of goetic magic and demonic invocation.",
        "related_figures": ["Cornelius Agrippa", "John Dee", "Heinrich Kramer"],
        "related_concepts": ["grimoires", "demonology", "demonic-magic", "solomonic-tradition"],
        "body": """## The Practice and Its Condemnation

Necromancy (Greek *nekros*, "dead," + *manteia*, "divination") denotes communication with the dead for purposes of divination or obtaining magical power. In its original Greek sense, it referred specifically to consulting the shades of the dead through ritual—the practice famously described in Homer's *Odyssey* (book XI) and in Virgil's *Aeneid* (book VI). In medieval and early modern Latin, *nigromantia* ("black divination," a folk etymology replacing *nekros* with *niger*, black) had become the standard term for demonic or black magic more generally, indicating how closely necromancy and demonic magic were associated in learned discourse.

Christian theology condemned communication with the dead as fundamentally illegitimate: the dead were either with God (saints), in purgatory, or in hell, and their spirits were not properly available for communication with the living. Apparently successful necromantic communication was therefore either demonic deception (demons impersonating the dead) or illusion produced by the devil to mislead the practitioner. The specific condemnation of Saul's consultation of the Witch of Endor (1 Samuel 28) was a standard proof-text.

## Necromancy in the Learned Tradition

Despite its condemnation, necromantic practice appears throughout medieval and early modern magical literature—both in treatises condemning it and in practical handbooks purporting to teach it. Richard Kieckhefer's study of a fifteenth-century necromantic handbook (*Forbidden Rites*, 1997) provides detailed analysis of the procedures described: conjurations invoking demons (or the spirits of the dead) by their names, binding them to appear and provide information, and dismissing them safely. The technical procedures draw on the same resources as other forms of ceremonial magic (divine names, magical circles, ritual purification) while targeting specifically the spirits of the deceased.

The theoretical ambiguity in necromancy was significant: were the "spirits of the dead" actually the souls of deceased persons, or were they demons who impersonated the dead? Most theologically orthodox accounts insisted on the demonic interpretation, since allowing genuine soul communication would complicate doctrines about the afterlife. But the practical manuals and their users often seemed to operate on the assumption that something genuinely connected to the dead could be contacted, regardless of the theological complexities.

## Necromancy and Medical Context

An interesting dimension of Renaissance necromantic practice was its occasional medical context. Belief that the recently dead retained vital forces (*spiritus*) that could be extracted and used therapeutically appears in alchemical and Paracelsian medicine: human blood, fat, skull (*usnea*), and other body parts of executed criminals (whose death was violent and sudden, trapping vital energies in the body) were used in folk medicine and occasionally in learned medical recipes.

This medical use of corpse-derived materials was not strictly necromantic—it did not involve communication with the dead—but it operated on related assumptions about the retention of vital *spiritus* in recently dead bodies. The boundaries between medical use of corpse materials, necromantic contact with spirits of the dead, and alchemical extraction of subtle virtues from decomposing matter were not always clearly maintained in practice.

## Scholarly Treatment

The historiography of necromancy has been shaped primarily by studies of medieval learned magic (Kieckhefer, Klaassen) that situate it within the broader category of ceremonial or ritual magic. The distinction between "necromancy" (communication with the dead) and "goetia" (demonic invocation generally) was not always maintained clearly in practice: the Lemegeton's *Goetia* was sometimes called the *Goetia* or "goetic magic" in distinction from the more respectable ceremonial magic of the *Ars Notoria*, but the boundary was porous.

For the Renaissance specifically, necromancy is important as the limiting case of the natural/demonic spectrum: it was the form of magic that most unambiguously involved demonic assistance (since whatever appeared in necromantic operations was, by theological definition, demonic), and it therefore served as a foil against which more defensible forms of magic were distinguished. Agrippa discussed it seriously but condemned it; Ficino avoided it entirely in his public works; Dee insisted his angelic conversations were categorically different from necromancy.
""",
    },
    {
        "slug": "magic-and-the-scientific-revolution",
        "title": "Magic and the Scientific Revolution",
        "category": "Historiographic Concepts",
        "summary": "The complex and contested relationship between Renaissance magic, natural philosophy, and the emergence of early modern science—a relationship that resists simple narratives of 'superstition overcome by reason,' as historians have shown that magical traditions contributed methods, problems, and attitudes that shaped the new natural philosophy.",
        "related_figures": ["Francis Bacon", "Newton", "Kepler", "Giordano Bruno", "Frances Yates"],
        "related_concepts": ["the-yates-thesis", "natural-magic", "alchemy", "disenchantment", "mechanical-philosophy"],
        "body": """## The Standard Narrative and Its Problems

The standard narrative of the Scientific Revolution presents it as a triumph of reason, observation, and mathematical method over the superstition, authority-worship, and mysticism of the medieval and Renaissance periods. On this account, magic was simply what science replaced: as Copernicus, Galileo, Newton, and their colleagues established the laws of nature through experiment and mathematics, the credulous beliefs in astrology, alchemy, and natural magic were simply pushed aside by superior knowledge.

This narrative was largely established by nineteenth-century historians of science and was given its most influential form in the early-to-mid twentieth century by Alexandre Koyré and E.J. Dijksterhuis. Its problems have been extensively documented by subsequent scholarship: it is teleological (reading history backward from the eventual outcome), it underestimates the genuine intellectual content of the traditions it dismisses, and it misrepresents the actual historical process of transition.

## Yates's Reversal

Frances Yates's thesis in *Giordano Bruno and the Hermetic Tradition* (1964) provided the most dramatic reversal of the standard narrative: not only was magic not simply the opponent of science, but the Hermetic-magical worldview was a precondition of the Scientific Revolution. By placing the human being at the center of a cosmos that could be actively manipulated through knowledge of its hidden forces, Hermeticism enabled the shift from the medieval contemplative attitude toward nature to the active, operative, world-transforming attitude of the new natural philosopher.

Yates's specific thesis has been criticized and substantially modified (see the entry on the Yates Thesis), but it permanently opened the question of the relationship between magic and science, making it impossible to write the history of the Scientific Revolution without engaging with Renaissance natural magic, alchemy, and Hermeticism.

## Specific Connections

Historians have documented several specific ways in which magical traditions contributed to the emergence of early modern science:

**Alchemy and chemistry**: The Paracelsian and Helmontian traditions of chemical natural philosophy developed sophisticated laboratory techniques, quantitative methods (van Helmont's willow tree experiment), and theoretical concepts (gas, archaeus, acids and alkalis) that fed directly into the chemical revolution of Boyle and eventually Lavoisier. Robert Boyle himself learned chemistry partly through engagement with alchemical texts, and Newton's alchemy was continuous with his natural philosophical investigations.

**Natural magic and experimental method**: William Eamon (*Science and the Secrets of Nature*, 1994) has argued that the Renaissance tradition of investigating "secrets of nature"—hidden properties, unusual phenomena, striking effects—contributed directly to the empirical program of early experimental science. The natural magician who investigated occult properties was practicing a form of empirical inquiry whose methods (observation, manipulation, testing) anticipated the experimental program even when its theoretical framework was different.

**Astrology and mathematical astronomy**: The need for accurate astrological predictions drove improvements in astronomical observation and calculation. Tycho Brahe's rigorous observational program was partly motivated by astrological purposes; Kepler's discovery of the elliptical orbits of planets grew from calculations he performed partly for astrological almanacs. The reform of astronomy and the reform of astrology were not separable enterprises in the late sixteenth century.

**The occult and the mathematical**: Kepler's Pythagorean-Neoplatonic commitment to mathematical harmonics in the cosmos—his conviction that God had created the world according to geometrical principles—drove his search for planetary laws and his discovery of the third law (relating planetary periods to orbital distances). This commitment was simultaneously "mystical" and "scientific": it was the same aesthetic-mathematical sense that had drawn Renaissance thinkers to musical proportions and geometrical harmony.

## Continuity and Rupture

The current scholarly consensus rejects both the simple-discontinuity narrative (magic suddenly replaced by science) and the simple-continuity narrative (science straightforwardly develops out of magic). What actually happened was a complex, uneven, and contested process in which some elements of the magical tradition were incorporated into the new natural philosophy (observational empiricism, chemical analysis, mathematical cosmology), some were explicitly rejected (occult qualities, action at a distance, the animate cosmos), and some persisted in transformed forms alongside the new science.

The mechanical philosophy's explicit rejection of "occult qualities" was partly a rhetorical move—presenting mechanism as clean, rational, and anti-magical—rather than a complete description of what natural philosophers actually did. Newton's gravitational force, which acted at a distance through empty space without any contact mechanism, was vulnerable to exactly the objections mechanists raised against occult properties. Newton himself was deeply uncomfortable with the "occult" implications of gravity and sought throughout his life to explain it through a material medium—efforts continuous with his alchemical search for an active principle in matter.

## Scholarly Significance

The historiographic significance of "magic and the Scientific Revolution" as a topic is that it forces historians to confront the contingency of the scientific tradition—to see that the winners of intellectual history were not inevitable, that the alternatives they displaced had genuine intellectual content, and that the boundary between "science" and "magic" is itself a historical construction rather than a natural fact. This has important implications for how we understand both the history of science and the history of magic: neither can be understood purely on its own terms without attending to their complex, contested, mutual relationship.
""",
    },
    {
        "slug": "love-magic",
        "title": "Love Magic",
        "category": "Magic Theory and Practice",
        "summary": "The use of magical procedures to attract, bind, or repel erotic and affective attachment—one of the most extensively attested forms of popular magic practice across all social levels in early modern Europe, raising important questions about gender, agency, consent, and the relationship between elite and popular magical traditions.",
        "related_figures": ["Marsilio Ficino", "Cornelius Agrippa", "Giovanni Battista della Porta"],
        "related_concepts": ["natural-magic", "grimoires", "fascination-and-evil-eye", "cosmic-sympathy", "cunning-folk"],
        "body": """## The Practice

Love magic—the use of magical procedures to attract, maintain, or destroy erotic and affective relationships—is among the most extensively attested forms of magical practice across time, culture, and social level. Ancient Greek and Roman magical papyri provide detailed recipes for love-drawing spells, binding spells (*defixiones*), and separation spells; medieval penitentials condemned love magic along with other forms of harmful sorcery; and early modern court records, inquisitorial documents, and cunning folk accounts document its continued widespread practice.

The specific procedures attributed to love magic were diverse: material operations (herbs, potions, wax images, knotted cords, menstrual blood, hair, nail-clippings), verbal formulae (charms, invocations, prayers to saints or supernatural beings), and more elaborate ritual procedures drawing on astrological timing, planetary correspondences, and spirit invocation. The social contexts of practice ranged from the household remedies of female healers to the professional services of cunning folk to the elaborate celestial magic of learned practitioners.

## Ficino on Erotic Magic and Spiritus

Marsilio Ficino's *De amore* (1469), his commentary on Plato's *Symposium*, includes substantial discussion of the natural mechanism of erotic attraction and its connection to magical theory. For Ficino, erotic love was primarily a phenomenon of *spiritus*: the lover, gazing at the beloved, projected *spiritus* charged with his own vital qualities into the beloved's body through the eyes, simultaneously drawing the beloved's *spiritus* back through his own eyes into his heart. Love was thus literally a spiritual exchange—an exchange of *spiritus* through the medium of vision.

This account of love made erotic influence continuous with both fascination and astral magic: all three worked through the projection and reception of *spiritus*, the difference being in the emotional charge and directedness of the projection. Love magic, on this account, was not categorically different from other forms of magical operation but was a specifically erotic deployment of the same *spiritus* mechanism. Ficino's discussion drew on Plato, Neoplatonic philosophy, and medical theory to provide a philosophically sophisticated account of a phenomenon usually treated only in popular practice.

## Learned vs. Popular Love Magic

The relationship between learned and popular love magic was complex. Learned practitioners drew on the same cosmological framework as elite natural magic (planetary correspondences, elemental sympathies, astral influences) but applied it to erotic ends: Venus-natured herbs, stones, and suffumigations attracted amatory influence; Mars-natured materials repelled or aroused; Luna-natured materials governed the fluidity and receptivity of erotic sentiment. Porta's *Magia Naturalis* includes extensive sections on love magic grounded in natural philosophical principles.

Popular love magic drew on a different repertoire: specific plants and animals with local reputations for erotic power (*mandragora*, verbena, lodestones, sparrows), material operations involving bodily substances (hair, menstrual blood, sweat) that created physical connection between lovers, and verbal formulae invoking saints, demons, or anonymous powers. The practitioners of popular love magic—frequently women, including midwives, healer-women, and wise women—operated in the interstices of community life, providing services that neither the Church nor medicine could supply.

## Gender and Agency

The gendering of love magic in early modern Europe was complex and sometimes paradoxical. Women were both the most frequent providers of love magic services (as cunning women, healers, and practitioners of household magic) and among its most frequent users—particularly women seeking to attract or retain male partners, or to leave abusive situations. At the same time, women were disproportionately accused of using love magic harmfully (administering love potions that drove men mad, using binding magic to destroy marriages, deploying malefic magic against rivals).

This double positioning—women as both practitioners and victims of love magic—reflects broader early modern anxieties about female agency in erotic life. Love magic represented one of the few available resources for women seeking to influence their own romantic and marital situations in societies where they had very limited formal power. Its condemnation by the Church and by secular law targeted precisely this form of agency, though prosecution was generally less severe than for more straightforwardly harmful forms of sorcery.

## Consent and the Ethics of Love Magic

Love magic raised ethical questions that were explicitly addressed by some of its learned practitioners. If love magic worked by compelling someone's will—forcing them to feel attraction they would not otherwise feel—then it violated their freedom, which was theologically as well as ethically problematic. God alone could compel the will; any magic that purported to do so was implicitly claiming a divine prerogative.

Ficino's response was to argue that genuine love magic operated only through natural persuasion—concentrating and directing the natural *spiritus* of attraction, not compelling the will. Legitimate erotic magic, on this account, worked by making the practitioner more attractive (by concentrating Solar and Venusian *spiritus*), not by forcing the beloved's will. This distinction was not always maintained in practice, but it illustrates how learned magic theory engaged seriously with the ethical dimensions of specific practices.

## Scholarly Significance

Love magic is important for the historiography of Renaissance magic because it bridges the gap between elite learned magic and popular practice, showing that the same cosmological assumptions operated at both levels while the specific procedures, social contexts, and practitioners differed significantly. It also highlights the social dimensions of magic—particularly its relationship to gender, agency, and the regulation of erotic life—in ways that illuminate broader features of early modern culture. Keith Thomas's social-historical approach to love magic in England, Katharine Park's work on Florentine medical and magical practice, and more recent microhistorical studies have all shown how love magic was embedded in specific community relationships rather than floating free as abstract "magical belief."
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
    print(f"\nBatch 7 done: {inserted} inserted, {skipped} skipped.")


if __name__ == "__main__":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
    main()
