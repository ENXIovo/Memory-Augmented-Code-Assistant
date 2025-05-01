import os
import json
import pandas as pd
from openai import OpenAI
import config as c
import re
import matplotlib.pyplot as plt

# 初始化新版 SDK 客户端
client = OpenAI(api_key=c.OPENAI_API_KEY)

# ========== 基础设置 ==========
repo_names = [
    "django", "fastapi", "flask", "numpy",
    "pandas", "pytorch", "readme-ai", "requests", "scikit-learn"
]

base_dir = "analysis_results/cloned_repos"
analysis_dir = "analysis_results/analysis_results"

expected_sections = [
    "Project Title", "Introduction", "Installation", "Usage", "Directory Structure",
    "Key Components", "Examples", "License", "API Overview"
]

qa_questions = [
    "How to install the project?",
    "What is the project used for?",
    "How to run a basic example?",
    "What are the key components or modules?",
    "Is there an API or interface provided?",
    "How is the code organized?"
]

# ========== 工具函数 ==========
def read_file(path: str) -> str:
    return open(path, encoding="utf-8").read() if os.path.exists(path) else ""

def read_generated_readme(repo: str) -> str:
    return read_file(os.path.join(analysis_dir, repo, f"{repo}_README.md"))

def read_generated_readme_improved(repo: str) -> str:
    return read_file(os.path.join(analysis_dir, repo, f"{repo}_new_readme.md"))

def read_original_readme(repo: str) -> str:
    for name in ["README.md", "README.rst", "README"]:
        p1 = os.path.join(base_dir, repo, repo, name)
        p2 = os.path.join(base_dir, repo, name)
        content = read_file(p1) or read_file(p2)
        if content:
            return content
    return ""

def gpt_score_prompt(original: str, generated: str) -> str:
    return f"""
You are an expert software developer. Given the following AI-generated README and the original README, evaluate the AI-generated README on a scale of 0 to 1 (higher is better, retain two decimal places) for:

1. **Completeness**: Does it include all necessary sections (e.g., installation, usage, dependencies)?
2. **Clarity**: Is it easy to understand?
3. **Accuracy**: Does it correctly describe the project?
4. **Similarity**: Is it similar to the original readme?
5. **Structure**: Is the format well-structured and typical of good open source READMEs?
6. **Fluency**: Is the writing smooth and natural?

Respond with a JSON object like:
{{"Completeness": 0.85, "Clarity": 0.90, "Accuracy": 0.80, "Similarity": 0.88, "Structure": 0.93, "Fluency": 0.91}}

Original README:
\"\"\"
{original[:3000]}
\"\"\"

Generated README:
\"\"\"
{generated[:3000]}
\"\"\"
"""

def qa_score_prompt(readme: str) -> str:
    questions = "\n".join([f"{i+1}. {q}" for i, q in enumerate(qa_questions)])
    return f"""
You are an AI evaluator. Given the following README and a list of user questions, determine how many of the questions can be directly and correctly answered using only the README.

README:
\"\"\"
{readme[:3500]}
\"\"\"

Questions:
{questions}

Return the number of questions you can confidently answer, as an integer out of {len(qa_questions)}.
"""

def parse_gpt_score(text: str) -> dict:
    keys = ["Completeness", "Clarity", "Accuracy", "Similarity", "Structure", "Fluency"]
    scores = {}
    for key in keys:
        match = re.search(rf"{key}[^0-9]*([01](?:\.\d+)?)", text, re.IGNORECASE)
        if match:
            scores[key] = round(float(match.group(1)), 2)
    return scores

def extract_qa_score(text: str, total: int) -> float:
    match = re.search(r"(\d+)\s*(?:out of|/)\s*%s" % total, text, re.IGNORECASE)
    if match:
        answered = int(match.group(1))
    else:
        # fallback: 抓第一个独立数字小于等于 total 的
        numbers = re.findall(r"\b\d+\b", text)
        numbers = [int(n) for n in numbers if int(n) <= total]
        answered = numbers[0] if numbers else 0
    return round(answered / total, 2)

# ========== 主流程 ==========
results = []

for repo in repo_names:
    gen = read_generated_readme(repo)
    orig = read_original_readme(repo)
    if not gen or not orig:
        continue

    gpt_response = client.chat.completions.create(
        model=c.LLM_MODEL,
        messages=[{"role": "user", "content": gpt_score_prompt(orig, gen)}]
    )
    gpt_raw = gpt_response.choices[0].message.content
    gpt_scores = parse_gpt_score(gpt_raw)
    gpt_avg = round(sum(gpt_scores.values()) / len(gpt_scores), 2)

    qa_response = client.chat.completions.create(
        model=c.LLM_MODEL,
        messages=[{"role": "user", "content": qa_score_prompt(gen)}]
    )
    qa_text = qa_response.choices[0].message.content
    qa_score = extract_qa_score(qa_text, total=len(qa_questions))

    results.append({
        "Readme": repo.upper(),
        "QA": qa_score,
        **gpt_scores,
        "GPTScore Avg": gpt_avg
    })

# ========== 输出 ==========
df = pd.DataFrame(results)
df.loc["AVERAGE"] = df.drop(columns=["Readme"]).mean(numeric_only=True)
df["Readme"] = df["Readme"].fillna("AVERAGE")

results_improved = []

for repo in repo_names:
    gen = read_generated_readme_improved(repo)
    orig = read_original_readme(repo)
    if not gen or not orig:
        continue

    gpt_response = client.chat.completions.create(
        model=c.LLM_MODEL,
        messages=[{"role": "user", "content": gpt_score_prompt(orig, gen)}]
    )
    gpt_raw = gpt_response.choices[0].message.content
    gpt_scores = parse_gpt_score(gpt_raw)
    gpt_avg = round(sum(gpt_scores.values()) / len(gpt_scores), 2)

    qa_response = client.chat.completions.create(
        model=c.LLM_MODEL,
        messages=[{"role": "user", "content": qa_score_prompt(gen)}]
    )
    qa_text = qa_response.choices[0].message.content
    qa_score = extract_qa_score(qa_text, total=len(qa_questions))

    results_improved.append({
        "Readme": repo.upper(),
        "QA": qa_score,
        **gpt_scores,
        "GPTScore Avg": gpt_avg
    })

# 转 DataFrame
df_improved = pd.DataFrame(results_improved)
df_improved.loc["AVERAGE"] = df_improved.drop(columns=["Readme"]).mean(numeric_only=True)
df_improved["Readme"] = df_improved["Readme"].fillna("AVERAGE")

# ========== 输出两个表格 ==========

print("\n=== Baseline README Evaluation ===")
print(df.round(2).to_markdown(index=False))

print("\n=== Improved README Evaluation ===")
print(df_improved.round(2).to_markdown(index=False))

# ========== 柱状图对比 ==========

baseline_df = df.copy()
improved_df = df_improved.copy()
baseline_df["Type"] = "Baseline"
improved_df["Type"] = "Improved"

# 合并对比
combined_df = pd.concat([baseline_df, improved_df], ignore_index=True)
metrics = ["Completeness", "Clarity", "Accuracy", "Similarity", "Structure", "Fluency", "QA"]
bar_data = combined_df.groupby("Type")[metrics].mean().T

# 画图
ax = bar_data.plot(kind="bar", figsize=(10, 6), title="Baseline vs Improved README Scores")
ax.set_ylabel("Score")
ax.set_ylim(0, 1)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
