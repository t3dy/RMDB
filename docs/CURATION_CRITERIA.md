# Curation Criteria

**Version:** 1.0  
**Applies to:** `CurationArtifact`, Curation Agent, news aggregator pipeline  
**See also:** [ARTIFACT_PIPELINE.md](ARTIFACT_PIPELINE.md), [AGENT_ARTIFACT_RULES.md](AGENT_ARTIFACT_RULES.md)

---

## Purpose

This document defines the standards for deciding whether and how content appears in the RenMagDB portal and its curated news aggregator. The curation stage (stage F) is where editorial judgment is applied. It is the only stage that asks: should this appear?

---

## Core Principle

**The portal targets intelligent non-specialists and specialists in Renaissance magic, Western esotericism, and adjacent fields.** It does not serve the general occult consumer market. Every curation decision should ask: would a serious scholar or a seriously curious reader find this useful?

---

## Relevance Status Definitions

| Status | Meaning |
|--------|---------|
| `reject` | Not relevant or does not meet scholarly standards. Should not appear in the portal in any form. |
| `archive` | Marginally relevant or low scholarly value. Store but do not publish. May be useful for corpus completeness. |
| `review` | Uncertain relevance or quality. Needs human curatorial attention before a decision. |
| `publish` | Should appear in the portal. Meets scholarly standards and serves the portal's audience. Requires `reasons_for_inclusion`. |
| `feature` | Especially significant. Should be highlighted or featured. Requires `reasons_for_inclusion`. |

---

## Scholarly Value Assessment

Assign `scholarly_value` from: `high`, `medium`, `low`, `none`, `uncertain`.

### High scholarly value (publish or feature)

- Peer-reviewed monographs or articles on Renaissance magic, Western esotericism, Hermetism, alchemy, Christian Kabbalah, Neoplatonism, grimoire tradition, ritual magic, astrology, witchcraft studies, history of science, manuscript studies, book history, or iconography.
- Primary source editions, critical editions, or translations with scholarly apparatus.
- Foundational works in the historiography (Yates, Walker, Copenhaver, Hanegraaff, Kieckhefer, Peters, Thomas, Klaassen, Saif, Leinkauf, etc.).
- Works that engage seriously with historiographical debates.
- Works that provide new archival or manuscript evidence.
- Works on methodology relevant to the study of esotericism or magic.

### Medium scholarly value (publish or archive)

- Reliable introductory or survey works by credentialed scholars.
- Conference proceedings or edited volumes with strong contributions.
- Serious popular treatments by scholars (e.g. Hanegraaff writing for a general audience).
- Interdisciplinary work that intersects with the portal's subjects from adjacent fields (art history, philosophy, religious studies, history of science).

### Low scholarly value (archive or reject)

- Works that treat esoteric traditions as living spiritual practices without historical analysis.
- Works that assert uncritically the validity of Renaissance magical claims (alchemy "works," Kabbalah "reveals truth," etc.).
- Works by non-scholars that recycle secondary sources without engagement with primary texts or scholarship.
- Works that confuse actor categories and analyst categories — treating "Hermetism" as a real tradition rather than a historical construct.

### None / reject

See Reject Criteria below.

---

## Reject Criteria

Reject any source that matches one or more of the following:

1. **Pop-occult lifestyle content.** Generic content about crystals, astrology "for your sign," tarot readings, or witchcraft as spiritual practice without historical grounding. This is not the portal's audience.

2. **AI-generated spam.** Content that appears to be produced by AI without editorial review: formulaic structure, no specific claims, no citations, generic prose about "ancient wisdom."

3. **Vague spirituality.** Content that invokes esotericism, mysticism, or "the occult" as aesthetic or spiritual categories without substantive historical or philosophical content.

4. **Low-relevance pop content.** Books, podcasts, or videos aimed at mass-market spiritual consumers (e.g., popular witchcraft guides, New Age channeling texts, conspiracy-adjacent "ancient mysteries" content).

5. **Pseudohistory.** Content that makes historically false claims about Renaissance magic or the history of Western esotericism without acknowledging scholarly consensus (e.g., claiming Hermetism "really is" ancient Egyptian, that alchemy "really" turned lead to gold, etc.).

6. **Commercially motivated content without scholarly merit.** Course promotions, spiritual coaching advertisements, product pitches dressed as essays.

---

## Positive Curation Signals

These increase the likelihood of `publish` or `feature`:

- Primary source discussion: engages directly with specific texts, passages, or manuscripts.
- Scholarly reliability: cites peer-reviewed scholarship, engages with field debates.
- Historiographic awareness: knows the Yates thesis and its critics.
- Methodological care: distinguishes actor categories from analyst categories.
- New scholarship or new source material: introduces material not widely covered in the field.
- Accessibility without loss of rigor: explains complex ideas to intelligent non-specialists without dumbing them down.
- Portal alignment: directly relevant to figures, texts, terms, or traditions already in the portal.
- Esoteric tradition coverage: covers one or more of the portal's core traditions with substantive historical content.

---

## Esoteric Traditions Coverage (positive signals for curation)

Content on any of the following traditions at a scholarly level is a strong positive signal:

- Western esotericism (as a scholarly field)
- Renaissance magic (natural, celestial, demonic, angelic)
- Alchemy (transmutation, Paracelsian, laboratory)
- Hermetism (Corpus Hermeticum, Asclepius, prisca theologia)
- Neoplatonism (Plotinus, Iamblichus, Proclus, Ficino)
- Christian Kabbalah (Pico, Reuchlin, Agrippa, Lazzarelli)
- Jewish Kabbalah (when discussed in Renaissance or early modern context)
- Grimoire tradition (Key of Solomon, Picatrix, lesser-known texts)
- Ritual magic (ceremonial magic, angel magic, Solomonic tradition)
- Astrology (judicial, natural, medical; as historical practice)
- Witchcraft studies (historical, not practice-oriented)
- Enochian tradition (Dee, Kelley, angels)
- Rosicrucianism (Rosicrucian manifestos, early modern context)
- Natural philosophy and history of science (when intersecting with esotericism)
- Manuscript studies and book history (when covering esoteric texts)
- Iconography (emblems, symbolic imagery, Maier, Fludd)

---

## News Aggregator Pipeline

For news aggregator items (podcasts, articles, videos, blog posts, new publications), the pipeline is:

```
source
  → SourceMetadataArtifact
  → RawExtractionArtifact (from title, description, transcript, body)
  → OntologyTaggingArtifact (including pop_occult_flag)
  → CurationArtifact (with aggregator_link_card filled)
  → PublicProseArtifact (the link card as final output)
```

### Link Card Fields

The `aggregator_link_card` in `CurationArtifact` should include:

| Field | Notes |
|-------|-------|
| `title` | Original title, not rewritten |
| `source_name` | Publication, podcast, channel, etc. |
| `date` | Publication date (ISO 8601 or YYYY-MM-DD) |
| `url` | Original URL |
| `short_summary` | 2-3 sentences: what it covers and why it matters |
| `tags` | From the ontology |
| `why_it_matters` | 1 sentence on scholarly significance |
| `editorial_note` | Optional: context, caveats, or framing notes |

### What Disqualifies a News Item

- `pop_occult_flag: true` in `OntologyTaggingArtifact` → `reject` unless human override
- `scholarly_reliability: "low"` → `archive` at most
- No specific scholarly content beyond the title → `reject`
- Paywall content with no excerpt or transcript available → `archive`
- AI-generated content without editorial oversight → `reject`

---

## Distinguishing Scholarly from Pop-Occult: Test Cases

| Source | Decision | Reason |
|--------|----------|--------|
| Hanegraaff, *Esotericism and the Academy* (2012) | feature | Foundational methodological work; shapes the portal's own framework |
| Walker, *Spiritual and Demonic Magic* (1958) | feature | Foundational primary scholarship on the portal's core subjects |
| Podcast episode interviewing a historian of alchemy about Paracelsus | publish | Scholarly content in accessible format, specific topic |
| Podcast episode "10 facts about witchcraft history" by a wellness blogger | reject | Pop-occult lifestyle content, no scholarly grounding |
| YouTube video: "The Secret History of the Rosicrucians" (pseudohistory channel) | reject | Pseudohistory, no scholarly apparatus |
| YouTube lecture by a university professor on Agrippa's sources | publish | Scholarly content in accessible format |
| Blog post by a practicing Wiccan on "drawing down the moon ritual history" | reject | Practice-oriented, no historical scholarship |
| Article in *Magic, Ritual, and Witchcraft* journal | publish or feature | Peer-reviewed, directly relevant |
| New critical edition of *Picatrix* with introduction | feature | Primary source scholarship, rare |
| Goodreads review of Yates | reject | Not scholarly content |
