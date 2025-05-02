# Memory-Augmented Code Assistant: Automatic README Generation for Large Repositories

This project introduces **MACA**, a retrieval-augmented generation (RAG) system that automatically generates high-quality `README.md` files for large, under-documented code repositories using code parsing, vector memory, and LLM reasoning.

## 🚀 Overview

MACA takes as input a raw source code repository and produces a complete, human-readable README covering:

- Project purpose and functionality
- Setup and installation steps
- File structure (depth-limited)
- Key modules and usage examples
- Dependencies and APIs

## 🧠 Technical Pipeline

MACA adopts a four-stage architecture:

1. **Static Code Parsing**  
   Extract file-level gists and code-unit details (functions, classes, metadata) using AST parsing.

2. **Dual-layer Vector Memory**  
   Embed both gists and details using `text-embedding-3-small` and store them in **Pinecone** across two namespaces.

3. **Prompt Decomposition & Retrieval**  
   Split README generation into five targeted queries (purpose, usage, setup, structure, key modules), retrieve top-$k$ chunks per layer, and merge with the repo directory tree.

4. **README Generation & Evaluation**  
   Feed aggregated context into **GPT-4o**, which generates the README using a structured prompt. Quality is measured via **GPT-based rubric scoring** and **QA-based answerability tests**.

## 📊 Evaluation Metrics

We evaluate README quality using:

- ✅ **GPT Rubric Score** (Completeness, Clarity, Accuracy, Similarity, Structure, Fluency)
- ✅ **QA Answerability** (Can a developer answer 6 key questions from the README?)
- 🔍 Traditional metrics (for reference only): **BERTScore**, **METEOR**, **WMD**

> 📈 MACA improved GPT-rubric scores from **0.71 → 0.85** and doubled QA answerability from **0.22 → 0.70** across 9 real-world Python repositories.

## 📂 Project Status

- [x] Data collection and preprocessing
- [x] AST-based summarization baseline
- [x] Dual-layer embedding + Pinecone vector store
- [x] GPT-based README generation pipeline
- [x] GPT-based evaluation framework (rubric + QA)
- [x] Final report and submission

## 🧪 Compared to Prior Work

| Tool           | Focus                          | Our Advantage                      |
|----------------|--------------------------------|------------------------------------|
| `readme-ai`    | AST-based summarization        | Ours adds semantic vector memory   |
| `RepoAgent`    | RAG for code query             | We target full README generation   |
| `Cursor-AI`    | IDE in-context support         | We’re editor-agnostic and offline  |

## 📚 References

- [readme-ai](https://github.com/eli64s/readme-ai)
- [RepoAgent (arXiv 2402.16667)](https://arxiv.org/abs/2402.16667)
- [Recursive Summarization (Yao et al. 2023)](https://arxiv.org/abs/2305.14314)
- [LLMEval (Liu et al. 2024)](https://arxiv.org/abs/2402.13929)
- "Lift Yourself Up: Retrieval-Augmented Text Generation with Self Memory"
- "Bridging Relevance and Reasoning: Rationale Distillation in RAG"

## 📅 Milestones

- ✅ Feb 12 – Proposal submitted  
- ✅ Feb 28 – Data + baseline complete  
- ✅ Apr 25 – Poster presented  
- ✅ May 1 – Final report submitted
