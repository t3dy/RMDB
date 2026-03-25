"""Insert event descriptions for all 40 timeline events missing descriptions."""
import io, sqlite3, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

DB = "db/renmagic.db"
conn = sqlite3.connect(DB)

descs = {
    27: "Plotinus, the founder of Neoplatonism, was born in Lycopolis, Egypt. His metaphysical system of the One, Intellect, and Soul would become the philosophical architecture of Renaissance magical thought.",
    31: "Iamblichus was born in Chalcis, Syria. His defense of theurgy against purely contemplative ascent provided the theoretical basis for Renaissance ceremonial magic.",
    28: "Plotinus died in Campania. His Enneads, compiled by Porphyry, would wait over a millennium for Ficino to translate them into Latin.",
    32: "Iamblichus died. His De Mysteriis established the principle that the soul requires ritual mediation through material symbols to reach the divine.",
    29: "Proclus was born in Constantinople. The last great systematic Neoplatonist, his hierarchical theology influenced Ficino and provided resources for Kabbalistic-Neoplatonic synthesis.",
    30: "Proclus died in Athens, the last head of the Platonic Academy before Justinian closed it in 529.",
    33: "Al-Kindi was born in Kufa, Iraq. His De Radiis Stellarum theorized universal radiation as the mechanism of astrological influence, profoundly shaping Latin magical theory.",
    34: "Al-Kindi died in Baghdad. His ray theory would reach the Latin West through translation and inform Ficino\u2019s natural magic, though the Arabic source was rarely acknowledged.",
    37: "Albertus Magnus was born in Lauingen, Bavaria. His Speculum Astronomiae would provide the most influential medieval framework for distinguishing licit from illicit magic.",
    39: "Roger Bacon was born in Ilchester, England. His advocacy of scientia experimentalis alongside natural magic anticipated the empirical dimension of Renaissance philosophy.",
    23: "Ramon Llull was born in Palma de Mallorca. His combinatory Ars Magna would be transformed by Bruno into a Hermetic memory system.",
    38: "Albertus Magnus died in Cologne. His taxonomy of acceptable and condemnable magical practices framed how Renaissance magi argued for their own legitimacy.",
    40: "Roger Bacon died in Oxford. His discussions of the power of words and mathematical figures influenced later magical thought.",
    24: "Ramon Llull died in Tunis, reportedly stoned by a crowd while on a missionary journey. His Art survived to become one of the most creatively repurposed intellectual systems in Renaissance philosophy.",
    35: "Nicholas of Cusa was born in Kues, Germany. His doctrine of learned ignorance and coincidence of opposites influenced both Pico and Bruno.",
    9: "Marsilio Ficino was born in Figline Valdarno, near Florence. Under Medici patronage, he would translate the Corpus Hermeticum, Plato, and Plotinus, creating the intellectual infrastructure for Renaissance magical philosophy.",
    13: "Johannes Reuchlin was born in Pforzheim, Germany. He would become the most accomplished Christian Hebraist of his generation and a founder of Christian Cabala.",
    11: "Johannes Trithemius was born in Trittenheim, Germany. As abbot of Sponheim, he would produce the Steganographia \u2014 a work that embeds genuine cryptography within an angelic magical framework.",
    3: "Giovanni Pico della Mirandola was born in Mirandola, Italy. His 900 Conclusions and Oration on the Dignity of Man would become defining documents of Renaissance syncretic philosophy.",
    36: "Nicholas of Cusa died in Todi, Italy. His philosophical legacy flowed into the Renaissance through both Ficino (who read him) and Bruno (who radicalized him).",
    7: "Heinrich Cornelius Agrippa was born in Cologne. His De Occulta Philosophia would provide the most comprehensive Renaissance synthesis of magical philosophy.",
    25: "Paracelsus was born in Einsiedeln, Switzerland. His chemical medicine and doctrine of the tria prima reframed alchemy as a medical art.",
    4: "Giovanni Pico della Mirandola died in Florence at thirty-one, possibly poisoned. He left unfinished his massive attack on judicial astrology.",
    10: "Marsilio Ficino died in Florence. He had made Plato, Plotinus, and Hermes Trismegistus available to the Latin West and established the philosophical framework within which all subsequent Renaissance magic operated.",
    12: "Johannes Trithemius died at the monastery of St. James in Wurzburg. His Polygraphia, the first printed book on cryptography, was published posthumously two years later.",
    14: "Johannes Reuchlin died in Stuttgart. His defense of Jewish books and his Kabbalistic treatises had made Christian Cabala a respectable intellectual enterprise.",
    1: "John Dee was born in Tower Ward, London. He would become Elizabeth I\u2019s court philosopher, owner of one of Europe\u2019s largest private libraries, and the inventor of the Enochian angelic system.",
    8: "Heinrich Cornelius Agrippa died in Grenoble, impoverished and under suspicion of heresy. His De Occulta Philosophia would remain the standard reference for ceremonial magic for over a century.",
    26: "Paracelsus died in Salzburg. His chemical philosophy and insistence on experiential knowledge over textual authority continued to generate controversy and followers for generations.",
    5: "Giordano Bruno was born in Nola, near Naples. He would push the Hermetic philosophical project further than any Renaissance thinker \u2014 and pay for it with his life.",
    15: "Robert Fludd was born in Bearsted, Kent. His encyclopedic Utriusque Cosmi Historia would produce the most visually ambitious maps of macrocosm-microcosm correspondence in Renaissance philosophy.",
    19: "Jacob Boehme was born in Alt-Seidenberg, Saxony. A cobbler with no formal education, he would produce a theosophical system of extraordinary originality.",
    6: "Giordano Bruno was burned at the stake in Rome\u2019s Campo de\u2019 Fiori for heresy. His execution effectively ended open Hermetic philosophy in Catholic Europe.",
    17: "Athanasius Kircher was born in Geisa, Germany. As a Jesuit polymath at the Collegium Romanum, he would attempt to domesticate Hermeticism within Catholic institutional frameworks.",
    2: "John Dee died in Mortlake, impoverished and stripped of his library. His angel diaries would be published posthumously by Meric Casaubon in 1659.",
    21: "Francis Mercury van Helmont was born. Son of the chemist Jan Baptist van Helmont, he would collaborate on the Kabbala Denudata and advocate for the transmigration of souls.",
    20: "Jacob Boehme died in Goerlitz. His theosophical writings would influence German Idealism, English Romanticism, and Western esotericism for centuries.",
    16: "Robert Fludd died in London. His elaborate cosmological diagrams and Rosicrucian philosophy carried Renaissance Hermeticism into the seventeenth century.",
    18: "Athanasius Kircher died in Rome. His attempt to decipher Egyptian hieroglyphics was wrong, but his encyclopedic ambition preserved and transmitted Hermetic ideas within Jesuit scholarship.",
    22: "Francis Mercury van Helmont died. His Kabbalistic universalism and advocacy of metempsychosis (gilgul) had bridged Renaissance Christian Cabala and Enlightenment philosophy.",
}

updated = 0
for eid, desc in descs.items():
    conn.execute(
        "UPDATE timeline_events SET description=?, source_method='LLM_ASSISTED', confidence='MEDIUM', review_status='DRAFT', updated_at=datetime('now') WHERE id=?",
        (desc, eid),
    )
    if conn.execute("SELECT changes()").fetchone()[0] > 0:
        updated += 1

conn.commit()
total = conn.execute("SELECT COUNT(*) FROM timeline_events WHERE description IS NOT NULL").fetchone()[0]
print(f"Event descriptions updated: {updated}")
print(f"Total with description: {total}/58")
conn.close()
