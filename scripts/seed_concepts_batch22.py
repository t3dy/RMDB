"""Seed batch 22: Demonology extended — Witch's Sabbath, Diabolism, Demonic Pact, Maleficium, Skepticism about Witchcraft."""

import sqlite3
import sys
import io
import json
from datetime import datetime

DB_PATH = "db/renmagic.db"

CONCEPTS = [
    {
        "slug": "witchs-sabbath",
        "title": "The Witch's Sabbath: Collective Nightmare and Prosecutorial Fantasy",
        "category": "Demonology and Witchcraft",
        "summary": "The nocturnal assembly of witches — flying to meet the Devil, feasting, dancing, sexual congress with demons, and renewing their diabolical pact — as constructed in learned demonological theory and confessional evidence from the fifteenth century onward, and analyzed by modern scholarship as a collective fantasy shaped by prosecution dynamics.",
        "related_figures": ["Heinrich Institoris", "Johannes Nider", "Pierre de Lancre"],
        "related_concepts": ["witchcraft", "malleus-maleficarum", "demonology", "magic-and-the-church", "magic-and-gender", "cunning-folk"],
        "body": """## The Witch's Sabbath: Collective Nightmare and Prosecutorial Fantasy

The witch's sabbath — the nocturnal assembly at which witches allegedly gathered to worship the Devil, feast on diabolical food, dance obscenely, engage in sexual congress with demons, and renew their pact of servitude to Satan — was the central collective image of European witchcraft prosecution from the late fifteenth through the early eighteenth centuries. Constructed through the interaction of learned demonological theory, confessional testimony elicited through torture and leading questions, and existing folklore about nocturnal assemblies and demonic visitation, the sabbath image was simultaneously a prosecutorial tool, a theological statement about the reality and organized nature of diabolism, and a cultural dream that revealed deep anxieties about social inversion, sexual transgression, and the boundaries of the Christian community.

### Origins and Development

The sabbath concept developed gradually in the late fourteenth and early fifteenth centuries through the synthesis of several distinct traditions:

**The strigae tradition**: Ancient and early medieval accounts of women who flew through the night (strigae, striae, lamiae) in animal form and attacked sleeping children were primarily folkloric and were often dismissed by earlier medieval ecclesiastical opinion as delusion. The *Canon Episcopi* (a canon of church law from the ninth or tenth century, falsely attributed to the Council of Ancyra) explicitly stated that women who claimed to ride out at night with Diana were deceived by demonic illusions rather than physically traveling — implying that witchcraft was primarily a problem of false belief rather than real activity.

**The heresy model**: The inquisitorial prosecution of heretical groups — Cathars, Waldensians, Beguines — developed a template of the secret nocturnal assembly at which orthodox religion was inverted: worshipping a cat or goat (identified with the devil), engaging in sexual promiscuity, murdering and eating children. These charges, recycled from ancient anti-Jewish and anti-Christian polemic, were adapted for use against suspected witches.

**Learned demonological synthesis**: The synthesis of nocturnal flight, diabolical assembly, and the heresy model into the coherent sabbath image occurred primarily in the mid-fifteenth century, in works like Johannes Nider's *Formicarius* (1435) and *Errores Gazariorum* (anonymous, c. 1437). The *Malleus Maleficarum* (1486) provided the fullest early systematization.

### Structure of the Sabbath

Learned demonological accounts of the sabbath described a relatively consistent structure, though details varied by region and period:

**The journey**: Witches traveled to the sabbath by flying — anointing themselves with a magical unguent (the "witch's salve," said to be made from the fat of murdered infants and psychoactive herbs), mounting a broomstick, goat, or other vehicle, and flying through the night to the assembly site.

**The assembly**: The gathering was held in a desolate location — a mountaintop, a crossroads, a wasteland — at midnight. The Devil presided in the form of a man or an animal (goat, black cat, or toad were common) seated on a throne or altar.

**Homage and renunciation**: Witches paid homage to the Devil by kissing his posterior (*osculum infame*, the "obscene kiss") and renouncing their baptism, their Christian faith, and their obligations to God.

**Feasting and dancing**: The company feasted on foul food (tasteless bread, poisoned meat, the bodies of murdered infants) and danced — typically described as dancing back-to-back in a ring, the inversion of the proper dance.

**Orgiastic sexuality**: The Devil or his demons engaged in sexual intercourse with the witches, and sexual promiscuity among the assembly was common. Demonological accounts were explicit about the physical unpleasantness of intercourse with demons (icy cold, painful) while insisting on the reality of the carnal transaction.

**Magical instruction**: The Devil or senior witches instructed the assembly in maleficia — the techniques of causing harm through magical means.

### Interpretation in Modern Scholarship

Modern scholarship on the sabbath has taken several interpretive directions:

**The skeptical tradition**: Following Reginald Scot's *Discoverie of Witchcraft* (1584), which argued that confessions of sabbath attendance were the product of delusion, melancholy, or torture, many modern scholars have emphasized that the sabbath was a prosecutorial construction rather than a social reality. The consistency of sabbath descriptions across widely separated regions and periods reflects the consistency of the questions investigators asked (shaped by demonological theory) rather than independent accounts of a common experience.

**The folk culture thesis**: Carlo Ginzburg's *Night Battles* (*I Benandanti*, 1966) and *Ecstasies* (*Storia Notturna*, 1989) proposed that beneath the demonological overlay of sabbath confessions lay genuine folk traditions of nocturnal spiritual journeys — shamanic or quasi-shamanic practices in which practitioners entered trance states and experienced (or believed they experienced) travel to a realm of spirits. The demonological framework imposed on these traditions by inquisitors transformed benign fertility-cult practices into diabolism.

**The prosecution dynamics thesis**: Many historians have emphasized how the specific dynamics of witch trials — the expectation of naming accomplices under torture, the interrogators' leading questions shaped by demonological theory, the social pressures of the community in which trials occurred — produced the sabbath confessions rather than extracting pre-existing beliefs.

**See also:** Witchcraft; Malleus Maleficarum; Demonology; Magic and the Church; Magic and Gender; Cunning Folk and Popular Magic.
""",
    },
    {
        "slug": "demonic-pact",
        "title": "The Demonic Pact: Covenant, Apostasy, and the Faust Legend",
        "category": "Demonology and Witchcraft",
        "summary": "The theological and legal concept of a compact between a human being and the Devil — exchanging the soul for knowledge, power, or pleasure — that made witchcraft a form of apostasy rather than mere sorcery, and achieved its fullest cultural expression in the Faust legend.",
        "related_figures": ["Heinrich Institoris", "Johann Faustus (legendary)", "Johannes Weyer"],
        "related_concepts": ["demonology", "witchcraft", "witchs-sabbath", "malleus-maleficarum", "ceremonial-magic", "solomonic-tradition"],
        "body": """## The Demonic Pact: Covenant, Apostasy, and the Faust Legend

The demonic pact (*pactum cum daemone*, compact with the Devil) was the theological concept that transformed witchcraft from mere harmful sorcery (*maleficium*) into a heresy — apostasy from Christianity in favor of a counter-religious allegiance to Satan. By entering a pact with the Devil, the witch was not merely using forbidden magical means to cause harm but was renouncing her baptism, her Christian faith, and her membership in the body of Christ, submitting instead to the sovereignty of Christ's cosmic adversary. This elevation of witchcraft to the status of heresy had profound implications for the severity of its prosecution: heresy was a capital offense under both civil and ecclesiastical law, while mere sorcery (*maleficium*) was not.

### Theological Origins

The concept of a demonic pact derived ultimately from Augustine's argument (in *De Doctrina Christiana* and elsewhere) that all magical operations that went beyond the natural properties of things involved implicit communication with demons. Augustine had argued that even if the practitioner was unaware of demonic agency, magic that could not be explained by natural causes presupposed an implicit compact (*quasi pactum*) with demons who agreed to produce the apparent effects.

Medieval theologians elaborated this implicit pact into an explicit one: the witch or sorcerer did not merely inadvertently invite demonic agency but consciously chose to enter into a relationship of service and obedience to the Devil in exchange for magical power. The formal elements of the pact — the explicit renunciation of Christ, the signing of a diabolical book or register in blood, the rendering of homage to the Devil — were developed in learned demonological literature from the thirteenth century onward and became fully systematized in the fifteenth-century sabbath accounts.

The theological significance of the pact was that it made witchcraft analogous to the covenant relationship that God had established with Israel and through Christ with the Church. The witch's covenant with the Devil was a diabolical parody of the divine covenant — a fundamental inversion of the proper relationship between human beings and their creator that placed the witch outside the Christian community as surely as an apostate or heretic.

### Legal Implications

The elevation of witchcraft through the pact concept to the status of apostasy had direct legal consequences. Apostasy and heresy were capital crimes under ecclesiastical law (though the penalty was technically imposed by the secular arm — the Church could not shed blood — through burning at the stake). The *Malleus Maleficarum* and subsequent demonological literature consistently emphasized the pact as the foundation of the witch's guilt: even if the witch had caused no specific harm to specific persons (*maleficium*), the pact itself was a capital crime.

This meant that the prosecution of witchcraft did not require proof of specific harmful acts — the confession of the pact itself was sufficient. And since the pact was an internal spiritual transaction rather than an observable external act, the primary evidence had to be the witch's own confession, which was typically obtained through torture.

### The Faust Legend

The legend of Johann Faustus — the scholar who sold his soul to the Devil in exchange for 24 years of knowledge, pleasure, and magical power — achieved its first major literary form in the *Historia von D. Johann Fausten* (1587, Frankfurt: publisher Johann Spies), compiled from circulating oral traditions about a reputed historical magician. The *Historia* was quickly translated into English (as *The Damnable Life and Deserved Death of Doctor John Faustus*, 1592), French, Dutch, and other languages, and provided the source for Christopher Marlowe's *Doctor Faustus* (c. 1592).

The Faust legend crystallized the most powerful cultural images of the demonic pact: the scholar's overweening intellectual ambition that led him to seek forbidden knowledge beyond what God had permitted; the Devil Mephistopheles (in Marlowe's version) as an ambiguous figure, at once servile and terrifying; the 24 years of magical adventure that ultimately yielded not happiness but increasing desperation; and the final reckoning — the Devil's claim on the soul he had purchased — that was the inevitable end of the pact.

What made the Faust legend culturally enduring was not merely its theological message (pride and the demonic pact lead to damnation) but its dramatization of the tragic dimensions of intellectual ambition. Marlowe's Faustus, asking "Is it not passing brave to be a King / And ride in triumph through Persepolis?", is not simply wicked but genuinely tragic — driven by desires for knowledge and experience that are, the play acknowledges, both understandable and ultimately self-destructive.

### The Pact and Ceremonial Magic

The demonic pact concept created an interpretive problem for learned practitioners of ceremonial magic who believed they were working through divine authority rather than demonic compact. If, as Trithemius and many theological critics argued, any apparent compliance by spiritual beings with human ritual commands was ultimately demonic in origin, then the learned ceremonial magician was in exactly the same position as the witch — he was simply unaware that his "angelic" invocations were in fact demonic operations.

This critique could not be definitively answered within the framework that both sides shared, because neither side had independent access to the identity of the beings that appeared in magical operations. The practitioner's subjective certainty that he was working with holy angels was no guarantee, since (as every theologian acknowledged) demons could appear as angels of light.

**See also:** Demonology; Witchcraft; Witch's Sabbath; Malleus Maleficarum; Ceremonial Magic; Solomonic Tradition.
""",
    },
    {
        "slug": "maleficium",
        "title": "Maleficium: Harmful Magic and Its Social Contexts",
        "category": "Demonology and Witchcraft",
        "summary": "The practice of causing illness, death, agricultural failure, sexual dysfunction, or other harm through magical means — the most socially concrete dimension of witchcraft prosecution, arising from specific interpersonal conflicts and community tensions rather than abstract theological concerns about apostasy.",
        "related_figures": ["Heinrich Institoris", "Reginald Scot", "Johannes Weyer", "Keith Thomas"],
        "related_concepts": ["witchcraft", "malleus-maleficarum", "witchs-sabbath", "demonology", "cunning-folk", "magic-and-gender"],
        "body": """## Maleficium: Harmful Magic and Its Social Contexts

*Maleficium* (Latin: harmful deed, sorcery) designated the concrete harmful magical operations attributed to witches: causing illness or death in specific persons, destroying crops and livestock, preventing butter from churning, inducing sexual impotence (*ligatura*, tying), causing women to miscarry, blighting orchards, and producing storms. Distinguished from the theological dimension of witchcraft (the pact, the sabbath, the apostasy from Christianity) by its focus on specific, concrete, attributable harm, maleficium was in many ways the most socially significant dimension of witchcraft from the perspective of the communities where accusations arose: it was the charge that made witchcraft prosecution urgent and personal, connecting abstract demonological theory to the everyday experience of misfortune.

### Social Mechanisms of Accusation

The social mechanisms through which maleficium accusations arose have been extensively analyzed by social historians of witchcraft. Alan Macfarlane's study of Essex (*Witchcraft in Tudor and Stuart England*, 1970) identified a pattern that has since been found in many European regions: the "refusal-guilt" model. A marginalized person — typically an older woman without male household support — sought assistance (food, money, labor) from a more prosperous neighbor. The neighbor refused (violating the traditional norms of communal mutual aid in an era when those norms were breaking down under early capitalist pressures). The neighbor subsequently suffered a misfortune — an illness, a dead animal, a failed crop. Overcome by guilt about the refused request and needing an explanation for the misfortune, the neighbor attributed it to the malicious resentment of the refused person: she had bewitched him in revenge.

This model elegantly explained several features of maleficium accusations:
- Why accused witches were typically socially marginal figures (those most likely to make requests that would be refused)
- Why they were often older women (the most economically vulnerable and socially isolated)
- Why accusations arose specifically after interpersonal conflicts (the guilt generated by the refusal)
- Why the supposed motive was consistently resentment (the psychological reality of the guilty refuser's imagination)

The model did not require that maleficium was real — it only required that specific people, in specific social conditions of guilt and anxiety, attributed specific misfortunes to the magical agency of specific others.

### Healing Countertransference: Cunning Folk and Maleficium

The relationship between practitioners of beneficial magic (cunning folk, wise-women) and accusations of maleficium was ambiguous and sometimes circular. Cunning folk were typically the first resource for those who believed themselves bewitched: they diagnosed the bewitchment, identified the likely witch, recommended counter-measures, and in some cases claimed to be able to "unwitche" the victim. This diagnostic role gave cunning folk both authority (they could identify who had cast the *maleficium*) and danger (their identification of the alleged witch, if wrong or contested, could generate further conflict and accusations against themselves).

Moreover, the same knowledge that made a cunning folk practitioner effective at healing and protection was, in principle, the knowledge that could be used for harm. The village healer who knew which herbs were protective was also the person who knew which were poisonous; the person who could lift a curse was also the person who might have cast it. The line between the beneficial practitioner and the maleficent witch was drawn by intent and community reputation rather than by any clear technical boundary.

### Detecting and Countering Maleficium

A substantial part of the practical literature on witchcraft (as opposed to the theological demonology) was devoted to detecting and countering maleficium. Standard methods for detecting bewitchment included:
- Diagnosis by symptoms: specific configurations of symptoms (unexplained wasting disease, unusual behavior in animals, repeated failures of domestic operations) were identified as indicators of maleficium rather than natural illness
- The "swimming test" (ducking): the person suspected of maleficium was thrown into water; if they floated, they were guilty (the water rejected them as baptismally defiled); if they sank, they were innocent
- Physical examination for the "witch's mark" (an insensible spot on the body, allegedly the place where the familiar spirit or the Devil sucked blood)

Counter-magical practices included: nailing horseshoes or iron objects to doors and windows (iron being apotropaic against supernatural harm), burying "witch bottles" (sealed pottery vessels containing the victim's urine, pins, and other materials, intended to reverse the maleficium onto its sender), and consulting a cunning folk practitioner who might identify and neutralize the source.

**See also:** Witchcraft; Malleus Maleficarum; Witch's Sabbath; Demonology; Cunning Folk and Popular Magic; Magic and Gender.
""",
    },
    {
        "slug": "skepticism-about-witchcraft",
        "title": "Skepticism about Witchcraft: Weyer, Scot, and the Critique of Persecution",
        "category": "Demonology and Witchcraft",
        "summary": "The sixteenth-century tradition of skeptical critique of witchcraft prosecution — associated above all with Johannes Weyer and Reginald Scot — that challenged the reality of demonic compact, the validity of witchcraft confession, and the justice of execution, and that became a touchstone for later historical and social analysis.",
        "related_figures": ["Johannes Weyer", "Reginald Scot", "Pietro Pomponazzi", "Johann Wier"],
        "related_concepts": ["witchcraft", "demonology", "malleus-maleficarum", "demonic-pact", "magic-and-the-church", "magic-and-gender"],
        "body": """## Skepticism about Witchcraft: Weyer, Scot, and the Critique of Persecution

The sixteenth century produced not only the major texts of witchcraft demonology (*Malleus Maleficarum*, 1486; *Demonolatreiae*, 1595; *Tableau de l'inconstance des mauvais anges*, 1612) but also a tradition of skeptical critique that challenged the reality of the sabbath and demonic pact, questioned the validity of confessions obtained through torture, and argued that the women prosecuted as witches were victims of mental illness and judicial cruelty rather than genuine servants of Satan. This skeptical tradition — associated above all with the physician Johannes Weyer (1515–1588) and the English gentleman Reginald Scot (c. 1538–1599) — was a minority position in its own time but became increasingly influential as the great wave of witch prosecution began to ebb in the later seventeenth century.

### Johannes Weyer: Medical Skepticism

Weyer's *De Praestigiis Daemonum* ("On the Illusions of Demons," 1563) is the foundational text of the skeptical tradition. Weyer was a physician, a disciple of Heinrich Cornelius Agrippa (whose anti-misogynist arguments he absorbed), and a convinced Protestant who combined genuine belief in the reality of demons with a skeptical assessment of their actual operations.

Weyer's central argument was that the women accused of witchcraft were primarily *melancholic* — suffering from a medical condition (melancholic frenzy) that caused them to believe they had made pacts with the Devil, attended sabbaths, and performed maleficia, when in fact they had done none of these things. The Devil, Weyer argued, exploited the condition of melancholic women to delude them into false beliefs about their own agency; the women were victims of demonic deception and mental illness rather than willful apostates deserving execution.

Weyer's medical diagnosis was not incompatible with theological belief in the Devil's reality and power: he was not arguing that the Devil was a fiction but that the Devil's primary activity was deception rather than the physical operations attributed to witches. The Devil could not actually empower witches to fly, cause storms, or kill by magical means — these claimed powers were beyond demonic capacity in Weyer's account — but he could delude melancholic women into believing they had done so.

The practical implication was that accused witches should be treated as patients rather than criminals: they needed medical care for their melancholy rather than execution for their apostasy. This was a genuinely compassionate position, however patronizing its assumption that the women's own testimony about their experiences was a symptom of illness rather than evidence.

### Reginald Scot: Broader Skepticism

Reginald Scot's *Discoverie of Witchcraft* (1584) took a more thoroughgoing skeptical position than Weyer's. Scot accepted Weyer's arguments about the medical condition of accused witches but extended the skepticism further: he questioned not merely whether witches could perform the supernatural acts attributed to them but whether the entire demonological framework — the reality of the sabbath, the efficacy of magical operations, the physical operations of demons in the world — was supported by rational evidence.

Scot was a convinced Protestant whose skepticism about witchcraft was partly motivated by his belief that Catholic ritual and the Catholic tradition of miraculous intervention in the world were forms of superstition. If Catholics were wrong to believe in the miraculous power of holy water, relics, and exorcism, then Protestants were equally wrong to believe in the magical power of witches: both were forms of irrational credulity that proper Protestant theology rejected.

The *Discoverie* collected an enormous quantity of materials illustrating the variety and absurdity of magical and witchcraft belief, including detailed accounts of conjuring tricks and illusionistic performances that mimicked "miraculous" effects. Scot's implicit message was that many apparent supernatural phenomena were explainable as fraud, illusion, or natural causes, without recourse to either divine miracle or diabolic magic.

### The Limits of Skepticism

Both Weyer and Scot were operating within the theological and legal constraints of their era, and their skepticism had significant limits. Neither denied the existence of the Devil, the reality of demonic influence on human beings, or the in-principle possibility of genuine witchcraft. Their arguments were about the prevalence, extent, and prosecutorial methods of witchcraft persecution rather than about the fundamental framework. Both were criticized, in their own time and later, for failing to provide a fully coherent alternative framework that could explain why the testimony of accused witches — who often provided circumstantially detailed accounts of sabbaths, pacts, and maleficia — should be disbelieved.

The gradual decline of witchcraft prosecution in the later seventeenth century owed something to the skeptical tradition (which had circulated and accumulated advocates over a century) but also to changes in legal theory (particularly the declining credibility of torture-based confession), changes in elite cultural attitudes (educated elites becoming less willing to credit popular reports of supernatural phenomena), and changes in the social conditions that had generated witchcraft accusations in the first place.

**See also:** Witchcraft; Demonology; Malleus Maleficarum; Demonic Pact; Witch's Sabbath; Magic and Gender.
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
    print(f"\nBatch 22 done: {inserted} inserted, {skipped} skipped.")


if __name__ == "__main__":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
    main()
