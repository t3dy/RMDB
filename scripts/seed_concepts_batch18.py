"""Seed batch 18: Historiographic concepts — Rejected Knowledge, Magic vs Religion, Social History of Magic, Psychoanalysis and Magic, Decolonizing Magic Studies."""

import sqlite3
import sys
import io
import json
from datetime import datetime

DB_PATH = "db/renmagic.db"

CONCEPTS = [
    {
        "slug": "rejected-knowledge",
        "title": "Rejected Knowledge: The Epistemology of the Occult",
        "category": "Historiography and Methodology",
        "summary": "The concept — developed by historian of religion Wouter Hanegraaff — of 'rejected knowledge' as the defining characteristic of Western esotericism: knowledge-claims that have been systematically excluded from the canon of legitimate science and religion, generating a distinct alternative intellectual tradition.",
        "related_figures": ["Wouter Hanegraaff", "Antoine Faivre"],
        "related_concepts": ["western-esotericism-as-category", "the-yates-thesis", "disenchantment", "magic-and-the-scientific-revolution", "gnosis-and-gnosticism"],
        "body": """## Rejected Knowledge: The Epistemology of the Occult

"Rejected knowledge" is a concept developed most systematically by the Dutch historian of religion Wouter J. Hanegraaff, particularly in his major work *Esotericism and the Academy: Rejected Knowledge in Western Culture* (2012), to characterize the distinctive epistemological status of the Western esoteric tradition. The concept proposes that Western esotericism is not primarily defined by its content (specific beliefs about correspondences, living nature, imagination, etc.) but by its position in the Western intellectual landscape: it consists of knowledge-claims and ways of knowing that have been systematically *excluded* from the canon of legitimate knowledge by the two dominant institutional gatekeepers of Western culture — scientific reason and normative religion (whether Jewish, Christian, or Muslim). Esotericism is, in this sense, the sum of what Western intellectual culture has decided it does not want to know.

### The Concept of Rejection

Hanegraaff's concept builds on but extends earlier work on the definition of Western esotericism, particularly Antoine Faivre's influential typology (correspondences, living nature, imagination, transmutation, concordance, transmission) which identified a set of positive characteristics shared by esoteric traditions. Hanegraaff's move is to supplement Faivre's content-based definition with a relational one: what makes something "esoteric" in the Western context is not merely that it shares these characteristics but that it has been systematically rejected by the mainstream gatekeepers of knowledge.

The mechanism of rejection has taken different forms in different historical periods:

- **In the medieval and early modern period**: Magic, Hermeticism, and related traditions were rejected as diabolical, superstitious, or theologically deviant by ecclesiastical authorities.
- **In the early modern period of the Scientific Revolution**: The same traditions were rejected as unscientific, irrational, and superseded by the new mechanical natural philosophy.
- **In the modern academic period**: Occult traditions were rejected as "pseudoscience" by scientific institutions and as "non-canonical" or "heterodox" by religious institutions.

The effect of this double rejection — by both normative religion and secular science — is that esoteric traditions occupy a space outside the mainstream of both, forced into the margins where they have developed a distinctive counter-cultural identity and often an explicit self-presentation as *alternative* ways of knowing.

### The Polemical Construction of "Magic"

One of Hanegraaff's most important arguments is that the modern concept of "magic" is itself a *polemical* construction, not a neutral description of a category of practices that actually exists in the world. "Magic" — as a category distinct from "religion" and "science" — was created by the very acts of rejection that defined the boundaries of legitimate knowledge. When Christian theologians condemned magical practice as diabolical, when Protestant reformers attacked Catholic ritual as magical superstition, when Enlightenment philosophers described traditional beliefs as "magical thinking" to be superseded by rational science — in all these cases, the category "magic" was being constructed as the negative other of legitimate knowledge.

This constructivist insight means that the history of magic cannot be written simply as the history of practices that were called magic, because the labeling itself was already a political and epistemological act. The wise-woman who healed with herbs and charms did not necessarily think of herself as practicing "magic" — she might have thought of herself as practicing medicine, or religion, or tradition. The "magic" label was applied to her practice from outside, by agents who had the institutional power to define what counted as legitimate and what was rejected.

### The Polemics of "Legitimate" Science and Religion

Hanegraaff also draws attention to the role of *polemics* in the construction of both the esoteric traditions and their normative alternatives. Mainstream science defined itself partly *against* "occult" knowledge (the Royal Society's programmatic rejection of occult qualities and hidden causes is a key moment); mainstream religion defined itself partly against "magic" (the Reformation critique of Catholic superstition, the Counter-Reformation condemnation of Protestant heterodoxy). The establishment of legitimate knowledge domains required the simultaneous construction of the rejected domains against which they were defined.

This means that the history of Western esotericism is inseparable from the history of Western science and religion — not because esotericism influenced those mainstream traditions (though it did) but because the mainstream traditions constituted themselves partly through the act of rejecting the esoteric alternatives.

### Implications for Historiography

The "rejected knowledge" framework has significant implications for how the history of magic and esotericism should be written. It suggests that:

1. Historians should not simply adopt the categories of rejection (treating magical practice as obviously superstitious or irrational from a modern perspective)
2. Historians should analyze the *acts of rejection* themselves as historical events requiring explanation
3. Historians should attend to the perspective of the practitioners themselves — how did they understand what they were doing? — rather than merely the perspective of institutional gatekeepers

This emphatically "emic" (insider's perspective) approach to historical scholarship on esotericism has been controversial: critics have argued that it risks surrendering the critical perspective necessary for historical analysis, while defenders argue that the alternative — assuming that mainstream science and religion got the epistemological questions right and that rejected knowledge was simply wrong — is itself a form of presentism.

### The Limits of the Framework

The "rejected knowledge" framework has been influential but also contested. Some critics argue that it defines esotericism too broadly (making almost any heterodox intellectual position potentially "esoteric"), or that the emphasis on rejection understates the degree to which esoteric traditions participated in and influenced mainstream culture, or that the framework is too specifically Western to apply to non-Western traditions.

Nevertheless, the concept has enriched the historiography of Renaissance magic by directing attention to the power relations embedded in categories like "magic," "superstition," and "pseudoscience," and by insisting that the history of what was excluded is as important as the history of what was included in the canon of legitimate knowledge.

**See also:** Western Esotericism as a Scholarly Category; The Yates Thesis; Disenchantment; Magic and the Scientific Revolution.
""",
    },
    {
        "slug": "magic-vs-religion",
        "title": "Magic versus Religion: A Contested Scholarly Distinction",
        "category": "Historiography and Methodology",
        "summary": "The long-debated scholarly question of whether 'magic' and 'religion' can be analytically distinguished, from Frazer's evolutionary theory through sociological and anthropological approaches to the contemporary consensus that the distinction is largely a polemical construction rather than a neutral description.",
        "related_figures": ["James George Frazer", "Bronisław Malinowski", "Keith Thomas", "Wouter Hanegraaff"],
        "related_concepts": ["western-esotericism-as-category", "rejected-knowledge", "natural-magic", "the-yates-thesis", "cunning-folk"],
        "body": """## Magic versus Religion: A Contested Scholarly Distinction

One of the most durable and contentious debates in the history of religions, anthropology, and sociology has been the question of whether "magic" and "religion" can be meaningfully distinguished — whether they are genuinely different kinds of human activity with different logics and social functions, or whether the distinction is a polemic weapon deployed by some religious traditions against others, or whether it is a specifically Western intellectual construction that does not translate across cultural contexts.

### Frazer's Evolutionary Schema

The classical anthropological framework for distinguishing magic from religion was provided by James George Frazer (1854–1941) in *The Golden Bough* (1890, expanded in subsequent editions to 12 volumes by 1915). Frazer proposed an evolutionary schema in which human cultures progressed through three stages:

1. **Magic**: The earliest stage, in which humans believed they could directly control natural forces through ritual manipulation based on the principles of sympathy (like produces like: homeopathic magic) and contagion (things once in contact remain connected: contagious magic).
2. **Religion**: When magic failed to deliver reliable results, humans recognized that natural forces were controlled by personal supernatural beings, and shifted from manipulation to propitiation — asking the gods rather than compelling nature.
3. **Science**: The final stage, in which humans recognized that nature operated according to impersonal laws discoverable through empirical investigation.

On this schema, magic and religion were different stages in a developmental sequence, with religion being more sophisticated than magic and science being more sophisticated than both. This placed the magical practices of non-Western peoples at the bottom of an evolutionary hierarchy while positioning Western scientific culture at the top.

Frazer's schema was enormously influential in early twentieth-century intellectual culture but has been thoroughly criticized from multiple directions. The evolutionist framework is now recognized as ethnocentric (assuming that Western science represents the telos of human intellectual development); the proposed distinction between magic's "compulsion" and religion's "propitiation" is difficult to maintain empirically; and the categories of "magic," "religion," and "science" have been shown to be culturally variable rather than universal.

### Durkheim and the Social Functions of Religion

Émile Durkheim's *Elementary Forms of Religious Life* (1912) offered a sociological rather than evolutionary account of the distinction. For Durkheim, religion was fundamentally a collective phenomenon — the expression of a community's consciousness of itself through the distinction between sacred and profane, expressed in collective ritual. Magic, by contrast, was primarily an individual enterprise: the magician served clients one by one rather than binding a community together.

This sociological distinction — religion as community-binding, magic as individual transaction — captured something real about the contrast between, say, Christian liturgy and the consultation of a cunning folk healer, but it struggled with cases like collective magical ritual or with the community-binding functions of certain magical practices.

### Malinowski and the Psychological Function

Bronisław Malinowski's ethnographic work in the Trobriand Islands (published in *Magic, Science and Religion*, 1925) proposed that magic functioned to manage anxiety in situations of genuine uncertainty: Trobriand fishermen used magic when fishing in dangerous deep waters but not when fishing in the safe lagoon, suggesting that magic supplemented empirical knowledge rather than replacing it. Malinowski thus challenged Frazer's evolutionary schema (magic and empirical knowledge coexist rather than sequencing) while maintaining a functional distinction between them.

### Keith Thomas and the Decline Thesis

Keith Thomas's *Religion and the Decline of Magic* (1971), while not primarily a theoretical work, applied the magic/religion distinction to English history in a way that proved enormously influential. Thomas followed a broadly Durkheimian approach, treating magic and religion as functionally distinct (magic providing certainty, religion providing meaning) and analyzing the decline of both popular magic and orthodox religion in the face of the Scientific Revolution and the new emotional self-sufficiency generated by Protestant theology.

Thomas's work has been extensively critiqued and revised by subsequent scholars but remains a fundamental reference point for the social history of magic in early modern England.

### The Constructivist Turn

The most radical challenge to the magic/religion distinction has come from scholars who argue that it is not a neutral analytical category but a *polemical construction* created within particular cultural and institutional contexts. Jonathan Z. Smith (*Imagining Religion*, 1982) argued that "there is no data for religion" — the category of religion (and by extension magic) is a scholarly construct imposed on diverse phenomena that do not naturally sort into these categories. Talal Asad's genealogical analysis (*Genealogies of Religion*, 1993) showed how the modern Western concept of "religion" as a private, inner, voluntary affair was itself a historically specific construction that emerged from the Reformation and Enlightenment, not a universal human category.

Applied to magic, this constructivist approach suggests that the distinction between "magic" and "religion" served polemical purposes within Christian, post-Christian, and colonial discourse: magic was what other people did, or what benighted pre-modern people did, or what uneducated women did. The scholars who drew the distinction were simultaneously participants in the processes that produced the distinction.

### Contemporary Approaches

Contemporary scholars of magic and religion generally reject the idea that a clean analytical distinction between the two can be maintained, while acknowledging that practitioners themselves often drew such distinctions and that those distinctions were historically important. The focus has shifted from defining magic in contrast to religion to analyzing how specific actors in specific historical contexts drew, deployed, and contested the magic/religion boundary, and with what social and political consequences.

**See also:** Western Esotericism as a Scholarly Category; Rejected Knowledge; The Yates Thesis; Cunning Folk and Popular Magic.
""",
    },
    {
        "slug": "social-history-of-magic",
        "title": "The Social History of Magic: Context, Practice, and Community",
        "category": "Historiography and Methodology",
        "summary": "The historiographical approach that situates magical practice within its social context — analyzing who practiced magic, who used it, what social needs it served, and how it functioned within specific communities — as opposed to the intellectual history approach focused on the ideas and texts of learned magicians.",
        "related_figures": ["Keith Thomas", "Alan Macfarlane", "Robin Briggs", "Richard Kieckhefer"],
        "related_concepts": ["cunning-folk", "witchcraft", "learned-vs-popular-magic", "magic-and-gender", "magic-vs-religion"],
        "body": """## The Social History of Magic: Context, Practice, and Community

The social history of magic — the approach that analyzes magical practice in terms of its social context, functions, practitioners, clients, and community dynamics — emerged as a distinct historiographical method in the late 1960s and 1970s and transformed the study of Renaissance and early modern magical culture. Where earlier intellectual history had focused primarily on the ideas and texts of learned magical philosophers (Ficino, Pico, Agrippa, Bruno), the social history approach directed attention to the social conditions that made magical practice possible and meaningful: who used magic, who provided it, what social tensions it expressed, and how it functioned within the specific communities where it operated.

### Foundations: Thomas and Macfarlane

The foundational texts of the social history of magic in English scholarship are Keith Thomas's *Religion and the Decline of Magic: Studies in Popular Beliefs in Sixteenth and Seventeenth Century England* (1971) and Alan Macfarlane's *Witchcraft in Tudor and Stuart England* (1970), which appeared almost simultaneously and established complementary social-historical approaches to the study of magical belief and practice.

Thomas's *Religion and the Decline of Magic* surveyed the entire range of popular magical practice in early modern England — astrology, prophecy, cunning folk, witchcraft, charms, divination, and the magical dimensions of orthodox religion — against the background of the changing social, intellectual, and religious conditions of the sixteenth and seventeenth centuries. Thomas argued that magical beliefs served specific social functions — providing certainty in uncertain situations, explaining misfortune, offering therapeutic interventions where medicine failed — and that these functions declined as alternative institutions (insurance, medicine, the church) became more reliable providers of certainty, healing, and meaning.

Macfarlane's study, focused specifically on witchcraft in Essex, combined statistical analysis of prosecution records with detailed local social history to show that witchcraft accusations followed specific social patterns: they arose predominantly from disputes between neighbors over charity and obligation, typically following the refusal of a beggar woman's request. This "refusal-guilt" model — the accuser who had refused a request felt guilty, attributed subsequent misfortune to the refused person's resentment, and accused her of witchcraft — connected witchcraft to the breakdown of the traditional economy of communal obligation under the pressure of early capitalism.

### The Continental Social History of Witchcraft

The social history approach spread rapidly to continental scholarship. Robin Briggs's *Witches and Neighbors: The Social and Cultural Context of European Witchcraft* (1996) synthesized decades of European research to show that witchcraft accusations arose primarily from within communities rather than being primarily driven by witch-hunters from outside, and that the social dynamics of accusation — the role of community conflict, gender relations, age, and economic marginalization — were broadly consistent across European regions.

Wolfgang Behringer's work on witch-hunting in the Holy Roman Empire, Eva Pöcs's research on Hungarian witch belief, and similar national and regional studies collectively built up a picture of European witchcraft as primarily a local and community phenomenon whose prosecution dynamics were shaped by the specific social, religious, and legal configurations of each region.

### Crime Records, Inquisition Trials, and the Social Historical Evidence

The social history of magic depends heavily on judicial records — Inquisition trial transcripts, common law depositions, ecclesiastical court records, and civic prosecution records — for evidence of what ordinary people believed and practiced. These records are invaluable but require careful interpretation: they are the records of a juridical process, not transcripts of lived experience; the questions asked and the answers elicited were shaped by the legal categories and institutional interests of the investigators; and the records systematically over-represent the cases that came to judicial attention (which were not a random sample of all magical practice).

Sophisticated social historians of magic have developed methods for reading against the grain of trial records — attending to what defendants said when they were not directly responding to the leading questions of investigators, comparing cross-culturally to assess what was common to many accounts and thus potentially reflecting genuine popular belief, and using quantitative analysis of prosecution patterns to identify social structures that transcended individual cases.

### Beyond the Prosecution Records

The social history of magic has expanded beyond the prosecution records that were its initial primary source to incorporate a wider range of evidence:

- **Material culture**: Physical objects associated with magical practice — amulets, witch bottles, sealed rooms found during building renovations, written charms — provide direct evidence of practice independent of judicial records.
- **Medical records**: The records of medical practitioners who treated patients for conditions attributed to witchcraft or for whom magical healing was sought provide evidence of the overlap between medicine and magic.
- **Church court records**: Ecclesiastical courts that dealt with "superstitious" practice generated records of the range of magical activity that came to official attention outside the criminal justice system.
- **Literary and visual sources**: Popular printed literature, ballads, chapbooks, and visual representations of magical practice provide evidence of how magic was imagined and represented in popular culture, though the relationship between representation and practice requires careful analysis.

### Tensions with Intellectual History

The relationship between the social history of magic and the intellectual history of occult philosophy has been one of productive tension. Social historians criticized intellectual historians for focusing exclusively on elite texts and ideas while ignoring the overwhelming majority of magical practice that left no textual record. Intellectual historians criticized social historians for reducing complex philosophical and theological systems to functional social mechanisms and ignoring the genuine intellectual content of the traditions they studied.

The best contemporary scholarship in the history of magic integrates both approaches: attending both to the social contexts that shaped magical practice and to the intellectual content that practitioners brought to their work.

**See also:** Learned vs. Popular Magic; Cunning Folk and Popular Magic; Witchcraft; Magic and Gender; Magic vs. Religion.
""",
    },
    {
        "slug": "fate-and-free-will",
        "title": "Fate, Free Will, and Astral Determinism",
        "category": "Historiography and Methodology",
        "summary": "The central theological and philosophical problem posed by Renaissance astrology — whether celestial influences determine human action, threatening free will and divine justice — and the range of solutions proposed by natural philosophers, theologians, and astrologers to reconcile astrological influence with human freedom.",
        "related_figures": ["Ptolemy", "Giovanni Pico della Mirandola", "Marsilio Ficino", "Pietro Pomponazzi", "Thomas Aquinas"],
        "related_concepts": ["learned-astrology", "natal-astrology", "ptolemaic-cosmos", "natural-magic", "disenchantment"],
        "body": """## Fate, Free Will, and Astral Determinism

The most serious theological and philosophical challenge posed by astrology to Renaissance thought was not whether it worked but whether, if it worked, this was compatible with Christian theology. If the stars truly determined the course of individual human lives — if the planetary configuration at birth fixed a person's temperament, intelligence, fortune, and even the time of their death — then human freedom was an illusion and divine judgment was unjust (since one could not be held responsible for a fate one could not have avoided). This problem — astral determinism versus free will — was debated intensively from late antiquity through the Renaissance and constituted one of the most important philosophical contexts within which Renaissance natural magic and astrology were theorized.

### The Classical Sources of Astral Determinism

Stoic philosophy provided the ancient world's most comprehensive defense of astral determinism. For the Stoics, the cosmos was a perfectly rational system governed by universal *logos* (reason), and every event in the cosmos — including every human action and thought — was a necessary consequence of the laws of nature. The stars and planets were not causes of events in any simple sense but symptoms: manifestations of the same cosmic *logos* that governed everything, readable by those with the knowledge to interpret them. This complete determinism was compatible with Stoic ethics because the Stoics redefined freedom as acceptance of and cooperation with the inevitable rather than deviation from it.

Ptolemy's *Tetrabiblos* (the foundational text of learned astrology) attempted to maintain astrological influence while limiting its scope to tendencies rather than necessities. The stars incline (rather than compel), said Ptolemy: they create tendencies in the sublunary world that the practitioner of medicine, magic, or practical wisdom can mitigate through timely intervention. The wise man "commands the stars" not by overriding them but by using knowledge of stellar inclinations to work with rather than against them. This "inclinatory" rather than "deterministic" account of stellar influence became the standard position of learned Renaissance astrological theory.

### Medieval Solutions: Aquinas and Beyond

Thomas Aquinas provided the authoritative Scholastic solution to the astral determinism problem. Aquinas accepted that the stars influenced human bodies (through their light and motion, operating on the sublunary world through the medium of the air) and, through the body, influenced human passions and imagination. But the rational will — the specifically human faculty that enabled genuinely free choice — was not directly accessible to stellar influence. Only God had direct access to the will.

Therefore, Aquinas argued, the stars could produce tendencies toward certain actions by influencing the body and passions, but these tendencies could always be overridden by the exercise of rational will. The astrologer who predicted that a person born under Mars would be aggressive was making a probabilistic statement about typical behavior rather than a deterministic prediction about individual necessity. Most people, most of the time, followed their passions rather than exercising full rational control — which was why astrological predictions were often accurate. But the free human individual could always, in principle, choose differently.

This Thomistic solution preserved both the validity of astrology (as the science of probabilities regarding human tendencies) and the freedom of the will (as the genuinely free rational power not subject to stellar determination), and became the standard position of Renaissance Scholastic natural philosophy.

### Ficino's Practical Response

Marsilio Ficino's practical response to the threat of astral determinism was characteristically Renaissance: he accepted Aquinas's theoretical solution (the stars incline but do not compel the will) but devoted *De Vita III* to the practical question of how to manage astrological tendencies. If the Saturnine scholar was inclined to melancholy, cold, and contemplative excess, he could use Jovial and Solar countermeasures to moderate the Saturnine influence — not because the stars were overriding a different fate but because the skillful use of sympathies could cultivate the most favorable aspects of an astrological tendency and mitigate the less favorable.

This was a kind of astrological self-management: using knowledge of one's natal chart not to resign oneself to a determined fate but to cultivate the most favorable expression of one's astrological constitution. The "wise man commands the stars" in the sense that he uses knowledge of them to live as well as his stars allow.

### Pico's Attack

Giovanni Pico della Mirandola's *Disputationes Adversus Astrologiam Divinatricem* (written in the 1490s, published posthumously 1496) launched the most sustained and systematic Renaissance attack on astrological determinism and on the theoretical foundations of judicial astrology generally. Pico accepted the general principle of celestial influence on the sublunary world (he did not deny that the Sun caused the seasons or that the Moon influenced tides) but attacked the specific claims of judicial astrology — that planetary positions at birth determined individual fates — on both theoretical and empirical grounds.

Pico's theoretical arguments included: the impossibility of determining the exact moment of birth (a few seconds' difference would change the chart significantly but be impossible to measure accurately); the confusion between celestial bodies and their light (which was the actual physical mechanism of influence) and the arbitrary imaginary figures of the zodiacal signs (which had no physical reality); and the irrelevance of the "signs" to any genuine physical influence of the stars.

Pico's attack was influential but did not end astrological practice or silence its defenders. Girolamo Cardano and subsequent mathematical astrologers engaged seriously with Pico's arguments, responding that the empirical successes of astrology (predictions that were confirmed by observation) could not be explained away by theoretical objections.

**See also:** Learned Astrology; Natal Astrology; Ptolemaic Cosmos; Natural Magic; Disenchantment.
""",
    },
    {
        "slug": "decolonizing-magic-studies",
        "title": "Decolonizing Magic Studies: Non-Western Traditions and Global Perspectives",
        "category": "Historiography and Methodology",
        "summary": "The emerging critique of the Western-centric orientation of magic studies and the call to incorporate non-Western magical traditions, colonial encounters with indigenous magic, and Islamic and African contributions to Renaissance occultism into a genuinely global history of magical practice.",
        "related_figures": ["Liana Saif", "Paola Zambelli"],
        "related_concepts": ["western-esotericism-as-category", "translation-movements", "rejected-knowledge", "magic-vs-religion", "egyptian-wisdom"],
        "body": """## Decolonizing Magic Studies: Non-Western Traditions and Global Perspectives

The field of Western esotericism and Renaissance magic studies has been — with some important exceptions — oriented primarily toward a canonical tradition that runs from ancient Greek and Neoplatonic sources through medieval and Renaissance Latin culture to the modern West. This orientation has meant that significant dimensions of the global history of magical practice have been systematically underrepresented or misrepresented: the Islamic scholarly tradition that preserved and transmitted Greek magical knowledge to the Latin West; the African and indigenous American traditions that encountered European magic through colonial contact; the Hebrew and Aramaic sources of Kabbalistic practice; and the broader question of whether the category of "magic" as defined within Western academic frameworks applies meaningfully to traditions developed in other cultural contexts.

The call to "decolonize" magic studies — to challenge the Western-centric orientation of the field and to develop more genuinely global approaches — has emerged as an important critical intervention in the historiography of the early twenty-first century, building on broader movements for decolonization in the humanities and social sciences.

### The Islamic Contribution to Renaissance Magic

One of the most significant historiographical recoveries in recent scholarship on Renaissance magic has been the systematic reconsideration of the Islamic intellectual tradition as a foundational source rather than merely a transmission vehicle. The conventional narrative — in which Greek magical and philosophical texts were preserved by Islamic scholars during Europe's "Dark Ages" and then recovered by Latin scholars in the twelfth-century translation movements — has been revised by historians including Liana Saif (*The Arabic Influences on Early Modern Occult Philosophy*, 2015) to show that Islamic scholars were not merely preservers but active innovators who made substantial original contributions to astrological, alchemical, and magical theory.

The *Picatrix* (Arabic: *Ghāyat al-Ḥakīm*), a comprehensive astrological-magical encyclopedia composed in Arabic in the eleventh century and translated into Latin and Castilian in the thirteenth century, is perhaps the most important single text for demonstrating this point. The *Picatrix* synthesized Neoplatonic, Hermetic, and indigenous Arab magical traditions in ways that were not simply translations of earlier Greek sources but represented a distinctive and original synthesis. Its accounts of talisman-making, the animation of celestial images, and the philosophical theory underlying these operations went beyond anything in the Greek Hermetic sources and became one of the most important resources for Renaissance natural magic.

Ibn Khaldūn (1332–1406), the North African historian and philosopher, wrote the *Muqaddimah* (Introduction to History) which includes a sophisticated analysis of occult sciences — astrology, alchemy, geomancy, letter magic — within a broader epistemological framework that is both empirically skeptical and theoretically nuanced. Ibn Khaldūn's analysis of the cognitive and social dimensions of magical practice anticipates in some respects the concerns of modern social history of magic.

### African Magical Traditions and Colonial Encounter

The encounter between European magical traditions and African magical practices in the context of the Atlantic slave trade and colonialism created complex dynamics that are only beginning to receive sustained scholarly attention. Europeans who encountered African ritual specialists and their practices variously labeled them as "sorcerers," "witch doctors," or "diabolical" — applying the European polemical category of magic to practices that African communities understood in very different terms.

The Atlantic circulation of magical knowledge — the ways in which African, Indigenous American, and European magical traditions interacted, merged, and mutually influenced each other in the colonial context — has been studied in the context of specific New World traditions (Candomblé, Vodou, Santería, and related syncretic traditions) by historians including Yvonne Chireau (*Black Magic: Religion and the African American Conjuring Tradition*, 2003) and Karen McCarthy Brown (*Mama Lola: A Vodou Priestess in Brooklyn*, 1991). These studies demonstrate the creativity and resilience of African magical traditions in the context of enslavement and colonization, and the extent to which these traditions incorporated, reinterpreted, and transformed European Catholic elements in ways that were neither simple adoption nor simple resistance.

### The Category Problem: Is "Magic" a Universal?

The most fundamental decolonizing challenge to magic studies is the question of whether the category "magic" — as defined within Western academic frameworks, with its specific history of polemical construction and its particular relationship to "religion" and "science" — is applicable to traditions developed in non-Western cultural contexts.

Many scholars of non-Western religious practices have argued that applying the Western category "magic" to their subjects is itself a form of cultural imperialism: it imposes a Western framework (with its implicit hierarchy placing magic below religion and science) onto practices that their own communities understand in entirely different terms. An Ifá divination ritual in Yoruba culture, for example, is not "magic" in the Western sense — it is a specific form of religious-intellectual practice with its own epistemological claims, its own internal criteria of validity, and its own social functions — and calling it "magic" obscures more than it illuminates.

The response to this problem has taken several forms: some scholars argue for abandoning the category "magic" entirely in favor of more culture-specific terms; others argue for a critically self-conscious use of the category that acknowledges its problematic history while using it as a heuristic for cross-cultural comparison; and others argue for a systematic comparison between the polemical construction of "magic" in Western culture and analogous boundary-drawing practices in other cultures.

### Toward a More Inclusive History

The emerging field of global history of magic — practiced by scholars including Saif, Chireau, and others — seeks to construct a history of magical practice that takes seriously the contributions of non-Western traditions while avoiding the Eurocentrism of earlier approaches. This involves not merely adding non-Western "cases" to a Western analytical framework but reconsidering the framework itself in light of non-Western perspectives.

For the specific field of Renaissance magic studies, this means recognizing that the Renaissance "recovery" of ancient knowledge was always a selective and culturally specific recovery — that the Greek and Latin texts canonized by Italian humanists were themselves products of cultural selection and translation, that the Arabic and Hebrew intermediaries who preserved and transformed these texts made their own substantial contributions, and that the world beyond Europe had its own magical traditions that were beginning to impinge on European consciousness through colonial contact during precisely the period when Renaissance magic was at its most theoretically elaborate.

**See also:** Western Esotericism as a Scholarly Category; Translation Movements; Rejected Knowledge; The Yates Thesis.
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
    print(f"\nBatch 18 done: {inserted} inserted, {skipped} skipped.")


if __name__ == "__main__":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
    main()
