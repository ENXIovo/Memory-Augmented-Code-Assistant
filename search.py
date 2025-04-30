import os
import pinecone
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Pinecone as LangchainPinecone
from langchain.llms import OpenAI

# --- 配置你的密钥和索引信息 ---
os.environ["OPENAI_API_KEY"] = "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"
PINECONE_API_KEY = "pcsk_7UkkDg_6ihCp883iLLthEBfRa9e1BXCDBTJzFCryyqjjLCaoEtobByTatuN1kZGrN96UVN"
PINECONE_ENV = "us-east-1-aws"
GIST_INDEX = "repo-gist-index"
DETAIL_INDEX = "repo-detail-index"
REPO_NAME = "django"
TOP_K_GIST = 5
TOP_K_DETAIL = 10
OUTPUT_FILE = "README.md"

SUB_QUESTIONS = [
    "What is the purpose of this project?",
    "What are the key modules or components?",
    "How can I install or set it up?",
    "What are the important functions or APIs?",
    "Are there any examples or usage instructions?"
]

# ---------- 初始化 Pinecone ----------
pinecone.init(api_key=PINECONE_API_KEY, environment=PINECONE_ENV)
embedding = OpenAIEmbeddings()

# ---------- 多轮检索 gist 和 detail ----------
def retrieve_top_chunks(repo_name: str, questions: list, top_k_gist=5, top_k_detail=10):
    # gist summaries
    gist_store = LangchainPinecone.from_existing_index(GIST_INDEX, embedding)
    gist_chunks = set()
    for q in questions:
        results = gist_store.similarity_search(query=q, k=top_k_gist, filter={"repo": repo_name})
        for r in results:
            gist_chunks.add(r.page_content.strip())

    # detail code chunks
    detail_store = LangchainPinecone.from_existing_index(DETAIL_INDEX, embedding)
    detail_chunks = set()
    for q in questions:
        results = detail_store.similarity_search(query=q, k=top_k_detail, filter={"repo": repo_name})
        for r in results:
            # 拼接函数信息
            meta = r.metadata
            code_label = f"[{meta.get('type', 'code')} {meta.get('name', '')} in {meta.get('path', '')}]:"
            detail_chunks.add(code_label + "\n" + r.page_content.strip())

    return list(gist_chunks), list(detail_chunks)

# ---------- 构造 prompt 并生成 README ----------
def generate_readme(gist_chunks, detail_chunks):
    llm = OpenAI(model="gpt-4o")
    prompt = (
        "Below are two types of retrieved information from a GitHub repository:\n\n"
        "1. **File-level summaries** (high-level descriptions of files)\n"
        "2. **Detail-level code units** (important class/function definitions)\n\n"
        "Please use these to generate a comprehensive, clear, and well-structured README.md file in English. "
        "It should include: project purpose, key components, installation, important functions, and examples.\n\n"
        "## File-level Summaries (Gists):\n"
        + "\n\n".join(gist_chunks) +
        "\n\n## Detail-level Functions and Classes:\n"
        + "\n\n".join(detail_chunks)
    )
    return llm.invoke(prompt)

# ---------- 保存到文件 ----------
def save_readme(text: str, path="README.md"):
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"✅ README saved to: {path}")

# ---------- 主流程 ----------
if __name__ == "__main__":
    print("🔍 Retrieving summaries from both gist and detail indexes...")
    gist_chunks, detail_chunks = retrieve_top_chunks(REPO_NAME, SUB_QUESTIONS, TOP_K_GIST, TOP_K_DETAIL)

    print(f"✅ Retrieved {len(gist_chunks)} gist chunks and {len(detail_chunks)} detail chunks.")

    print("🧠 Generating README with GPT...")
    readme = generate_readme(gist_chunks, detail_chunks)

    save_readme(readme, OUTPUT_FILE)