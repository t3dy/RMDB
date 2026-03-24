"""TF-IDF topic clustering on the markdown corpus.

Uses scikit-learn to cluster documents into 8-15 topic groups.
Seeds the topics table and populates document_topics.
Outputs data/topic_clusters.json.
"""

import io
import json
import sqlite3
import sys
from pathlib import Path

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.decomposition import TruncatedSVD
import numpy as np

CORPUS_ROOT = Path(__file__).resolve().parent.parent
DB_PATH = CORPUS_ROOT / "db" / "renmagic.db"
CLUSTERS_PATH = CORPUS_ROOT / "data" / "topic_clusters.json"

N_CLUSTERS = 12  # Target topic count
MAX_FEATURES = 5000
TOP_TERMS_PER_CLUSTER = 15


def main():
    conn = sqlite3.connect(str(DB_PATH))

    # Load documents
    rows = conn.execute("SELECT id, path, md_path, folder_figure FROM documents").fetchall()

    doc_ids = []
    doc_texts = []
    doc_meta = []

    for doc_id, path, md_path, folder in rows:
        if not md_path:
            continue
        p = Path(md_path)
        if not p.exists():
            p = CORPUS_ROOT / "md" / Path(path).with_suffix(".md")
        if not p.exists():
            continue
        try:
            text = p.read_text(encoding="utf-8", errors="replace")[:20000]  # First 20K chars
        except Exception:
            continue
        if len(text.strip()) < 100:
            continue
        doc_ids.append(doc_id)
        doc_texts.append(text)
        doc_meta.append({"id": doc_id, "path": path, "folder": folder})

    print(f"Documents loaded: {len(doc_texts)}")

    # TF-IDF vectorization
    vectorizer = TfidfVectorizer(
        max_features=MAX_FEATURES,
        stop_words="english",
        min_df=3,
        max_df=0.8,
        ngram_range=(1, 2),
    )
    tfidf_matrix = vectorizer.fit_transform(doc_texts)
    feature_names = vectorizer.get_feature_names_out()

    print(f"TF-IDF matrix: {tfidf_matrix.shape}")

    # Dimensionality reduction for better clustering
    svd = TruncatedSVD(n_components=min(50, tfidf_matrix.shape[1] - 1))
    reduced = svd.fit_transform(tfidf_matrix)

    # K-Means clustering
    kmeans = KMeans(n_clusters=N_CLUSTERS, random_state=42, n_init=10)
    labels = kmeans.fit_predict(reduced)

    # Extract top terms per cluster from original TF-IDF
    # Get cluster centers in original feature space
    original_centers = svd.inverse_transform(kmeans.cluster_centers_)

    clusters = {}
    for i in range(N_CLUSTERS):
        top_indices = original_centers[i].argsort()[-TOP_TERMS_PER_CLUSTER:][::-1]
        top_terms = [feature_names[idx] for idx in top_indices]

        # Get documents in this cluster
        cluster_docs = [doc_meta[j] for j in range(len(labels)) if labels[j] == i]
        cluster_folders = {}
        for d in cluster_docs:
            f = d.get("folder") or "(root)"
            cluster_folders[f] = cluster_folders.get(f, 0) + 1

        cluster_name = f"Topic {i+1}: {', '.join(top_terms[:3])}"
        clusters[cluster_name] = {
            "id": i + 1,
            "top_terms": top_terms,
            "doc_count": len(cluster_docs),
            "folder_distribution": cluster_folders,
        }

    # Seed topics table
    for name, info in clusters.items():
        short_name = ", ".join(info["top_terms"][:3])
        conn.execute("""
        INSERT OR IGNORE INTO topics (name, description)
        VALUES (?, ?)
        """, (short_name, f"TF-IDF cluster {info['id']}: {', '.join(info['top_terms'][:8])}"))

    # Populate document_topics
    topic_rows = {row[1]: row[0] for row in conn.execute("SELECT id, name FROM topics").fetchall()}
    join_count = 0
    for j, label in enumerate(labels):
        doc_id = doc_ids[j]
        cluster_info = list(clusters.values())[label]
        topic_name = ", ".join(cluster_info["top_terms"][:3])
        topic_id = topic_rows.get(topic_name)
        if topic_id:
            conn.execute("""
            INSERT OR IGNORE INTO document_topics (document_id, topic_id, score, source_method)
            VALUES (?, ?, ?, 'DETERMINISTIC')
            """, (doc_id, topic_id, float(1.0)))
            join_count += 1

    conn.commit()

    # Save clusters JSON
    CLUSTERS_PATH.parent.mkdir(parents=True, exist_ok=True)
    CLUSTERS_PATH.write_text(json.dumps(clusters, indent=2, ensure_ascii=False), encoding="utf-8")

    print(f"\n=== TF-IDF TOPIC CLUSTERING ===")
    print(f"Documents clustered: {len(doc_texts)}")
    print(f"Topics created: {len(clusters)}")
    print(f"Document-topic links: {join_count}")
    print(f"\nTopics:")
    for name, info in clusters.items():
        top_folders = sorted(info["folder_distribution"].items(), key=lambda x: -x[1])[:3]
        folder_str = ", ".join(f"{f}:{c}" for f, c in top_folders)
        print(f"  [{info['doc_count']} docs] {', '.join(info['top_terms'][:5])} | {folder_str}")

    conn.close()


if __name__ == "__main__":
    main()
