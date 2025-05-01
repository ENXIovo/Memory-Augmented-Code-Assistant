#!/usr/bin/env python3
"""
Generate a README.md for a GitHub repo using indexed gist and detail embeddings in Pinecone.
Optimizations included:
- Token-aware truncation (tiktoken)
- Structured prompt formatting
- Improved retrieval prompts
"""
import os
import tiktoken
from pinecone import Pinecone
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_pinecone import PineconeVectorStore
import config as C

# 配置
PINECONE_API_KEY = C.PINECONE_API_KEY
GIST_INDEX    = C.GIST_INDEX_NAME
DETAIL_INDEX  = C.DETAIL_INDEX_NAME
REPO_NAME     = "scikit-learn"
TOP_K_GIST    = 5
TOP_K_DETAIL  = 10
OUTPUT_FILE   = "README-TEST.md"

SUB_QUESTIONS = [
    f"Overview of the {REPO_NAME} project and its purpose",
    f"What are the main components or modules in {REPO_NAME}?",
    f"Installation or setup instructions for {REPO_NAME}",
    f"Key functions, classes or APIs exposed by {REPO_NAME}",
    f"Examples or usage patterns in {REPO_NAME}"
]

# Token 限制（防止 GPT 调用超出 TPM）
MAX_GIST_TOKENS = 4000
MAX_DETAIL_TOKENS = 6000

# 截断函数（基于 tiktoken）
def get_token_length(text: str) -> int:
    enc = tiktoken.encoding_for_model(C.LLM_MODEL)
    return len(enc.encode(text))

def truncate_chunks(chunks, max_tokens):
    result, total = [], 0
    for chunk in chunks:
        tokens = get_token_length(chunk)
        if total + tokens > max_tokens:
            break
        result.append(chunk)
        total += tokens
    return result

# 初始化 Pinecone 客户端
pc = Pinecone(api_key=PINECONE_API_KEY)

# 连接已存在的索引
gist_index   = pc.Index(GIST_INDEX)
detail_index = pc.Index(DETAIL_INDEX)

# 嵌入模型
embeddings = OpenAIEmbeddings(model=C.EMBED_MODEL)

# 向量存储
gist_store = PineconeVectorStore(
    index=gist_index,
    embedding=embeddings,
    namespace=C.GIST_NAMESPACE
)
detail_store = PineconeVectorStore(
    index=detail_index,
    embedding=embeddings,
    namespace=C.DETAIL_NAMESPACE
)

# 检索函数
def retrieve_top_chunks(repo_name: str, questions: list, top_k_gist: int = TOP_K_GIST, top_k_detail: int = TOP_K_DETAIL):
    gist_chunks = []
    for q in questions:
        docs = gist_store.similarity_search(
            query=q,
            k=top_k_gist,
            filter={"repo": repo_name}
        )
        for d in docs:
            meta = d.metadata or {}
            filename = meta.get("path", "unknown")
            gist_chunks.append(f"### {filename}\n{d.page_content.strip()}")

    detail_chunks = []
    for q in questions:
        docs = detail_store.similarity_search(
            query=q,
            k=top_k_detail,
            filter={"repo": repo_name}
        )
        for d in docs:
            meta = d.metadata or {}
            label = f"### [{meta.get('type', 'code')} {meta.get('name', '')} in {meta.get('path', '')}]"
            detail_chunks.append(f"{label}\n{d.page_content.strip()}")

    # 截断到安全的 token 范围
    gist_chunks = truncate_chunks(gist_chunks, MAX_GIST_TOKENS)
    detail_chunks = truncate_chunks(detail_chunks, MAX_DETAIL_TOKENS)

    return gist_chunks, detail_chunks

# 生成 README
EXAMPLE_README_STYLE = """
# Project Name
A short and clear description of what this project does, its purpose, and key goals.

## Installation
Step-by-step instructions for setting up the project.

## Components
An outline of the important files or modules.

## Usage
Code examples or typical workflows.

## API Overview
Key functions, modules or classes with descriptions.
"""

def generate_readme(gist_chunks: list, detail_chunks: list) -> str:
    llm = ChatOpenAI(model=C.LLM_MODEL)
    prompt = (
        "You are an expert technical writer. Using the retrieved documentation below, write a professional, complete, and clear README.md file.\n\n"
        "Use the following README style as reference:\n\n"
        f"{EXAMPLE_README_STYLE}\n\n"
        "Now generate the README based on this information:\n\n"
        f"## File-level Summaries (Gists):\n\n" + "\n\n".join(gist_chunks) +
        f"\n\n## Detail-level Code Units:\n\n" + "\n\n".join(detail_chunks)
    )
    return llm.invoke(prompt).content

# 保存 README
def save_readme(text: str, path: str = OUTPUT_FILE):
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"✅ README saved to {path}")

# 主流程
if __name__ == "__main__":
    print("🔍 Retrieving gist & detail chunks...")
    gist_chunks, detail_chunks = retrieve_top_chunks(REPO_NAME, SUB_QUESTIONS)
    print(f"✅ Retrieved {len(gist_chunks)} gist and {len(detail_chunks)} detail chunks.")
    print("🧠 Generating README...")
    readme_text = generate_readme(gist_chunks, detail_chunks)
    # 构造输出路径
    OUTPUT_DIR = os.path.join("analysis_results", "analysis_results", REPO_NAME)
    OUTPUT_FILE = os.path.join(OUTPUT_DIR, f"{REPO_NAME}_new_readme.md")
    save_readme(readme_text, OUTPUT_FILE)
