#!/usr/bin/env python3
import os
import sys
import json
import PyPDF2
from pathlib import Path
from collections import defaultdict
import re

# Handle text encoding
sys.stdout = __import__('io').TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

def extract_text_from_pdf(pdf_path, max_pages=50):
    """Extract text from first N pages of PDF"""
    text = []
    try:
        with open(pdf_path, 'rb') as f:
            reader = PyPDF2.PdfReader(f)
            for i, page in enumerate(reader.pages[:max_pages]):
                text.append(page.extract_text())
        return '\n'.join(text)
    except Exception as e:
        print(f"Error reading {pdf_path}: {e}", file=sys.stderr)
        return None

def extract_key_figures_and_concepts(text):
    """Extract mentioned figures and concepts from text"""
    if not text:
        return [], []

    # Known Renaissance magic figures
    figures = [
        'Ficino', 'Pico', 'Agrippa', 'Dee', 'Bruno', 'Paracelsus', 'Fludd',
        'Reuchlin', 'Böhme', 'Trithemius', 'Kircher', 'Weigel', 'Della Porta',
        'Bacon', 'Picatrix', 'Hermes', 'Plato', 'Plotinus', 'Iamblichus',
        'Avicenna', 'Al-Ghazali', 'Al-Kindi', 'Ibn Sina', 'Jabir', 'Aquinas',
        'Albertus Magnus', 'Roger Bacon', 'Thomas Aquinas', 'Averroes'
    ]

    # Key concepts
    concepts = [
        'magia naturalis', 'natural magic', 'demonic magic', 'goeteia', 'theurgy',
        'alchemy', 'astrology', 'Kabbalah', 'Hermeticism', 'Neoplatonism',
        'prisca theologia', 'Hermetic Corpus', 'theologia naturalis',
        'correspondence', 'planetary magic', 'demonology', 'divine names',
        'Sefirot', 'astrological magic', 'talismans', 'ritual magic',
        'Renaissance philosophy', 'occult philosophy', 'Islamic magic'
    ]

    found_figures = []
    found_concepts = []

    for figure in figures:
        if re.search(r'\b' + figure + r'\b', text, re.IGNORECASE):
            found_figures.append(figure)

    for concept in concepts:
        if re.search(r'\b' + concept + r'\b', text, re.IGNORECASE):
            found_concepts.append(concept)

    return list(set(found_figures)), list(set(found_concepts))

# Main analysis
corpus_dir = Path('C:/Dev/renaissance magic')
results = {
    'corpus_analysis': {},
    'total_documents': 0,
    'figures_mentioned': defaultdict(int),
    'concepts_mentioned': defaultdict(int)
}

print("Analyzing scholarship corpus...")
print("=" * 60)

# Target high-priority documents
priority_docs = [
    'Frances A Yates Giordano Bruno and the Hermetic Tradition.pdf',
    'Frank Klaassen The Transformations of Magic.pdf',
    'D P Walker Spiritual and Demonic Magic.pdf',
    'Stuart Clark Thinking with Demons.pdf',
    'Wouter J. Hanegraaff (editor) - Dictionary of Gnosis & Western Esotericism (2006, Brill Academic Publishers) - libgen.li.pdf'
]

for doc_name in priority_docs:
    doc_path = corpus_dir / doc_name
    if doc_path.exists():
        print(f"\nAnalyzing: {doc_name[:50]}...")
        text = extract_text_from_pdf(str(doc_path), max_pages=100)

        if text:
            figures, concepts = extract_key_figures_and_concepts(text)
            results['corpus_analysis'][doc_name] = {
                'figures': figures,
                'concepts': concepts,
                'pages_analyzed': 100,
                'text_length': len(text)
            }

            for fig in figures:
                results['figures_mentioned'][fig] += 1
            for concept in concepts:
                results['concepts_mentioned'][concept] += 1

            print(f"  Figures found: {len(figures)}")
            print(f"  Concepts found: {len(concepts)}")

print("\n" + "=" * 60)
print("\nFREQUENCY ANALYSIS:")
print(f"Total documents analyzed: {len(results['corpus_analysis'])}")

print("\nMost frequently mentioned figures:")
for fig, count in sorted(results['figures_mentioned'].items(), key=lambda x: -x[1])[:15]:
    print(f"  {fig}: {count} documents")

print("\nMost frequently mentioned concepts:")
for concept, count in sorted(results['concepts_mentioned'].items(), key=lambda x: -x[1])[:15]:
    print(f"  {concept}: {count} documents")

# Save results
with open('corpus_analysis_results.json', 'w', encoding='utf-8') as f:
    json.dump({
        'analysis': results['corpus_analysis'],
        'figure_frequency': dict(results['figures_mentioned']),
        'concept_frequency': dict(results['concepts_mentioned'])
    }, f, indent=2, ensure_ascii=False)

print("\n✓ Results saved to corpus_analysis_results.json")
