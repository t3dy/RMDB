# Agent Artifact Rules

**Version:** 1.0  
**See also:** [ARTIFACT_PIPELINE.md](ARTIFACT_PIPELINE.md), [CURATION_CRITERIA.md](CURATION_CRITERIA.md)

---

## Core Rule

**No agent may jump from source material to public prose.**

Every LLM-assisted content production task must pass through the pipeline stages in order. Skipping stages is only permitted when explicitly instructed by a human curator and when `emergency_prototype_mode: true` is set on the output artifact.

---

## Agent Role Assignments

Each agent role is authorized to produce and consume specific artifact types only.

### Extraction Agent

**Produces:** `RawExtractionArtifact` only  
**Consumes:** Source text (PDF, markdown, transcript), `SourceMetadataArtifact`

Rules:
- Extract only what is explicitly present in the source.
- Do not make historiographical claims the source does not make.
- Do not classify, interpret, or evaluate scholarly significance.
- Record uncertainties honestly (ambiguous passages, illegible text, missing pages).
- Every important passage must include a `location` (page, section, paragraph, timestamp).
- Use actor language: describe what the source says, not what is "really" true about a tradition.

---

### Validation Agent

**Produces:** `ValidationArtifact` only  
**Consumes:** Any prior artifact (typically `RawExtractionArtifact` or `OntologyTaggingArtifact`)

Rules:
- Check whether claims in the target artifact are grounded in the source or in prior artifacts.
- Flag suspected hallucinations (claims that appear invented or unsupported).
- Do not generate new interpretations or classifications.
- `validation_status: "fail"` should be set for any artifact with hallucinations or schema errors.
- `validation_status: "warn"` for completeness gaps or minor grounding issues.
- `validation_status: "pass"` only when the artifact is schema-valid, contract-compliant, and grounded.

---

### Ontology Agent

**Produces:** `OntologyTaggingArtifact` only  
**Consumes:** `RawExtractionArtifact`, `ValidationArtifact` (to know if input is trustworthy)

Rules:
- Map entities, topics, and terms to the portal's controlled vocabulary.
- Use the controlled vocabulary defined in `artifacts/schemas/ontology_tagging.schema.json`:
  - `esoteric_traditions` — from the enum list
  - `scholarly_fields` — from the enum list
  - `content_types` — from the enum list
  - `periods` — from the enum list
- Include `confidence_by_tag` scores.
- Document `rejected_tags` with reasons.
- Set `pop_occult_flag: true` for sources that are generic occult lifestyle, AI spam, vague spirituality, or low-scholarly-relevance content. See [CURATION_CRITERIA.md](CURATION_CRITERIA.md).
- Do not write public prose.
- Do not make interpretive claims about the significance of the source.

---

### Interpretation Agent

**Produces:** `InterpretiveArtifact` only  
**Consumes:** `RawExtractionArtifact`, `OntologyTaggingArtifact`, `ValidationArtifact`

Rules:
- Every interpretive claim must include `evidence_links` pointing to prior artifact locations and passages.
- Claims with no direct evidence must be marked `"speculative": true` and `"confidence": "speculative"`.
- Include `alternative_readings` for any claim that has genuine scholarly disagreement.
- Include `limitations` explaining what the interpretation cannot establish.
- Include `historiographical_relevance` to situate claims within field debates (Yates thesis, Copenhaver revision, Hanegraaff constructionism, Walker on demonic vs natural magic, etc.).
- Do not write public prose.
- Distinguish: what the source says (extraction) vs what the portal can claim about it (interpretation).

---

### Curation Agent

**Produces:** `CurationArtifact` only  
**Consumes:** `SourceMetadataArtifact`, `OntologyTaggingArtifact`, `InterpretiveArtifact`

Rules:
- Decide `relevance_status`: `reject`, `archive`, `review`, `publish`, `feature`.
- `publish` and `feature` require `reasons_for_inclusion` (at least one entry).
- Set `scholarly_value` honestly: `high`, `medium`, `low`, `none`, or `uncertain`.
- For news aggregator items: fill `aggregator_link_card` with title, source, date, URL, short_summary, tags, why_it_matters.
- See [CURATION_CRITERIA.md](CURATION_CRITERIA.md) for content standards.
- Do not write body prose. The `aggregator_link_card.short_summary` is a short summary (2-3 sentences), not an essay.

---

### Writing Agent

**Produces:** `PublicProseArtifact` only  
**Consumes:** `RawExtractionArtifact`, `OntologyTaggingArtifact`, `InterpretiveArtifact`, `CurationArtifact`

Rules:
- Must list prior artifact IDs in `input_artifact_ids`.
- `editorial_status` starts at `"draft"`. Only a human reviewer may advance to `"reviewed"` or `"published"`.
- Body prose must be grounded in prior artifacts, not re-derived from the raw source.
- Follow the voice and style rules in `docs/WRITING_TEMPLATES_REVISED.md`:
  - Museum-curator scholarly voice
  - Accessible to intelligent non-specialists
  - Historiographically aware (mark Yates thesis as contested; use Copenhaver/Hanegraaff framing)
  - Clear about uncertainty
  - Resistant to overinterpretation
  - Distinguish source description from scholarly interpretation
  - Actor terms vs analyst terms (see RMESSAY1.md)
- `emergency_prototype_mode: true` is the only way to skip prior artifact requirements; it must be explicitly set and will prevent the artifact from reaching `reviewed` status automatically.

---

### Comparison Agent

**Produces:** `TextComparisonArtifact` only  
**Consumes:** Two or more `RawExtractionArtifact`s from different versions of the same text, plus their `SourceMetadataArtifact`s

Rules:
- Identify `difference_type` from the controlled enum.
- Include `evidence_locations` (source A location, source B location, or both).
- Include `interpretive_implications` if clear; otherwise leave null.
- Be explicit about `confidence` in the comparison.

---

### Bibliography Agent

**Produces:** `ScholarCitationArtifact` only  
**Consumes:** `RawExtractionArtifact` from a scholarly secondary source, `SourceMetadataArtifact`

Rules:
- Clearly distinguish `bibliographic_source_id` (the scholar's work) from `cited_work` (what the scholar discusses).
- `exact_quote` must always have a `page_or_location`.
- `historiographical_angle` places the citation within the field's debates.
- `related_portal_entities` links the claim to figures, texts, or terms in the portal.

---

## What All Agents Must Never Do

1. Skip stages in the pipeline without explicit human authorization.
2. Generate public prose from raw source material directly.
3. Make interpretive claims in an extraction artifact.
4. Run Bash, Python, or SQL (Swarm constraint — see SWARMRMDB.md).
5. Consult external APIs (Wikipedia, Wikidata) for content that the corpus contains (BLUNDER3 rule).
6. Use UTF-8 strings without the encoding wrapper in any Python helper (BLUNDER2 rule).
7. Advance `editorial_status` from `draft` to `reviewed` or `published` without a human reviewer.

---

## Quick Reference: Artifact Type → Stage → Producing Agent

| Artifact Type | Stage | Producing Agent |
|--------------|-------|----------------|
| `source_metadata` | A | Ingest scripts (deterministic) or Extraction Agent |
| `raw_extraction` | B | Extraction Agent |
| `validation` | C | Validation Agent or `validate_artifacts.py` |
| `ontology_tagging` | D | Ontology Agent |
| `interpretive` | E | Interpretation Agent |
| `curation` | F | Curation Agent |
| `public_prose` | G | Writing Agent |
| `text_comparison` | H | Comparison Agent |
| `scholar_citation` | I | Bibliography Agent |
