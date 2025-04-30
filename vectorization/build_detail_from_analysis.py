#!/usr/bin/env python3
"""
build_detail_from_analysis.py

Generate per-function / per-class code snippets from the AST analysis JSON,
ready for vectorization. Emits a `details.json` in each repo’s output folder.

Each record in details.json:
{
  "id"   : "<repo>:<file_path>:<type>:<name>:chunk<index>",
  "text" : "<source code chunk>",
  "repo" : "<repo>",
  "path" : "<file_path>",
  "type" : "function" | "class",
  "name" : "<function_or_class_name>",
  "loc"  : <line number>,
  "role" : "<src|tests|docs|examples|benchmarks|scripts>"
}
"""
import json
import argparse
from pathlib import Path

import tiktoken  # pip install tiktoken

# 调整最大 token 数和重叠数
MAX_TOKENS = 8000
OVERLAP   = 200
ENC_MODEL = "text-embedding-3-small"  # 或你要用的 embedding 模型

def detect_role(path: str) -> str:
    parts = {p.lower() for p in Path(path).parts}
    if 'tests' in parts:
        return 'tests'
    if 'docs' in parts or 'doc' in parts:
        return 'docs'
    if 'examples' in parts or 'example' in parts:
        return 'examples'
    if 'benchmarks' in parts or 'benchmark' in parts:
        return 'benchmarks'
    if 'scripts' in parts or 'bin' in parts:
        return 'scripts'
    return 'src'

def split_by_tokens(text: str, enc, max_tokens: int, overlap: int):
    """将长文本按 token 数切分，返回若干文本片段。"""
    token_ids = enc.encode(text)
    chunks = []
    step = max_tokens - overlap
    for i in range(0, len(token_ids), step):
        chunk_ids = token_ids[i : i + max_tokens]
        chunks.append(enc.decode(chunk_ids))
        if i + max_tokens >= len(token_ids):
            break
    return chunks

def process_repo(analysis_file: Path, output_root: Path) -> None:
    repo = analysis_file.parent.name
    out_dir = output_root / repo
    out_dir.mkdir(parents=True, exist_ok=True)
    out_file = out_dir / 'details.json'

    # 初始化 tiktoken 编码器
    enc = tiktoken.encoding_for_model(ENC_MODEL)

    with analysis_file.open('r', encoding='utf-8') as f:
        analysis = json.load(f)

    records = []
    for file_data in analysis.get('files', []):
        path = file_data['file_path']
        role = detect_role(path)

        # 函数
        for func in file_data.get('functions', []):
            source = func.get('source_code', '').strip()
            if not source:
                continue
            chunks = split_by_tokens(source, enc, MAX_TOKENS, OVERLAP)
            for idx, chunk in enumerate(chunks, 1):
                records.append({
                    'id':    f"{repo}:{path}:function:{func['name']}:chunk{idx}",
                    'text':  chunk,
                    'repo':  repo,
                    'path':  path,
                    'type':  'function',
                    'name':  func['name'],
                    'loc':   func.get('lineno', 0),
                    'role':  role
                })

        # 类
        for cls in file_data.get('classes', []):
            source = cls.get('source_code', '').strip()
            if not source:
                continue
            chunks = split_by_tokens(source, enc, MAX_TOKENS, OVERLAP)
            for idx, chunk in enumerate(chunks, 1):
                records.append({
                    'id':    f"{repo}:{path}:class:{cls['name']}:chunk{idx}",
                    'text':  chunk,
                    'repo':  repo,
                    'path':  path,
                    'type':  'class',
                    'name':  cls['name'],
                    'loc':   cls.get('lineno', 0),
                    'role':  role
                })

    with out_file.open('w', encoding='utf-8') as f:
        json.dump(records, f, ensure_ascii=False, indent=2)

    print(f"[OK] Wrote {len(records)} detailed segments to {out_file}")

def main():
    parser = argparse.ArgumentParser(
        description="Generate detailed code segments for vectorization"
    )
    parser.add_argument(
        "--analysis-root",
        type=Path,
        default=Path("analysis_results/analysis_results"),
        help="Root directory of *_analysis.json files"
    )
    parser.add_argument(
        "--output-root",
        type=Path,
        default=Path("processed_detail"),
        help="Where to write per-repo details.json files"
    )
    args = parser.parse_args()

    if not args.analysis_root.is_dir():
        raise SystemExit(f"Analysis root not found: {args.analysis_root}")

    for repo_dir in sorted(args.analysis_root.iterdir()):
        analysis_file = repo_dir / f"{repo_dir.name}_analysis.json"
        if analysis_file.exists():
            process_repo(analysis_file, args.output_root)
        else:
            print(f"[skip] Missing analysis JSON for {repo_dir.name}")

if __name__ == "__main__":
    main()
