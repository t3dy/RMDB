"""Initialize the RenMagDB SQLite database with Phase 1 schema.

Creates all tables per BUCKMANONTRMDB.md revised specification:
- Core entities: documents, figures, texts, dictionary_terms, timeline_events
- Flexible eras: era_assignments join table
- Term variants: term_variants table
- Join/relationship tables with cardinality docs
- Provenance on all content tables + interpretive joins
- FTS5 virtual tables
- Controlled vocabularies: topics, schema_version

Idempotent: uses CREATE TABLE IF NOT EXISTS throughout.
"""

import sqlite3
import sys
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent.parent / "db" / "renmagic.db"


def init_db():
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(str(DB_PATH))
    conn.execute("PRAGMA journal_mode=WAL")
    conn.execute("PRAGMA foreign_keys=ON")
    c = conn.cursor()

    # ── Schema version tracking ──
    c.execute("""
    CREATE TABLE IF NOT EXISTS schema_version (
        version INTEGER PRIMARY KEY,
        applied_at TEXT DEFAULT (datetime('now')),
        description TEXT
    )""")

    # ── Core entity: documents (the 358 corpus files) ──
    c.execute("""
    CREATE TABLE IF NOT EXISTS documents (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        path TEXT UNIQUE NOT NULL,
        md_path TEXT,
        title TEXT,
        title_from_filename TEXT,
        author_from_filename TEXT,
        year INTEGER,
        format TEXT CHECK(format IN ('PDF','EPUB','HTML','CHM','OTHER')),
        doc_type TEXT CHECK(doc_type IN (
            'MONOGRAPH','ARTICLE','CHAPTER','REVIEW','PRIMARY_SOURCE',
            'ANTHOLOGY','DISSERTATION','UNKNOWN'
        )),
        pages INTEGER,
        chars INTEGER,
        quality_flag TEXT CHECK(quality_flag IN ('GOOD','PARTIAL','SCANNED','EMPTY')),
        language TEXT,
        folder_figure TEXT,
        is_primary_source INTEGER DEFAULT 0,
        duplicate_group_id INTEGER,
        summary TEXT,
        relevance TEXT CHECK(relevance IN ('PRIMARY','DIRECT','CONTEXTUAL')),
        -- Provenance
        source_method TEXT DEFAULT 'DETERMINISTIC'
            CHECK(source_method IN ('DETERMINISTIC','CORPUS_EXTRACTION','LLM_ASSISTED','HUMAN_VERIFIED','SEED_DATA')),
        review_status TEXT DEFAULT 'DRAFT'
            CHECK(review_status IN ('DRAFT','REVIEWED','VERIFIED')),
        confidence TEXT DEFAULT 'HIGH'
            CHECK(confidence IN ('HIGH','MEDIUM','LOW')),
        created_at TEXT DEFAULT (datetime('now')),
        updated_at TEXT DEFAULT (datetime('now'))
    )""")

    # ── Core entity: figures (historical persons + modern scholars) ──
    c.execute("""
    CREATE TABLE IF NOT EXISTS figures (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT UNIQUE NOT NULL,
        name_latin TEXT,
        figure_type TEXT CHECK(figure_type IN ('HISTORICAL','SCHOLAR')),
        birth_year INTEGER,
        death_year INTEGER,
        nationality TEXT,
        biography TEXT,
        significance TEXT,
        primary_tradition TEXT,
        key_works TEXT,
        wikidata_id TEXT,
        -- Provenance
        source_method TEXT DEFAULT 'DETERMINISTIC',
        review_status TEXT DEFAULT 'DRAFT',
        confidence TEXT DEFAULT 'HIGH',
        created_at TEXT DEFAULT (datetime('now')),
        updated_at TEXT DEFAULT (datetime('now'))
    )""")

    # ── Core entity: texts (referenced primary sources) ──
    c.execute("""
    CREATE TABLE IF NOT EXISTS texts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        title_latin TEXT,
        title_original TEXT,
        author_figure_id INTEGER REFERENCES figures(id),
        corpus_document_id INTEGER REFERENCES documents(id),
        era TEXT,
        tradition TEXT,
        language TEXT,
        significance TEXT,
        date_composed TEXT,
        -- Provenance
        source_method TEXT DEFAULT 'DETERMINISTIC',
        review_status TEXT DEFAULT 'DRAFT',
        confidence TEXT DEFAULT 'HIGH',
        created_at TEXT DEFAULT (datetime('now')),
        updated_at TEXT DEFAULT (datetime('now'))
    )""")

    # ── Core entity: dictionary_terms ──
    c.execute("""
    CREATE TABLE IF NOT EXISTS dictionary_terms (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        term TEXT NOT NULL,
        term_language TEXT CHECK(term_language IN ('LATIN','GREEK','HEBREW','ARABIC','GERMAN','ITALIAN','FRENCH','ENGLISH','OTHER')),
        canonical_form TEXT,
        english_translation TEXT,
        definition_brief TEXT,
        definition_long TEXT,
        domain TEXT CHECK(domain IN (
            'ALCHEMICAL','HERMETIC','KABBALISTIC','NEOPLATONIC',
            'MEDICAL','ASTROLOGICAL','THEOLOGICAL','GENERAL',
            'ENOCHIAN','MAGICAL','PHILOSOPHICAL'
        )),
        frequency INTEGER DEFAULT 0,
        -- Provenance
        source_method TEXT DEFAULT 'DETERMINISTIC',
        review_status TEXT DEFAULT 'DRAFT',
        confidence TEXT DEFAULT 'HIGH',
        created_at TEXT DEFAULT (datetime('now')),
        updated_at TEXT DEFAULT (datetime('now')),
        UNIQUE(term, term_language)
    )""")

    # ── Term variants (Kabbalah/Cabala/Qabalah) ──
    c.execute("""
    CREATE TABLE IF NOT EXISTS term_variants (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        term_id INTEGER NOT NULL REFERENCES dictionary_terms(id),
        variant TEXT NOT NULL,
        variant_language TEXT,
        variant_script TEXT CHECK(variant_script IN ('LATIN','HEBREW','GREEK','ARABIC','CYRILLIC','OTHER')),
        UNIQUE(term_id, variant)
    )""")

    # ── Core entity: timeline_events ──
    c.execute("""
    CREATE TABLE IF NOT EXISTS timeline_events (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        year INTEGER NOT NULL,
        year_end INTEGER,
        event_type TEXT CHECK(event_type IN (
            'PUBLICATION','BIOGRAPHY','SCHOLARSHIP','TRIAL','INSTITUTION',
            'TRANSLATION','DISCOVERY','POLITICAL','OTHER'
        )),
        title TEXT NOT NULL,
        description TEXT,
        -- Provenance
        source_method TEXT DEFAULT 'DETERMINISTIC',
        review_status TEXT DEFAULT 'DRAFT',
        confidence TEXT DEFAULT 'HIGH',
        created_at TEXT DEFAULT (datetime('now')),
        updated_at TEXT DEFAULT (datetime('now'))
    )""")

    # ── Flexible era assignments ──
    c.execute("""
    CREATE TABLE IF NOT EXISTS era_assignments (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        entity_type TEXT NOT NULL CHECK(entity_type IN ('FIGURE','TEXT','EVENT')),
        entity_id INTEGER NOT NULL,
        era TEXT NOT NULL CHECK(era IN ('ANCIENT','MEDIEVAL','RENAISSANCE','EARLY_MODERN','ENLIGHTENMENT')),
        era_role TEXT,
        UNIQUE(entity_type, entity_id, era, era_role)
    )""")

    # ── Controlled vocabulary: topics ──
    c.execute("""
    CREATE TABLE IF NOT EXISTS topics (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT UNIQUE NOT NULL,
        description TEXT,
        created_at TEXT DEFAULT (datetime('now'))
    )""")

    # ── JOIN TABLES ──

    # document <-> figure (M:N, optional — some docs are thematic)
    c.execute("""
    CREATE TABLE IF NOT EXISTS document_figures (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        document_id INTEGER NOT NULL REFERENCES documents(id),
        figure_id INTEGER NOT NULL REFERENCES figures(id),
        relationship TEXT DEFAULT 'SUBJECT',
        source_method TEXT DEFAULT 'DETERMINISTIC',
        UNIQUE(document_id, figure_id)
    )""")

    # document <-> referenced text (M:N, optional, interpretive)
    c.execute("""
    CREATE TABLE IF NOT EXISTS document_texts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        document_id INTEGER NOT NULL REFERENCES documents(id),
        text_id INTEGER NOT NULL REFERENCES texts(id),
        source_method TEXT DEFAULT 'DETERMINISTIC',
        confidence TEXT DEFAULT 'HIGH',
        UNIQUE(document_id, text_id)
    )""")

    # document <-> topic (M:N, required — every doc gets >=1 topic)
    c.execute("""
    CREATE TABLE IF NOT EXISTS document_topics (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        document_id INTEGER NOT NULL REFERENCES documents(id),
        topic_id INTEGER NOT NULL REFERENCES topics(id),
        score REAL,
        source_method TEXT DEFAULT 'DETERMINISTIC',
        UNIQUE(document_id, topic_id)
    )""")

    # figure -> figure influence (M:N, directed, interpretive)
    c.execute("""
    CREATE TABLE IF NOT EXISTS figure_influences (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        source_figure_id INTEGER NOT NULL REFERENCES figures(id),
        target_figure_id INTEGER NOT NULL REFERENCES figures(id),
        influence_type TEXT,
        source_method TEXT DEFAULT 'LLM_ASSISTED',
        confidence TEXT DEFAULT 'MEDIUM',
        notes TEXT,
        UNIQUE(source_figure_id, target_figure_id)
    )""")

    # figure <-> text (M:N, optional — authored/translated/commented)
    c.execute("""
    CREATE TABLE IF NOT EXISTS figure_texts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        figure_id INTEGER NOT NULL REFERENCES figures(id),
        text_id INTEGER NOT NULL REFERENCES texts(id),
        relationship TEXT CHECK(relationship IN ('AUTHORED','TRANSLATED','COMMENTED','EDITED','ATTRIBUTED')),
        UNIQUE(figure_id, text_id, relationship)
    )""")

    # term <-> document occurrence (M:N, required — terms must appear in >=1 doc)
    c.execute("""
    CREATE TABLE IF NOT EXISTS term_documents (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        term_id INTEGER NOT NULL REFERENCES dictionary_terms(id),
        document_id INTEGER NOT NULL REFERENCES documents(id),
        frequency INTEGER DEFAULT 1,
        UNIQUE(term_id, document_id)
    )""")

    # term <-> figure association (M:N, optional)
    c.execute("""
    CREATE TABLE IF NOT EXISTS term_figures (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        term_id INTEGER NOT NULL REFERENCES dictionary_terms(id),
        figure_id INTEGER NOT NULL REFERENCES figures(id),
        UNIQUE(term_id, figure_id)
    )""")

    # term <-> term cross-reference (M:N, typed)
    c.execute("""
    CREATE TABLE IF NOT EXISTS term_links (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        term_id INTEGER NOT NULL REFERENCES dictionary_terms(id),
        linked_term_id INTEGER NOT NULL REFERENCES dictionary_terms(id),
        link_type TEXT CHECK(link_type IN ('RELATED','SEE_ALSO','OPPOSITE','PARENT','CHILD')),
        UNIQUE(term_id, linked_term_id, link_type)
    )""")

    # event <-> figure (M:N, optional)
    c.execute("""
    CREATE TABLE IF NOT EXISTS event_figures (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        event_id INTEGER NOT NULL REFERENCES timeline_events(id),
        figure_id INTEGER NOT NULL REFERENCES figures(id),
        UNIQUE(event_id, figure_id)
    )""")

    # event <-> text (M:N, optional)
    c.execute("""
    CREATE TABLE IF NOT EXISTS event_texts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        event_id INTEGER NOT NULL REFERENCES timeline_events(id),
        text_id INTEGER NOT NULL REFERENCES texts(id),
        UNIQUE(event_id, text_id)
    )""")

    # ── Indexes ──
    c.execute("CREATE INDEX IF NOT EXISTS idx_documents_folder ON documents(folder_figure)")
    c.execute("CREATE INDEX IF NOT EXISTS idx_documents_type ON documents(doc_type)")
    c.execute("CREATE INDEX IF NOT EXISTS idx_figures_type ON figures(figure_type)")
    c.execute("CREATE INDEX IF NOT EXISTS idx_terms_domain ON dictionary_terms(domain)")
    c.execute("CREATE INDEX IF NOT EXISTS idx_terms_language ON dictionary_terms(term_language)")
    c.execute("CREATE INDEX IF NOT EXISTS idx_era_entity ON era_assignments(entity_type, entity_id)")
    c.execute("CREATE INDEX IF NOT EXISTS idx_era_era ON era_assignments(era)")

    # ── FTS5 virtual tables ──
    # Documents full-text search
    c.execute("""
    CREATE VIRTUAL TABLE IF NOT EXISTS documents_fts USING fts5(
        title, summary, full_text,
        content=documents, content_rowid=id
    )""")

    # Dictionary terms full-text search
    c.execute("""
    CREATE VIRTUAL TABLE IF NOT EXISTS terms_fts USING fts5(
        term, english_translation, definition_long,
        content=dictionary_terms, content_rowid=id
    )""")

    # ── Record schema version ──
    c.execute("""
    INSERT OR IGNORE INTO schema_version (version, description)
    VALUES (1, 'Phase 1 schema: core entities, joins, FTS5, provenance')
    """)

    conn.commit()
    conn.close()
    print(f"Database initialized: {DB_PATH}")
    print(f"Schema version: 1")

    # Verify tables
    conn = sqlite3.connect(str(DB_PATH))
    tables = conn.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name").fetchall()
    conn.close()
    print(f"Tables created: {len(tables)}")
    for t in tables:
        print(f"  {t[0]}")


if __name__ == "__main__":
    init_db()
