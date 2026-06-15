#!/usr/bin/env python3
"""
Expand 30 priority dictionary terms into 500-1000 word conceptual essays.
Output: JSON with full essays + word counts + publication readiness flags.

PRIORITY TERMS (30 most important):
ACTOR TERMS (what Renaissance figures called their work):
- magia naturalis, occult qualities, sympathia, correspondentia, celestial influence, temperament
- prisca theologia, pia sapientia, ars, ars combinatoria, philosophia naturalis
- essentia, forma, materia, causa, potentia

ANALYST TERMS (what modern scholars call it):
- hermeticism, esotericism, occult philosophy, neoplatonism
- kabbalah, alchemy, astrology, theurgy, goeteia

CROSSCUTTING CONCEPTS:
- microcosm-macrocosm, reception history, intellectus agens, emanation
"""

import json
import sys
import io

# Force UTF-8 output
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

# Load existing definitions from data/definitions.json
with open('C:\\Dev\\renaissance magic\\data\\definitions.json', 'r', encoding='utf-8') as f:
    existing_defs = json.load(f)

# Map existing terms to their data for reference
term_map = {entry['term']: entry for entry in existing_defs}

# 30 PRIORITY TERMS for essay expansion
PRIORITY_TERMS = [
    # ACTOR TERMS (what Renaissance figures called their work)
    "magia naturalis",
    "occult qualities",
    "sympathia",
    "correspondentia",
    "celestial influence",
    "temperament",
    "prisca theologia",
    "pia sapientia",
    "ars",
    "ars combinatoria",
    "philosophia naturalis",
    "essentia",
    "forma",
    "materia",
    "causa",
    "potentia",
    # ANALYST TERMS
    "hermeticism",
    "esotericism",
    "occult philosophy",
    "neoplatonism",
    "kabbalah",
    "alchemy",
    "astrology",
    "theurgy",
    "goeteia",
    # CROSSCUTTING CONCEPTS
    "microcosm-macrocosm",
    "reception history",
    "intellectus agens",
    "emanation",
    "daemon",
]

# Build essay data structure
essays = []

for term in PRIORITY_TERMS:
    # Check if term exists in current definitions
    if term.lower() in [t['term'].lower() for t in existing_defs]:
        existing = next((e for e in existing_defs if e['term'].lower() == term.lower()), None)

        # Build expanded essay entry
        essay_entry = {
            "term": term,
            "language": existing.get("language", "Latin"),
            "category_type": "ACTOR_TERM" if term in [
                "magia naturalis", "occult qualities", "sympathia", "correspondentia",
                "celestial influence", "temperament", "prisca theologia", "pia sapientia",
                "ars", "ars combinatoria", "philosophia naturalis", "essentia", "forma",
                "materia", "causa", "potentia"
            ] else "ANALYST_TERM",
            "brief_definition": existing.get("definition_brief", ""),
            "sections": [
                {
                    "heading": "Etymology & Origins",
                    "content": f"[To be expanded from existing definition] {existing.get('definition_brief', '')}"
                },
                {
                    "heading": "Renaissance Usage",
                    "content": f"[Renaissance context from {existing.get('definition_long', '')[:150]}...]"
                },
                {
                    "heading": "Modern Scholarly Usage",
                    "content": "[Modern interpretation and scholarly framework]"
                },
                {
                    "heading": "Related Terms",
                    "content": "[Cross-references to other concepts in the database]"
                },
                {
                    "heading": "Key Figures",
                    "content": "[Figures who engaged with this concept]"
                },
                {
                    "heading": "Historiographic Note",
                    "content": "[Is this category contested? Yates vs Copenhaver?]"
                },
                {
                    "heading": "Corpus Citations",
                    "content": "[3-5 specific references to database documents]"
                }
            ],
            "word_count": 0,  # To be filled during generation
            "corpus_citations": existing.get("corpus_citations", []),
            "ready_for_publication": False
        }
        essays.append(essay_entry)
    else:
        print(f"WARNING: Term not found in existing definitions: {term}", file=sys.stderr)

# Output schema for verification
output = {
    "project": "RenMagDB",
    "task": "Dictionary Essay Expansion",
    "target_count": 30,
    "terms_found": len(essays),
    "total_word_count": 0,
    "status": "STRUCTURE_READY",
    "instructions": "Expand each section according to JOECHIPV2RMDB.md guidelines. Each essay should be 500-1000 words with clear actor/analyst distinction.",
    "dictionary_entries": essays
}

print(json.dumps(output, indent=2, ensure_ascii=False))
