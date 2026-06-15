"""Seed batch 17: Social/Institutional — Courts and Esotericism, Magic and the Church, Censorship/Index, Magic and Gender, Learned vs Popular Magic."""

import sqlite3
import sys
import io
import json
from datetime import datetime

DB_PATH = "db/renmagic.db"

CONCEPTS = [
    {
        "slug": "courts-and-esotericism",
        "title": "Courts and Esotericism: Patronage, Power, and Occult Knowledge",
        "category": "Social and Institutional Contexts",
        "summary": "The role of royal and princely courts as centers of patronage for occult practitioners — astrologers, alchemists, natural magicians, and Kabbalists — and the complex interplay between esoteric knowledge and political legitimacy in Renaissance and early modern Europe.",
        "related_figures": ["John Dee", "Heinrich Cornelius Agrippa", "Marsilio Ficino", "Athanasius Kircher", "Paracelsus"],
        "related_concepts": ["patronage-and-magic", "learned-astrology", "alchemy", "republic-of-letters", "rosicrucianism"],
        "body": """## Courts and Esotericism: Patronage, Power, and Occult Knowledge

The courts of Renaissance and early modern Europe were among the most important institutional contexts for the practice and intellectual development of occult philosophy and esoteric knowledge. Royal and princely courts provided patronage for astrologers who cast horoscopes and advised on auspicious timing, for alchemists who promised to fill treasury coffers with transmuted gold, for natural magicians who offered to perform wonders as demonstrations of power, and for learned esotericists whose mastery of ancient wisdom enhanced the cultural prestige of their patrons. The court was simultaneously the site of genuine intellectual exchange about occult philosophy and a stage on which esoteric knowledge was performed as a form of political theater.

### The Court as Patronage System

The material basis of Renaissance intellectual culture was patronage: scholars, artists, and practitioners of all kinds depended on wealthy individuals — princes, cardinals, merchants, and eventually national monarchies — to provide the resources (salary, accommodation, library access, experimental materials) necessary for sustained intellectual work. Occult practitioners occupied a particular position within this system: they offered services that courts genuinely needed (astrological counsel, medical advice, technological innovation through alchemy) and that were difficult to obtain from ordinary university-trained scholars.

The court astrologer was perhaps the most socially stable of the occult practitioners at court. From the thirteenth century onward, European courts regularly employed salaried astrologers to advise on political decisions, to calculate auspicious timing for battles, treaties, and royal births, and to warn of dangerous celestial configurations. These astrologers were typically university-trained in medicine and philosophy, and their work overlapped with medical practice (natal astrology was inseparable from constitutional diagnosis in learned medicine) and natural philosophy.

The court alchemist occupied a more precarious position. The promises of alchemists — transmutation of metals, production of medicines of extraordinary power, manufacture of artificial gold — were too attractive to ignore and too impossible to fulfill to provide a stable basis for long-term employment. Courts across Europe employed alchemists, invested resources in their laboratories, and were consistently disappointed with the results. The history of court alchemy is punctuated by spectacular frauds, by imprisoned or executed practitioners who could not deliver what they had promised, and by occasional genuine pharmaceutical or metallurgical discoveries that fell far short of the promised transmutation.

### Ficino and the Medici Court

The paradigmatic example of court patronage enabling esoteric intellectual work is the relationship between Marsilio Ficino and the Medici family in fifteenth-century Florence. Cosimo de' Medici (1389–1464), the effective ruler of Florence and the most powerful banker in Europe, provided Ficino with a villa at Careggi, a library of Greek manuscripts, and the financial support that made possible his translation of the entire Platonic corpus, the Hermetic writings, Plotinus, Proclus, and Porphyry. Without Medici patronage, the Florentine Platonic Academy — the most important intellectual center for Renaissance Neoplatonism and the foundational institution of Renaissance esoteric culture — would not have existed.

Ficino's relationship with successive Medici (Cosimo, then Lorenzo "the Magnificent," then Lorenzo's son Piero) was mutually beneficial in the complex ways typical of court patronage: Ficino provided intellectual prestige and cultural capital; the Medici provided financial support and protection. The Platonic Academy that Ficino organized around the Villa Careggi was not a formal institution but a network of learned conversations, correspondence, and collaborative projects that positioned the Medici as the patrons of the revival of ancient wisdom — a political as well as intellectual claim.

### The Emperor Rudolf II

The court of the Holy Roman Emperor Rudolf II (r. 1576–1612) in Prague represents the most intensive concentration of occult practitioners at a single European court. Rudolf — a melancholic, reclusive, but intellectually passionate ruler — gathered at Prague an extraordinary collection of natural philosophers, alchemists, astrologers, artists, and collectors whose work collectively constituted what one historian has called the most important cultural center in late sixteenth-century Europe for the integration of art, natural science, and occult philosophy.

Among the practitioners who worked at or visited Rudolf's court were: John Dee and Edward Kelley, who spent several years in the Empire seeking imperial patronage for their angelic magical work; the astronomers Tycho Brahe and Johannes Kepler, who served as Imperial Mathematici; and dozens of alchemists, natural magicians, and physicians. Rudolf's *Kunstkammer* (art and curiosity cabinet) — which included natural specimens, mechanical automata, astrological instruments, paintings by Arcimboldo (whose portraits composed of natural objects embodied the occult theme of the macrocosm-microcosm), and works of art from across Europe — was itself a material embodiment of the occult philosophical conviction that art, nature, and magic were fundamentally connected.

Rudolf's court patronage was motivated by genuine personal interest in occult philosophy rather than purely political calculation, though the two were not easily separated: imperial patronage of learned occultists enhanced the Emperor's prestige as a ruler whose court attracted the greatest minds of Europe, and the alchemists' promised transmutation gold would have solved the Empire's chronic financial difficulties had it been achievable.

### Esotericism and Political Legitimacy

Courts used occult knowledge not only instrumentally but symbolically: the possession and patronage of esoteric wisdom was a form of political legitimacy, positioning the ruler as the heir of ancient royal magic and as the center of a universe ordered by divine wisdom. Astrological symbolism pervaded court ceremonies, festivals, and artworks: the ruler was depicted as a solar figure (Apollonian, golden, life-giving) or a Jovian figure (benevolent, just, kingly) or as the representative of the most auspicious planetary configuration of their era.

The Florentine Medici developed an elaborate symbolic program centered on Platonic philosophical imagery (the Graces, Venus, the Muses, the sun) that positioned them as philosopher-kings in the tradition of the Platonic *Republic*. The French court of Francis I cultivated a similar program of Neoplatonic-Hermetic symbolism. The Elizabethan court in England developed an "Astraea" mythology around Elizabeth I as the returning golden-age goddess — a mythology with Hermetic, Neoplatonic, and astrological dimensions that Frances Yates analyzed extensively.

### The Decline of Court Esotericism

The institutionalization of the new experimental natural philosophy in the seventeenth century — through the Royal Society (founded 1660), the Académie des Sciences (founded 1666), and their national equivalents — gradually displaced the court esotericist with the professional natural philosopher. The new scientists cultivated a public, collective, institutionalized form of natural knowledge that was deliberately distinguished from the private, hierarchical, and secretive knowledge of the occult tradition.

This shift did not eliminate esotericism from courts immediately: astrologers continued to advise monarchs throughout the seventeenth century, and alchemical laboratories at European courts persisted well into the eighteenth century. But the social prestige of occult practitioners relative to "scientists" declined steadily from the mid-seventeenth century onward, until the court astrologer and court alchemist became figures of historical curiosity rather than active intellectual forces.

**See also:** Patronage and Magic; Learned Astrology; Alchemy; Republic of Letters; Rosicrucianism.
""",
    },
    {
        "slug": "magic-and-the-church",
        "title": "Magic and the Church: Condemnation, Toleration, and Ecclesiastical Magic",
        "category": "Social and Institutional Contexts",
        "summary": "The complex relationship between Christian institutional religion and magical practice — including the Church's evolving positions on natural magic, demonic magic, and witchcraft, the ambiguity between ritual and magic, and the Church's own 'magical' practices of blessing, exorcism, and sacramental efficacy.",
        "related_figures": ["Thomas Aquinas", "Heinrich Institoris", "Johannes Weyer", "Marsilio Ficino"],
        "related_concepts": ["witchcraft", "malleus-maleficarum", "demonology", "exorcism", "natural-magic", "ceremonial-magic"],
        "body": """## Magic and the Church: Condemnation, Toleration, and Ecclesiastical Magic

The relationship between Christianity and magical practice is among the most complex and contested subjects in the history of Western religion. The Christian Church from its earliest centuries condemned magic (*mageia*, *maleficium*, *sortilegi*) as demonic, idolatrous, and incompatible with true faith; yet the Church's own practices — the blessing of water and salt, the consecration of bread and wine in the Eucharist, the exorcism of demons, the invocation of saints for miraculous healing, the use of relics — shared structural features with the magical practices it condemned. The boundary between religion and magic, so fundamental to the Church's self-understanding, was never as clear in practice as in theory, and the history of Christianity's relationship to magic is largely the history of attempts to draw, maintain, and redraw this contested boundary.

### The Patristic Condemnation

The early Christian writers established the basic framework for the Church's attitude toward magic. Magic was condemned primarily as a form of idolatry: the practices of the Graeco-Roman magical tradition (divination, love magic, curse tablets, astrological prediction, the animation of divine statues) involved implicit or explicit engagement with pagan gods and daemons, and were therefore violations of the first commandment. Augustine of Hippo (354–430 CE), in *De Doctrina Christiana* and *The City of God*, provided the most influential patristic account: all magical operations that went beyond the natural properties of things involved communication with demons (even when the practitioner was unaware of this), and demons were fallen angels who aided human beings only to corrupt them.

The Augustinian framework made demonic involvement the distinguishing mark of magic: what made magic different from legitimate religious practice was not the formal structure of the operation (invocation, petition, use of material objects) but the identity of the beings invoked. God, the saints, and the angels were legitimate objects of invocation through prayer; demons were not. And all magical practice — not explicitly directed toward God — was presumed to involve demonic complicity.

### The Medieval Distinction: Natural Magic vs. Demonic Magic

The twelfth and thirteenth centuries saw the elaboration of a more nuanced distinction that would be crucial for the Renaissance: the distinction between *magia naturalis* (natural magic, operating through the hidden natural properties of things) and *magia daemoniaca* (demonic magic, requiring the involvement of evil spirits).

Albert the Great (c. 1200–1280) and Roger Bacon (c. 1214–1292) argued that many operations that appeared magical were in fact natural: the attraction of iron by a lodestone, the effect of specific herbs on specific diseases, the tidal influence of the Moon — these were "occult" (hidden) properties of natural things but were not magical in the sense of requiring demonic agency. A natural philosophy that understood these hidden properties could make use of them without falling into demonic magic.

Thomas Aquinas (1225–1274) provided the authoritative Scholastic synthesis: natural magic was acceptable insofar as it operated through truly natural causes; magic that claimed to work through causes beyond natural explanation was presumptively demonic; and magic that explicitly invoked spiritual beings (whether labeled "angels" or "spirits" or "daemons") crossed the line into the forbidden, unless those beings were God and the saints properly invoked through the Church's liturgical forms.

This distinction gave learned Renaissance magicians like Ficino, Pico, and Agrippa their most important theoretical resource: *magia naturalis* could be defended as a form of learned natural philosophy operating within the framework of Thomistic natural causation. The harder cases — talismanic magic, celestial magic, ceremonial invocation — required more elaborate justification.

### The Ambiguity of Ecclesiastical Practice

The Church's own sacramental and liturgical practices created a persistent ambiguity about where religion ended and magic began. The Eucharist — in the Catholic doctrine of transubstantiation — involved the transformation of bread and wine into the Body and Blood of Christ through the priest's correct pronunciation of specific words ("Hoc est enim corpus meum" / "This is my body"), performed in the proper ritual context. This structure — specific words producing a physical transformation through religious authority — was structurally parallel to the claims made for ceremonial magic.

Popular misuse of the Eucharist for magical purposes (communion wafers used in love magic, healing spells, or agricultural magic) was a persistent problem documented throughout the medieval period. The magical efficacy attributed to holy water, consecrated salt, the sign of the cross, and the names and relics of saints by ordinary Christians was often difficult to distinguish from magical practice as the theologians defined it. The concept of *opus operatum* — the idea that sacraments work by virtue of the correctly performed act, regardless of the spiritual state of the minister — made the sacraments more (not less) analogous to magic in their formal structure.

This ambiguity was not a peripheral problem but a central one: if the Church's practices were defined as efficacious by virtue of correctly performed ritual acts invoking divine authority, then the charge that magical practices were illegitimately claiming similar efficacy required the Church to maintain a distinction that was difficult to articulate clearly.

### The Inquisition and the Persecution of Magic

The formal institutional mechanism of the Church's condemnation of magic was the Inquisition — the system of ecclesiastical courts established in the thirteenth century (papal inquisition established 1231–33) to investigate and prosecute heresy, and extended in the later medieval period to include witchcraft, sorcery, and various forms of magical practice.

The Inquisition's approach to magical practice evolved significantly over the medieval and early modern periods. Early medieval penitentials (manuals for confessors) treated most magical practices as superstition rather than heresy — spiritually harmful but not requiring the full apparatus of inquisitorial prosecution. The late medieval elaboration of the witchcraft theory (the idea that witches formed a Devil-worshipping conspiracy, met in sabbaths, and performed diabolical ceremonies) raised the theological stakes dramatically, making witchcraft a form of heresy (apostasy from Christianity in favor of a demonic counter-religion) that the Inquisition was duty-bound to prosecute.

The *Malleus Maleficarum* (1486) — whatever its actual influence on inquisitorial practice — represented the fullest theological elaboration of the witch as heretic and the fully diabolized account of witchcraft that made large-scale prosecution theoretically available.

**See also:** Witchcraft; Malleus Maleficarum; Demonology; Exorcism; Natural Magic; Ceremonial Magic.
""",
    },
    {
        "slug": "magic-and-gender",
        "title": "Magic and Gender: Women, Witchcraft, and the Gendering of the Occult",
        "category": "Social and Institutional Contexts",
        "summary": "The profoundly gendered dimensions of Renaissance magical discourse — the overwhelming identification of witchcraft with women, the feminization of magic's dangerous dimensions, and the male dominance of learned magical traditions — and feminist historiographical interventions in the study of magic.",
        "related_figures": ["Heinrich Institoris", "Johannes Weyer", "Reginald Scot"],
        "related_concepts": ["witchcraft", "malleus-maleficarum", "demonology", "cunning-folk", "love-magic", "magic-and-the-church"],
        "body": """## Magic and Gender: Women, Witchcraft, and the Gendering of the Occult

The relationship between magic and gender in Renaissance and early modern Europe was not incidental but structural: magical practice, magical accusations, and magical theory were all deeply shaped by the gender categories, anxieties, and power relations of the societies in which they operated. The overwhelming gendering of witchcraft accusations as accusations against women (approximately 75–80% of witchcraft accused across most European regions were female), the learned demonological account of why women were more susceptible to demonic influence, the feminization of dangerous magic alongside the male dominance of learned magical philosophy, and the use of witchcraft prosecution as a mechanism of social control over women who deviated from normative gender roles — all of these patterns require analysis that attends to gender as a primary analytic category.

### The Gendering of Witchcraft

The statistical dominance of women among witchcraft accused is one of the most consistent features of early modern European witchcraft prosecution and one of the most discussed in the scholarly literature. The pattern varied by region and period — in some areas (Iceland, Russia, certain regions of France) men constituted the majority of accused — but the overall European pattern was strongly female. This was not merely a reflection of existing assumptions: it was actively produced and maintained by the demonological theory that explained why women were more susceptible to demonic temptation.

The *Malleus Maleficarum* (1486) by Heinrich Institoris (Kramer) provides the most systematic and most misogynistic account of female susceptibility to witchcraft. Chapter VI of Part I, "Why Women are Chiefly Addicted to Evil Superstitions," argues on the basis of classical and patristic sources that women are more credulous (and thus more easily deceived by demons), more impressionable, more given to excessive passion, weaker in reason, and more carnal than men. The Latin word for "woman" — *foemina* — is etymologized (spuriously) as deriving from *fe* (faith) and *minus* (less): women are, by nature, less faithful.

These claims drew on a deep tradition of misogynistic thought in classical antiquity and Christian theology: Aristotelian biology treated the female as a defective male (a failure of the male form to fully actualize); patristic theology associated women with carnality and temptation (Eve's role in the Fall). The *Malleus* synthesized these traditions into a specifically demonological account: women's naturally greater susceptibility to carnal desire and their weaker rational control made them more vulnerable to demonic seduction, which typically took the form of sexual congress with an incubus.

### Social History: Who Were the Accused?

The social profile of accused witches across European regions reveals patterns that complicate the purely theological account. Studies by historians including Alan Macfarlane (*Witchcraft in Tudor and Stuart England*, 1970), Keith Thomas (*Religion and the Decline of Magic*, 1971), and the subsequent generation of historians of witchcraft prosecution (Robin Briggs, Lyndal Roper, Diane Purkiss) have shown that accused witches were disproportionately:

- Older women (post-menopausal, outside the normative reproductive female role)
- Widows (women without male household heads, economically marginalized)
- Women with reputations for quarrelsomeness, unusual knowledge, or social deviance
- Women accused by neighbors following failed requests for assistance (the "refusal-guilt" pattern: neighbor refuses a beggar woman's request, neighbor subsequently suffers misfortune, neighbor blames the woman)

These patterns suggest that witchcraft accusations served social functions beyond the purely theological: they provided a mechanism for managing marginal, disruptive, or threatening women, for resolving neighborhood disputes about obligation and charity, and for channeling communal anxieties about misfortune into individual blame.

### Women and Cunning Folk

The social history of popular magic — healing, divination, love magic, protection — shows a considerably more complex gender picture than the theology of witchcraft suggests. Cunning folk (practitioners of beneficial magic for hire) included women as well as men across most European regions, and healing in particular was strongly associated with women — through the tradition of female herbalists, midwives, and lay healers who constituted the primary healthcare providers for most ordinary people.

The famous accusation that women herbalists and midwives were being persecuted as witches — articulated by feminist historians in the 1970s (Barbara Ehrenreich and Deirdre English, *Witches, Midwives, and Nurses*) and influential in popular understanding — has been substantially critiqued by subsequent scholarship, which showed that male cunning folk were just as likely as female to be accused of witchcraft under some circumstances, that midwifery and herbal healing were not systematically targeted by witch-hunters, and that the relationship between female healing and witchcraft was more complex than the persecution narrative allowed. Nevertheless, the gendered dimensions of popular healing practice and its relationship to magical accusation remain important topics.

### Learned Magic as Male Domain

If dangerous magic was overwhelmingly identified with women, the learned tradition of natural magic, Neoplatonic philosophy, Kabbalah, and ceremonial magic was overwhelmingly male. The magicians-as-philosophers of the Renaissance — Ficino, Pico, Agrippa, Bruno, Dee — were all men, and the learned magical tradition was embedded in institutional contexts (universities, courts, humanist networks, religious orders) that effectively excluded women.

This is not to say that women were entirely absent from learned esoteric culture: women received astrological consultations, commissioned alchemical work, and served as patrons for occult practitioners. Some women participated in the alchemical tradition as laboratory assistants or in alchemical-medical practice. The figure of the sibyl or prophetess — a woman with access to divine revelation — appeared in Renaissance Neoplatonic thought, and some women became associated with prophetic gifts.

But the exclusion of women from university education, from the priesthood, and from most forms of public intellectual authority meant that the learned magical tradition was effectively a male domain, while the popular magical tradition was more gender-mixed and the dangerous magical tradition (witchcraft) was predominantly female.

### Feminist Historiography and the History of Magic

Feminist historiography has transformed the study of Renaissance and early modern magic in several significant ways. The pathbreaking work of scholars including Lyndal Roper (*Oedipus and the Devil*, 1994), Diane Purkiss (*The Witch in History*, 1996), and Deborah Willis (*Malevolent Nurture*, 1995) brought gender analysis to the center of witchcraft studies, showing how the demonological and prosecution literature produced and reproduced specifically gendered anxieties — about maternal power, female sexuality, the social liminality of old women — that were constitutive of the witchcraft phenomenon rather than merely incidental to it.

**See also:** Witchcraft; Malleus Maleficarum; Demonology; Cunning Folk and Popular Magic; Love Magic.
""",
    },
    {
        "slug": "censorship-and-the-index",
        "title": "Censorship, the Index, and the Control of Occult Knowledge",
        "category": "Social and Institutional Contexts",
        "summary": "The mechanisms by which Catholic and Protestant authorities attempted to suppress, regulate, or redirect magical and esoteric knowledge — through the Index of Forbidden Books, Inquisitorial prosecution, and confessional policing — and the paradoxical effects of censorship on the spread of occult texts.",
        "related_figures": ["Heinrich Cornelius Agrippa", "Giordano Bruno", "John Dee", "Johannes Trithemius"],
        "related_concepts": ["printing-and-the-occult", "magic-and-the-church", "grimoires", "rosicrucianism", "the-yates-thesis"],
        "body": """## Censorship, the Index, and the Control of Occult Knowledge

The attempt to control the production and circulation of occult knowledge through institutional mechanisms — the Catholic Church's Index of Forbidden Books (*Index Librorum Prohibitorum*), Inquisitorial prosecution of magical practitioners, Reformation condemnations of "superstition," and Protestant confessional policing — is a central feature of the social history of Renaissance and early modern magic. The control of occult knowledge was never merely an intellectual matter: it was simultaneously about social order, religious authority, and the management of the boundary between legitimate spiritual practice and forbidden magic. And censorship of occult texts, like censorship generally, produced paradoxical effects — stimulating curiosity, driving material underground, and sometimes increasing the authority of forbidden knowledge.

### The Index Librorum Prohibitorum

The *Index Librorum Prohibitorum* (Index of Prohibited Books), first published by Pope Paul IV in 1559 and subsequently revised multiple times, provided the official Catholic list of books that Catholics were forbidden to read, own, or disseminate without special dispensation. The Index was a response to the threat of heresy posed by Protestant literature and the diffusion of heterodox ideas through print, and it covered theological, philosophical, and scientific works as well as specifically magical texts.

The treatment of occult literature in the Index was complex. The most obviously demonic magical texts — grimoires, sorcery manuals, texts of explicitly diabolical magic — were categorically prohibited. More philosophically sophisticated occult texts required individual assessment: Agrippa's *De Occulta Philosophia* was placed on the Index; Ficino's *De Vita* (which contained substantive magical content) was initially spared (partly because Ficino was careful to include protective theological disclaimers and partly because he had powerful ecclesiastical patrons) but later controversial. The Hermetic *Corpus Hermeticum* and *Asclepius*, despite their pagan and potentially magical content, were generally accessible because they were treated as philosophical rather than magical texts.

The Index was enforced through the Inquisition in Catholic countries and through episcopal inspection of booksellers in others. Its effectiveness varied enormously by region: in Italy (where the Roman Inquisition was active) and Spain (where the Spanish Inquisition had broad powers), enforcement could be substantial; in France, the German Protestant states, and England, Catholic censorship had no legal authority.

### Trithemius and the Secrecy Ethic

The abbess and learned magician Johannes Trithemius (1462–1516) illustrates the complex relationship between esoteric secrecy and institutional censorship. Trithemius was the author of the *Steganographia* ("Hidden Writing"), a work ostensibly on cryptography but widely suspected of encoding instructions for magical operations using spirits to carry messages. Trithemius declined to publish the *Steganographia* during his lifetime, responding to critics that the work was misunderstood — it was about cryptography, not magic — but the work circulated in manuscript and generated enormous controversy.

The secrecy ethic of the esoteric tradition — the claim that occult knowledge should be communicated only to the worthy and must be hidden from the unworthy — was both a philosophical position (drawing on the Pythagorean tradition of esoteric transmission and the Neoplatonic idea that higher truths require philosophical preparation) and a practical response to the dangers of prosecution. Magical practitioners who encoded their knowledge in allegory, cipher, or ambiguous philosophical language were both practicing genuine esoteric secrecy and protecting themselves from censorship.

### Giordano Bruno and Inquisitorial Prosecution

Giordano Bruno's trial and execution by the Roman Inquisition (1600) is the most dramatic example of the Inquisition's engagement with ideas connected to the occult philosophical tradition. Bruno was burned not specifically for his magical beliefs but primarily for a combination of theological positions (his denial of Christ's divinity, the Trinity, transubstantiation, and possibly the immortality of the soul in its traditional Christian form) that placed him clearly within the category of heresy.

However, Bruno's natural philosophy — his infinite universe, his panpsychism, his theory of a universal living spirit pervading matter — was inseparable from the Hermetic and Neoplatonic magical tradition, and the Inquisitorial process was certainly aware of this connection. Whether Bruno was primarily prosecuted for theological heresy or for his magical-philosophical positions is a matter of scholarly debate, but the case illustrates how the intellectual tradition of Renaissance occult philosophy could bring its practitioners into fatal conflict with ecclesiastical authority.

### Protestant Censorship of Magic

The Protestant Reformation created new contexts for the censorship and condemnation of magic. Protestant reformers condemned the "magical" dimensions of Catholic practice (the Eucharist, relics, holy water, exorcism, the invocation of saints) as superstition — explicitly drawing on the same Augustinian critique of demonic magic that had been used against practitioners of explicitly magical arts. Luther, Calvin, and their successors argued that Catholic ceremonialism was a form of practical magic that exploited human credulity and contradicted the principle that God operated through Word alone, not through material vehicles.

This Protestant critique of Catholic "magic" complicated the censorship question: if Catholic sacramental practice was magical in a bad sense, then Protestant censorship of magic could not simply follow Catholic categories. Protestant reformers developed their own criteria for distinguishing superstition from genuine religion and proper medicine, criteria that generally emphasized the role of faith and the Word over the role of material objects and ritual procedures.

**See also:** Printing and the Occult Sciences; Magic and the Church; Grimoires; Rosicrucianism; The Yates Thesis.
""",
    },
    {
        "slug": "learned-vs-popular-magic",
        "title": "Learned vs. Popular Magic: Distinctions, Interactions, and Challenges",
        "category": "Social and Institutional Contexts",
        "summary": "The historiographical and social distinction between elite learned magic (natural philosophy, Neoplatonism, Kabbalah) and popular folk magic (village healers, cunning folk, rural customs) — a distinction that shaped both the prosecution of magic and its modern scholarly analysis, but that requires careful critique.",
        "related_figures": ["Keith Thomas", "Richard Kieckhefer", "Owen Davies"],
        "related_concepts": ["cunning-folk", "witchcraft", "grimoires", "natural-magic", "western-esotericism-as-category", "the-yates-thesis"],
        "body": """## Learned vs. Popular Magic: Distinctions, Interactions, and Challenges

The distinction between "learned magic" (the natural philosophy, Neoplatonism, Kabbalah, and ceremonial magic of the educated elite) and "popular magic" (the healing practices, charms, divination, and protective magic of village practitioners and their clients) has been one of the most influential conceptual frameworks in the modern scholarly study of Renaissance and early modern magical culture. This distinction organized Keith Thomas's pioneering *Religion and the Decline of Magic* (1971), shaped the subsequent social history of witchcraft prosecution, and provided the basic taxonomic structure for many decades of subsequent scholarship. It has also been extensively critiqued, revised, and complicated by historians who have shown that the two categories were more porous, more mutually dependent, and more analytically problematic than the initial framework suggested.

### The Historiographical Origins

The learned/popular distinction emerged in Renaissance scholarly culture itself before it became a historiographical category. Renaissance natural magicians were at pains to distinguish their learned, philosophically justified practice from the "vulgar magic" (*magia vulgaris*) of village healers, charmers, and wise-women whose practices they sometimes condemned as superstitious and sometimes quietly incorporated. The social hierarchy of magical knowledge — ancient philosophy, Kabbalah, and Neoplatonic cosmology at the top; village herbal healing and love charms at the bottom — was explicitly defended by Renaissance practitioners who wanted to claim intellectual respectability for their own work.

Keith Thomas's *Religion and the Decline of Magic* applied the learned/popular distinction with great analytical power to early modern England, distinguishing between the educated astrologers and Hermetic philosophers (whose work is analyzable in terms of intellectual history) and the cunning folk, wise-women, and magical healers (whose work is analyzable in terms of social history). Thomas's thesis — that both learned and popular magic declined in the face of the Scientific Revolution, Protestantism, and the growth of human technological control over the environment — depended on treating these two spheres as broadly parallel, both constituting "magic" in a general sense that could be contrasted with "religion" and "science."

### The Porosity of the Distinction

Subsequent scholarship has shown in multiple ways that the learned/popular boundary was far more porous than the initial framework suggested.

**Grimoires as mediating texts**: The grimoire tradition illustrates the impossibility of maintaining the learned/popular distinction cleanly. Grimoires existed at multiple social levels: the most sophisticated Latin ceremonial manuals (*Key of Solomon*, *Picatrix*) circulated primarily among literate, educated practitioners; vernacular versions reached a wider audience; and the content of the high-magic tradition (divine names, planetary spirits, conjuration procedures) filtered down into the amulets, charms, and procedures of village practitioners who could not read the original texts. A wise-woman's protective charm inscribed with half-remembered divine names and Hebrew-looking script might be a direct descendant of learned Kabbalistic magic, transmitted through multiple stages of social descent.

**Cunning folk and literacy**: Research by Owen Davies (*Popular Magic: Cunning-folk in English History*, 2003) and others has shown that many cunning folk were literate, owned books (including printed grimoires), and incorporated elements of learned magical theory into their practice. The "popular" practitioner was often not simply a bearer of folk tradition but an active reader of available magical literature who combined learned and traditional elements in eclectic ways.

**Shared clients**: The learned astrologer or natural magician and the village healer or wise-woman often served the same clients for overlapping purposes: love magic, recovery of stolen goods, protection from enemies, healing. The clients moved between learned and popular practitioners depending on cost, accessibility, and recommendation.

### The Social History of Magic

Richard Kieckhefer's *Magic in the Middle Ages* (1989) introduced the concept of the "common tradition" of magic — practices and beliefs shared across social levels — as a supplement to the learned/popular distinction. Rather than a sharp binary, Kieckhefer proposed a spectrum from the highly learned to the minimally literary, with the "common tradition" in the middle: practices like protective amulets, healing charms, and divination techniques that appeared in learned texts, in popular practice, and everywhere in between.

The sociology of magic — who practiced it, who used it, who prosecuted it, and how these social positions shaped what magic meant — became a central concern of the social history approach inaugurated by Thomas and developed by historians including Macfarlane, Briggs, Levack, and Rowlands. This approach attended to the social contexts of magical practice rather than primarily to its intellectual content, asking questions like: What social needs did magical practice serve? Who were the practitioners and clients by social class, gender, and age? How did magical accusations function within community dynamics?

### Theoretical Critiques: The Category of "Popular"

More recent scholarship has questioned the analytical validity of the category "popular" itself. "Popular culture" or "popular religion" as categories imply a coherent, autonomous cultural sphere associated with "the people" (as distinct from the elite) that many historians now find difficult to maintain. The "people" in question were not a culturally homogeneous group; their beliefs and practices were deeply shaped by the learned religious and philosophical culture that was transmitted to them through sermons, catechism, and printed texts; and the "popular" magical practices attributed to the rural poor were often shared by social elites who consulted the same practitioners.

The distinction between learned and popular magic, while useful as a rough sociological indicator of social location and educational level, is now generally treated as a heuristic rather than a descriptive reality — a starting point for analysis that must be complicated rather than a settled taxonomy.

**See also:** Cunning Folk and Popular Magic; Witchcraft; Grimoires; Natural Magic; Western Esotericism as a Scholarly Category.
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
    print(f"\nBatch 17 done: {inserted} inserted, {skipped} skipped.")


if __name__ == "__main__":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
    main()
