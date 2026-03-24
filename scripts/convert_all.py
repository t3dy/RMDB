"""Orchestrator: run all conversion scripts in sequence.

Usage:
    python scripts/convert_all.py              # Convert entire corpus
    python scripts/convert_all.py Ficino       # Convert one folder only
"""

import subprocess
import sys
import json
from pathlib import Path


CORPUS_ROOT = Path(__file__).resolve().parent.parent
SCRIPTS_DIR = CORPUS_ROOT / "scripts"
MANIFEST_PATH = CORPUS_ROOT / "data" / "conversion_manifest.json"


def run_script(script_name: str, args: list = None):
    cmd = [sys.executable, str(SCRIPTS_DIR / script_name)]
    if args:
        cmd.extend(args)
    print(f"\n{'='*60}")
    print(f"Running: {' '.join(cmd)}")
    print(f"{'='*60}")
    result = subprocess.run(cmd, cwd=str(CORPUS_ROOT))
    return result.returncode


def main():
    args = sys.argv[1:] if len(sys.argv) > 1 else []

    # Run each converter
    for script in ["convert_pdf.py", "convert_epub.py", "convert_html.py"]:
        rc = run_script(script, args)
        if rc != 0:
            print(f"\nWARNING: {script} exited with code {rc}")

    # Print combined summary
    if MANIFEST_PATH.exists():
        manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
        flags = {}
        formats = {}
        for e in manifest:
            flags[e["quality_flag"]] = flags.get(e["quality_flag"], 0) + 1
            formats[e["format"]] = formats.get(e["format"], 0) + 1

        print(f"\n{'='*60}")
        print(f"COMBINED CONVERSION MANIFEST")
        print(f"{'='*60}")
        print(f"Total files: {len(manifest)}")
        print(f"\nBy format:")
        for fmt, count in sorted(formats.items()):
            print(f"  {fmt}: {count}")
        print(f"\nBy quality:")
        for flag, count in sorted(flags.items()):
            print(f"  {flag}: {count}")
    else:
        print("\nNo manifest found.")


if __name__ == "__main__":
    main()
