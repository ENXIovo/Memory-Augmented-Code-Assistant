#!/usr/bin/env python3
"""
Read every processed_gist/<repo>/summaries.json → embed with OpenAI
→ create / connect Pinecone serverless index → upsert to namespace.

Requires:
  pip install openai pinecone-client tqdm
"""

from __future__ import annotations
import json, time, itertools
from pathlib import Path

from tqdm import tqdm
import openai
from pinecone import Pinecone, ServerlessSpec
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import config as C

# ── Initialise clients ───────────────────────────────────────────────────
openai.api_key = C.OPENAI_API_KEY

pc = Pinecone(api_key=C.PINECONE_API_KEY)

# ── Create / connect index (serverless) ──────────────────────────────────
if not pc.list_indexes().names().__contains__(C.GIST_INDEX_NAME):
    print(f"[Pinecone] Creating serverless index '{C.GIST_INDEX_NAME}' …")
    pc.create_index(
        name=C.GIST_INDEX_NAME,
        dimension=C.EMBED_DIMENSION,               # text-embedding-3-small
        metric="cosine",
        spec=ServerlessSpec(
            cloud="aws",
            region="us-east-1"
        )
    )

# 等待索引就绪
while not pc.describe_index(C.GIST_INDEX_NAME).status["ready"]:
    time.sleep(1)

index = pc.Index(C.GIST_INDEX_NAME)

# ── Helper: batch embed ──────────────────────────────────────────────────
def embed_openai(texts: list[str]) -> list[list[float]]:
    backoff = 1.0
    while True:
        try:
            resp = openai.embeddings.create(
                input=texts,
                model=C.EMBED_MODEL,          # text-embedding-3-small
            )
            return [d.embedding for d in resp.data]
        except openai.RateLimitError:
            print("OpenAI rate-limited → sleeping", backoff, "s")
            time.sleep(backoff)
            backoff = min(backoff * 2, 32)

# ── Iterate summaries.json files & upsert ────────────────────────────────
summary_files = list(Path(C.PROCESSED_GIST_ROOT).rglob("summaries.json"))

for file_path in tqdm(summary_files, desc="Repos"):
    repo = file_path.parent.name
    records = json.loads(file_path.read_text(encoding="utf-8"))

    # split into batches
    for i in range(0, len(records), C.EMBED_BATCH):
        chunk = records[i : i + C.EMBED_BATCH]
        vectors = embed_openai([r["summary"] for r in chunk])

        upserts = [
            {
                "id": f"{repo}:{r['id']}",
                "values": v,
                "metadata": {
                    "repo": repo,
                    "path": r["id"],
                    "role": r["role"],
                    "loc" : r["loc"],
                },
            }
            for r, v in zip(chunk, vectors)
        ]

        index.upsert(
            vectors=upserts,
            namespace=C.GIST_NAMESPACE
        )

print("✔︎  All summaries embedded & upserted to Pinecone.")
