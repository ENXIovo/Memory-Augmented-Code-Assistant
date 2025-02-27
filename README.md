# Memory-Augmented Code Assistant: Automatic README Generation for Large Repositories

This project aims to automatically analyze large code repositories lacking proper documentation, summarize their code structure, and generate high-quality README files that help developers quickly understand complex codebases.

## 🚀 Project Overview

The system scans an entire code repository, analyzes its structure and content, and produces a comprehensive README that includes:

- Project description and purpose
- Installation and setup instructions
- File structure with descriptions
- Key components and their relationships
- Technologies and dependencies used
- Basic usage examples

## 🛠️ Technical Approach

Our approach uses a multi-stage pipeline:

1. **Code Analysis**: Extract repository structure, important functions, classes, dependencies, and code comments using AST (Abstract Syntax Tree) parsing
2. **Information Processing**: Generate embeddings for code artifacts and store them in a vector database
3. **Context-Aware Summarization**: Leverage large language models to query and synthesize information from the vector database
4. **README Generation**: Structure the extracted insights into a standardized, human-readable README format

## 📊 Evaluation Metrics

We evaluate our system using the following metrics:

- **ROUGE-L**: Measures sequence overlap between generated and reference READMEs
- **BERTScore**: Semantic similarity evaluation using contextual embeddings
- **BLEU**: N-gram precision between generated and reference text
- **METEOR**: Evaluates machine translation quality
- **FKGL**: Flesch-Kincaid Grade Level to assess readability
- **WMD**: Word Mover's Distance for semantic similarity

## 📋 Project Status

Current progress:
- [x] Project setup and requirements definition
- [x] Research on existing solutions and baselines
- [x] Data collection and preprocessing
- [x] AST-based code structure extraction
- [ ] Vector database integration
- [ ] README generation module
- [ ] Evaluation pipeline
- [ ] Performance benchmarking

## 🔄 Comparison with Existing Solutions

We build upon but differentiate from existing tools:
- **readme-ai**: Our approach focuses on more robust code understanding through improved embedding strategies
- **RepoAgent**: We emphasize better hierarchical representation of code structures
- **Cursor-AI**: Unlike IDE-specific solutions, we provide a standalone tool for documentation generation

## 🔍 References

1. [readme-ai](https://github.com/eli64s/readme-ai) - Similar approach for README generation
2. [RepoAgent: Large Language Model Code Analysis and Beyond](https://arxiv.org/abs/2402.16667)
3. [Cursor-AI](https://www.cursor.com/) - VSCode extension for in-context code understanding
4. "Recursively Summarizing Enables Long-Term Dialogue Memory in Large Language Models"
5. "Enhancing Long-Term Memory using Hierarchical Aggregate Tree for Retrieval Augmented Generation"
6. "Impossible Distillation: from Low-Quality Model to High-Quality Dataset & Model for Summarization and Paraphrasing"
7. "Lift Yourself Up: Retrieval-augmented Text Generation with Self Memory"
8. "Bridging Relevance and Reasoning: Rationale Distillation in Retrieval-Augmented Generation"

## 📅 Project Timeline

- Milestone 1: Project Proposal (February 12, 2025)
- Milestone 2: Data and Baseline (February 28, 2025)
- Milestone 3: Poster Presentation (April 25, 2025)
- Milestone 4: Final Project Report (May 1, 2025)
