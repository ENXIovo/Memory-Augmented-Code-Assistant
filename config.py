# config.py
"""
Project-wide configuration constants.
All settings are defined here; no need to modify other code files.
"""

import os
from pathlib import Path

# ── Pinecone configuration ───────────────────────────────────────────────
# API key for authenticating with Pinecone (required)
PINECONE_API_KEY     = os.environ["PINECONE_API_KEY"]
# Name of the Pinecone index for file-level summaries
GIST_INDEX_NAME      = "repo-gist-index"
# Namespace within the Pinecone index for Gist-level entries
GIST_NAMESPACE       = "gist"
DETAIL_INDEX_NAME       = "repo-detail-index"
DETAIL_NAMESPACE        = "detail"

# ── OpenAI Embedding Model ──────────────────────────────────────────────
OPENAI_API_KEY  = os.environ["OPENAI_API_KEY"]                 # required
EMBED_MODEL     = "text-embedding-3-small"                     # 1,536-D
EMBED_DIMENSION         = 1536

# ── Local data paths ───────────────────────────────────────────────────
# processed_gist/<repo>/summaries.json 由 build_gist_from_analysis.py 生成
PROCESSED_GIST_ROOT = Path("processed_gist")
PROCESSED_DETAIL_ROOT = Path("processed_detail")

# batch size for embedding calls
EMBED_BATCH = 96

LLM_MODEL = "gpt-4o"