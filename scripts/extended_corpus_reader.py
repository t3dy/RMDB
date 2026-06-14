#!/usr/bin/env python3
"""
Extended corpus reader - process ALL available scholarship documents
"""
import os
import sys
import json
import re
import PyPDF2
from pathlib import Path
from collections import defaultdict

sys.stdout = __import__('io').TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

def extract_pdf_text(pdf_path, max_pages=100):
    """Extract text from PDF"""
    try:
        with open(pdf_path, 'rb') as f:
            reader = PyPDF2.PdfReader(f)
            pages_available = len(reader.pages)
            text_parts = []
            for i in range(min(max_pages, pages_available)):
                try:
                    text_parts.append(reader.pages[i].extract_text())
                except:
                    pass
            return '\n'.join(text_parts), pages_available
    except:
        return None, 0

def find_mentions(text, name_patterns):
    """Find all mentions of items in text"""
    found = {}
    for item_name, patterns in name_patterns.items():
        for pattern in patterns:
            if re.search(pattern, text, re.IGNORECASE):
                found[item_name] = True
                break
    return list(found.keys())

# Define comprehensive lookup
figures_dict = {
    'Ficino': [r'\bFicino\b', r'Marsilio Ficino'],
    'Pico': [r'\bPico\b', r'Giovanni Pico', r'Pico della Mirandola'],
    'Agrippa': [r'\bAgrippa\b', r'Cornelius Agrippa'],
    'Dee': [r'\bJohn Dee\b', r'\bDee\b'],
    'Bruno': [r'\bBruno\b', r'Giordano Bruno'],
    'Paracelsus': [r'\bParacelsus\b', r'Theophrastus'],
    'Trithemius': [r'\bTrithemius\b', r'Johannes Trithemius'],
    'Fludd': [r'\bFludd\b', r'Robert Fludd'],
    'Böhme/Bohme': [r'\bBöhme\b', r'\bBohme\b', r'Jacob Böhme'],
    'Albertus Magnus': [r'\bAlbertus\b', r'Albertus Magnus'],

    'Aquinas': [r'\bAquinas\b', r'Thomas Aquinas'],
    'Roger Bacon': [r'\bRoger Bacon\b', r'Roger Bacon\b'],
    'Reginald Scot': [r'\bReginald Scot\b', r'\bScot\b'],
    'Plotinus': [r'\bPlotinus\b'],
    'Porphyry': [r'\bPorphyry\b'],
    'Iamblichus': [r'\bIamblichus\b'],
    'Avicenna': [r'\bAvicenna\b', r'\bIbn Sina\b'],

    'Martín del Río': [r'\bDel Rio\b', r'del Río'],
    'Johann Weyer': [r'\bWeyer\b'],
    'Della Porta': [r'\bDella Porta\b'],
    'Cardano': [r'\bCardano\b'],
    'Kircher': [r'\bKircher\b'],
    'Andreae': [r'\bAndreae\b'],
    'Van Helmont': [r'\bVan Helmont\b'],
    'Al-Ghazali': [r'\bAl-Ghazali\b', r'\bGhazali\b'],
    'Al-Kindi': [r'\bAl-Kindi\b', r'\bKindi\b'],
    'Jabir': [r'\bJabir\b', r'\bGeber\b'],
}

concepts_dict = {
    'natural magic': [r'\bnatural magic\b', r'\bmagia naturalis\b'],
    'demonic magic': [r'\bdemonic magic\b'],
    'witchcraft': [r'\bwitchcraft\b'],
    'astrology': [r'\bastrology\b'],
    'alchemy': [r'\balchemy\b'],
    'Kabbalah': [r'\bKabbalah\b', r'\bQabbalah\b'],
    'demonology': [r'\bdemonology\b'],
    'theurgy': [r'\btheurgy\b'],
    'Hermeticism': [r'\bHermetic\b'],
    'Neoplatonism': [r'\bNeoplatonism\b', r'\bNeoplatonic\b'],
    'divination': [r'\bdivination\b'],
    'necromancy': [r'\bnecromancy\b'],
    'talisman': [r'\btalismans?\b'],
}

# Process all PDFs in corpus
corpus_dir = Path('C:/Dev/renaissance magic')
pdf_files = list(corpus_dir.glob('*.pdf'))

print(f"Found {len(pdf_files)} PDF documents in corpus")
print("Processing...")

figure_count = defaultdict(int)
concept_count = defaultdict(int)
doc_count = 0
processed_docs = []

for pdf_path in sorted(pdf_files)[:35]:  # Process up to 35 documents
    text, pages = extract_pdf_text(str(pdf_path), max_pages=80)
    if not text:
        continue

    doc_count += 1
    doc_name = pdf_path.name[:50]

    figures_found = find_mentions(text, figures_dict)
    concepts_found = find_mentions(text, concepts_dict)

    for fig in figures_found:
        figure_count[fig] += 1
    for concept in concepts_found:
        concept_count[concept] += 1

    processed_docs.append({
        'name': doc_name,
        'figures': len(figures_found),
        'concepts': len(concepts_found)
    })

    if doc_count % 5 == 0:
        print(f"  [{doc_count}] {doc_name}...")

print(f"\nProcessed {doc_count} documents")

print("\n" + "="*70)
print("FIGURES BY DOCUMENT FREQUENCY:")
print("="*70)
for fig, count in sorted(figure_count.items(), key=lambda x: -x[1])[:30]:
    status = "✓" if count >= 3 else " "
    print(f"  {status} {fig:25} {count:2} documents")

print("\n" + "="*70)
print("CONCEPTS BY DOCUMENT FREQUENCY:")
print("="*70)
for concept, count in sorted(concept_count.items(), key=lambda x: -x[1]):
    status = "✓" if count >= 3 else " "
    print(f"  {status} {concept:25} {count:2} documents")

# Identify what needs to be written
figures_3plus = [f for f, c in figure_count.items() if c >= 3]
concepts_3plus = [c for c, cnt in concept_count.items() if cnt >= 3]

written_figures = {'Ficino', 'Dee', 'Pico', 'Agrippa', 'Bruno', 'Paracelsus', 'Trithemius', 'Albertus Magnus', 'Fludd', 'Böhme/Bohme'}
unwritten_3plus = [f for f in figures_3plus if f not in written_figures]

print("\n" + "="*70)
print("CRITICAL GAPS (Mentioned 3+ times, not yet written):")
print("="*70)
for fig in sorted(unwritten_3plus):
    count = figure_count[fig]
    print(f"  ❌ {fig:25} {count} documents — MUST WRITE")

print("\n" + "="*70)
print("PRIORITY SUMMARY:")
print("="*70)
print(f"Figures mentioned 3+ times: {len(figures_3plus)}")
print(f"  Already written: {len([f for f in figures_3plus if f in written_figures])}")
print(f"  Still needed: {len(unwritten_3plus)} essays")
print(f"\nHighest priority figures to write:")
for i, fig in enumerate(sorted(unwritten_3plus, key=lambda f: -figure_count[f])[:10], 1):
    print(f"  {i}. {fig} ({figure_count[fig]} docs)")

results = {
    'documents_processed': doc_count,
    'figures_mentioned_3plus': [f for f in figures_3plus if f not in written_figures],
    'figure_frequencies': dict(figure_count),
    'concept_frequencies': dict(concept_count)
}

with open('extended_corpus_analysis.json', 'w', encoding='utf-8') as f:
    json.dump(results, f, indent=2, ensure_ascii=False)

print("\n✓ Results saved to extended_corpus_analysis.json")
