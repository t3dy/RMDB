"""Validate all artifact JSON files against their schemas and the artifact contract.

Usage:
  python scripts/validate_artifacts.py                    # validate all fixtures
  python scripts/validate_artifacts.py --all              # validate fixtures + generated/
  python scripts/validate_artifacts.py --file PATH        # validate a single file
  python scripts/validate_artifacts.py --fixtures         # validate fixtures only (default)

Exit codes:
  0 — all artifacts valid
  1 — one or more schema errors or contract violations
  2 — usage error

Requires: pip install jsonschema>=4.0.0
"""

import io
import json
import sys
from pathlib import Path

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8", errors="replace")

# Locate repo root relative to this script's location.
REPO_ROOT = Path(__file__).resolve().parent.parent
ARTIFACTS_DIR = REPO_ROOT / "artifacts"
FIXTURES_DIR = ARTIFACTS_DIR / "fixtures"
GENERATED_DIR = ARTIFACTS_DIR / "generated"

# Add scripts/ to path so we can import artifact_pipeline.
sys.path.insert(0, str(REPO_ROOT / "scripts"))
from artifact_pipeline import (  # noqa: E402
    ARTIFACT_TYPES,
    validate_artifact,
    load_artifact,
)


def find_artifact_files(*dirs: Path) -> list[Path]:
    paths = []
    for d in dirs:
        if d.exists():
            paths.extend(sorted(d.rglob("*.json")))
    return paths


def validate_file(path: Path) -> tuple[bool, dict]:
    try:
        data = load_artifact(path)
    except json.JSONDecodeError as e:
        return False, {"schema_errors": [f"JSON parse error: {e}"], "contract_violations": [], "warnings": []}
    result = validate_artifact(data)
    return result["valid"], result


def check_id_uniqueness(paths: list[Path]) -> list[str]:
    """Return a list of duplicate artifact_id errors."""
    seen: dict[str, Path] = {}
    duplicates: list[str] = []
    for path in paths:
        try:
            data = load_artifact(path)
        except Exception:
            continue
        artifact_id = data.get("artifact_id")
        if artifact_id:
            if artifact_id in seen:
                duplicates.append(
                    f"DUPLICATE artifact_id '{artifact_id}': {seen[artifact_id]} and {path}"
                )
            else:
                seen[artifact_id] = path
    return duplicates


def check_unknown_artifact_types(paths: list[Path]) -> list[str]:
    errors = []
    for path in paths:
        try:
            data = load_artifact(path)
        except Exception:
            continue
        atype = data.get("artifact_type")
        if atype and atype not in ARTIFACT_TYPES:
            errors.append(f"UNKNOWN artifact_type '{atype}' in {path}")
    return errors


def run_validation(paths: list[Path]) -> bool:
    """Run all validation checks. Returns True if all pass."""
    print(f"\n{'='*60}")
    print(f"RenMagDB Artifact Validation")
    print(f"{'='*60}")
    print(f"Checking {len(paths)} artifact file(s)...\n")

    all_pass = True
    results_summary = []

    # ── Per-file validation ──
    for path in paths:
        valid, result = validate_file(path)
        rel = path.relative_to(REPO_ROOT) if path.is_relative_to(REPO_ROOT) else path
        status = "PASS" if valid else "FAIL"
        if not valid:
            all_pass = False

        results_summary.append((rel, status, result))

        if not valid or result.get("warnings"):
            print(f"[{status}] {rel}")
            for err in result.get("schema_errors", []):
                print(f"       SCHEMA:    {err}")
            for viol in result.get("contract_violations", []):
                print(f"       CONTRACT:  {viol}")
            for warn in result.get("warnings", []):
                print(f"       WARNING:   {warn}")
            print()

    # ── Cross-file checks ──
    dup_errors = check_id_uniqueness(paths)
    type_errors = check_unknown_artifact_types(paths)

    if dup_errors or type_errors:
        all_pass = False
        print("Cross-file checks:")
        for err in dup_errors + type_errors:
            print(f"  FAIL: {err}")
        print()

    # ── Summary ──
    passed = sum(1 for _, s, _ in results_summary if s == "PASS")
    failed = len(results_summary) - passed
    print(f"{'='*60}")
    print(f"Results: {passed} passed, {failed} failed out of {len(results_summary)} files")
    if dup_errors:
        print(f"         {len(dup_errors)} duplicate artifact_id error(s)")
    if type_errors:
        print(f"         {len(type_errors)} unknown artifact_type error(s)")

    if all_pass:
        print("\nAll artifacts valid.")
    else:
        print("\nValidation FAILED. See errors above.")
    print(f"{'='*60}\n")

    return all_pass


def main(argv: list[str]) -> int:
    mode = "fixtures"
    single_path = None

    i = 0
    while i < len(argv):
        arg = argv[i]
        if arg == "--all":
            mode = "all"
        elif arg == "--fixtures":
            mode = "fixtures"
        elif arg == "--file":
            mode = "file"
            i += 1
            if i >= len(argv):
                print("Error: --file requires a path argument", file=sys.stderr)
                return 2
            single_path = Path(argv[i])
        elif arg in ("-h", "--help"):
            print(__doc__)
            return 0
        i += 1

    if mode == "file":
        if not single_path or not single_path.exists():
            print(f"Error: file not found: {single_path}", file=sys.stderr)
            return 2
        paths = [single_path]
    elif mode == "fixtures":
        paths = find_artifact_files(FIXTURES_DIR)
        if not paths:
            print(f"No fixture files found in {FIXTURES_DIR}")
            return 0
    else:  # all
        paths = find_artifact_files(FIXTURES_DIR, GENERATED_DIR)
        if not paths:
            print(f"No artifact files found in {ARTIFACTS_DIR}")
            return 0

    ok = run_validation(paths)
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
