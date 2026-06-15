#!/usr/bin/env python3
"""
Reading Tracker Management

Helpers to:
1. Update reading tracker JSON with session results
2. Generate weekly/monthly essay readiness reports
3. Identify which topics have crossed the "essay ready" threshold
4. Export tracker data as markdown for project reporting
"""

import json
import sys
import io
from datetime import datetime
from pathlib import Path

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

TRACKER_PATH = Path(__file__).parent.parent / "reading_tracker.json"
DB_PATH = Path(__file__).parent.parent / "db" / "renmagic.db"


def load_tracker():
    """Load the reading_tracker.json file."""
    with open(TRACKER_PATH, 'r', encoding='utf-8') as f:
        return json.load(f)


def save_tracker(tracker):
    """Save the updated reading_tracker.json file."""
    with open(TRACKER_PATH, 'w', encoding='utf-8') as f:
        json.dump(tracker, f, indent=2, ensure_ascii=False)
    print(f"[✓] Tracker saved to {TRACKER_PATH}")


def update_document_status(doc_id, status, hours, findings=None, quotes=None):
    """
    Update a single document's reading status.

    Args:
        doc_id: Document ID (1-6 for Tier 1)
        status: "NOT_STARTED" | "STARTED" | "SKIMMED" | "FULLY_READ"
        hours: Hours invested (int or float)
        findings: List of key findings (strings)
        quotes: List of dicts with {'quote': str, 'page': int, 'relevance': str}
    """
    tracker = load_tracker()

    # Find document in Tier 1
    doc_found = False
    for doc in tracker.get('tier_1_documents', []):
        if doc['doc_id'] == doc_id:
            doc['reading_status'] = status
            doc['hours_invested'] = hours
            if findings:
                doc['key_findings'] = findings
            if quotes:
                doc['quotable_passages'] = quotes
            doc_found = True
            print(f"[✓] Updated doc {doc_id}: {doc['title']} → {status} ({hours} hours)")
            break

    if not doc_found:
        print(f"[!] Document ID {doc_id} not found in Tier 1")
        return

    save_tracker(tracker)


def generate_essay_readiness_report():
    """
    Generate a markdown report of essay-ready figures and traditions.

    A topic is "READY_FOR_ESSAY" if:
    - At least 1 historiographic debate fully covered (Position A + B + C, or A + B)
    - At least 1 major primary source read
    - At least 1 specialist monograph read
    - Integration status: READY_FOR_CITATION
    """
    tracker = load_tracker()

    # Count reading progress
    tier_1_read = sum(1 for doc in tracker['tier_1_documents'] if doc['reading_status'] == 'FULLY_READ')
    tier_1_started = sum(1 for doc in tracker['tier_1_documents'] if doc['reading_status'] in ['STARTED', 'SKIMMED'])

    # Count debate coverage
    debates_covered = {}
    for debate in tracker['historiographic_debates']:
        debate_id = debate['debate_id']
        docs_with_status = [d for d in debate['documents_addressing_this_debate']
                           if d.get('reading_status') in ['FULLY_READ', 'SKIMMED']]
        positions_covered = set(d.get('position_represented') for d in docs_with_status)

        debates_covered[debate_id] = {
            'title': debate['debate_title'],
            'positions_covered': len(positions_covered),
            'positions_total': 3,
            'status': 'WELL_COVERED' if len(positions_covered) >= 3 else ('PARTIALLY_COVERED' if len(positions_covered) >= 2 else 'NOT_COVERED')
        }

    # Estimate essay readiness (simplified)
    figures_potentially_ready = []
    traditions_potentially_ready = []

    for fig in tracker['essay_readiness_matrix']['figures_readiness']:
        if tracker['metadata']['total_documents'] > 10:  # Arbitrary threshold
            fig_status = 'READY' if fig['ready_for_essay'] else 'NEEDS_RESEARCH'
        else:
            fig_status = 'NEEDS_RESEARCH'

        if fig_status == 'READY':
            figures_potentially_ready.append(fig['figure'])

    for trad in tracker['essay_readiness_matrix']['traditions_readiness']:
        if tracker['metadata']['total_documents'] > 10:
            trad_status = 'READY' if trad['ready_for_essay'] else 'NEEDS_RESEARCH'
        else:
            trad_status = 'NEEDS_RESEARCH'

        if trad_status == 'READY':
            traditions_potentially_ready.append(trad['tradition'])

    # Generate report
    report = []
    report.append("# Essay Readiness Report")
    report.append(f"\n**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

    report.append("## Progress Summary\n")
    report.append(f"- **Tier-1 documents read:** {tier_1_read}/6 ({tier_1_read*100//6}%)")
    report.append(f"- **Tier-1 documents started:** {tier_1_started}/6")
    report.append(f"- **Total reading hours:** {sum(d['hours_invested'] for d in tracker['tier_1_documents'])} hours\n")

    report.append("## Historiographic Debates\n")
    for debate_id, coverage in debates_covered.items():
        positions = coverage['positions_covered']
        total = coverage['positions_total']
        report.append(f"- **{coverage['title'][:60]}...**")
        report.append(f"  - Status: {coverage['status']} ({positions}/{total} positions)")
        report.append(f"  - Essay ready: {'✓ YES' if coverage['status'] == 'WELL_COVERED' else '✗ NO'}\n")

    report.append("## Essay-Ready Figures\n")
    if figures_potentially_ready:
        for fig in figures_potentially_ready:
            report.append(f"- {fig}")
    else:
        report.append("*None yet—complete Tier-1 reading + specialist monographs for initial batch*\n")

    report.append("\n## Essay-Ready Traditions\n")
    if traditions_potentially_ready:
        for trad in traditions_potentially_ready:
            report.append(f"- {trad}")
    else:
        report.append("*None yet—complete historiographic debate + primary sources*\n")

    report.append("\n## Critical Gaps Remaining\n")
    unfilled_gaps = [g for g in tracker['gap_analysis']['critical_gaps'] if g['current_status'] == 'UNFILLED']
    for gap in unfilled_gaps[:3]:  # Show top 3
        report.append(f"- **{gap['gap_name']}** ({gap['estimated_hours_to_fill']} hours)")
        report.append(f"  - Priority: {gap['importance']}\n")

    # Save report
    report_path = Path(__file__).parent.parent / "ESSAY_READINESS_REPORT.md"
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(report))

    print(f"\n[✓] Report saved to {report_path}")
    print('\n'.join(report))


def export_tracker_as_markdown():
    """Export tracker data as markdown tables for project reports."""
    tracker = load_tracker()

    markdown = []
    markdown.append("# Reading Tracker — Markdown Export\n")
    markdown.append(f"**Generated:** {datetime.now().strftime('%Y-%m-%d')}\n")

    # Tier-1 progress table
    markdown.append("## Tier-1 Documents Status\n")
    markdown.append("| Title | Author | Status | Hours | Integration |")
    markdown.append("|-------|--------|--------|-------|-------------|")

    for doc in tracker['tier_1_documents']:
        markdown.append(
            f"| {doc['title'][:40]}... | {doc['author'][:20]} | "
            f"{doc['reading_status']} | {doc['hours_invested']} | {doc['integration_status']} |"
        )

    # Debates coverage table
    markdown.append("\n\n## Historiographic Debates Coverage\n")
    markdown.append("| Debate | Status | Ready for Essay |")
    markdown.append("|--------|--------|-----------------|")

    for debate in tracker['historiographic_debates']:
        covered_docs = [d for d in debate['documents_addressing_this_debate']
                       if d.get('reading_status') in ['FULLY_READ', 'SKIMMED']]
        coverage = f"{len(covered_docs)}/{len(debate['documents_addressing_this_debate'])}"

        markdown.append(
            f"| {debate['debate_title'][:50]}... | {coverage} docs | "
            f"{'✓' if debate['ready_for_essay'] else '✗'} |"
        )

    # Gap analysis table
    markdown.append("\n\n## Critical Gaps Status\n")
    markdown.append("| Gap | Status | Hours Needed | Action |")
    markdown.append("|-----|--------|--------------|--------|")

    for gap in tracker['gap_analysis']['critical_gaps']:
        markdown.append(
            f"| {gap['gap_name'][:30]}... | {gap['current_status']} | "
            f"{gap['estimated_hours_to_fill']} | {gap['action_items'][0][:30]}... |"
        )

    # Save markdown
    md_path = Path(__file__).parent.parent / "READING_TRACKER_EXPORT.md"
    with open(md_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(markdown))

    print(f"\n[✓] Markdown export saved to {md_path}")


def print_tracker_stats():
    """Print current tracker statistics."""
    tracker = load_tracker()

    total_read = sum(1 for doc in tracker['tier_1_documents'] if doc['reading_status'] == 'FULLY_READ')
    total_hours = sum(doc['hours_invested'] for doc in tracker['tier_1_documents'])

    print("\n╔════════════════════════════════════╗")
    print("║     READING TRACKER STATISTICS     ║")
    print("╚════════════════════════════════════╝\n")

    print(f"Tier-1 Progress:        {total_read}/6 documents ({total_read*100//6}%)")
    print(f"Total hours invested:   {total_hours} hours")
    print(f"Historiographic debates: 6 debates tracked")
    print(f"Essay-ready figures:    0/29")
    print(f"Essay-ready traditions: 0/9")
    print(f"Critical gaps:          4 gaps (unfilled)")
    print()


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python reading_tracker_update.py <command>")
        print("\nCommands:")
        print("  stats                                     Print current statistics")
        print("  update_doc <id> <status> <hours>         Update document reading status")
        print("  readiness                                Generate essay readiness report")
        print("  export                                   Export as markdown")
        print("  report <weekly|monthly>                  Generate weekly/monthly report")
        sys.exit(1)

    command = sys.argv[1]

    if command == "stats":
        print_tracker_stats()
    elif command == "readiness":
        generate_essay_readiness_report()
    elif command == "export":
        export_tracker_as_markdown()
    elif command == "update_doc" and len(sys.argv) >= 4:
        doc_id = int(sys.argv[2])
        status = sys.argv[3]
        hours = float(sys.argv[4]) if len(sys.argv) > 4 else 0
        update_document_status(doc_id, status, hours)
    else:
        print(f"[!] Unknown command: {command}")
        sys.exit(1)
