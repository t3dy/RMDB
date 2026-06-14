#!/usr/bin/env python3
"""
Comprehensive scholarship corpus reader
Extracts figures, concepts, topics, and practices from Renaissance magic scholarship
"""
import os
import sys
import json
import re
import PyPDF2
from pathlib import Path
from collections import defaultdict

sys.stdout = __import__('io').TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

def extract_text_with_context(pdf_path, pages=100):
    """Extract text from PDF with better handling"""
    try:
        with open(pdf_path, 'rb') as f:
            reader = PyPDF2.PdfReader(f)
            text = []
            for i, page in enumerate(reader.pages[:pages]):
                try:
                    text.append(page.extract_text())
                except:
                    pass
            return '\n'.join(text), min(pages, len(reader.pages))
    except Exception as e:
        print(f"Error reading {pdf_path}: {e}", file=sys.stderr)
        return None, 0

def extract_figures(text):
    """Extract all figure names from text"""
    # Comprehensive list of possible figures
    figures = {
        # Renaissance core
        'Ficino': r'\bFicino\b',
        'Pico': r'\bPico\b|Pico della Mirandola',
        'Agrippa': r'\bAgrippa\b|Cornelius Agrippa',
        'Dee': r'\bDee\b|John Dee',
        'Bruno': r'\bBruno\b|Giordano Bruno',
        'Paracelsus': r'\bParacelsus\b|Theophrastus Bombastus',
        'Trithemius': r'\bTrithemius\b|Johannes Trithemius',
        'Fludd': r'\bFludd\b|Robert Fludd',
        'Böhme': r'\bBöhme\b|Bohme\b|Jacob Böhme',
        'Della Porta': r'\bDella Porta\b|Giovanni Battista Della Porta',
        'Cardano': r'\bCardano\b|Gerolamo Cardano',
        'Kircher': r'\bKircher\b|Athanasius Kircher',
        'Andreae': r'\bAndreae\b|Johann Valentin Andreae',
        'Weigel': r'\bWeigel\b|Valentin Weigel',

        # Medieval foundation
        'Albertus': r'\bAlbertus\b|Albertus Magnus',
        'Aquinas': r'\bAquinas\b|Thomas Aquinas',
        'Roger Bacon': r'\bRoger Bacon\b|Bacon',
        'Aquinas': r'\bAquinas\b',

        # Neoplatonic
        'Plotinus': r'\bPlotinus\b',
        'Porphyry': r'\bPorphyry\b',
        'Iamblichus': r'\bIamblichus\b',
        'Lamblichus': r'\bLamblichus\b',

        # Islamic
        'Al-Ghazali': r'\bAl-Ghazali\b|Ghazali',
        'Al-Kindi': r'\bAl-Kindi\b',
        'Avicenna': r'\bAvicenna\b|Ibn Sina',
        'Ibn Sina': r'\bIbn Sina\b',
        'Jabir': r'\bJabir\b|Geber',

        # Witchcraft/demonology
        'Weyer': r'\bWeyer\b|Johann Weyer',
        'Scot': r'\bReginald Scot\b|Scot\b',
        'Del Rio': r'\bDel Rio\b|Martín del Río',
        'Boguet': r'\bBoguet\b|Henry Boguet',
        'Sprenger': r'\bSprenger\b|Malleus Maleficarum',

        # Later figures
        'Swedenborg': r'\bSwedenborg\b|Emanuel Swedenborg',
        'Van Helmont': r'\bVan Helmont\b|J.B. van Helmont',
        'Khunrath': r'\bKhunrath\b|Heinrich Khunrath',
        'Blavatsky': r'\bBlavatsky\b|Madame Blavatsky',
    }

    found = {}
    for name, pattern in figures.items():
        if re.search(pattern, text, re.IGNORECASE):
            found[name] = True

    return list(found.keys())

def extract_concepts(text):
    """Extract key concepts from text"""
    concepts = {
        # Core magical concepts
        'magia naturalis': r'\bmagia naturalis\b',
        'natural magic': r'\bnatural magic\b',
        'demonic magic': r'\bdemonic magic\b',
        'goeteia': r'\bgoeteia\b',
        'theurgy': r'\btheurgy\b',
        'occult philosophy': r'\boccult philosophy\b',
        'hermetic philosophy': r'\bHermetic\b|hermetic',
        'prisca theologia': r'\bprisca theologia\b',

        # Traditions
        'alchemy': r'\balchemy\b',
        'astrology': r'\bastrology\b',
        'Kabbalah': r'\bKabbalah\b|Qabbalah',
        'Neoplatonism': r'\bNeoplatonism\b|Neoplatonic',
        'witchcraft': r'\bwitchcraft\b',
        'demonology': r'\bdemonology\b|demonic',
        'cryptography': r'\bcryptography\b|steganography',
        'sympathetic magic': r'\bsympathetic magic\b',

        # Specific doctrines/concepts
        'correspondence': r'\bcorrespondence\b',
        'celestial influence': r'\bcelestial influence\b',
        'planetary magic': r'\bplanetary magic\b',
        'talismans': r'\btalismans\b|talisman',
        'divine names': r'\bdivine names\b',
        'Sefirot': r'\bSefirot\b|sephiroth',
        'Hermetic Corpus': r'\bHermetic Corpus\b|Hermetica',
        'macrocosm-microcosm': r'\bmacrocosm\b|\bmicrocosm\b',
        'signature': r'\bsignature\b|signatura rerum',

        # Practices
        'ritual magic': r'\britual magic\b',
        'ceremonial magic': r'\bceremoni\w+ magic\b',
        'spirit invocation': r'\bspirit invocation\b|invoking spirits',
        'angel magic': r'\bangel magic\b|angelic\b',
        'necromancy': r'\bnecromancy\b',
        'divination': r'\bdivination\b',

        # Historical/reception
        'Yates thesis': r'\bYates\b|Yates thesis',
        'Hermetic Tradition': r'\bHermetic Tradition\b',
        'reception history': r'\breception\b',
        'early modern': r'\bearly modern\b',
        'scientific revolution': r'\bscientific revolution\b',
    }

    found = {}
    for name, pattern in concepts.items():
        if re.search(pattern, text, re.IGNORECASE):
            found[name] = True

    return list(found.keys())

# Main execution
print("=" * 70)
print("COMPREHENSIVE SCHOLARSHIP CORPUS ANALYSIS")
print("=" * 70)

corpus_dir = Path('C:/Dev/renaissance magic')
priority_docs = [
    ('Paola Zambelli Astrology and Magic from the Medieval Latin and Islamic World to Renaissance Europe.pdf', 'Zambelli - Astrology & Magic'),
    ('Paola Zambelli White Magic Black Magic in the European Renaissance.pdf', 'Zambelli - White/Black Magic'),
    ('John S Mebane Renaissance Magic and the Return of the Golden Age.pdf', 'Mebane - Renaissance Magic'),
    ('Keith Thomas - Religion and the Decline of Magic Studies in Popular Beliefs in Sixteenth- and Seventeenth-Century England (1973, Penguin Books) - libgen.li (1).pdf', 'Thomas - Religion & Magic'),
]

all_figures = defaultdict(int)
all_concepts = defaultdict(int)
doc_results = {}

for doc_file, doc_label in priority_docs:
    doc_path = corpus_dir / doc_file
    if not doc_path.exists():
        print(f"\n⊘ NOT FOUND: {doc_label}")
        continue

    print(f"\n📖 Reading: {doc_label}")
    text, pages_read = extract_text_with_context(str(doc_path), pages=150)

    if text:
        figures = extract_figures(text)
        concepts = extract_concepts(text)

        doc_results[doc_label] = {
            'figures': figures,
            'concepts': concepts,
            'pages_read': pages_read
        }

        for fig in figures:
            all_figures[fig] += 1
        for concept in concepts:
            all_concepts[concept] += 1

        print(f"  ✓ Pages: {pages_read}")
        print(f"  ✓ Figures found: {len(figures)}")
        print(f"  ✓ Concepts found: {len(concepts)}")
    else:
        print(f"  ✗ Failed to extract text")

print("\n" + "=" * 70)
print("COMPREHENSIVE FINDINGS")
print("=" * 70)

print(f"\nTotal documents analyzed: {len(doc_results)}")
print(f"Unique figures found: {len(all_figures)}")
print(f"Unique concepts found: {len(all_concepts)}")

print("\n🔷 FIGURES BY FREQUENCY:")
for fig, count in sorted(all_figures.items(), key=lambda x: -x[1]):
    status = "✓ WRITTEN" if fig in ['Ficino', 'Dee', 'Pico', 'Agrippa', 'Bruno', 'Paracelsus', 'Trithemius', 'Albertus', 'Fludd', 'Böhme', 'Bohme'] else "❌ UNWRITTEN"
    print(f"  {fig:20} {count} docs  {status}")

print("\n🔶 CONCEPTS BY FREQUENCY:")
for concept, count in sorted(all_concepts.items(), key=lambda x: -x[1])[:25]:
    print(f"  {concept:30} {count} docs")

# Save results
results = {
    'timestamp': '2026-06-14',
    'documents_analyzed': len(doc_results),
    'all_figures': dict(all_figures),
    'all_concepts': dict(all_concepts),
    'document_details': doc_results
}

with open('comprehensive_corpus_analysis.json', 'w', encoding='utf-8') as f:
    json.dump(results, f, indent=2, ensure_ascii=False)

print("\n✓ Results saved to comprehensive_corpus_analysis.json")
