"""Seed batch 14: Magic Practice — Ceremonial Magic, Sigils, Solomonic Tradition, Magic Circle, Exorcism."""

import sqlite3
import sys
import io
import json
from datetime import datetime

DB_PATH = "db/renmagic.db"

CONCEPTS = [
    {
        "slug": "ceremonial-magic",
        "title": "Ceremonial Magic: Ritual, Hierarchy, and the Art of Conjuration",
        "category": "Magic: Theory and Practice",
        "summary": "The learned tradition of ritual magic involving elaborate preparations, precise procedures, invocations of angels and demons, and the use of magical implements — distinct from both natural magic and popular folk practice, demanding specialist knowledge and careful ritual execution.",
        "related_figures": ["Heinrich Cornelius Agrippa", "John Dee", "Marsilio Ficino", "Solomon (legendary)"],
        "related_concepts": ["grimoires", "angelic-hierarchy", "divine-names", "solomonic-tradition", "magic-circle", "demonology"],
        "body": """## Ceremonial Magic: Ritual, Hierarchy, and the Art of Conjuration

Ceremonial magic — the learned tradition of ritual magical operations conducted according to elaborate prescribed procedures, involving the invocation of angels, spirits, or demons through consecrated implements, ritual spaces, and precise verbal formulas — represents the most technically demanding and socially specialized strand of magical practice in the Renaissance. Distinguished by its elaborateness, its dependence on textual authority, its claim to work through legitimate spiritual hierarchy rather than demonic compact, and its association with learned practitioners rather than cunning folk or village healers, ceremonial magic occupied a complex position in Renaissance intellectual culture: simultaneously condemned by theological authorities, studied by natural philosophers, and practiced by a significant stratum of learned specialists.

### Defining Ceremonial Magic

The term "ceremonial magic" (*magia caerimonialis* or *magia ritualis*) was used by Renaissance authors primarily to distinguish ritual operations involving formal procedures, implements, and invocations from *magia naturalis* (natural magic, which operated through the inherent properties of natural things without ritual). Agrippa, following the standard tripartite division, distinguished natural magic (working through elemental sympathies), celestial magic (working through astrological influences), and intellectual or ceremonial magic (working through ritual engagement with spiritual beings — angels, daemons, and God).

The "ceremonial" quality of this magic referred to its dependence on ritual *ceremony*: specific times (determined by astrological calculation), specific places (the magic circle or triangle), specific words (conjurations, divine names, barbarous words), specific objects (the sword, wand, lamen, seal, incense, candles), and specific preparations (fasting, purification, ritual clothing). Each element of the ceremony was theoretically justified within the magical-cosmological worldview: the timing aligned the operation with favorable celestial influences; the circle protected the operator from unruly spirits; the divine names invoked the authority that compelled spiritual beings to appear; the operator's purification elevated his spiritual state to the level needed for effective communication with higher beings.

### The Textual Tradition: Grimoires and Handbooks

Ceremonial magic was essentially a textual tradition — it depended on written handbooks (*grimoires*) that specified the procedures for particular operations, the names and seals of the spirits to be invoked, the divine names to be used, and the constellation of circumstances required for success. The grimoire tradition extends from late antique Greek magical papyri through medieval Arabic and Latin compendia to the Renaissance handbooks that circulated widely in manuscript and print.

Key texts of the ceremonial magical tradition included:

- **The Solomonic tradition**: The *Key of Solomon* (*Clavicula Salomonis*), the *Lesser Key of Solomon* (*Lemegeton*), and related texts claimed the authority of King Solomon, who according to tradition had received his magical knowledge from God and used it to command demons in the construction of the Temple. These texts specified elaborate rituals for conjuring demonic spirits and compelling them to perform specific tasks.

- **The *Picatrix***: An Arabic astrological-magical encyclopedia (*Ghāyat al-Ḥakīm*, "The Goal of the Sage") composed in the eleventh century and translated into Latin in the thirteenth, the *Picatrix* provided a sophisticated philosophical account of magical operations (drawing on Neoplatonic and Hermetic cosmology) alongside practical instructions for constructing talismans, performing invocations, and working with planetary spirits.

- **The *Ars Notoria***: A text attributed to Solomon and claiming to confer, through the contemplation of magical figures (*notae*) and recitation of divine names, instant mastery of all the arts and sciences — grammar, rhetoric, logic, arithmetic, geometry, music, and astronomy. The *Ars Notoria* was one of the most widely circulated magical texts of the medieval period and was translated into vernacular languages.

- **Agrippa's *De Occulta Philosophia***: While not a grimoire in the narrowest sense, Agrippa's systematic treatise provided the philosophical and technical foundation for ceremonial magical practice that subsequent practitioners drew upon.

### The Cosmological Framework

Ceremonial magic operated within a coherent cosmological framework that distinguished levels of spiritual reality and specified the appropriate methods for engaging each level. The standard Neoplatonic-Christian schema divided the spiritual world into:

1. **God and the divine names**: The ultimate source of all power, invoked through the *Tetragrammaton* and other divine names to authorize and empower magical operations.
2. **Angels**: Divine messengers and administrators of cosmic functions, organized in hierarchies (the nine orders of Pseudo-Dionysius, or the seven archangels of the planetary tradition). Angels could be invoked for benevolent purposes and would respond to properly authorized invocation without the need for coercion.
3. **Daemons/Demons**: Ambiguous spiritual beings that in the classical tradition might be either benevolent (daimones as intermediaries in Platonic thought) or malevolent (fallen angels in the Christian tradition). The treatment of daemonic beings was the most theologically controversial aspect of ceremonial magic.
4. **Elemental spirits**: Beings inhabiting the four elements (sylphs in air, salamanders in fire, undines in water, gnomes in earth) described in the Paracelsian tradition and associated with natural magic rather than full ceremonial operation.

The hierarchy was crucial for the legitimation of ceremonial magic: if the operator's invocations consistently named God and the holy angels *before* addressing subordinate spirits, and if the operation was authorized by divine names, then it was argued to be an extension of legitimate spiritual authority rather than an illicit compact with demonic powers.

### John Dee and the Angelic System

John Dee's angelic communications (1582–1589) represent the most documented and most sophisticated example of Renaissance ceremonial magical practice, as well as its most radical extension. Dee's operations — conducted with Edward Kelley as scryer, using a *shewstone* (crystal ball), a *speculum* (obsidian mirror), and a table of practice covered with elaborate letter-squares — were explicitly modeled on the tradition of legitimate angelic invocation but claimed a degree of direct divine revelation unprecedented in the tradition.

The "Enochian" system that resulted from these operations — including a new "angelic" language, an elaborate cosmological geography of 30 Aethyrs and 91 Parts of the Earth, and 48 Calls or Keys for opening the Aethyrs — represented both the culmination of the ceremonial tradition and its creative transformation: Dee was not merely following an existing grimoire but receiving what he understood to be new divine revelation, delivered through legitimate angelic channels.

Dee's extensive diaries of the communications (*A True and Faithful Relation*, published posthumously in 1659) provide an unparalleled window into the practice of Renaissance ceremonial magic: the specific procedures, the interpretive challenges, the tensions between operator and scryer, and the theological anxieties that attended the enterprise.

### Legitimation and Condemnation

The central problem of ceremonial magic, from a theological perspective, was distinguishing legitimate operations (working through divine authority and holy angels) from forbidden demonic magic (working through compact with evil spirits). Practitioners and their defenders argued that operations properly authorized by divine names, conducted in a state of ritual purity, and aimed at legitimate ends (knowledge, protection, healing) were extensions of religion rather than departures from it.

Theological critics argued that any operation that claimed to compel spiritual beings to appear and perform tasks was implicitly a form of demonic magic, since God and the angels could not be compelled by human ritual. The apparent success of magical operations — if success was achieved — could only be the result of demonic deception: the demon mimicked the angel, performed the required task (at a price in corrupted souls), and deceived the operator into thinking he had achieved legitimate spiritual communication.

This debate — whether any form of conjuration magic could be legitimate — was never definitively resolved in the Renaissance period and remains a live question in the history of religion.

**See also:** Grimoires; Solomonic Tradition; Magic Circle; Divine Names; Angelic Hierarchy; Demonology.
""",
    },
    {
        "slug": "solomonic-tradition",
        "title": "The Solomonic Tradition in Magic",
        "category": "Magic: Theory and Practice",
        "summary": "The body of magical texts and practices claiming the authority of King Solomon — who according to legend commanded demons through his seal-ring — forming the backbone of medieval and Renaissance learned ceremonial magic and leaving a legacy from the Key of Solomon through modern occultism.",
        "related_figures": ["Solomon (legendary)", "Heinrich Cornelius Agrippa", "John Dee"],
        "related_concepts": ["ceremonial-magic", "grimoires", "demonology", "angelic-hierarchy", "divine-names", "magic-circle"],
        "body": """## The Solomonic Tradition in Magic

The figure of King Solomon — biblical monarch, builder of the Temple, possessor of divine wisdom and supernatural power — stands at the center of the most influential current in Western learned magic. The Solomonic tradition in magic comprises a substantial body of texts, techniques, and symbolic structures claiming Solomon's authority: handbooks for conjuring demonic spirits, catalogues of the names and seals of supernatural beings, formulae for constructing magical implements, and philosophical accounts of how Solomon acquired and used his power. From the medieval period through the Renaissance and into modern occultism, the Solomonic tradition has been the primary framework within which learned ceremonial magic has operated.

### Solomon in Biblical and Post-Biblical Tradition

The historical basis for Solomon's magical reputation lies primarily in the biblical accounts of his wisdom and his command over demons and spirits in post-biblical Jewish tradition. The historical Solomon (tenth century BCE) is presented in 1 Kings as a king of extraordinary wisdom and building accomplishment, but with no explicitly magical attributes. However, two features of the biblical narrative provided hooks for later magical elaboration: Solomon's unsurpassed wisdom (which the biblical text attributes to divine gift: God appeared to Solomon in a dream and asked what gift he desired, and Solomon chose wisdom rather than riches or military power) and the construction of the Temple using Phoenician craftsmen, which tradition later described as involving the coercion of supernatural labor.

The *Testament of Solomon*, a Greek text probably composed in the early centuries CE, is the key document in the development of Solomon as magician. In it, God sends Solomon a ring with a seal that allows him to command demons and press them into service in building the Temple. Each demon who is captured by the ring's power declares its name, its activity (the illnesses or disasters it causes), and the name of the angel who can defeat it. This catalogue of demons and their angelic counterparts became the template for subsequent demonological and magical literature.

By the early medieval period, the tradition that Solomon had a complete knowledge of demonic beings, had bound them into service, and had left a written record of his knowledge for his successors was well established. Arabic sources (which contributed significantly to the Solomonic tradition through the medieval translation movements) presented Sulayman ibn Dawud as a prophet with command over jinn and winds, and Arabic magical texts attributed to Solomon circulated widely.

### The Key of Solomon (Clavicula Salomonis)

The most important single text in the Solomonic tradition is the *Key of Solomon* (*Clavicula Salomonis*), a grimoire of uncertain origin and complex manuscript tradition that survives in numerous Latin and vernacular versions from the medieval and early modern periods. The *Key* is attributed to Solomon as its author (claiming to be the text he left for his son Roboam); it covers the ritual preparations required for magical operations, the construction and consecration of magical implements (knife, wand, pentacles, robes), the timing of operations (by planetary day and hour), the forms of invocation and conjuration, and the methods for dismissing spirits at the end of an operation.

The *Key*'s theoretical framework is broadly Christian: it emphasizes the need for ritual purity (fasting, confession, prayer), authorizes all operations by divine names and biblical verses, and situates the practitioner's power over spirits as derived from legitimate divine authority rather than demonic compact. The spirits conjured by the *Key* are compelled by the divine names written in the pentacles (magical seals) and spoken in the conjurations; they have no choice but to appear and execute the operator's commands, because the divine authority invoked is absolute.

A related text, the *Lemegeton* (also known as the *Lesser Key of Solomon* or *Goetia*), provides catalogues of 72 demons — their names, appearances, ranks, and the services they can perform — along with the specific seals to be drawn and procedures to be followed in conjuring each. The 72 demons of the Goetia became the standard repertoire of demonic names in the Western ceremonial tradition, carried forward from medieval grimoires through Agrippa and Dee into modern occultism.

### The Philosophical Justification

Renaissance natural philosophers who engaged seriously with the Solomonic tradition faced the challenge of providing a philosophically respectable account of how and why the tradition worked. The dominant strategy was to distinguish between legitimate operations — those working through divine authority and holy angels — and forbidden operations — those working through demonic compact. The Solomonic tradition, with its emphasis on divine names and angelic authorization, could be claimed to fall in the former category.

Agrippa provides the most systematic Renaissance philosophical account. In *De Occulta Philosophia* III, he argues that spirits — including demons — are bound by the divine names because those names invoke the authority of the Creator over all created beings. When the operator properly invokes the *Tetragrammaton* and the angelic names appropriate to the operation, he is not conducting a demonic compact but extending legitimate divine authority into the spiritual world. The demons who appear and serve are not freely cooperating but are compelled by a power higher than themselves.

This argument was not universally accepted. Johannes Trithemius (1462–1516), Agrippa's teacher, warned that many who thought they were engaging with holy angels through legitimate operation were in fact being deceived by demons who mimicked angelic appearance. The devil, in the standard Christian demonology, could appear as an angel of light (2 Corinthians 11:14), and the operator's subjective sense of working with legitimate spiritual authority was no guarantee of actual legitimacy.

### The Solomonic Legacy

The Solomonic tradition proved remarkably durable. Its basic structure — the operator equipped with divine names and angelic authority, working within a protected magic circle, commanding demonic spirits through the power of a superior spiritual authority — persisted from the medieval period through the Renaissance and into the early modern world with remarkably little structural change.

The tradition was transmitted through manuscript networks in the medieval period, was discussed and partially systematized by Renaissance natural philosophers, and continued to circulate in print and manuscript throughout the early modern period despite repeated condemnation by both Catholic and Protestant theological authorities. The Faust legend, which spread widely in printed form from the 1580s onward, represents the popular cultural image of Solomonic magic — the scholar who commands demons — with the crucial difference that Faust's compact is unambiguously demonic rather than divinely authorized.

**See also:** Ceremonial Magic; Grimoires; Magic Circle; Demonology; Divine Names; Angelic Hierarchy.
""",
    },
    {
        "slug": "magic-circle",
        "title": "The Magic Circle: Ritual Space and Spiritual Boundary",
        "category": "Magic: Theory and Practice",
        "summary": "The geometrically inscribed sacred space — typically a circle bearing divine names, pentacles, and protective formulas — that defined and protected the operator's working area in ceremonial magic, serving simultaneously as a cosmological map and a boundary between human and spiritual realms.",
        "related_figures": ["Heinrich Cornelius Agrippa", "John Dee", "Solomon (legendary)"],
        "related_concepts": ["ceremonial-magic", "solomonic-tradition", "divine-names", "demonology", "angelic-hierarchy"],
        "body": """## The Magic Circle: Ritual Space and Spiritual Boundary

The magic circle — a geometrically precise inscribed boundary, typically nine feet in diameter, marked with divine names, angelic names, pentacles, and protective formulas — is among the most visually iconic elements of Western ceremonial magic and one of its most theoretically significant features. More than a mere precaution, the magic circle embodies a cosmological claim: that ritual space can be distinguished from ordinary space, that the boundary between human and spiritual realms can be ritually marked and maintained, and that the properly equipped practitioner can work within a protected zone that is simultaneously part of the world and set apart from it.

### Construction and Components

The instructions for constructing a magic circle vary across the different grimoire traditions but share several consistent features. The basic form is a circle (or concentric circles) drawn on the ground or floor with chalk, coal, or a consecrated implement such as a sword or knife. Within and around this circle are inscribed:

- **Divine names**: The *Tetragrammaton* (YHWH) and other names of God (*El Shaddai, Adonai, Ehyeh Asher Ehyeh*) written at the cardinal points or distributed around the circumference
- **Angelic names**: The seven archangels (*Michael, Gabriel, Raphael, Uriel, Sachiel, Samael, Cassiel*) and their planetary correspondences
- **Pentacles and seals**: Geometric figures associated with specific divine or angelic powers, derived from the Solomonic grimoire tradition
- **Protective formulas**: Biblical verses (particularly psalms), names of power, and commands addressed to malevolent spirits
- **Triangle of Art**: A separate triangle drawn outside the circle, into which the conjured spirit is commanded to appear and take visible form

The *Key of Solomon* specifies that the circle should be drawn at the exact hour appropriate to the planned operation (determined by the planetary hour system), using a new pen and ink mixed with holy water, and that the operator must purify himself thoroughly before beginning.

### The Theoretical Functions of the Circle

The magic circle serves at least three distinct theoretical functions within the ceremonial magic tradition, and the tension between these functions reflects broader tensions in the theory of magical operations:

**Protection**: The primary explicit function of the circle in most grimoire texts is to protect the operator from the spirits he conjures. Spirits — particularly demonic spirits — are presumed to be hostile to humans and would harm the operator if given the opportunity. The circle, marked with divine names and angelic authority, is a barrier that the spirit cannot cross: it cannot enter the circle to harm the operator, and the operator within the circle is therefore able to address and command the spirit from a position of safety. This protective function makes the circle analogous to a fortress or armor rather than to sacred space in the religious sense.

**Sacred space**: The circle also functions as a consecrated space set apart from ordinary reality — analogous to the Temple or the altar space in religious ritual. By marking out the circle with divine names and entering it in a state of ritual purity, the operator creates a zone of heightened spiritual significance in which communication with higher (or lower) spiritual beings is possible. This function aligns the circle with ritual space in religious traditions more generally.

**Cosmological mapping**: The magic circle, with its inscribed divine names at the cardinal points, its planetary and angelic attributions, and its precise geometric proportions, can also function as a model or map of the cosmos — a miniature universe in which the practitioner stands at the center, surrounded by the divine and spiritual powers that organize the real universe. In this reading, the circle is a kind of operational mandala: by standing within the correctly inscribed circle, the operator literally situates himself at the center of the cosmological order, in a position from which he can address all the surrounding spiritual powers.

### The Circle and Spiritual Hierarchy

The magic circle embodies a claim about spiritual hierarchy and authority. The operator inside the circle is, ritually speaking, in a position superior to the spirit commanded to appear in the triangle outside the circle. The divine names written in the circle authorize the operator to give commands that the spirit is obligated to obey: the operator speaks "in the name of" the divine authority that the circle's inscriptions invoke, and that authority is greater than any spiritual being, demonic or angelic.

This claim about authority was, as noted, theologically controversial: critics argued that no ritual procedure could give a human being genuine authority over spiritual beings, and that any apparent compliance by spirits was a demonic deception. Defenders argued that the circle — when properly constructed, properly inscribed, and entered in the proper ritual condition — was a legitimate extension of divine authority rather than a pretension to powers the operator didn't really have.

### The Triangle of Art

The triangle drawn outside the circle — into which the conjured spirit is commanded to appear — is the complementary structure to the operator's circle. Where the circle is the operator's protected space, the triangle is the spirit's constrained space: by commanding the spirit to "enter the triangle and appear in a fair and visible form," the operator channels the spirit's manifestation into a controlled, bounded space where it can be seen and addressed without being able to harm the operator.

The triangle's dimensions and inscriptions vary across the tradition, but it typically bears three divine names at its corners, a central seal or pentacle associated with the spirit being conjured, and the specific names of the spirit being summoned. The triangle is designed not merely to contain the spirit but to provide a structured space of communication — to establish the possibility of speech between human and spirit within a ritually controlled frame.

### From Protective Circle to Sacred Space

The history of the magic circle in Western esotericism shows a gradual transformation from primarily protective function (the circle as defense against potentially hostile spiritual forces) toward primarily sacred space function (the circle as the operator's ritual cosmos). This shift is associated with the development of more explicitly "white magic" or "angelic" traditions in which the spirits invoked are presumed to be benevolent and in which the primary purpose of the ritual space is to create conditions for spiritual communication rather than to defend against spiritual attack.

In the modern Western esoteric tradition, particularly in Wicca and other contemporary magical practices, the magic circle has undergone a further transformation: it is cast as sacred space and then "opened" at the end of the ritual, with the emphasis on creating a temporary sacred community rather than on defense or spiritual compulsion. This contemporary form of the circle is genealogically continuous with the Renaissance ceremonial tradition but has been significantly transformed through the filtering of the tradition through nineteenth and twentieth century esoteric movements.

**See also:** Ceremonial Magic; Solomonic Tradition; Divine Names; Demonology; Angelic Hierarchy.
""",
    },
    {
        "slug": "exorcism",
        "title": "Exorcism: Expelling Demons and the Boundaries of Ritual Authority",
        "category": "Magic: Theory and Practice",
        "summary": "The ritual expulsion of demonic beings from persons, places, or objects — a practice with deep roots in Jewish, Christian, and ancient Near Eastern tradition — occupying a contested boundary between legitimate religious practice and forbidden magic in the Renaissance.",
        "related_figures": ["Heinrich Cornelius Agrippa", "Johannes Weyer", "Pietro Pomponazzi"],
        "related_concepts": ["demonology", "ceremonial-magic", "divine-names", "grimoires", "witchcraft", "malleus-maleficarum"],
        "body": """## Exorcism: Expelling Demons and the Boundaries of Ritual Authority

Exorcism — the ritual expulsion of a demon from a possessed person, place, or object — occupied a peculiar position in Renaissance religious and magical culture: it was officially recognized by the Catholic Church as a legitimate religious practice, performed by ordained priests using approved formulas, yet it shared nearly all its structural features with the ceremonial magic that the same Church condemned as illicit. Both exorcism and conjuration involved the invocation of divine names, the command given to a spiritual being to obey and depart, and the claim that a human being could exercise authority over supernatural forces through ritual means. The difference lay in authority and purpose: exorcism was performed by authorized representatives of the Church for purposes of liberation, while conjuration was performed by private individuals for private ends.

### Biblical and Early Christian Foundations

The practice of exorcism in the Christian tradition rests on the synoptic Gospel accounts of Jesus casting out demons — the most frequent category of miraculous activity attributed to Jesus in the Synoptic Gospels. The Markan narrative in particular presents Jesus as a practitioner of extraordinary exorcistic power: "What is this? A new teaching — and with authority! He even gives orders to evil spirits and they obey him" (Mark 1:27). The Beelzebub controversy (Matthew 12:22–32; Mark 3:22–30; Luke 11:14–23) records the accusation that Jesus cast out demons by the power of the chief demon, and Jesus's defense — that a kingdom divided against itself cannot stand — affirms that his exorcisms operate through divine rather than demonic power.

Jesus commissioned his disciples to cast out demons (Matthew 10:1), and the Acts of the Apostles records successful exorcisms by the apostles in Jesus's name. However, it also records an unsuccessful attempt by non-disciples — the "seven sons of Sceva" — to use the name "Jesus whom Paul preaches" for exorcism, with disastrous results (Acts 19:13–16), underlining the point that successful exorcism requires legitimate authority, not merely the correct verbal formula.

The early Christian church maintained an order of *exorcists* (the third of the minor orders below the diaconate in the Latin Church), responsible for performing exorcisms over catechumens before baptism and over the possessed. By the medieval period, the formal exorcism of persons allegedly possessed by demons had developed an elaborate ritual form, eventually codified in the *Rituale Romanum* (1614, formally promulgated after the Council of Trent's systematization of Catholic practice).

### The Structure of the Exorcism Rite

The Catholic exorcism rite as it developed through the medieval and early modern periods shares its fundamental structure with the ceremonial magic of the grimoire tradition:

1. **Invocation of divine authority**: The rite begins with the invocation of God, Christ, the Holy Spirit, and the Virgin Mary, establishing the divine authority under which the exorcist operates.
2. **Litanies and scriptural passages**: Extended litanies to the saints, psalms, and Gospel readings establish the religious context and summon the protective power of the entire Christian community.
3. **Imperative command**: The exorcist directly addresses the demon, commanding it to identify itself (in some versions) and depart, using the authority of divine names: "I command you, unclean spirit... by the name of Jesus Christ of Nazareth, to depart."
4. **Imposition of hands and blessing with holy water**: Physical contact and the use of blessed material substances (holy water, salt) accompany the verbal formula.
5. **Prayers of thanksgiving and dismissal**: The rite concludes with prayers of thanksgiving if successful.

The structural parallel with conjuration is unmistakable: both involve the claim to exercise authority over a spiritual being through the power of divine names. The difference is directional and intentional: the exorcist commands the demon to leave a human host (liberation), while the conjurer commands a demon or spirit to appear and serve (compulsion). But the underlying claim about the relationship between ritual authority, divine names, and spiritual obedience is the same.

### Possession, Medicine, and Skepticism

The Renaissance debates about demonic possession were inseparable from debates about exorcism's legitimacy and effectiveness. If the possessed person was not genuinely possessed by a demon but was suffering from a natural illness (melancholy, hysteria, epilepsy), then the exorcism ritual was at best useless theater and at worst a harmful distraction from proper medical care.

Pietro Pomponazzi (1462–1525), in his *De Incantationibus* (written around 1520), argued that all apparent cases of demonic action — including possession and the effects of witchcraft — could be explained by natural causes: the occult properties of celestial influences acting on human psychology through the imagination. On this view, demonic possession was not real; the "exorcism" was effective (when it was) only through its psychological effects on the sufferer, who believed in it and was thus susceptible to its placebo power.

Johannes Weyer (1515–1588), a physician and disciple of Agrippa, argued in *De Praestigiis Daemonum* (1563) that most accused witches were mentally ill women suffering from melancholy, whose confessions of demonic compact and attendance at sabbaths were delusions rather than realities. Weyer accepted the existence of demons but denied that they worked through the women commonly accused of witchcraft; instead, the real agency in apparent bewitchment cases was natural illness plus diabolic delusion. Weyer's skepticism about witchcraft did not extend to skepticism about possession per se, but his natural-cause explanations were used by later skeptics.

The tension between theological accounts of possession (genuine demonic invasion requiring exorcism) and medical accounts (natural illness requiring medical treatment) was never definitively resolved in the Renaissance and remains unresolved in some religious communities today. The historical scholarship on this tension — including its gender dimensions (the majority of possession cases involved women) and its social-power dimensions (possession and exorcism were public dramas that could both enhance and disrupt ecclesiastical authority) — has become a significant area of inquiry in the social history of religion.

**See also:** Demonology; Ceremonial Magic; Divine Names; Witchcraft; Malleus Maleficarum.
""",
    },
    {
        "slug": "sigils-and-magical-seals",
        "title": "Sigils, Magical Seals, and the Language of Spirits",
        "category": "Magic: Theory and Practice",
        "summary": "The graphic signs, seals, and characters associated with spiritual beings in the Western magical tradition — serving as the visual identity and binding signature of angels and demons — along with techniques for constructing them from divine names through Kabbalistic letter manipulation.",
        "related_figures": ["Heinrich Cornelius Agrippa", "John Dee", "Solomon (legendary)"],
        "related_concepts": ["ceremonial-magic", "divine-names", "solomonic-tradition", "gematria-and-letter-mysticism", "magic-squares", "talismans"],
        "body": """## Sigils, Magical Seals, and the Language of Spirits

The *sigil* (from Latin *sigillum*, "seal") and the *magical seal* or *character* — graphic signs associated with specific spiritual beings, divine names, or magical operations — constitute one of the most distinctive elements of the Western ceremonial magic tradition. In the Renaissance, these graphic signs were understood as more than arbitrary labels: they were the visual equivalents of divine and angelic names, bearing in their geometric forms the same inherent power that divine names carried in their phonetic forms. To draw a spirit's seal correctly was to invoke the spirit's presence; to inscribe it on a talisman was to embed the spirit's power in material form.

### The Theory of Magical Signs

The philosophical foundation of magical seals rests on the same premise as the doctrine of divine names: that certain signs are not merely conventional representations of realities but genuine participations in the powers they designate. Just as the Hebrew letters are not arbitrary symbols but the building blocks of creation, so the geometric figures of magical seals are not arbitrary designs but visual expressions of spiritual realities.

Agrippa, in *De Occulta Philosophia* I and III, provides the most systematic Renaissance account of the theory of magical signs and characters. He distinguishes several types of characters:

1. **Characters from celestial figures**: Derived from the arrangement of stars in a constellation (the "image" of a planet or star as seen in the sky), tracing the outline of that arrangement and thus carrying the celestial body's power in visual form.

2. **Characters from names**: Derived through the manipulation of Hebrew letters. The most important technique was the *aiq bekar* (or "Kabbalistic square"), which reduced each letter to a number and then used the resulting numbers to generate a geometric path on a nine-box grid. The path traced by connecting the numbered positions of the letters of an angel's name produced that angel's seal.

3. **Characters from spirits themselves**: Some grimoire texts claimed that spirits had their own natural signs — intrinsic to their nature as letters are intrinsic to words — and that these signs could be received through revelation (the spirit itself revealed its seal to the practitioner in a properly conducted operation) or derived from traditional sources.

### The Rose Cross and the Magic Square Method

The most technically elaborate method for deriving angel seals was through the *kamea* (magic square) in combination with a letter-to-number encoding of the angel's name. Magic squares — numerical arrays where all rows, columns, and diagonals sum to the same value — were associated with specific planets in the Agrippa-derived tradition (Saturn's 3×3 square, Jupiter's 4×4 square, Mars's 5×5 square, Sun's 6×6 square, Venus's 7×7 square, Mercury's 8×8 square, Moon's 9×9 square). By assigning Hebrew letters to the numbers of the appropriate planetary square and then tracing the path of an angel's name through the square, a unique geometric sigil for that angel could be derived.

This technique — which combined magic square mathematics, Hebrew gematria, and visual design in a single procedure — exemplified the Renaissance synthesis of Pythagorean number mysticism, Kabbalistic letter-mysticism, and practical magical technique. The resulting sigil was not arbitrary: it was derived by a systematic procedure from the angel's name, so that anyone who knew the procedure could verify that a given sigil correctly represented a given name.

### The Seals of the 72 Demons

The Solomonic tradition provided a canonical set of demonic seals: the *Lemegeton* or *Lesser Key of Solomon* included seals for each of the 72 demons listed in its "Goetia" section. These seals — intricate interlocking geometric forms often resembling letters, crosses, or abstract diagrams — were inscribed on the magical implements used in conjuring the associated demon, printed on the "lamen" (a breastplate) worn by the operator, and drawn in the circle and triangle of the ritual space.

The practical function of the demonic seal in the conjuration procedure was both identificatory (marking which spirit was being summoned) and compulsory: the demon was "bound" to appear and serve by the power of its own seal, inscribed in the context of the divine names that authorized the operator to invoke it. The demon could not ignore the invocation of its own seal any more than it could ignore the divine names — for its seal, derived from its name, participated in the same structural reality as its name.

### Dee's Enochian Seals and Tables

John Dee's angelic communications introduced an entirely new set of magical seals: the letter-squares received through Edward Kelley's scrying, which Dee called the *Tabula Recensa* and related tables. The Enochian system's fundamental document, the Great Table (or Watchtower system), is a large letter-square from which, through various methods of extraction and recombination, the names and seals of the angelic governors of the four elemental quarters and the 30 Aethyrs can be derived.

Dee's approach to angelic seals was in some respects more radical than the Agrippa-Solomonic tradition: rather than deriving seals from already-known angel names through Kabbalistic letter-manipulation, Dee claimed to receive entire new systems of spiritual names and their corresponding visual forms directly from the angels themselves. The resulting seals were authoritative because divinely revealed, not because correctly derived from established tradition.

### The Lasting Influence of Magical Seals

The sigil tradition proved remarkably durable. The seals of the *Lemegeton* demons and the Agrippa-derived planetary spirit seals were carried forward into the nineteenth-century esoteric revival (Eliphas Lévi's *Dogme et Rituel de la Haute Magie*, the *Key of Solomon* editions of Arthur Edward Waite and S.L. MacGregor Mathers) and became foundational elements of the Golden Dawn's ritual system. In contemporary Western magic, "sigilization" — the creation of custom sigils from the practitioner's own intention, rather than from received traditional signs — has become a widespread technique, secularizing the Kabbalistic sigil-from-name technique into a form of self-directed psychological practice.

**See also:** Ceremonial Magic; Divine Names; Solomonic Tradition; Magic Squares; Gematria and Letter Mysticism; Talismans.
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
    print(f"\nBatch 14 done: {inserted} inserted, {skipped} skipped.")


if __name__ == "__main__":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
    main()
