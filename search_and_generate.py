#!/usr/bin/env python3
"""
Generate a README.md for a GitHub repo using indexed gist and detail embeddings
in Pinecone, with the real file system directory structure included in the prompt.
"""

import os
import tiktoken
from typing import Any, List

from pinecone import Pinecone
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_pinecone import PineconeVectorStore

import config as C

# ====== Configuration ======
PINECONE_API_KEY = C.PINECONE_API_KEY
GIST_INDEX       = C.GIST_INDEX_NAME
DETAIL_INDEX     = C.DETAIL_INDEX_NAME
REPO_NAME        = "scikit-learn"
TOP_K_GIST       = 5
TOP_K_DETAIL     = 10
REPO_PATH = os.path.join("analysis_results", "cloned_repos", REPO_NAME)

OUTPUT_DIR = os.path.join("analysis_results", "analysis_results", REPO_NAME)
os.makedirs(OUTPUT_DIR, exist_ok=True)
OUTPUT_FILE = os.path.join(OUTPUT_DIR, f"{REPO_NAME}_new_readme.md")

SUB_QUESTIONS = [
    f"Overview of the {REPO_NAME} project and its purpose",
    f"What are the main components or modules in {REPO_NAME}?",
    f"Installation or setup instructions for {REPO_NAME}",
    f"Key functions, classes or APIs exposed by {REPO_NAME}",
    f"Examples or usage patterns in {REPO_NAME}"
]

MAX_GIST_TOKENS   = 4000
MAX_DETAIL_TOKENS = 6000


# ====== Utility functions ======
def get_token_length(text: str) -> int:
    enc = tiktoken.encoding_for_model(C.LLM_MODEL)
    return len(enc.encode(text))

def truncate_chunks(chunks: List[str], max_tokens: int) -> List[str]:
    result, total = [], 0
    for chunk in chunks:
        tokens = get_token_length(chunk)
        if total + tokens > max_tokens:
            break
        result.append(chunk)
        total += tokens
    return result

def build_directory_tree_fs(repo_root: str, max_depth: int = 2) -> str:
    """Scan the actual file system to generate the directory tree string."""
    tree: List[str] = []
    for root, dirs, files in os.walk(repo_root):
        level = root.replace(repo_root, "").count(os.sep)
        if level > max_depth:
            continue
        indent = "    " * level
        tree.append(f"{indent}├── {os.path.basename(root)}/")
        subindent = "    " * (level + 1)
        for f in files:
            tree.append(f"{subindent}└── {f}")
    return "\n".join(tree)


# ====== Pinecone Setup ======
pc = Pinecone(api_key=PINECONE_API_KEY)

gist_index   = pc.Index(GIST_INDEX)
detail_index = pc.Index(DETAIL_INDEX)

embeddings = OpenAIEmbeddings(model=C.EMBED_MODEL)

gist_store = PineconeVectorStore(index=gist_index,   embedding=embeddings, namespace=C.GIST_NAMESPACE)
detail_store = PineconeVectorStore(index=detail_index, embedding=embeddings, namespace=C.DETAIL_NAMESPACE)


# ====== Vector Retrieval ======
def retrieve_top_chunks(repo_name: str) -> tuple[list[str], list[str]]:
    seen_gist = set()
    seen_detail = set()
    gist_chunks = []
    detail_chunks = []

    for q in SUB_QUESTIONS:
        gist_docs = gist_store.similarity_search(query=q, k=TOP_K_GIST, filter={"repo": repo_name})
        for d in gist_docs:
            key = (d.metadata.get("path", ""), d.page_content.strip())
            if key not in seen_gist:
                seen_gist.add(key)
                gist_chunks.append(f"### {key[0]}\n{key[1]}")

        detail_docs = detail_store.similarity_search(query=q, k=TOP_K_DETAIL, filter={"repo": repo_name})
        for d in detail_docs:
            key = (d.metadata.get("type", ""), d.metadata.get("name", ""), d.metadata.get("path", ""), d.page_content.strip())
            if key not in seen_detail:
                seen_detail.add(key)
                label = f"### [{key[0]} {key[1]} in {key[2]}]"
                detail_chunks.append(f"{label}\n{key[3]}")

    gist_chunks = truncate_chunks(gist_chunks, MAX_GIST_TOKENS)
    detail_chunks = truncate_chunks(detail_chunks, MAX_DETAIL_TOKENS)
    return gist_chunks, detail_chunks


# ====== README Prompt & Generation ======
EXAMPLE_README_STYLE = """
# Project Name
A short and clear description of what this project does, its purpose, and key goals.

## Project Structure
A three-level directory tree of the project, with brief descriptions where possible.

## Installation
Step-by-step instructions for setting up the project.

## Components
An outline of the important files or modules.

## Usage
Code examples or typical workflows.

## API Overview
Key functions, modules or classes with descriptions.
""".strip()

def generate_readme(gist_chunks: list[str], detail_chunks: list[str], dir_tree: str) -> str:
    """Generate the README using GPT and the given context."""
    llm = ChatOpenAI(model=C.LLM_MODEL)
    prompt = (
        "You are an expert technical writer. "
        "Use the directory structure and retrieved documentation below to write a polished README.\n\n"
        f"## Directory Structure\n```\n{dir_tree}\n```\n\n"
        "Follow this README style template:\n\n"
        f"{EXAMPLE_README_STYLE}\n\n"
        "Now generate the README based on:\n\n"
        f"## File-level Summaries (Gists):\n\n" + "\n\n".join(gist_chunks) +
        f"\n\n## Detail-level Code Units:\n\n" + "\n\n".join(detail_chunks)
    )
    print(prompt)
    return llm.invoke(prompt).content


def save_readme(text: str, path: str) -> None:
    """Save the generated README to file."""
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"✅ README saved to {path}")


# ====== Main Process ======
if __name__ == "__main__":
    print("🔍 Retrieving gist & detail chunks ...")
    gist_chunks, detail_chunks = retrieve_top_chunks(REPO_NAME)
    print(f"✅ Retrieved {len(gist_chunks)} gist and {len(detail_chunks)} detail chunks.")

    print("📁 Building real directory tree from filesystem ...")
    dir_tree_str = build_directory_tree_fs(REPO_PATH)
    print("✅ Directory tree built from file system.")

    print("🧠 Generating README via GPT ...")
    readme_text = generate_readme(gist_chunks, detail_chunks, dir_tree_str)

    save_readme(readme_text, OUTPUT_FILE)
