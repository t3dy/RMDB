# RenMagDB — Renaissance Magic Database

A digital humanities project cataloging a research corpus of 337 scholarly documents on Renaissance magic — covering figures from Marsilio Ficino to John Dee, traditions from Hermeticism to Kabbalah, and texts from the *Corpus Hermeticum* to the Enochian *Calls*.

**Live site:** [https://t3dy.github.io/RMDB/](https://t3dy.github.io/RMDB/)

## What's In the Database

| Content | Count |
|---------|-------|
| Scholarly documents cataloged | 337 |
| Historical figures + modern scholars | 29 |
| Dictionary terms (Latin/Greek/Hebrew/Arabic) | 139 defined |
| Timeline events | 58 |
| Referenced primary sources | 36 |
| Intellectual traditions | 9 |

## Architecture

SQLite → Python scripts → static HTML → GitHub Pages

No frameworks, no build tools, no JavaScript frameworks. Vanilla HTML/CSS/JS with warm parchment palette.

## Key Features

- **Dictionary** of Renaissance magic terminology with definitions, cross-references, and domain classification
- **Figure biographies** for 22 historical practitioners and 7 modern scholars
- **Timeline** spanning from Plato through the 2006 *Dictionary of Gnosis*
- **Library** of 36 referenced primary sources from ancient through Renaissance periods
- **Full corpus catalog** with searchable document metadata

## Methodology

The database was built using a Python-first pipeline:
1. Documents converted to markdown via PyMuPDF
2. Metadata extracted via regex and spaCy NER
3. Terms detected via a 200-term seed list with KWIC concordance
4. Topic clusters generated via TF-IDF
5. AI-generated content (definitions, biographies) tagged as DRAFT pending human review

For the scholarly framing, see the project essay "Magic as a Scholarly Category: From Yates to Copenhaver" (`RMESSAY1.md`).

## Built With

Python 3.14 | SQLite | PyMuPDF | spaCy | scikit-learn | Claude Code
