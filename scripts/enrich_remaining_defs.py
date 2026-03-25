"""Generate definitions for remaining 47 undefined dictionary terms."""
import io, sqlite3, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

DB = "db/renmagic.db"
conn = sqlite3.connect(DB)

defs = {
    # PHILOSOPHICAL terms
    230: {
        "brief": "Being or entity \u2014 the most general metaphysical category in Scholastic and Renaissance philosophy.",
        "long": "Ens (Latin: 'being' or 'entity') is the most fundamental category of Scholastic metaphysics, denoting anything that exists or can exist. In Renaissance magical philosophy, the concept of *ens* bridges the physical and spiritual: Paracelsus distinguished five types of *ens* (astral, venomous, natural, spiritual, divine) as causes of disease, while Scholastic magi debated whether occult properties belonged to the *ens* of a thing or to external influences acting upon it."
    },
    235: {
        "brief": "Reason or rational faculty \u2014 the discursive mode of knowing, contrasted with direct intellectual intuition.",
        "long": "Ratio (Latin: 'reason' or 'reckoning') designates discursive reasoning in Scholastic and Renaissance philosophy \u2014 the step-by-step movement from premise to conclusion, contrasted with the direct apprehension of *intellectus*. In Ficino's Neoplatonic psychology, *ratio* occupies a middle position: higher than *sensus* (sensation) but lower than *intellectus* (intellective vision). The magical practitioner aspires to transcend *ratio* and reach *intellectus*, where truths are grasped whole rather than constructed through argument."
    },
    236: {
        "brief": "Nature \u2014 the operative principle in all things, whose hidden workings (*magia naturalis*) the Renaissance magus sought to harness.",
        "long": "Natura (Latin: 'nature') designates both the totality of the created world and the immanent principle of growth and change within each thing. Renaissance natural magic (*magia naturalis*) defined itself as the art of working with nature's hidden sympathies and antipathies rather than against them. The boundary between 'natural' and 'supernatural' operations was the most contested distinction in Renaissance magical philosophy: what the magus called natural, the inquisitor might call demonic."
    },
    223: {
        "brief": "Form \u2014 the organizing principle that gives matter its identity and properties in Aristotelian-Scholastic metaphysics.",
        "long": "Forma (Latin: 'form') designates the essential organizing principle that determines what a thing is, as distinct from its *materia* (matter). In Renaissance magical philosophy, the question of whether occult properties inhere in a thing's substantial form or are impressed from without (by celestial influences) was central to debates about the mechanism of natural magic. Ficino's *spiritus mundi* theory proposed that celestial forms could be drawn down into material objects through sympathetic correspondences."
    },
    222: {
        "brief": "Matter \u2014 the passive substrate that receives form in Aristotelian metaphysics; the starting point of alchemical transformation.",
        "long": "Materia (Latin: 'matter') designates the passive, formless substrate that receives *forma* to become a determinate thing. In alchemical philosophy, *materia* intersects with *prima materia* (the primal undifferentiated substance) as the starting point from which the alchemist works. The relationship between *materia* and *forma* \u2014 how form can be imposed on resistant matter \u2014 is the central metaphysical problem of both alchemy and natural magic."
    },
    221: {
        "brief": "Body \u2014 the material, extended substance in which spirit and soul are housed.",
        "long": "Corpus (Latin: 'body') designates the material, extended component of any composite being. In Ficino's three-part anthropology (*corpus*-*spiritus*-*anima*), the body is the densest level, connected to the soul through the intermediary of *spiritus* (spirit). The alchemical and magical traditions treat the body not as inert matter but as a locus of occult properties and sympathetic connections to celestial bodies."
    },
    229: {
        "brief": "Plato's cosmological dialogue \u2014 the foundational text for Renaissance magical cosmology.",
        "long": "The Timaeus is Plato's cosmological dialogue describing the demiurge's fashioning of the world-soul (*anima mundi*) and the ensouled, mathematically structured cosmos. For Renaissance magical philosophy, it was the single most influential ancient text after the *Corpus Hermeticum*, providing the framework of a living universe governed by mathematical harmonies and accessible to human manipulation through knowledge of its structural principles."
    },
    228: {
        "brief": "Ficino's Three Books on Life \u2014 the key text applying Neoplatonic cosmology to astrological medicine and natural magic.",
        "long": "De Vita (Latin: 'On Life'), fully *De Vita Libri Tres* (1489), is Marsilio Ficino's practical guide to health, longevity, and celestial influence. Book III, *De Vita Coelitus Comparanda* ('On Obtaining Life from the Heavens'), is the most important Renaissance text on natural magic, carefully describing how to draw down planetary influences through talismans, music, fragrances, and colors while maintaining that these operations work through natural *spiritus* rather than demonic invocation."
    },

    # KEY PHILOSOPHICAL terms
    226: {
        "brief": "Coincidence of opposites \u2014 Nicholas of Cusa's doctrine that contradictions are unified in the infinite God.",
        "long": "Coincidentia oppositorum (Latin: 'coincidence of opposites') is Nicholas of Cusa's central philosophical doctrine, articulated in *De Docta Ignorantia* (1440). It holds that the infinite God transcends all finite distinctions: in God, maximum and minimum, unity and plurality, being and non-being coincide. The doctrine influenced Pico's syncretic ambitions and Bruno's radical cosmology, providing philosophical license for reconciling apparently incompatible traditions."
    },

    # ALCHEMICAL process terms
    85: {
        "brief": "First matter \u2014 the primal undifferentiated substance from which all materials derive and to which the alchemist reduces them.",
        "long": "Prima materia (Latin: 'first matter') designates the original, undifferentiated substance posited in both Aristotelian physics and alchemical philosophy as the substrate underlying all material forms. The alchemist's first task is to reduce a substance to its *prima materia* \u2014 stripping away its accidental forms \u2014 before rebuilding it toward perfection. The identity of the *prima materia* was the central secret of alchemy: variously identified with mercury, lead, antimony, or a philosophical substance accessible only through symbolic understanding."
    },
    86: {
        "brief": "The philosopher's stone \u2014 the ultimate goal of the alchemical *opus*, capable of transmuting base metals into gold and conferring longevity.",
        "long": "Lapis philosophorum (Latin: 'philosopher's stone') designates the perfected substance produced by the alchemical *opus magnum*, believed capable of transmuting base metals into gold (*chrysopoeia*) and extending human life (*elixir vitae*). Whether understood literally or allegorically, the *lapis* represents the endpoint of alchemical transformation \u2014 the union of all opposites in a single perfected substance. Renaissance alchemists debated whether the *lapis* was a physical product, a spiritual achievement, or both simultaneously."
    },
    87: {
        "brief": "The Great Work \u2014 the complete alchemical process from *prima materia* to the *lapis philosophorum*.",
        "long": "Opus magnum (Latin: 'great work') designates the entire alchemical process of purification, dissolution, and reconstitution through which the practitioner transforms base matter into the *lapis philosophorum*. The stages of the *opus* \u2014 *nigredo*, *albedo*, *citrinitas*, *rubedo* \u2014 were understood as both chemical procedures and spiritual transformations of the alchemist."
    },
    88: {
        "brief": "Blackening \u2014 the first stage of the alchemical *opus*, involving putrefaction and dissolution of matter.",
        "long": "Nigredo (Latin: 'blackening') designates the first and darkest stage of the alchemical *opus magnum*, in which the starting material undergoes *putrefactio* (decomposition), turning black. Psychologically interpreted, *nigredo* represents the death of the old self, the confrontation with chaos and dissolution that precedes regeneration. It corresponds to the element earth and the planet Saturn."
    },
    89: {
        "brief": "Whitening \u2014 the second stage of the alchemical *opus*, involving purification after the darkness of *nigredo*.",
        "long": "Albedo (Latin: 'whitening') designates the second stage of the alchemical *opus*, following *nigredo*. The blackened matter is washed and purified until it turns white, signifying the first degree of perfection. Psychologically, *albedo* represents the dawn of new consciousness after the dissolution of *nigredo*. It corresponds to the element water and the Moon."
    },
    90: {
        "brief": "Reddening \u2014 the final stage of the alchemical *opus*, producing the perfected *lapis philosophorum*.",
        "long": "Rubedo (Latin: 'reddening') designates the final stage of the alchemical *opus magnum*, in which the purified white matter is brought to full perfection, turning red. The *rubedo* signifies the completion of the Great Work \u2014 the production of the *lapis philosophorum* or the *tinctura* capable of transmuting base metals into gold. It corresponds to the element fire and the Sun."
    },
    91: {
        "brief": "Yellowing \u2014 an intermediate alchemical stage between *albedo* and *rubedo*, not always distinguished as a separate phase.",
        "long": "Citrinitas (Latin: 'yellowing') designates an intermediate stage in the alchemical *opus* between *albedo* (whitening) and *rubedo* (reddening). Not all alchemical authors recognize *citrinitas* as a distinct phase; some systems move directly from *albedo* to *rubedo*. Where it appears, it represents the dawning of solar consciousness and the element air."
    },
    92: {
        "brief": "Tincture \u2014 the coloring or transformative agent in alchemy, closely related to the *lapis philosophorum*.",
        "long": "Tinctura (Latin: 'tincture') designates the active, coloring principle that the *lapis philosophorum* imparts to base metals to transmute them into gold. The term carries both a literal chemical sense (a dissolved extractive) and a metaphysical sense: the *tinctura* is what transforms, the operative essence of the stone. Some alchemists identified the *tinctura* with the stone itself."
    },
    93: {
        "brief": "A transformative substance in alchemical tradition, believed capable of perfecting matter and extending life.",
        "long": "Elixir (Arabic: 'al-iksir,' from Greek 'xerion,' dry powder) designates a liquid or powder capable of transmuting base metals into gold or conferring longevity. The Arabic alchemical tradition treated the elixir and the philosopher's stone as closely related if not identical concepts. Renaissance alchemists inherited both the term and the ambiguity, sometimes distinguishing the *elixir vitae* (elixir of life) from the *lapis* (transmutative stone)."
    },
    94: {
        "brief": "Water of life \u2014 a distilled essence believed to possess medicinal and transmutative powers.",
        "long": "Aqua vitae (Latin: 'water of life') designates a highly purified distilled spirit, typically alcohol, credited with medicinal and occasionally transmutative properties. In Paracelsian iatrochemistry, *aqua vitae* served as both a solvent and a medicine, bridging the practical and symbolic dimensions of alchemical pharmacy. The term reflects alchemy's persistent equation of purification with life-giving power."
    },
    95: {
        "brief": "Dissolve and coagulate \u2014 the fundamental alchemical axiom describing the rhythm of the *opus magnum*.",
        "long": "Solve et coagula (Latin: 'dissolve and coagulate') is the foundational maxim of alchemical practice, describing the two complementary operations that drive the *opus magnum*: breaking matter down into its components (*solve*) and reassembling them in a more perfect configuration (*coagula*). This rhythmic alternation of destruction and reconstitution governs every stage of the Great Work."
    },
    96: {
        "brief": "Transmutation \u2014 the fundamental alchemical operation of changing one substance into another, especially base metal into gold.",
        "long": "Transmutatio (Latin: 'transmutation') designates the conversion of one substance into another, the defining aspiration of alchemy. Whether transmutation was possible \u2014 and if so, whether it occurred through natural or supernatural means \u2014 was a central controversy in Renaissance natural philosophy. Defenders of alchemy argued that transmutation simply accelerated natural processes; critics contended that substantial forms could not be altered by human art."
    },
    97: {
        "brief": "Putrefaction \u2014 the controlled decomposition of matter that initiates the alchemical *nigredo*.",
        "long": "Putrefactio (Latin: 'putrefaction') designates the controlled decomposition of the starting material in the alchemical vessel, the operation that produces the *nigredo* (blackening). Alchemists understood *putrefactio* as a necessary death: the old form must be dissolved before a new and more perfect one can emerge. The parallel with agricultural composting and with Christian death-and-resurrection theology was frequently drawn."
    },
    98: {
        "brief": "Sublimation \u2014 the alchemical operation of purifying a substance by heating it to vapor and collecting the condensate.",
        "long": "Sublimatio (Latin: 'sublimation') designates the alchemical operation in which a solid is heated until it vaporizes, then collected as a purified condensate. Both a practical chemical technique and a symbolic operation, *sublimatio* represents the elevation of gross matter to a more refined state \u2014 the ascent from earthly density to aerial subtlety."
    },
    99: {
        "brief": "Calcination \u2014 the alchemical operation of reducing a substance to powder through intense heat.",
        "long": "Calcinatio (Latin: 'calcination') designates the reduction of a substance to powder or ash through intense, prolonged heating. As the first destructive operation of the *opus*, *calcinatio* represents the burning away of impurities and the reduction of complex matter to its simplest components. It is associated with the element fire and with the initial purificatory phase of the Great Work."
    },
    100: {
        "brief": "Mercury \u2014 both the liquid metal and one of the three alchemical principles (tria prima) representing volatility and spirit.",
        "long": "Mercurius (Latin: 'mercury') designates both the physical liquid metal (quicksilver) and one of the three Paracelsian principles (*tria prima*) alongside *sulphur* and *sal*. As an alchemical principle, *mercurius* represents the volatile, spiritual, and feminine aspect of matter. The identification of philosophical mercury with the physical metal was a persistent source of confusion that alchemical authors exploited for both practical and initiatory purposes."
    },
    101: {
        "brief": "Sulphur \u2014 both the mineral element and one of the three alchemical principles representing combustibility and soul.",
        "long": "Sulphur (Latin: 'sulphur') designates both the physical mineral and one of the three Paracelsian principles (*tria prima*) alongside *mercurius* and *sal*. As an alchemical principle, *sulphur* represents the combustible, active, and masculine aspect of matter \u2014 the principle of fixity and color. The sulphur-mercury theory of metals (predating Paracelsus) held that all metals are composed of varying proportions and purities of these two principles."
    },
    102: {
        "brief": "Coagulation \u2014 the alchemical operation of solidifying a dissolved or volatile substance.",
        "long": "Coagulatio (Latin: 'coagulation') designates the solidification of a previously dissolved or volatile substance, the complement of *solutio* (dissolution). In the rhythmic pattern of *solve et coagula*, *coagulatio* represents the reconstitution of matter in a more perfect form after purification through dissolution."
    },
    103: {
        "brief": "Distillation \u2014 the alchemical operation of purifying a liquid by vaporization and condensation.",
        "long": "Distillatio (Latin: 'distillation') designates the separation and purification of a liquid by heating it to vapor and collecting the condensate. One of the most practical alchemical operations, *distillatio* was used to produce *aqua vitae*, essential oils, and mineral acids. Symbolically, it represents the extraction of the subtle essence from gross matter."
    },
    104: {
        "brief": "Fermentation \u2014 the alchemical operation of enlivening purified matter through the introduction of a transformative agent.",
        "long": "Fermentatio (Latin: 'fermentation') designates the stage of the alchemical *opus* in which the purified white matter is enlivened by the addition of a 'ferment' or 'seed' \u2014 a small quantity of gold (for the red work) or silver (for the white work) that initiates the final transformation. Metaphorically, *fermentatio* represents the infusion of life into purified but inert matter."
    },
    105: {
        "brief": "Multiplication \u2014 the alchemical operation of increasing the quantity or potency of the *lapis philosophorum*.",
        "long": "Multiplicatio (Latin: 'multiplication') designates the process by which the completed *lapis philosophorum* is increased in quantity or potency, enabling it to transmute ever-larger quantities of base metal. *Multiplicatio* and *projectio* together represent the final, triumphant stages of the Great Work after the *lapis* has been achieved."
    },
    106: {
        "brief": "Projection \u2014 the final alchemical operation of casting the *lapis* onto base metal to effect transmutation.",
        "long": "Projectio (Latin: 'projection') designates the climactic moment of the alchemical *opus*: casting a small quantity of the completed *lapis philosophorum* onto molten base metal to transmute it into gold. As the last operation of the Great Work, *projectio* represents the proof and fulfillment of the entire alchemical process."
    },
    107: {
        "brief": "Separation \u2014 the alchemical operation of dividing a substance into its constituent parts.",
        "long": "Separatio (Latin: 'separation') designates the division of a composite substance into its pure components \u2014 extracting the subtle from the gross, the fixed from the volatile. One of the most fundamental alchemical operations, *separatio* enacts the principle that purification requires analysis: the mixture must be broken down before its elements can be individually perfected and recombined."
    },
    108: {
        "brief": "Conjunction \u2014 the alchemical union of previously separated principles, often symbolized as a marriage.",
        "long": "Conjunctio (Latin: 'conjunction' or 'union') designates the alchemical reunification of previously separated principles \u2014 typically sulphur and mercury, or king and queen in the symbolic language of the tradition. The *coniunctio* is frequently depicted as a *hieros gamos* (sacred marriage) and represents the reconciliation of opposites that produces the *lapis philosophorum*."
    },
    109: {
        "brief": "Mortification \u2014 the alchemical killing or destruction of a substance's existing form to prepare it for transformation.",
        "long": "Mortificatio (Latin: 'mortification' or 'killing') designates the symbolic death of the starting material in the alchemical vessel, closely related to *putrefactio* and *nigredo*. The substance must 'die' \u2014 lose its existing form \u2014 before it can be resurrected in a perfected state. The parallel with Christian soteriology was explicitly cultivated in alchemical literature."
    },
    110: {
        "brief": "Fixation \u2014 the alchemical operation of rendering a volatile substance stable and resistant to heat.",
        "long": "Fixatio (Latin: 'fixation') designates the process of rendering a volatile substance stable and permanent, so that it no longer evaporates under heat. In alchemical symbolism, *fixatio* represents the stabilization of spirit in matter \u2014 the grounding of the volatile and mercurial in a fixed and enduring form."
    },
    111: {
        "brief": "Drinkable gold \u2014 a liquid preparation of gold believed to possess healing and life-extending properties.",
        "long": "Aurum potabile (Latin: 'drinkable gold') designates a liquid gold preparation believed to possess extraordinary medicinal and life-extending properties. The concept bridges alchemy and Paracelsian medicine: if gold is the most perfect metal, then gold rendered consumable should confer its perfection on the human body. Whether *aurum potabile* was a colloidal suspension, a gold salt solution, or a purely symbolic concept remains debated."
    },
    112: {
        "brief": "Royal water \u2014 a mixture of acids capable of dissolving gold, the 'king of metals.'",
        "long": "Aqua regia (Latin: 'royal water') designates the mixture of nitric and hydrochloric acids capable of dissolving gold \u2014 the only common solvent that can attack the 'king of metals.' Its ability to dissolve what resists all other agents made *aqua regia* both a practical laboratory reagent and a potent alchemical symbol of the power to reduce even the most perfect substance to its *prima materia*."
    },
    113: {
        "brief": "A corrosive sulfate compound used in alchemical operations and encoded in the famous acrostic V.I.T.R.I.O.L.",
        "long": "Vitriol (Latin: 'vitriolum') designates various metal sulfate compounds, especially iron sulfate (green vitriol) and copper sulfate (blue vitriol), widely used in alchemical operations. The word was famously reinterpreted as an acrostic: 'Visita Interiora Terrae, Rectificando Invenies Occultum Lapidem' ('Visit the interior of the earth; by rectifying you will find the hidden stone') \u2014 encoding the alchemical imperative to descend into matter to discover the *lapis*."
    },
    114: {
        "brief": "A slow-burning alchemical furnace designed to maintain constant heat over extended operations.",
        "long": "Athanor (Arabic: 'al-tannur,' furnace) designates the principal alchemical furnace, designed to maintain a constant, moderate heat over the extended periods required by the *opus magnum*. The *athanor* was sometimes called the 'philosophical furnace' or the 'tower furnace,' and its ability to sustain steady warmth without constant tending made it a symbol of patient, self-regulating transformation."
    },
    115: {
        "brief": "Natural philosophy \u2014 the study of nature through reason and observation, the broader intellectual framework within which Renaissance magic claimed legitimacy.",
        "long": "Philosophia naturalis (Latin: 'natural philosophy') designates the systematic study of the natural world through reason and observation \u2014 the ancestor of modern science. Renaissance magi consistently claimed the status of *philosophi naturales* rather than sorcerers, insisting that their operations worked through natural causes (occult properties, celestial influences, sympathies) rather than demonic pacts. The boundary between *philosophia naturalis* and forbidden *magia* was the most consequential jurisdictional dispute in Renaissance intellectual life."
    },
    116: {
        "brief": "The stone \u2014 shorthand for the *lapis philosophorum*, the philosopher's stone.",
        "long": "Lapis (Latin: 'stone') is the abbreviated form of *lapis philosophorum* (philosopher's stone), used throughout alchemical literature as shorthand for the ultimate product of the Great Work. The identification of the *lapis* with Christ, with the self, or with a physical transmutative substance generated a rich tradition of multilevel interpretation."
    },
    269: {
        "brief": "Fifth essence \u2014 the refined celestial substance beyond the four elements, sought by alchemists as a universal medicine.",
        "long": "Quinta essentia (Latin: 'fifth essence' or 'quintessence') designates the refined substance beyond the four terrestrial elements (earth, water, air, fire), identified in Aristotelian cosmology with the material of the celestial spheres. Paracelsian and Lullian alchemists sought to extract the *quinta essentia* from terrestrial substances through repeated distillation, producing a universal medicine or perfect solvent. The concept bridges cosmology and pharmacy."
    },
    261: {
        "brief": "Union of opposites \u2014 the alchemical reconciliation of contrary principles, closely related to *coincidentia oppositorum*.",
        "long": "Coniunctio oppositorum (Latin: 'union of opposites') designates the alchemical reconciliation of contrary principles \u2014 masculine and feminine, fixed and volatile, sulphur and mercury \u2014 into a unified, perfected substance. The concept parallels Nicholas of Cusa's *coincidentia oppositorum* at the philosophical level, and the *hieros gamos* (sacred marriage) at the symbolic level."
    },

    # MAGICAL terms
    180: {
        "brief": "A magical seal or inscribed symbol believed to capture and direct spiritual forces.",
        "long": "Sigillum (Latin: 'seal') designates an inscribed symbol, typically combining geometric figures, divine names, and astrological correspondences, believed to capture and direct spiritual or celestial forces. Dee's *Sigillum Dei Aemeth* ('Seal of God's Truth') is the most elaborate example in this corpus \u2014 a complex wax disk inscribed with angelic names and planetary symbols, used as the foundation for the scrying table in the Enochian system."
    },
    187: {
        "brief": "A manual of ceremonial magic containing instructions for ritual invocation, talisman construction, and spirit communication.",
        "long": "Grimoire (French: 'grammar' or 'book of magic') designates a manual of ceremonial magic providing systematic instructions for ritual invocation, talisman construction, spirit summoning, and related operations. The grimoire tradition represents the practical, operative dimension of magic \u2014 the 'how-to' literature that Renaissance intellectuals like Agrippa sought to organize within a philosophical framework while distancing themselves from its more disreputable practitioners."
    },
    189: {
        "brief": "The combinatory art \u2014 Ramon Llull's system for generating all possible propositions, adapted by Bruno into a magical memory technique.",
        "long": "Ars combinatoria (Latin: 'combinatory art') designates the systematic method of combining fundamental concepts to generate all possible truths, originating with Ramon Llull's *Ars Magna* (1305). Llull designed the system as a missionary tool; Bruno transformed it into a Hermetic memory art in which combinatory operations on magical images simultaneously explore the cosmos and transform the practitioner's consciousness."
    },
    167: {
        "brief": "Divine frenzy \u2014 the Platonic doctrine of inspired madness through which poets, prophets, and lovers access divine truth.",
        "long": "Furor divinus (Latin: 'divine frenzy') designates the Platonic doctrine, elaborated by Ficino, that certain forms of madness are divine gifts rather than pathologies: poetic frenzy (from the Muses), prophetic frenzy (from Apollo), ritual frenzy (from Dionysus), and erotic frenzy (from Venus/Aphrodite). Ficino's treatment of *furor divinus* in his commentary on Plato's Phaedrus made it a central concept in Renaissance aesthetics and a philosophical justification for the inspired, visionary dimension of magical practice."
    },
}

updated = 0
for term_id, d in defs.items():
    conn.execute("""UPDATE dictionary_terms SET
        definition_brief=?, definition_long=?,
        source_method='LLM_ASSISTED', confidence='MEDIUM', review_status='DRAFT',
        updated_at=datetime('now')
    WHERE id=?""", (d["brief"], d["long"], term_id))
    if conn.execute("SELECT changes()").fetchone()[0] > 0:
        updated += 1

conn.commit()
total_def = conn.execute("SELECT COUNT(*) FROM dictionary_terms WHERE definition_brief IS NOT NULL AND definition_brief NOT LIKE '[GENERIC%'").fetchone()[0]
print(f"Definitions added: {updated}")
print(f"Total defined: {total_def}/186")
conn.close()
