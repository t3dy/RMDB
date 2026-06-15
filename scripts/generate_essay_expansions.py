#!/usr/bin/env python3
"""
Generate 500-1000 word conceptual essays for 30 priority RenMagDB dictionary terms.

Priority selection: Most important terms from existing database, focusing on:
- Core magical terminology (magia naturalis, daemon, theurgia)
- Philosophical foundations (emanatio, nous, intellectus)
- Kabbalistic concepts (kabbalah, sephiroth, zohar)
- Astrological operations (electio, aspectus, dignitates)
- Operative practices (imago, invocatio, characteres)
- Hermetic texts (corpus hermeticum, prisca theologia)
- Late developments (Dee's systems: enochian, claves angelicae)
"""

import json
import sys
import io

# Force UTF-8 output
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

# Load existing definitions
with open('C:\\Dev\\renaissance magic\\data\\definitions.json', 'r', encoding='utf-8') as f:
    existing_defs = json.load(f)

# Create term lookup
term_lookup = {entry['term']: entry for entry in existing_defs}

# 30 PRIORITY TERMS from existing database
PRIORITY_TERMS = [
    # CORE MAGICAL TERMINOLOGY (8)
    "magia naturalis",
    "daemon",
    "theurgia",
    "goetia",
    "sympatheia",
    "imago",
    "characteres",
    "incantatio",

    # PHILOSOPHICAL FOUNDATIONS (8)
    "emanatio",
    "nous",
    "intellectus",
    "causa",
    "essentia",
    "potentia",
    "participatio",
    "scala naturae",

    # KABBALISTIC CONCEPTS (7)
    "kabbalah",
    "sephiroth",
    "zohar",
    "ain soph",
    "sefer yetzirah",
    "nefesh",
    "tikkun",

    # HERMETIC TEXTS & CONCEPTS (5)
    "corpus hermeticum",
    "hermetica",
    "prisca theologia",
    "tabula smaragdina",
    "anima mundi",

    # ASTROLOGICAL OPERATIONS (3 from remaining slots)
    "electio",
    "aspectus",
    "dignitas",
]

print(f"Processing {len(PRIORITY_TERMS)} priority terms for essay expansion...\n")

essays = []
for term in PRIORITY_TERMS:
    if term in term_lookup:
        entry = term_lookup[term]

        essay = {
            "term": term,
            "language": entry.get("language", "Latin"),
            "category_type": "ACTOR_TERM" if term in [
                "magia naturalis", "daemon", "theurgia", "sympatheia", "imago",
                "characteres", "incantatio", "emanatio", "causa", "essentia",
                "potentia", "electio", "aspectus", "dignitas"
            ] else "ANALYST_TERM",
            "brief_definition": entry.get("definition_brief", ""),
            "existing_long_definition": entry.get("definition_long", ""),
            "sections_to_expand": [
                "Etymology & Origins",
                "Renaissance Usage & Practice",
                "Modern Scholarly Interpretation",
                "Related Conceptual Terms",
                "Key Historical Figures",
                "Historiographic Debates",
                "Corpus Evidence"
            ],
            "corpus_citations": entry.get("corpus_citations", []),
            "ready_for_publication": False
        }
        essays.append(essay)

# Output structure ready for Claude expansion
output = {
    "project": "RenMagDB",
    "phase": "v2 Dictionary Enrichment",
    "task": "Expand 30 priority terms to 500-1000 word conceptual essays",
    "terms_selected": len(essays),
    "total_target_words": f"{len(essays) * 750} (750 avg × {len(essays)} terms)",
    "essay_structure": {
        "heading_1": "Etymology & Origins — What does the word mean? Ancient/medieval origins?",
        "heading_2": "Renaissance Usage & Practice — How did Renaissance figures use this term? Quotes?",
        "heading_3": "Modern Scholarly Interpretation — How do contemporary scholars use this term?",
        "heading_4": "Related Conceptual Terms — Cross-references to other concepts",
        "heading_5": "Key Historical Figures — Who engaged this concept?",
        "heading_6": "Historiographic Debates — Is this category contested? (Yates vs Copenhaver?)",
        "heading_7": "Corpus Evidence — 3-5 specific references to database documents"
    },
    "quality_checklist": [
        "Actor/analyst distinction clearly marked",
        "Multiple primary source quotations",
        "Citations to major secondary works (Yates, Copenhaver, Walker, etc.)",
        "Clear connections to related terms",
        "500-1000 words per essay",
        "Museum-curator scholarly voice maintained",
        "All claims tied to corpus evidence"
    ],
    "dictionary_entries": essays
}

# Pretty print as JSON
print(json.dumps(output, indent=2, ensure_ascii=False))

sys.stderr.write(f"\n\n=== READY FOR EXPANSION ===\n")
sys.stderr.write(f"Selected {len(essays)} terms from {len(existing_defs)} existing entries.\n")
sys.stderr.write(f"Target: 7,500 words minimum (500-1000 × 30 terms)\n")
sys.stderr.write(f"\nNext step: Pass this JSON to Claude with expansion prompt.\n")
