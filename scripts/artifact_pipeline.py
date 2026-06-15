"""Core artifact pipeline module for RenMagDB.

Provides:
  - ARTIFACT_SCHEMA_VERSION: current schema version string
  - ARTIFACT_TYPES: canonical set of valid artifact_type values
  - generate_artifact_id(artifact_type): stable, readable ID generator
  - load_schema(artifact_type): load JSON Schema for an artifact type
  - validate_artifact(artifact_data): validate against schema + contract rules
  - artifact_contract_check(artifact_data): check contract rules beyond schema

All artifacts must include: artifact_id, artifact_type, schema_version,
source_id, generated_at. See docs/ARTIFACT_PIPELINE.md for the full pipeline.
See docs/AGENT_ARTIFACT_RULES.md for which agent may produce each type.
"""

import io
import json
import sys
import uuid
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

try:
    import jsonschema
    HAS_JSONSCHEMA = True
except ImportError:
    HAS_JSONSCHEMA = False

ARTIFACT_SCHEMA_VERSION = "1.0"

ARTIFACT_TYPES = {
    "source_metadata",
    "raw_extraction",
    "validation",
    "ontology_tagging",
    "interpretive",
    "curation",
    "public_prose",
    "text_comparison",
    "scholar_citation",
}

SCHEMAS_DIR = Path(__file__).resolve().parent.parent / "artifacts" / "schemas"

_SCHEMA_CACHE: dict[str, dict] = {}


def generate_artifact_id(artifact_type: str) -> str:
    """Return a readable, unique artifact ID: {type_prefix}_{8-char-uuid}."""
    if artifact_type not in ARTIFACT_TYPES:
        raise ValueError(f"Unknown artifact_type: {artifact_type!r}")
    prefix = artifact_type.replace("_", "-")
    short_uuid = uuid.uuid4().hex[:8]
    return f"{prefix}_{short_uuid}"


def now_iso() -> str:
    """Return current UTC time in ISO 8601 format."""
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def make_artifact_skeleton(artifact_type: str, source_id: str, **extra) -> dict:
    """Return a minimal valid artifact dict with required provenance fields."""
    if artifact_type not in ARTIFACT_TYPES:
        raise ValueError(f"Unknown artifact_type: {artifact_type!r}")
    return {
        "artifact_id": generate_artifact_id(artifact_type),
        "artifact_type": artifact_type,
        "schema_version": ARTIFACT_SCHEMA_VERSION,
        "source_id": source_id,
        "generated_at": now_iso(),
        **extra,
    }


def load_schema(artifact_type: str) -> dict:
    """Load and cache the JSON Schema for the given artifact_type."""
    if artifact_type not in ARTIFACT_TYPES:
        raise ValueError(f"Unknown artifact_type: {artifact_type!r}")
    if artifact_type in _SCHEMA_CACHE:
        return _SCHEMA_CACHE[artifact_type]
    schema_path = SCHEMAS_DIR / f"{artifact_type}.schema.json"
    if not schema_path.exists():
        raise FileNotFoundError(f"Schema not found: {schema_path}")
    with open(schema_path, encoding="utf-8") as f:
        schema = json.load(f)
    _SCHEMA_CACHE[artifact_type] = schema
    return schema


def validate_artifact(artifact_data: dict) -> dict:
    """Validate artifact_data against its JSON Schema and contract rules.

    Returns a dict with keys:
      - valid (bool): True iff schema_errors and contract_violations are empty
      - schema_errors (list[str]): JSON Schema validation errors
      - contract_violations (list[str]): Artifact contract rule violations
      - warnings (list[str]): Non-blocking issues
    """
    result: dict[str, Any] = {
        "valid": False,
        "schema_errors": [],
        "contract_violations": [],
        "warnings": [],
    }

    artifact_type = artifact_data.get("artifact_type")

    # ── Basic type check ──
    if artifact_type not in ARTIFACT_TYPES:
        result["schema_errors"].append(
            f"artifact_type {artifact_type!r} is not a known artifact type. "
            f"Valid types: {sorted(ARTIFACT_TYPES)}"
        )
        return result

    # ── JSON Schema validation ──
    if HAS_JSONSCHEMA:
        try:
            schema = load_schema(artifact_type)
            validator = jsonschema.Draft7Validator(schema)
            for error in sorted(validator.iter_errors(artifact_data), key=str):
                result["schema_errors"].append(
                    f"{'.'.join(str(p) for p in error.absolute_path) or '(root)'}: {error.message}"
                )
        except FileNotFoundError as e:
            result["schema_errors"].append(str(e))
        except Exception as e:
            result["schema_errors"].append(f"Schema load error: {e}")
    else:
        result["warnings"].append(
            "jsonschema not installed — schema validation skipped. "
            "Run: pip install jsonschema>=4.0.0"
        )

    # ── Contract rules (beyond JSON Schema) ──
    contract_violations = artifact_contract_check(artifact_data)
    result["contract_violations"].extend(contract_violations)

    result["valid"] = not result["schema_errors"] and not result["contract_violations"]
    return result


def artifact_contract_check(artifact_data: dict) -> list[str]:
    """Check artifact contract rules that JSON Schema cannot enforce.

    Returns a list of violation strings. Empty list = contract satisfied.
    """
    violations: list[str] = []
    artifact_type = artifact_data.get("artifact_type", "")

    # Rule 1: Core provenance fields must be present and non-empty on all artifacts.
    for field in ("artifact_id", "artifact_type", "schema_version", "source_id", "generated_at"):
        if not artifact_data.get(field):
            violations.append(f"CONTRACT: required provenance field '{field}' is missing or empty")

    # Rule 2: Interpretive artifacts — every claim must have evidence or be speculative.
    if artifact_type == "interpretive":
        for i, claim in enumerate(artifact_data.get("interpretive_claims", [])):
            has_evidence = bool(claim.get("evidence_links"))
            is_speculative = claim.get("speculative", False) or claim.get("confidence") == "speculative"
            if not has_evidence and not is_speculative:
                violations.append(
                    f"CONTRACT: interpretive_claims[{i}] has no evidence_links and is not marked speculative"
                )

    # Rule 3: Public prose reviewed/published status requires raw_extraction + validation in inputs.
    if artifact_type == "public_prose":
        status = artifact_data.get("editorial_status", "draft")
        if status in ("reviewed", "published"):
            emergency = artifact_data.get("emergency_prototype_mode", False)
            if not emergency:
                input_ids = artifact_data.get("input_artifact_ids", [])
                # We cannot resolve IDs to types here without a registry, so warn instead.
                if len(input_ids) < 2:
                    violations.append(
                        "CONTRACT: public_prose with status 'reviewed' or 'published' "
                        "must reference at least 2 prior artifacts in input_artifact_ids "
                        "(including at least one raw_extraction and one validation)"
                    )

    # Rule 4: Curation publish/feature requires reasons_for_inclusion.
    if artifact_type == "curation":
        status = artifact_data.get("relevance_status", "")
        if status in ("publish", "feature"):
            if not artifact_data.get("reasons_for_inclusion"):
                violations.append(
                    "CONTRACT: curation artifact with relevance_status 'publish' or 'feature' "
                    "must include reasons_for_inclusion"
                )

    # Rule 5: Interpretive artifact must list limitations.
    if artifact_type == "interpretive":
        if not artifact_data.get("limitations"):
            violations.append(
                "CONTRACT: interpretive artifact must include at least one entry in 'limitations'"
            )

    return violations


def load_artifact(path: Path) -> dict:
    """Load a JSON artifact from disk."""
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def save_artifact(artifact_data: dict, output_dir: Path, filename: str | None = None) -> Path:
    """Save an artifact to disk as JSON. Returns the path written."""
    output_dir.mkdir(parents=True, exist_ok=True)
    if filename is None:
        artifact_id = artifact_data.get("artifact_id", "unknown")
        filename = f"{artifact_id}.json"
    out_path = output_dir / filename
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(artifact_data, f, indent=2, ensure_ascii=False)
    return out_path


if __name__ == "__main__":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
    skeleton = make_artifact_skeleton("raw_extraction", "example-source", extraction_scope="test")
    print(json.dumps(skeleton, indent=2))
