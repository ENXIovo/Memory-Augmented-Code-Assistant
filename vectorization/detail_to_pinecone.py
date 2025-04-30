# detail_to_pinecone.py
#!/usr/bin/env python3
"""
detail_to_pinecone.py

Embed all detailed code segments and upsert them to a Pinecone index.
Reads each repo’s `details.json`, calls OpenAI to get embeddings,
creates/connects to a serverless Pinecone index, and batch-upserts.

Requires:
    pip install openai pinecone-client tqdm
"""

import time
import json
import unicodedata
from pathlib import Path
from tqdm import tqdm

import openai
from pinecone import Pinecone, ServerlessSpec
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import config as C

MAX_META_TEXT_BYTES = 40000
MAX_SAFE_BYTES = 30000
TRUNCATED_SUFFIX = "\n...[truncated]"

def safe_truncate_text(text: str) -> str:
    encoded = text.encode("utf-8")
    if len(encoded) <= MAX_SAFE_BYTES:
        return text
    truncated = encoded[:MAX_SAFE_BYTES - len(TRUNCATED_SUFFIX.encode("utf-8"))]
    return truncated.decode("utf-8", errors="ignore") + TRUNCATED_SUFFIX

def normalize_id(s: str) -> str:
    return unicodedata.normalize('NFKD', s).encode('ascii', 'ignore').decode('ascii')

# ── Initialise clients ───────────────────────────────────────────────────
openai.api_key = C.OPENAI_API_KEY
pc = Pinecone(api_key=C.PINECONE_API_KEY)

# ── Create / connect index (serverless) ──────────────────────────────────
if C.DETAIL_INDEX_NAME not in pc.list_indexes().names():
    print(f"[Pinecone] Creating serverless index '{C.DETAIL_INDEX_NAME}' …")
    pc.create_index(
        name=C.DETAIL_INDEX_NAME,
        dimension=C.EMBED_DIMENSION,
        metric="cosine",
        spec=ServerlessSpec(
            cloud="aws",
            region="us-east-1"
        )
    )

# Wait for the index to be ready
while not pc.describe_index(C.DETAIL_INDEX_NAME).status["ready"]:
    time.sleep(1)

index = pc.Index(C.DETAIL_INDEX_NAME)

# ── Helper: batch embed with exponential backoff ─────────────────────────
def embed_texts(texts: list[str]) -> list[list[float]]:
    backoff = 1.0
    while True:
        try:
            resp = openai.embeddings.create(
                model=C.EMBED_MODEL,
                input=texts
            )
            return [d.embedding for d in resp.data]
        except openai.RateLimitError:
            print(f"[OpenAI] Rate limited, sleeping {backoff}s")
            time.sleep(backoff)
            backoff = min(backoff * 2, 60)


# ── Iterate detail files & upsert ────────────────────────────────────────
detail_files = list(Path(C.PROCESSED_DETAIL_ROOT).rglob("details.json"))

for detail_file in tqdm(detail_files, desc="Repos"):
    repo = detail_file.parent.name
    segments = json.loads(detail_file.read_text(encoding="utf-8"))

    for i in range(0, len(segments), C.EMBED_BATCH):
        chunk = segments[i : i + C.EMBED_BATCH]
        texts = [seg["text"] for seg in chunk]
        embeddings = embed_texts(texts)

        vectors = []
        for seg, emb in zip(chunk, embeddings):
            clean_id = normalize_id(seg["id"])
            vectors.append({
                "id": clean_id,
                "values": emb,
                "metadata": {
                    "repo": seg["repo"],
                    "path": seg["path"],
                    "type": seg["type"],
                    "name": seg["name"],
                    "role": seg["role"],
                    "loc": seg["loc"],
                    "text": safe_truncate_text(seg["text"])
                }
            })

        index.upsert(
            vectors=vectors,
            namespace=C.DETAIL_NAMESPACE
        )

print("✔︎ All detailed segments embedded & upserted to Pinecone.")
