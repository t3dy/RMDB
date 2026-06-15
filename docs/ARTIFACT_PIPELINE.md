# RenMagDB Artifact Pipeline

**Version:** 1.0  
**Status:** Active — Phase B and beyond  
**See also:** [AGENT_ARTIFACT_RULES.md](AGENT_ARTIFACT_RULES.md), [CURATION_CRITERIA.md](CURATION_CRITERIA.md)

---

## Purpose

The artifact pipeline turns source material into public-facing portal content through a sequence of typed, versioned, durable intermediate steps. No agent may jump directly from source material to public prose.

Each stage produces a distinct artifact with its own schema, validation rules, and downstream consumers. This prevents interpretation from contaminating description, description from contaminating curation, and curation from contaminating writing.

---

## Pipeline Stages

```
source material
  ↓
A. SourceMetadataArtifact    — what it is, where it lives, basic facts
  ↓
B. RawExtractionArtifact     — what is explicitly present in the source
  ↓
C. ValidationArtifact        — is the extraction grounded and schema-valid?
  ↓
D. OntologyTaggingArtifact   — how does it map to the portal's controlled vocabulary?
  ↓
E. InterpretiveArtifact      — what bounded scholarly claims can we make?
  ↓
F. CurationArtifact          — should this appear in the portal? how?
  ↓
G. PublicProseArtifact       — final reader-facing text
```

Specialized types that can branch off at any stage:

- **H. TextComparisonArtifact** — comparing two versions of a text
- **I. ScholarCitationArtifact** — capturing a specific scholar's claim about a topic

---

## Artifact Types and Schemas

All schemas live in `artifacts/schemas/`. All fixtures live in `artifacts/fixtures/`.  
Generated artifacts live in `artifacts/generated/{source_id}/`.

| Type | Schema file | Stage |
|------|-------------|-------|
| `source_metadata` | `source_metadata.schema.json` | A |
| `raw_extraction` | `raw_extraction.schema.json` | B |
| `validation` | `validation.schema.json` | C |
| `ontology_tagging` | `ontology_tagging.schema.json` | D |
| `interpretive` | `interpretive.schema.json` | E |
| `curation` | `curation.schema.json` | F |
| `public_prose` | `public_prose.schema.json` | G |
| `text_comparison` | `text_comparison.schema.json` | H |
| `scholar_citation` | `scholar_citation.schema.json` | I |

---

## Artifact Contract

The following rules apply to all artifacts. Violations block publishing.

1. **Required provenance on every artifact:**
   Every artifact must include non-empty values for:
   `artifact_id`, `artifact_type`, `schema_version`, `source_id`, `generated_at`

2. **Interpretive claims need grounding:**
   Every claim in `interpretive_claims` must either have `evidence_links` (pointing to prior artifact locations) or be explicitly marked `"speculative": true` and `"confidence": "speculative"`.

3. **Public prose status gates:**
   A `public_prose` artifact may only have `editorial_status` of `"reviewed"` or `"published"` if its `input_artifact_ids` includes at least one `raw_extraction` artifact and at least one `validation` artifact. Exception: `emergency_prototype_mode: true` (must be explicitly set).

4. **Curation decisions need reasons:**
   A `curation` artifact with `relevance_status` of `"publish"` or `"feature"` must include at least one entry in `reasons_for_inclusion`.

5. **Interpretive artifacts need limitations:**
   Every `interpretive` artifact must include at least one entry in `limitations`.

6. **Validation failures block publishing:**
   Validation warnings allow work to continue. Validation failures (`validation_status: "fail"`) prevent a source from moving to `public_prose` with `editorial_status: "reviewed"` or `"published"`.

---

## Storage Layout

```
artifacts/
  schemas/                        # JSON Schema definitions (one per artifact type)
    source_metadata.schema.json
    raw_extraction.schema.json
    validation.schema.json
    ontology_tagging.schema.json
    interpretive.schema.json
    curation.schema.json
    public_prose.schema.json
    text_comparison.schema.json
    scholar_citation.schema.json
  fixtures/                       # Example artifacts for testing and reference
    example_source_metadata.json
    example_raw_extraction.json
    example_ontology_tagging.json
    example_interpretive.json
    example_curation.json
    example_public_prose.json
  generated/                      # Produced artifacts, organized by source_id
    {source_id}/
      source_metadata.json
      raw_extraction.{section_id}.json
      validation.raw_extraction.{section_id}.json
      ontology_tagging.{section_id}.json
      interpretive.{section_id}.json
      curation.json
      public_prose.draft.json
```

The `staging/` directory (existing) remains for LLM batch I/O: JSON batches in, JSON batches out, before processing into typed artifacts.

---

## Python API

```python
from scripts.artifact_pipeline import (
    ARTIFACT_SCHEMA_VERSION,
    generate_artifact_id,
    make_artifact_skeleton,
    validate_artifact,
    artifact_contract_check,
    load_schema,
    save_artifact,
    now_iso,
)

# Generate an artifact ID
artifact_id = generate_artifact_id("raw_extraction")  # e.g. "raw-extraction_a1b2c3d4"

# Create a skeleton with required fields pre-filled
skeleton = make_artifact_skeleton("raw_extraction", "yates-giordano-bruno-1964",
                                   extraction_scope="Introduction and Chapter 1")

# Validate an artifact dict
result = validate_artifact(skeleton)
# result = {"valid": bool, "schema_errors": [...], "contract_violations": [...], "warnings": [...]}
```

---

## Validation Command

```bash
# Validate all fixtures (default)
python scripts/validate_artifacts.py

# Validate all fixtures and generated artifacts
python scripts/validate_artifacts.py --all

# Validate a single file
python scripts/validate_artifacts.py --file artifacts/generated/yates-giordano-bruno-1964/raw_extraction.intro.json
```

Requires: `pip install jsonschema>=4.0.0`

Exit code 0 = all pass; 1 = failures; 2 = usage error.

---

## Relationship to Existing Pipeline

The existing pipeline (`staging/` → SQLite → Hugo site) does not change. The artifact pipeline supplements it for LLM-enriched content production:

- **Phase A (deterministic):** Documents, figures, terms, timeline → SQLite directly, no artifact files needed.
- **Phase B (LLM enrichment):** Summaries, biographies, definitions → LLM → artifact files → validated → SQLite insert or Hugo content.
- The `staging/` JSONs are inputs to the artifact pipeline, not artifacts themselves. They become `RawExtractionArtifact` or `SourceMetadataArtifact` once typed and validated.

---

## Guiding Principles

- **No stage skipping.** The purpose of the stages is separation of concerns: description, classification, interpretation, curation, and writing are different cognitive tasks requiring different constraints.
- **Artifacts are reusable.** A later stage reads prior artifacts rather than re-reading the full source. This is both more efficient and more auditable.
- **Artifacts are human-readable.** Use JSON with indentation. Prose fields exist but are specific fields, not the whole artifact.
- **Evidence trails survive.** Claims in interpretive artifacts point back to passages in extraction artifacts, which point back to pages in source documents. A reader can trace a public prose claim all the way back to the source page.
- **The portal describes; it does not endorse.** "Hermes Trismegistus as Renaissance magus" is an actor category actors used. The portal describes the category and its history; it does not assert that Hermetism is a real metaphysical tradition. See RMESSAY1.md and GNOSISDICTIONARYSTYLEANALYSISTAKEAWAYS.md.
