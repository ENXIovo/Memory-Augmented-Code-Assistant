#!/usr/bin/env python3
"""
build_gist_from_analysis.py

从 *_analysis.json 文件生成「Gist」级摘要，不做任何网络 / 向量化调用。

每条记录示例：
{
  "id"     : "src/package/foo.py",
  "summary": "Short informative line | classes: Foo, Bar | functions: spam, eggs | imports: numpy, pandas | [src package foo.py]",
  "role"   : "src",              # src | tests | docs | examples | benchmarks | scripts
  "loc"    : 123                 # 非空代码行数
}
"""

from __future__ import annotations
import argparse
import json
import re
import textwrap
from pathlib import Path
from typing import Iterable, List, Sequence

# ────────────────────────── 常量 ────────────────────────── #
DEFAULT_ANALYSIS_ROOT = Path("analysis_results/analysis_results")
DEFAULT_OUTPUT_ROOT   = Path("processed_gist")

MAX_CLASSES   = 6
MAX_FUNCS     = 6
MAX_IMPORTS   = 4
MAX_DOC_SCAN  = 5
MAX_SENT_LEN  = 120          # 单行最大字符
MAX_SUMMARY   = 300          # 整条 summary 最大字符

NOISE_IMPORTS = {
    "os", "sys", "typing", "warnings", "re", "math", "time", "pathlib",
    "contextlib", "itertools", "collections", "__future__", "enum", "logging",
}

DECOR_RE = re.compile(r"^[\W_]{2,}$")      # =====  ----  ****
# ───────────────────────────────────────────────────────── #

# ──────────────── 工具函数 ──────────────── #
def first_sentence(doc: str | None) -> str | None:
    """提取 docstring 中第一句有意义的内容。"""
    if not doc:
        return None

    # materialise -> 保证支持切片
    lines: List[str] = [ln.strip() for ln in doc.splitlines() if ln.strip()]
    for ln in lines[:MAX_DOC_SCAN]:
        if not DECOR_RE.match(ln):
            return ln[:MAX_SENT_LEN]
    return None


def dedup_keep_order(seq: Sequence[str]) -> List[str]:
    """去重并保持顺序（比生成器友好一些）。"""
    seen: set[str] = set()
    out: List[str] = []
    for item in seq:
        if item not in seen:
            seen.add(item)
            out.append(item)
    return out


def detect_role(path: str) -> str:
    parts = {p.lower() for p in Path(path).parts}
    if "tests"       in parts: return "tests"
    if {"docs", "doc"} & parts: return "docs"
    if {"examples", "example"} & parts: return "examples"
    if {"benchmarks", "benchmark"} & parts: return "benchmarks"
    if {"scripts", "bin"} & parts: return "scripts"
    return "src"


def make_summary(fdata: dict) -> str:
    chunks: List[str] = []

    # 1) 描述行（模块 / 类 / 函数 docstring）
    sent = (
        first_sentence(fdata.get("docstring"))
        or (
            fdata.get("classes")                        # 有类
            and first_sentence(fdata["classes"][0].get("docstring"))
        )
        or (
            fdata.get("functions")                      # 有函数
            and first_sentence(fdata["functions"][0].get("docstring"))
        )
    )
    if   sent:                                  chunks.append(sent)
    elif Path(fdata["file_path"]).name == "__init__.py":
                                                chunks.append("Package initializer")
    else:                                       chunks.append("No description")

    # 2) 标识符
    cls = dedup_keep_order(c["name"] for c in fdata.get("classes", []))[:MAX_CLASSES]
    fn  = dedup_keep_order(f["name"] for f in fdata.get("functions", []))[:MAX_FUNCS]
    if cls: chunks.append(f"classes: {', '.join(cls)}")
    if fn : chunks.append(f"functions: {', '.join(fn)}")

    # 3) imports（过滤噪声模块）
    mods = []
    for imp in fdata.get("imports", []):
        base = (imp.get("module") or "").split(".")[0]
        if base and base not in NOISE_IMPORTS:
            mods.append(base)
    mods = dedup_keep_order(mods)[:MAX_IMPORTS]
    if mods:
        chunks.append(f"imports: {', '.join(mods)}")

    # 4) 路径 token
    path_tok = fdata["file_path"].replace("\\", " ").replace("/", " ")
    chunks.append(f"[{path_tok}]")

    # 5) 总长裁剪
    return " | ".join(chunks)[:MAX_SUMMARY]


# ──────────────── 主流程 ──────────────── #
def process_repo(json_path: Path, out_root: Path) -> None:
    repo_name = json_path.stem.replace("_analysis", "")
    out_dir   = out_root / repo_name
    out_dir.mkdir(parents=True, exist_ok=True)
    out_file  = out_dir / "summaries.json"

    with json_path.open(encoding="utf-8") as fh:
        data = json.load(fh)

    records = []
    for fdata in data.get("files", []):
        if fdata.get("language") != "Python":
            continue
        records.append(
            {
                "id"     : fdata["file_path"],
                "summary": make_summary(fdata),
                "role"   : detect_role(fdata["file_path"]),
                "loc"    : fdata.get("loc", 0),
            }
        )

    if not records:
        print(f"[skip] {repo_name:>20}: no Python files")
        return

    with out_file.open("w", encoding="utf-8") as fh:
        json.dump(records, fh, ensure_ascii=False, indent=2)

    print(f"[OK]   {repo_name:>20}: {len(records):5} summaries → {out_file}")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Build compact gist-level summaries from *_analysis.json files",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=textwrap.dedent(
            """\
            默认目录结构：
              analysis_results/analysis_results/<repo>/<repo>_analysis.json
              processed_gist/<repo>/summaries.json
            """
        ),
    )
    parser.add_argument("--analysis-root", type=Path, default=DEFAULT_ANALYSIS_ROOT)
    parser.add_argument("--output-root",   type=Path, default=DEFAULT_OUTPUT_ROOT)
    args = parser.parse_args()

    if not args.analysis_root.is_dir():
        raise SystemExit(f"Analysis folder not found: {args.analysis_root}")

    args.output_root.mkdir(exist_ok=True)

    repos = [p for p in args.analysis_root.iterdir() if p.is_dir()]
    total = len(repos)
    for idx, repo_dir in enumerate(repos, 1):
        json_path = repo_dir / f"{repo_dir.name}_analysis.json"
        if json_path.exists():
            process_repo(json_path, args.output_root)
        else:
            print(f"[skip] {repo_dir.name:>20}: analysis json missing")
        if idx % 10 == 0 or idx == total:
            print(f"  …{idx}/{total} processed")

    print("✔︎  Gist dataset refreshed.")


if __name__ == "__main__":
    main()
