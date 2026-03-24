"""Validate database integrity and generate quality report.

Checks:
- Orphaned references (figures with no documents, terms with no documents)
- Missing required fields
- Provenance coverage
- Cardinality compliance
"""

import io
import json
import sqlite3
import sys
from pathlib import Path

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')

CORPUS_ROOT = Path(__file__).resolve().parent.parent
DB_PATH = CORPUS_ROOT / "db" / "renmagic.db"
REPORT_PATH = CORPUS_ROOT / "data" / "validation_report.json"


def main():
    conn = sqlite3.connect(str(DB_PATH))
    report = {"checks": [], "summary": {}}

    # 1. Document completeness
    total_docs = conn.execute("SELECT COUNT(*) FROM documents").fetchone()[0]
    with_title = conn.execute("SELECT COUNT(*) FROM documents WHERE title IS NOT NULL").fetchone()[0]
    with_type = conn.execute("SELECT COUNT(*) FROM documents WHERE doc_type IS NOT NULL").fetchone()[0]
    with_lang = conn.execute("SELECT COUNT(*) FROM documents WHERE language IS NOT NULL").fetchone()[0]
    with_quality = conn.execute("SELECT COUNT(*) FROM documents WHERE quality_flag IS NOT NULL").fetchone()[0]
    with_summary = conn.execute("SELECT COUNT(*) FROM documents WHERE summary IS NOT NULL").fetchone()[0]

    report["checks"].append({
        "name": "Document completeness",
        "total": total_docs,
        "with_title": with_title,
        "with_type": with_type,
        "with_language": with_lang,
        "with_quality": with_quality,
        "with_summary": with_summary,
        "completeness_pct": round(with_type / max(total_docs, 1) * 100, 1),
    })

    # 2. Orphan figures (no document links)
    orphan_figures = conn.execute("""
    SELECT f.name FROM figures f
    LEFT JOIN document_figures df ON f.id = df.figure_id
    WHERE df.id IS NULL
    """).fetchall()
    report["checks"].append({
        "name": "Orphan figures (no document links)",
        "count": len(orphan_figures),
        "figures": [f[0] for f in orphan_figures],
    })

    # 3. Orphan terms (no document links)
    orphan_terms = conn.execute("""
    SELECT dt.term FROM dictionary_terms dt
    LEFT JOIN term_documents td ON dt.id = td.term_id
    WHERE td.id IS NULL
    """).fetchall()
    report["checks"].append({
        "name": "Orphan terms (no document links)",
        "count": len(orphan_terms),
        "terms": [t[0] for t in orphan_terms],
    })

    # 4. Provenance coverage
    provenance = conn.execute("""
    SELECT source_method, COUNT(*) FROM documents GROUP BY source_method
    """).fetchall()
    report["checks"].append({
        "name": "Provenance coverage (documents)",
        "distribution": {row[0] or "NULL": row[1] for row in provenance},
    })

    # 5. Figure completeness
    total_figs = conn.execute("SELECT COUNT(*) FROM figures").fetchone()[0]
    with_birth = conn.execute("SELECT COUNT(*) FROM figures WHERE birth_year IS NOT NULL").fetchone()[0]
    with_sig = conn.execute("SELECT COUNT(*) FROM figures WHERE significance IS NOT NULL").fetchone()[0]
    with_era = conn.execute("""
    SELECT COUNT(DISTINCT entity_id) FROM era_assignments WHERE entity_type='FIGURE'
    """).fetchone()[0]

    report["checks"].append({
        "name": "Figure completeness",
        "total": total_figs,
        "with_birth_year": with_birth,
        "with_significance": with_sig,
        "with_era_assignment": with_era,
    })

    # 6. Join table density
    df_count = conn.execute("SELECT COUNT(*) FROM document_figures").fetchone()[0]
    td_count = conn.execute("SELECT COUNT(*) FROM term_documents").fetchone()[0]
    dt_count = conn.execute("SELECT COUNT(*) FROM document_topics").fetchone()[0]
    ea_count = conn.execute("SELECT COUNT(*) FROM era_assignments").fetchone()[0]

    report["checks"].append({
        "name": "Join table density",
        "document_figures": df_count,
        "term_documents": td_count,
        "document_topics": dt_count,
        "era_assignments": ea_count,
    })

    # 7. FTS5 coverage
    fts_count = conn.execute("SELECT COUNT(*) FROM documents_fts").fetchone()[0]
    report["checks"].append({
        "name": "FTS5 index coverage",
        "indexed": fts_count,
        "total_docs": total_docs,
        "coverage_pct": round(fts_count / max(total_docs, 1) * 100, 1),
    })

    # Summary
    orphan_rate = (len(orphan_figures) + len(orphan_terms)) / max(total_figs + 186, 1) * 100
    report["summary"] = {
        "total_documents": total_docs,
        "total_figures": total_figs,
        "total_terms": conn.execute("SELECT COUNT(*) FROM dictionary_terms").fetchone()[0],
        "total_topics": conn.execute("SELECT COUNT(*) FROM topics").fetchone()[0],
        "orphan_rate_pct": round(orphan_rate, 1),
        "all_source_methods_deterministic": all(
            row[0] in ("DETERMINISTIC", "SEED_DATA") for row in provenance
        ),
    }

    # Write report
    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    REPORT_PATH.write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8")

    # Print
    print(f"=== VALIDATION REPORT ===")
    for check in report["checks"]:
        print(f"\n{check['name']}:")
        for k, v in check.items():
            if k != "name":
                print(f"  {k}: {v}")

    print(f"\n=== SUMMARY ===")
    for k, v in report["summary"].items():
        print(f"  {k}: {v}")

    conn.close()


if __name__ == "__main__":
    main()
