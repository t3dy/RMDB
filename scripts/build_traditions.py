"""Build tradition taxonomy from term domain aggregation.

Aggregates dictionary_terms by domain to derive tradition labels.
Updates the topics table with tradition-quality names.
"""

import io
import sqlite3
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

from pathlib import Path
CORPUS_ROOT = Path(__file__).resolve().parent.parent
DB_PATH = CORPUS_ROOT / "db" / "renmagic.db"

# Domain -> tradition mapping with descriptions
DOMAIN_TRADITIONS = {
    "ALCHEMICAL": ("Alchemy", "The art and science of transmutation, encompassing both laboratory practice (chrysopoeia) and spiritual purification. Renaissance alchemists drew on Arabic, Greek, and medieval Latin sources to develop a symbolic system linking material transformation to cosmic and spiritual processes."),
    "HERMETIC": ("Hermeticism", "The philosophical and magical tradition attributed to Hermes Trismegistus, transmitted through the Corpus Hermeticum, Asclepius, and related texts. Ficino's 1463 Latin translation established Hermeticism as a prisca theologia — an ancient wisdom predating and prefiguring Christianity."),
    "KABBALISTIC": ("Kabbalah & Christian Cabala", "Jewish mystical tradition based on the Zohar, Sefer Yetzirah, and related texts, adapted by Christian scholars (Pico, Reuchlin) into a syncretic system integrating Hebrew letter-mysticism with Neoplatonic and Christian theology."),
    "NEOPLATONIC": ("Neoplatonism", "The philosophical tradition descending from Plotinus through Proclus and Iamblichus, providing the metaphysical framework (the One, Intellect, Soul, Matter) within which Renaissance magical philosophy operated. Ficino's translations and commentaries made Neoplatonism the dominant philosophical language of Renaissance magic."),
    "MAGICAL": ("Ritual & Ceremonial Magic", "The practical tradition of invoking spiritual beings, constructing talismans, and performing ceremonial operations. Encompasses natural magic (magia naturalis), angel magic, the Ars Notoria, and grimoire traditions. Agrippa's De Occulta Philosophia is the foundational Renaissance synthesis."),
    "ASTROLOGICAL": ("Astrology & Celestial Influence", "The system of celestial correspondences linking planetary movements to terrestrial events and human character. Renaissance magi used astrology both as a diagnostic tool and as the theoretical basis for timing magical operations and constructing talismans."),
    "THEOLOGICAL": ("Christian Theology & Magic", "The theological dimension of Renaissance magic, including debates over the legitimacy of magical practice, the doctrine of divine names, angelic hierarchies, and the relationship between theurgy and prayer. The tension between magic and orthodoxy drives much of the corpus."),
    "ENOCHIAN": ("Enochian & Angelic Communication", "The system of angel magic developed by John Dee and Edward Kelley through scrying sessions (1581-1589), producing the Enochian language, the Sigillum Dei Aemeth, and the Heptarchic system. Unique to Dee's circle but influential on later Western esotericism."),
    "PHILOSOPHICAL": ("Renaissance Philosophy (General)", "Broad philosophical concepts (form, matter, intellect, nature, being) that underpin all Renaissance magical traditions. These terms derive from Aristotelian and Neoplatonic sources and are used across every domain in the corpus."),
}


def main():
    conn = sqlite3.connect(str(DB_PATH))

    # Get domain stats
    domains = conn.execute("""
        SELECT domain, COUNT(*) as term_count, SUM(frequency) as total_freq
        FROM dictionary_terms
        GROUP BY domain ORDER BY total_freq DESC
    """).fetchall()

    # Clear old TF-IDF topic names and replace with tradition names
    # Keep TF-IDF topics for document_topics links, but add tradition topics
    added = 0
    for domain, term_count, total_freq in domains:
        if domain not in DOMAIN_TRADITIONS:
            continue
        name, description = DOMAIN_TRADITIONS[domain]
        conn.execute("""
        INSERT OR IGNORE INTO topics (name, description)
        VALUES (?, ?)
        """, (name, f"{description} [{term_count} terms, {total_freq} corpus occurrences]"))
        added += 1

    conn.commit()

    total = conn.execute("SELECT COUNT(*) FROM topics").fetchone()[0]
    print(f"=== TRADITION TAXONOMY ===")
    print(f"Traditions added: {added}")
    print(f"Total topics in DB: {total}")
    print(f"\nTraditions by corpus evidence:")
    for domain, term_count, total_freq in domains:
        if domain in DOMAIN_TRADITIONS:
            name = DOMAIN_TRADITIONS[domain][0]
            print(f"  {name}: {term_count} terms, {total_freq:,} corpus occurrences")

    conn.close()


if __name__ == "__main__":
    main()
