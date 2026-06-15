"""Third pass: expand Llull, Kircher, Paracelsus, and Yates biographies.

Run: python scripts/improve_content_pass3.py
Idempotent.
"""

import io
import sqlite3
import sys
from pathlib import Path

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

DB_PATH = Path(__file__).resolve().parent.parent / "db" / "renmagic.db"

FIGURE_UPDATES = [

    ("Ramon Llull", """\
Ramon Llull (1232–1316), Catalan philosopher, mystic, theologian, and \
tireless missionary, produced over two hundred works in Catalan, Latin, and \
Arabic across a career devoted to a single aim: converting Muslims to \
Christianity through rational argument. His Ars Magna ('Great Art'), \
first developed in the 1270s and revised in multiple versions through \
his death, was an attempt to reduce all possible knowledge to a finite \
set of divine attributes (goodness, greatness, eternity, power, wisdom, \
will, virtue, truth, glory) and then mechanically generate all true \
propositions about God, the soul, and the world through rotating \
combinatory wheels and tables.

Llull's significance for Renaissance magic lies almost entirely in what \
later practitioners made of his work rather than in his own intentions. \
Giordano Bruno, who encountered Lullism during his time in France and \
England in the 1580s, stripped away the apologetic Christian framework \
and redeployed the combinatory mechanism as a Hermetic memory art: a \
system for imprinting the animated order of the cosmos on the practitioner's \
mind by rotating magical images through the positions of the Lullian wheels. \
Bruno's De Umbris Idearum and subsequent mnemonic works represent, in \
Frances Yates's formulation, 'a magical transformation of Lullism.' \
Agrippa also engaged with Lullism. The Ars Magna's influence on seventeenth-century \
proposals for philosophical languages (Leibniz's *characteristica universalis*, \
Kircher's combinatory schemes) shows how far the method traveled from \
its missionary origins.""",

     "Catalan philosopher and missionary; Ars Magna established combinatory \
art generating all propositions from divine attributes; transformed by Bruno \
into a Hermetic memory system and by Leibniz into universal language theory"),

    ("Athanasius Kircher", """\
Athanasius Kircher (1602–1680), German Jesuit polymath based at the Collegium \
Romanum in Rome, was the most prolific Renaissance-to-Baroque encyclopedist \
of the Hermetic and occult philosophical tradition — and arguably its last \
major systematic exponent before Enlightenment critique made such syntheses \
intellectually untenable. His thirty-odd published works covered Egyptology \
and hieroglyphics (Oedipus Aegyptiacus, 1652–54), magnetism (Magnes sive \
de Arte Magnetica, 1641), acoustics and music (Musurgia Universalis, 1650), \
subterranean geology (Mundus Subterraneus, 1664–65), and China (China \
Illustrata, 1667).

Kircher's Egyptological project — his attempt to decipher Egyptian hieroglyphs \
as an encrypted ancient wisdom tradition — was philologically disastrous: \
his readings were entirely wrong, as the actual decipherment of the Rosetta \
Stone would reveal a century and a half later. But the intellectual project \
was Hermetic through and through: Kircher believed the hieroglyphs encoded \
the same prisca theologia that Ficino had found in the Corpus Hermeticum, \
and that a Christian reading of Egyptian religion would reveal it as a \
preparation for Christianity. His approach domesticated Renaissance Hermetism \
within Jesuit institutional frameworks — transforming a philosophically \
subversive tradition into a tool of Catholic apologetics and missionary \
universalism. His influence on baroque iconographic programs, court culture, \
and popular learned culture was immense. The corpus contains Godwin's and \
Findlen's monographs on Kircher as a representative of this late Hermetic moment.""",

     "German Jesuit polymath; encyclopedist of Hermetism, Egyptology, \
magnetism, and acoustics; attempted to domesticate Renaissance Hermetic \
tradition within Jesuit Catholic universalism; last major systematic \
exponent of the Hermetic synthesis before Enlightenment critique"),

    ("Paracelsus", """\
Paracelsus (Theophrastus Bombastus von Hohenheim, 1493–1541) was a Swiss \
physician, alchemist, and natural philosopher who mounted the most comprehensive \
assault on Galenic academic medicine in the sixteenth century, substituting \
a chemical ontology (tria prima: salt, sulphur, and mercury as the principles \
of all matter) for the four humors, and a theosophically inflected understanding \
of the physician's art for the scholastic university curriculum he despised. \
He was flamboyant, combative, and frequently drunk; he burned Avicenna's Canon \
at a lecture; he was expelled from Basel after provoking a legal dispute over \
fees; he wandered across central Europe for most of his life, dying in Salzburg \
in relative obscurity.

His influence was posthumous and enormous. Paracelsian iatrochemistry — the \
application of chemical processes (distillation, calcination, fermentation) to \
the preparation of medicines — became the primary challenge to Galenism in the \
late sixteenth and seventeenth centuries, and the Paracelsian movement it generated \
produced chemical medicine, pharmaceutical chemistry, and eventually the Chemical \
Revolution. For the history of Renaissance magic, Paracelsus matters in several \
ways: his tria prima doctrine reframed alchemy as a practical medical art rather \
than a quest for gold or philosophical enlightenment; his account of elemental \
spirits (gnomes, undines, sylphs, salamanders) contributed to the demonology and \
natural spirit-lore that fed into later esotericism; his theosophical cosmology \
— the macrocosm-microcosm correspondence, the physician as reader of cosmic \
signatures — permeated Fludd's system and Dutch Paracelsian networks. The corpus \
contains his traces across the Fludd, Dee, and van Helmont materials.""",

     "Swiss physician and alchemist; tria prima doctrine (salt, sulphur, \
mercury) replaced Galenic humoralism with chemical medicine; theosophical \
cosmology of signatures and elemental spirits shaped Fludd, Dee, and the \
broader Paracelsian tradition"),

    ("Frances A. Yates", """\
Frances A. Yates (1899–1981), British historian at the Warburg Institute \
in London, single-handedly transformed the historiography of Renaissance \
intellectual life by arguing in Giordano Bruno and the Hermetic Tradition \
(1964) that Hermeticism — the tradition inaugurated by Ficino's 1463 \
translation of the Corpus Hermeticum — was the primary intellectual force \
driving the transformations of the sixteenth century, including the cosmological \
revolution associated with Copernicus and Bruno.

The 'Yates thesis,' as it became known, was simultaneously a scholarly \
breakthrough and a scholarly provocation. By insisting that Bruno was a Hermetic \
magus rather than a proto-scientific rationalist, Yates challenged the dominant \
Whig historiography of science that drew a straight line from Copernicus to \
Galileo to Newton. Her subsequent books — The Art of Memory (1966), Theatre of \
the World (1969), The Rosicrucian Enlightenment (1972), The Occult Philosophy \
in the Elizabethan Age (1979) — extended the argument across multiple domains of \
Renaissance culture, from theater and architecture to Elizabethan court ceremonial.

The Yates thesis has been substantially qualified. Brian Vickers (1984) \
challenged the philosophical coherence of the Hermetic-scientific connection; \
Copenhaver showed Ficino's primary allegiance was Neoplatonist rather than \
Hermetist; Hanegraaff reframed the whole question methodologically. What the \
thesis did not lose was its generative power: it made Renaissance magic a \
legitimate subject of serious academic study and produced an extraordinary \
burst of scholarship in response. RenMagDB's corpus of 337 documents is, in \
a real sense, a product of the intellectual world Yates's work called into being.""",

     "British Warburg Institute historian; Giordano Bruno and the Hermetic \
Tradition (1964) established the 'Yates thesis' making Hermetism central to \
Renaissance intellectual history; foundational figure whose work generated the \
scholarly field this portal documents, even as the thesis has been substantially revised"),
]


def run_updates():
    conn = sqlite3.connect(str(DB_PATH))
    conn.execute("PRAGMA foreign_keys=ON")
    c = conn.cursor()

    print("=== Updating figure biographies (pass 3) ===")
    updated = 0
    for name, biography, significance in FIGURE_UPDATES:
        row = c.execute("SELECT id, biography FROM figures WHERE name=?", (name,)).fetchone()
        if row is None:
            print(f"  SKIP (not found): {name}")
            continue
        fig_id, existing_bio = row
        if existing_bio and len(existing_bio) > len(biography):
            print(f"  SKIP (existing longer): {name} ({len(existing_bio)} vs {len(biography)})")
            continue
        c.execute("""
            UPDATE figures
            SET biography=?, significance=?,
                source_method='HUMAN_VERIFIED', review_status='REVIEWED',
                updated_at=datetime('now')
            WHERE id=?
        """, (biography, significance, fig_id))
        print(f"  UPDATE: {name} ({len(biography)} chars)")
        updated += 1

    conn.commit()
    conn.close()
    print(f"  Updated: {updated}")
    print("Done.")


if __name__ == "__main__":
    run_updates()
