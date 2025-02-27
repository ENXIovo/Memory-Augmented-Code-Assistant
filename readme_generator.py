#!/usr/bin/env python3
"""
README Generator for Code Repositories

This script takes the output from the repository analyzer and generates
a comprehensive README.md file for the repository.

Usage:
    python readme_generator.py --input <analysis_json> --output <readme_file>

Example:
    python readme_generator.py --input ./analysis_results/repo_analysis.json --output ./README.md
"""

import os
import json
import argparse
import logging
from typing import Dict, List, Any, Optional
from pathlib import Path

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def format_directory_structure(structure: Dict[str, Any], indent: int = 0, max_depth: int = 3, 
                              max_items_per_level: int = 10, path_prefix: str = "") -> str:
    """
    Format directory structure as a tree string with limitations to avoid excessive output.
    
    Args:
        structure: Directory structure dictionary
        indent: Current indentation level
        max_depth: Maximum directory depth to display
        max_items_per_level: Maximum number of items to show per directory level
        path_prefix: Current path prefix for tracking full paths
        
    Returns:
        Formatted directory structure as string
    """
    result = []
    
    # Stop if we've reached maximum depth
    if indent > max_depth:
        return [f"{' ' * (indent * 4)}└── ..."]
    
    # Get sorted items (directories first, then files)
    dirs = {k: v for k, v in structure.items() if v is not None}
    files = {k: v for k, v in structure.items() if v is None}
    
    # Sort directories and files
    sorted_dirs = sorted(dirs.items())
    sorted_files = sorted(files.items())
    
    # Combine sorted items
    sorted_items = sorted_dirs + sorted_files
    
    # Limit number of items shown
    if len(sorted_items) > max_items_per_level:
        sorted_items = sorted_items[:max_items_per_level - 1]
        has_more = True
    else:
        has_more = False
    
    # Generate tree entries
    for i, (name, content) in enumerate(sorted_items):
        is_last = (i == len(sorted_items) - 1) and not has_more
        current_path = os.path.join(path_prefix, name)
        
        prefix = '    ' * indent
        connector = '└── ' if is_last else '├── '
        
        if content is None:  # File
            result.append(f"{prefix}{connector}{name}")
        else:  # Directory
            result.append(f"{prefix}{connector}{name}/")
            
            # Process subdirectory with updated path prefix
            sub_items = format_directory_structure(
                content, 
                indent + 1, 
                max_depth, 
                max_items_per_level, 
                current_path
            )
            
            # Add vertical lines for non-last items
            if not is_last:
                for j, line in enumerate(sub_items):
                    if line.strip():  # Skip empty lines
                        sub_items[j] = f"{prefix}│   {line[len(prefix) + 4:]}"
            
            result.extend(sub_items)
    
    # Add ellipsis if we're truncating the list
    if has_more:
        connector = '└── ' if len(sorted_items) == 0 else '├── '
        result.append(f"{prefix}{connector}... ({len(structure) - max_items_per_level + 1} more items)")
    
    return result

def summarize_file(file_data: Dict[str, Any]) -> str:
    """Generate a summary for a file based on its analysis."""
    file_path = file_data.get('file_path', 'Unknown file')
    language = file_data.get('language', 'Unknown')
    loc = file_data.get('loc', 0)
    
    summary = f"### {os.path.basename(file_path)}\n\n"
    summary += f"**Path**: {file_path}\n"
    summary += f"**Language**: {language}\n"
    summary += f"**Lines of Code**: {loc}\n"
    
    # Add docstring if available
    if file_data.get('docstring'):
        # Limit docstring length and clean it up
        docstring = file_data['docstring']
        if len(docstring) > 200:
            docstring = docstring[:200] + "..."
        # Replace newlines with spaces to avoid excessive line breaks
        docstring = ' '.join(docstring.split())
        summary += f"**Description**: {docstring}\n"
    
    # Add imports summary
    imports = file_data.get('imports', [])
    if imports:
        import_names = []
        for imp in imports:
            if imp.get('names'):
                for name in imp.get('names', []):
                    import_names.append(f"{imp.get('module')}.{name}")
            else:
                import_names.append(imp.get('module', ''))
        
        # Limit the number of imports shown
        if import_names:
            if len(import_names) > 5:
                summary += f"**Dependencies**: {', '.join(import_names[:5])} and {len(import_names) - 5} more\n"
            else:
                summary += f"**Dependencies**: {', '.join(import_names)}\n"
    
    # Add classes and functions count
    classes = file_data.get('classes', [])
    functions = file_data.get('functions', [])
    
    if classes:
        summary += f"**Classes**: {len(classes)}\n"
    if functions:
        summary += f"**Functions**: {len(functions)}\n"
    
    return summary

def generate_installation_instructions(repo_analysis: Dict[str, Any]) -> str:
    """Generate installation instructions based on repository analysis."""
    requirements = repo_analysis.get('requirements', [])
    
    instructions = "## Installation\n\n"
    instructions += "Clone the repository:\n\n"
    instructions += f"```bash\ngit clone {repo_analysis.get('repo_url', '')}\ncd {repo_analysis.get('repo_name', 'repository')}\n```\n\n"
    
    if requirements:
        instructions += "Install dependencies:\n\n"
        instructions += "```bash\npip install -r requirements.txt\n```\n\n"
    
    return instructions

def generate_readme(analysis_file: str, output_file: str) -> None:
    """Generate a README.md file from repository analysis data."""
    try:
        # Load analysis data
        with open(analysis_file, 'r', encoding='utf-8') as f:
            repo_analysis = json.load(f)
        
        repo_name = repo_analysis.get('repo_name', 'Unknown Repository')
        
        # Start building the README
        readme_content = f"# {repo_name}\n\n"
        
        # Add project overview
        readme_content += "## Project Overview\n\n"
        
        # If there's an existing README, try to extract description
        existing_readme = repo_analysis.get('readme_content', '')
        if existing_readme:
            # Try to find the first paragraph that's not a heading
            lines = existing_readme.split('\n')
            description = ""
            for i, line in enumerate(lines):
                if line and not line.startswith('#') and not line.startswith('!'):
                    # Get a few more lines if they're part of the paragraph
                    j = i
                    paragraph = []
                    while j < len(lines) and lines[j] and not lines[j].startswith('#'):
                        paragraph.append(lines[j].strip())
                        j += 1
                        if j > i + 5:  # Limit to 5 lines max
                            break
                    description = ' '.join(paragraph)
                    if len(description) > 50:  # Only use if it's substantial
                        break
            
            if description:
                readme_content += f"{description}\n\n"
            else:
                # Default description
                readme_content += f"This repository contains a {', '.join(list(repo_analysis.get('languages', {}).keys())[:3])} project.\n\n"
        else:
            # Default description
            readme_content += f"This repository contains a {', '.join(list(repo_analysis.get('languages', {}).keys())[:3])} project.\n\n"
        
        # Add installation instructions
        readme_content += generate_installation_instructions(repo_analysis)
        
        # Add project structure (simplified and limited)
        readme_content += "## Project Structure\n\n"
        
        # Add file statistics
        files = repo_analysis.get('files', [])
        languages = repo_analysis.get('languages', {})
        
        # Create a project summary with statistics
        if files:
            readme_content += "### Project Summary\n\n"
            readme_content += f"- **Total Files**: {len(files)}\n"
            readme_content += f"- **Languages**: {', '.join(list(languages.keys())[:5])}\n"
            
            # Add language statistics
            if languages:
                total_files = sum(languages.values())
                language_stats = sorted(languages.items(), key=lambda x: x[1], reverse=True)[:5]
                readme_content += "- **Language Distribution**:\n"
                for lang, count in language_stats:
                    percentage = (count / total_files) * 100
                    readme_content += f"  - {lang}: {count} files ({percentage:.1f}%)\n"
            
            readme_content += "\n"
        
        # Add directory structure visualization
        readme_content += "### Directory Structure\n\n"
        readme_content += "```\n"
        readme_content += f"{repo_name}/\n"
        dir_structure_lines = format_directory_structure(
            repo_analysis.get('directory_structure', {}),
            max_depth=3,  # Limit depth
            max_items_per_level=10  # Limit items per directory
        )
        readme_content += "\n".join(dir_structure_lines)
        readme_content += "\n```\n\n"
        
        # Add file summaries
        readme_content += "## Key Files\n\n"
        
        # Categorize files by type
        files_by_type = {}
        files = repo_analysis.get('files', [])
        
        # Identify configuration files
        config_extensions = {'.json', '.yml', '.yaml', '.toml', '.ini', '.cfg', '.config'}
        config_filenames = {'setup.py', 'requirements.txt', 'package.json', 'Pipfile', 'pyproject.toml', 
                           'Makefile', 'Dockerfile', '.gitignore', 'README.md', 'LICENSE'}
        
        # Group files by language/type
        for file_data in files:
            file_path = file_data.get('file_path', '')
            filename = os.path.basename(file_path)
            extension = Path(file_path).suffix.lower()
            language = file_data.get('language', 'Unknown')
            
            # Determine file type
            file_type = language
            if language == 'Unknown' and extension in config_extensions:
                file_type = 'Configuration'
            elif filename in config_filenames:
                file_type = 'Configuration'
                
            if file_type not in files_by_type:
                files_by_type[file_type] = []
            files_by_type[file_type].append(file_data)
        
        # Sort each type by importance (lines of code)
        for file_type in files_by_type:
            files_by_type[file_type] = sorted(
                files_by_type[file_type], 
                key=lambda f: f.get('loc', 0), 
                reverse=True
            )
        
        # Get the primary language
        primary_language = max(languages.items(), key=lambda x: x[1])[0] if languages else 'Unknown'
        
        # Display files by category
        categories_to_show = []
        
        # First show primary language (if it's a recognized programming language)
        if primary_language in files_by_type and primary_language not in ['Unknown', 'Configuration']:
            categories_to_show.append((f"{primary_language} Core Files", primary_language, 6))
        
        # Then show config files
        if 'Configuration' in files_by_type:
            categories_to_show.append(("Configuration Files", 'Configuration', 3))
        
        # Then other important languages
        for lang in sorted(files_by_type.keys()):
            if lang not in [primary_language, 'Configuration', 'Unknown']:
                categories_to_show.append((f"{lang} Files", lang, 3))
        
        # Finally, unknown files if needed
        if 'Unknown' in files_by_type:
            categories_to_show.append(("Other Files", 'Unknown', 2))
        
        # Make sure we have something to show
        if not categories_to_show and files:
            # If we couldn't categorize properly, just show most important files
            sorted_files = sorted(files, key=lambda f: f.get('loc', 0), reverse=True)
            readme_content += "### Important Files\n\n"
            for file_data in sorted_files[:10]:  # Show top 10 files
                readme_content += summarize_file(file_data)
                readme_content += "\n"
        else:
            # Show files by category
            for category_name, file_type, max_files in categories_to_show:
                type_files = files_by_type.get(file_type, [])
                if type_files:
                    readme_content += f"### {category_name}\n\n"
                    for file_data in type_files[:max_files]:  # Limit each category
                        readme_content += summarize_file(file_data)
                        readme_content += "\n"
        
        # Add usage examples if possible
        readme_content += "## Usage\n\n"
        readme_content += "Please refer to the file summaries for usage examples and API documentation.\n\n"
        
        # Add license information
        readme_content += "## License\n\n"
        readme_content += "This project is licensed under the terms specified in the repository.\n"
        
        # Write the README file
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(readme_content)
        
        logger.info(f"README generated successfully: {output_file}")
        
    except Exception as e:
        logger.error(f"Error generating README: {e}")
        raise

def parse_args():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(description='README Generator for Code Repositories')
    parser.add_argument('--input', type=str, required=True, help='Path to repository analysis JSON file')
    parser.add_argument('--output', type=str, required=True, help='Path to output README.md file')
    return parser.parse_args()

def main():
    """Main entry point."""
    args = parse_args()
    generate_readme(args.input, args.output)

if __name__ == '__main__':
    main()