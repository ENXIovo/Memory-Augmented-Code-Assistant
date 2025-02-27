#!/usr/bin/env python3
"""
Repository Code Structure Analyzer

This script analyzes GitHub repositories to extract code structure information
using Abstract Syntax Tree (AST) parsing and generates structured data for
README generation.

Usage:
    python repo_analyzer.py --repo <repository_url> --output <output_dir> [--analysis-output <analysis_file>]

Example:
    python repo_analyzer.py --repo https://github.com/username/repo --output ./analysis_results
"""

import os
import sys
import ast
import json
import argparse
import logging
import git
import shutil
import tempfile
from pathlib import Path
from typing import Dict, List, Any, Tuple, Set, Optional
from dataclasses import dataclass, asdict, field

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

@dataclass
class CodeFunction:
    """Represents a function or method in code."""
    name: str
    docstring: Optional[str] = None
    arguments: List[str] = field(default_factory=list)
    source_code: str = ""
    lineno: int = 0
    decorators: List[str] = field(default_factory=list)
    return_type: Optional[str] = None

@dataclass
class CodeClass:
    """Represents a class in code."""
    name: str
    docstring: Optional[str] = None
    methods: List[CodeFunction] = field(default_factory=list)
    base_classes: List[str] = field(default_factory=list)
    source_code: str = ""
    lineno: int = 0

@dataclass
class ImportInfo:
    """Represents import statements in code."""
    module: str
    names: List[str] = field(default_factory=list)
    alias: Optional[str] = None

@dataclass
class FileAnalysis:
    """Represents the analysis of a single file."""
    file_path: str
    language: str
    imports: List[ImportInfo] = field(default_factory=list)
    functions: List[CodeFunction] = field(default_factory=list)
    classes: List[CodeClass] = field(default_factory=list)
    global_variables: Dict[str, str] = field(default_factory=dict)
    loc: int = 0  # Lines of code
    docstring: Optional[str] = None

@dataclass
class RepositoryAnalysis:
    """Represents the analysis of an entire repository."""
    repo_name: str
    repo_url: str
    files: List[FileAnalysis] = field(default_factory=list)
    file_count: int = 0
    directory_structure: Dict[str, Any] = field(default_factory=dict)
    languages: Dict[str, int] = field(default_factory=dict)
    readme_content: Optional[str] = None
    requirements: List[str] = field(default_factory=list)

class PythonASTVisitor(ast.NodeVisitor):
    """AST visitor for Python code analysis."""
    
    def __init__(self, source_code: str):
        self.source_code = source_code.splitlines()
        self.functions = []
        self.classes = []
        self.imports = []
        self.global_vars = {}
        self.current_class = None
        
    def visit_FunctionDef(self, node):
        """Process function definitions."""
        func = CodeFunction(
            name=node.name,
            docstring=ast.get_docstring(node),
            arguments=[arg.arg for arg in node.args.args],
            lineno=node.lineno,
            source_code=self._get_source_segment(node),
            decorators=[self._get_source_segment(d) for d in node.decorator_list]
        )
        
        # Check for return annotation
        if node.returns:
            if isinstance(node.returns, ast.Name):
                func.return_type = node.returns.id
        
        if self.current_class:
            self.current_class.methods.append(func)
        else:
            self.functions.append(func)
        
        # Continue visiting child nodes
        self.generic_visit(node)
    
    def visit_ClassDef(self, node):
        """Process class definitions."""
        prev_class = self.current_class
        self.current_class = CodeClass(
            name=node.name,
            docstring=ast.get_docstring(node),
            base_classes=[self._get_source_segment(base) for base in node.bases],
            lineno=node.lineno,
            source_code=self._get_source_segment(node)
        )
        
        # Visit all the children (including methods)
        self.generic_visit(node)
        
        # Add to classes list and restore previous class context
        self.classes.append(self.current_class)
        self.current_class = prev_class
    
    def visit_Import(self, node):
        """Process import statements."""
        for name in node.names:
            self.imports.append(ImportInfo(
                module=name.name,
                alias=name.asname
            ))
    
    def visit_ImportFrom(self, node):
        """Process from-import statements."""
        names = [name.name for name in node.names]
        self.imports.append(ImportInfo(
            module=node.module,
            names=names
        ))
    
    def visit_Assign(self, node):
        """Process global variable assignments."""
        if not isinstance(node.parent, ast.ClassDef) and not isinstance(node.parent, ast.FunctionDef):
            for target in node.targets:
                if isinstance(target, ast.Name):
                    self.global_vars[target.id] = self._get_source_segment(node)
        self.generic_visit(node)
    
    def _get_source_segment(self, node):
        """Extract source code for a node."""
        if hasattr(node, 'lineno') and hasattr(node, 'end_lineno'):
            start = node.lineno - 1
            end = node.end_lineno if hasattr(node, 'end_lineno') else start + 1
            return "\n".join(self.source_code[start:end])
        return ""

def detect_language(file_path: str) -> str:
    """Detect the programming language from file extension."""
    extension = Path(file_path).suffix.lower()
    language_map = {
        '.py': 'Python',
        '.js': 'JavaScript',
        '.ts': 'TypeScript',
        '.jsx': 'React',
        '.tsx': 'React TypeScript',
        '.java': 'Java',
        '.c': 'C',
        '.cpp': 'C++',
        '.h': 'C/C++ Header',
        '.cs': 'C#',
        '.go': 'Go',
        '.rb': 'Ruby',
        '.php': 'PHP',
        '.swift': 'Swift',
        '.kt': 'Kotlin',
        '.rs': 'Rust',
    }
    return language_map.get(extension, 'Unknown')

def analyze_python_file(file_path: str, content: str) -> FileAnalysis:
    """Analyze a Python file using AST."""
    try:
        # Parse the AST
        tree = ast.parse(content)
        
        # Add parent references to nodes (requires Python 3.8+)
        for parent in ast.walk(tree):
            for child in ast.iter_child_nodes(parent):
                child.parent = parent
        
        # Visit the AST
        visitor = PythonASTVisitor(content)
        visitor.visit(tree)
        
        # Count lines of code (excluding empty lines and comments)
        loc = len([line for line in content.splitlines() 
                  if line.strip() and not line.strip().startswith('#')])
        
        return FileAnalysis(
            file_path=file_path,
            language='Python',
            imports=visitor.imports,
            functions=visitor.functions,
            classes=visitor.classes,
            global_variables=visitor.global_vars,
            loc=loc,
            docstring=ast.get_docstring(tree)
        )
    except SyntaxError as e:
        logger.error(f"Syntax error in {file_path}: {e}")
        return FileAnalysis(file_path=file_path, language='Python')
    except Exception as e:
        logger.error(f"Error analyzing {file_path}: {e}")
        return FileAnalysis(file_path=file_path, language='Python')

def build_dir_structure(repo_path: str, max_depth: int = 5) -> Dict[str, Any]:
    """
    Build a nested directory structure representation with depth limitation.
    
    Args:
        repo_path: Path to the repository
        max_depth: Maximum depth to traverse
        
    Returns:
        Dictionary representing the directory structure
    """
    result = {}
    
    def _build_structure(path, current_dict, current_depth=0):
        if current_depth >= max_depth:
            return
            
        try:
            items = os.listdir(path)
        except (PermissionError, OSError):
            return
            
        for item in items:
            if item.startswith('.'):
                continue
                
            item_path = os.path.join(path, item)
            try:
                if os.path.isdir(item_path):
                    current_dict[item] = {}
                    _build_structure(item_path, current_dict[item], current_depth + 1)
                elif os.path.isfile(item_path):
                    current_dict[item] = None
            except (PermissionError, OSError):
                continue
    
    _build_structure(repo_path, result)
    return result

def find_requirements(repo_path: str) -> List[str]:
    """Find and parse requirements files."""
    requirements = []
    req_files = [
        'requirements.txt',
        'Pipfile',
        'pyproject.toml',
        'setup.py',
        'package.json'
    ]
    
    for req_file in req_files:
        file_path = os.path.join(repo_path, req_file)
        if os.path.exists(file_path):
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    if req_file == 'requirements.txt':
                        requirements = [line.strip() for line in f.readlines() 
                                       if line.strip() and not line.strip().startswith('#')]
                    # Add parsers for other dependency file formats as needed
                    break
            except Exception as e:
                logger.error(f"Error reading {req_file}: {e}")
    
    return requirements

def analyze_repository(repo_url: str, output_dir: str, analysis_output_file: str) -> None:
    """Clone and analyze a GitHub repository, saving analysis result to specified file."""
    try:
        # Create output directory if it doesn't exist
        os.makedirs(output_dir, exist_ok=True)
        
        # Extract repo name from URL
        repo_name = repo_url.split('/')[-1]
        if repo_name.endswith('.git'):
            repo_name = repo_name[:-4]
        
        # Clone the repository
        repo_path = os.path.join(output_dir, repo_name)
        logger.info(f"Cloning {repo_url} to {repo_path}...")
        
        if os.path.exists(repo_path):
            logger.info(f"Repository already exists at {repo_path}, pulling latest changes...")
            repo = git.Repo(repo_path)
            origin = repo.remotes.origin
            origin.pull()
        else:
            git.Repo.clone_from(repo_url, repo_path)
        
        logger.info(f"Analyzing repository structure...")
        
        # Initialize repository analysis
        repo_analysis = RepositoryAnalysis(
            repo_name=repo_name,
            repo_url=repo_url,
            directory_structure=build_dir_structure(repo_path),
            requirements=find_requirements(repo_path)
        )
        
        # Check for existing README
        readme_path = os.path.join(repo_path, 'README.md')
        if os.path.exists(readme_path):
            with open(readme_path, 'r', encoding='utf-8') as f:
                repo_analysis.readme_content = f.read()
        
        # Track languages and file count
        language_count = {}
        file_analyses = []
        
        # Traverse all files
        for root, dirs, files in os.walk(repo_path):
            # Skip hidden directories
            dirs[:] = [d for d in dirs if not d.startswith('.')]
            
            for file in files:
                if file.startswith('.'):
                    continue
                
                file_path = os.path.join(root, file)
                rel_path = os.path.relpath(file_path, repo_path)
                
                # Skip binary files and too large files
                try:
                    if os.path.getsize(file_path) > 1000000:  # Skip files larger than 1MB
                        continue
                    
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                except (UnicodeDecodeError, IsADirectoryError):
                    continue
                
                language = detect_language(file_path)
                language_count[language] = language_count.get(language, 0) + 1
                
                # Analyze based on language
                if language == 'Python':
                    file_analysis = analyze_python_file(rel_path, content)
                    file_analyses.append(file_analysis)
                # Add other language analyzers as needed
        
        # Update repository analysis
        repo_analysis.files = file_analyses
        repo_analysis.file_count = len(file_analyses)
        repo_analysis.languages = language_count
        
        # Save analysis as JSON
        with open(analysis_output_file, 'w', encoding='utf-8') as f:
            # Convert dataclasses to dictionaries
            json.dump(asdict(repo_analysis), f, indent=2)
        
        logger.info(f"Analysis completed and saved to {analysis_output_file}")
        
    except Exception as e:
        logger.error(f"Error analyzing repository: {e}")
        raise

def parse_args():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(description='Repository Code Structure Analyzer')
    parser.add_argument('--repo', type=str, required=True, help='URL of the GitHub repository')
    parser.add_argument('--output', type=str, default='./analysis_results', help='Output directory for cloning')
    parser.add_argument('--analysis-output', type=str, help='Output file for analysis JSON (default: <output_dir>/<repo_name>_analysis.json)')
    return parser.parse_args()

def main():
    """Main entry point."""
    args = parse_args()
    
    # Extract repo name
    repo_name = args.repo.split('/')[-1]
    if repo_name.endswith('.git'):
        repo_name = repo_name[:-4]
    
    # Set default analysis output if not provided
    analysis_output = args.analysis_output
    if not analysis_output:
        analysis_output = os.path.join(args.output, f"{repo_name}_analysis.json")
    
    # Create directory for analysis output if needed
    os.makedirs(os.path.dirname(analysis_output), exist_ok=True)
    
    analyze_repository(args.repo, args.output, analysis_output)

if __name__ == '__main__':
    main()