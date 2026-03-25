"""Standardize biography citations to (Surname, Short Title) format."""
import io, sqlite3, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

DB = "db/renmagic.db"
conn = sqlite3.connect(DB)

# Citation fixes: old pattern -> new pattern
# Only fixing biographies that have surname-only citations
fixes = {
    "Athanasius Kircher": {
        "(Godwin; Findlen)": "(Godwin, Athanasius Kircher; Findlen, Athanasius Kircher)"
    },
    "Francis Mercury van Helmont": {
        "(Coudert)": "(Coudert, Impact of the Kabbalah)"
    },
    "Giordano Bruno": {
        "(Gatti; Rowland; Blum)": "(Gatti, Giordano Bruno; Rowland, Giordano Bruno; Blum, Giordano Bruno)"
    },
    "Heinrich Cornelius Agrippa": {
        "(Newman; Lehrich; Perrone Compagni)": "(Newman, Thomas Vaughan as Interpreter; Lehrich, Language of Demons; Perrone Compagni, De Occulta Philosophia)"
    },
    "Jacob Boehme": {
        "(Weeks; Stoudt)": "(Weeks, Boehme; Stoudt, Sunrise to Eternity)"
    },
    "Johannes Reuchlin": {
        "(Zika; Copenhaver)": "(Zika, Reuchlin and Erasmus; Copenhaver, Renaissance Philosophy)"
    },
    "Johannes Trithemius": {
        "(Brann; Arnold)": "(Brann, Trithemius; Arnold, Johannes Trithemius)"
    },
    "John Dee": {
        "(Clulee; Harkness; Sz\u00f6nyi)": "(Clulee, John Dee's Natural Philosophy; Harkness, John Dee's Conversations; Sz\u00f6nyi, John Dee's Occultism)"
    },
    "Hermes Trismegistus": {
        "(Copenhaver; Yates, Bruno and the Hermetic Tradition)": "(Copenhaver, Hermetica; Yates, Bruno and the Hermetic Tradition)"
    },
}

updated = 0
for name, replacements in fixes.items():
    row = conn.execute("SELECT id, biography FROM figures WHERE name=?", (name,)).fetchone()
    if not row:
        print(f"NOT FOUND: {name}")
        continue
    fig_id, bio = row
    changed = False
    for old, new in replacements.items():
        if old in bio:
            bio = bio.replace(old, new)
            changed = True
            print(f"  {name}: {old} -> {new}")
    if changed:
        conn.execute("UPDATE figures SET biography=?, updated_at=datetime('now') WHERE id=?", (bio, fig_id))
        updated += 1

conn.commit()
print(f"\nCitation fixes applied: {updated} biographies updated")
conn.close()
