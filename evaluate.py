import os
import nltk
import pandas as pd
import gensim
from rouge_score import rouge_scorer
from nltk.translate.bleu_score import sentence_bleu
from nltk.translate.meteor_score import meteor_score
from bert_score import score
from gensim.models import KeyedVectors
from nltk.translate.bleu_score import SmoothingFunction
import gensim.downloader as api

# 确保下载所需的NLTK资源
nltk.download('wordnet')
nltk.download('punkt_tab')
nltk.download('punkt')

# 设定路径
repo_names = [
    "django", "fastapi", "flask", "numpy",
    "pandas", "pytorch", "readme-ai", "requests", "scikit-learn"
]
base_dir = "analysis_results/cloned_repos"
analysis_dir = "analysis_results/analysis_results"


# 读取原始 README（.md 或 .rst）
def read_original_readme(repo_name):
    md_path = os.path.join(base_dir, repo_name, repo_name, "README.md")
    rst_path = os.path.join(base_dir, repo_name, repo_name, "README.rst")
    fallback_path = os.path.join(base_dir, repo_name, "README")  # 处理无后缀情况

    if os.path.exists(md_path):
        with open(md_path, "r", encoding="utf-8") as f:
            return f.read()
    elif os.path.exists(rst_path):
        with open(rst_path, "r", encoding="utf-8") as f:
            return f.read()
    elif os.path.exists(fallback_path):
        with open(fallback_path, "r", encoding="utf-8") as f:
            return f.read()
    return ""


# 读取 AST 生成的 README
def read_ast_readme(repo_name):
    ast_path = os.path.join(analysis_dir, repo_name, f"{repo_name}_new_readme.md")
    if os.path.exists(ast_path):
        with open(ast_path, "r", encoding="utf-8") as f:
            return f.read()
    return ""


# 计算 Flesch-Kincaid Grade Level (FKGL)
def compute_fkgl(text):
    sentences = nltk.sent_tokenize(text)
    words = nltk.word_tokenize(text)
    syllables = sum(len(nltk.word_tokenize(word)) for word in words)

    num_sentences = max(len(sentences), 1)
    num_words = max(len(words), 1)

    fkgl = 0.39 * (num_words / num_sentences) + 11.8 * (syllables / num_words) - 15.59
    return round(fkgl, 2)

# 选择替代的 Word2Vec 预训练模型
def load_word2vec_model(model):
    try:
        print("Loading Word2Vec model...")
        model = api.load(model)  # 你可以换成其他模型
        print("Word2Vec model loaded successfully!")
        return model
    except Exception as e:
        print(f"Failed to load Word2Vec model: {e}")
        return None

def compute_wmd(reference, hypothesis, model):
    # 加载 Word2Vec
    w2v_model = load_word2vec_model(model)
    if w2v_model is None:
        print("⚠ WMD not computed: Word2Vec model not available.")
        return -1  # 返回默认值
    try:
        ref_tokens = nltk.word_tokenize(reference)
        hyp_tokens = nltk.word_tokenize(hypothesis)
        wmd_score = w2v_model.wmdistance(ref_tokens, hyp_tokens)
        return round(wmd_score, 2)
    except Exception as e:
        print(f"⚠ Error computing WMD: {e}")
        return -1

# 计算各种指标
def compute_metrics(reference, hypothesis):
    # # 计算 Rouge-L
    # rouge = rouge_scorer.RougeScorer(["rougeL"], use_stemmer=True)
    # rouge_l = rouge.score(reference, hypothesis)["rougeL"].fmeasure

    # 计算 BLEU
    ref_tokens = nltk.word_tokenize(reference)
    hyp_tokens = nltk.word_tokenize(hypothesis)
    # smooth = SmoothingFunction().method1
    # bleu = sentence_bleu([ref_tokens], hyp_tokens, smoothing_function=smooth)

    # 计算 METEOR
    meteor = meteor_score([ref_tokens], hyp_tokens)  # 这里要传入列表

    # 计算 BERTScore
    if isinstance(hypothesis, str) and isinstance(reference, str):
        hyp_tokens = nltk.word_tokenize(hypothesis)  # 先分词
        ref_tokens = nltk.word_tokenize(reference)

        P, R, F1 = score([" ".join(hyp_tokens)], [" ".join(ref_tokens)], lang="en", verbose=False)
        bertscore = F1.mean().item()
    else:
        print(f"  ⚠ Skipping BERTScore computation (invalid input)")
        bertscore = -1

    # 计算 FKGL（可读性评分）
    # fkgl = compute_fkgl(hypothesis)

    # 计算 WMD（需要 Word2Vec 预训练模型）
    wmd = compute_wmd(reference, hypothesis, "glove-wiki-gigaword-100")

    # another WMD model
    wmd2 = compute_wmd(reference, hypothesis, "glove-wiki-gigaword-50")

    return meteor, bertscore, wmd, wmd2

gpt = [0.45, 0.43, 0.47, 0.46, 0.45, 0.44, 0.43, 0.52, 0.43]  # 手动输入的数据

# **确保数据数量匹配**
if len(gpt) != len(repo_names):
    raise ValueError("Manual data length must match number of repositories!")

# 遍历所有 README 进行评估
results = []
for i, repo in enumerate(repo_names):
    print(f"\nProcessing repository: {repo}")

    ref_text = read_original_readme(repo)
    ast_text = read_ast_readme(repo)

    # 检查文件是否正确读取
    if not ref_text:
        print(f"  Warning: Original README not found for {repo}")
        continue
    if not ast_text:
        print(f"  Warning: AST README not found for {repo}")
        continue

    # 计算指标
    try:
        meteor, bertscore, wmd, wmd2 = compute_metrics(ref_text, ast_text)
        results.append({
            "Readme": repo.upper(),
            # "Rouge-L": round(rouge_l, 2),
            # "BLEU": round(bleu, 2),
            "METEOR": round(meteor, 2),
            "BERTScore F1": round(bertscore, 2),
            # "FKGL": fkgl,
            "WMD(glove-wiki-gigaword-100)": wmd,
            "WMD(glove-wiki-gigaword-50)": wmd2,
            "GPT4": gpt[i]
        })
    except Exception as e:
        print(f"  Error computing metrics for {repo}: {e}")

# 转换为 DataFrame 并打印表格
df = pd.DataFrame(results)

average_row = {
    "Readme": "AVERAGE",
    # "Rouge-L": round(df["Rouge-L"].mean(), 2),
    # "BLEU": round(df["BLEU"].mean(), 2),
    "METEOR": round(df["METEOR"].mean(), 2),
    "BERTScore F1": round(df["BERTScore F1"].mean(), 2),
    # "FKGL": round(df["FKGL"].mean(), 2),
    "WMD(glove-wiki-gigaword-100)": round(df["WMD(glove-wiki-gigaword-100)"].mean(), 2),
    "WMD(glove-wiki-gigaword-50)": round(df["WMD(glove-wiki-gigaword-50)"].mean(), 2),
    "GPT4": round(sum(gpt) / len(gpt), 2)
}
df = df.append(average_row, ignore_index=True)

if df.empty:
    print("No results to display. Check if AST-generated files exist.")
else:
    print(df.to_markdown(index=False))  # 以 Markdown 格式输出表格
