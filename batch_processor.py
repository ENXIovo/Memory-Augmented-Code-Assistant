#!/usr/bin/env python3
"""
Batch Repository Analyzer

This script processes multiple GitHub repositories in batch, analyzing their
code structure and generating README files for each.

Usage:
    python batch_processor.py --repos-file <repos_list_file> --output-dir <output_directory>

Example:
    python batch_processor.py --repos-file repo_list.txt --output-dir ./analysis_results
"""

import os
import sys
import argparse
import logging
import concurrent.futures
import time
from typing import List, Tuple, Set
import subprocess
from pathlib import Path
import shutil

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("batch_processing.log"),
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)

def process_repository(repo_url: str, output_dir: str, timeout: int = 1800) -> bool:
    """
    Process a single repository with a timeout.
    
    Args:
        repo_url: URL of the repository
        output_dir: Output directory for results
        timeout: Timeout in seconds (default: 30 minutes)
        
    Returns:
        True if processing was successful, False otherwise
    """
    try:
        # Extract repo name from URL
        repo_name = repo_url.split('/')[-1]
        if repo_name.endswith('.git'):
            repo_name = repo_name[:-4]
        
        logger.info(f"Processing repository: {repo_name} ({repo_url})")
        
        # Create two separate directories:
        # 1. One for cloned code (which can be gitignored)
        # 2. One for generated artifacts (which should be committed)
        
        # Create directory for cloned repos
        cloned_repos_dir = os.path.join(output_dir, "cloned_repos")
        os.makedirs(cloned_repos_dir, exist_ok=True)
        repo_clone_dir = os.path.join(cloned_repos_dir, repo_name)
        
        # Create directory for analysis results
        analysis_dir = os.path.join(output_dir, "analysis_results")
        os.makedirs(analysis_dir, exist_ok=True)
        repo_analysis_dir = os.path.join(analysis_dir, repo_name)
        os.makedirs(repo_analysis_dir, exist_ok=True)
        
        # Step 1: Run the repository analyzer
        analysis_output = os.path.join(repo_analysis_dir, f"{repo_name}_analysis.json")
        analyzer_cmd = [
            "python", "repo_analyzer.py",
            "--repo", repo_url,
            "--output", repo_clone_dir,
            "--analysis-output", analysis_output
        ]
        
        logger.info(f"Running analyzer for {repo_name}...")
        try:
            # Run with timeout to prevent hanging
            result = subprocess.run(
                analyzer_cmd, 
                capture_output=True, 
                text=True,
                timeout=timeout
            )
            
            if result.returncode != 0:
                logger.error(f"Analyzer failed for {repo_name}: {result.stderr}")
                return False
        except subprocess.TimeoutExpired:
            logger.error(f"Analyzer timed out for {repo_name} after {timeout} seconds")
            return False
        
        # Check if analysis file was created
        if not os.path.exists(analysis_output):
            logger.error(f"Analysis file not created for {repo_name}")
            return False
        
        # Step 2: Generate README
        readme_output = os.path.join(repo_analysis_dir, f"{repo_name}_README.md")
        generator_cmd = [
            "python", "readme_generator.py",
            "--input", analysis_output,
            "--output", readme_output
        ]
        
        logger.info(f"Generating README for {repo_name}...")
        try:
            # Run with shorter timeout
            result = subprocess.run(
                generator_cmd, 
                capture_output=True, 
                text=True,
                timeout=300  # 5 minutes for README generation should be plenty
            )
            
            if result.returncode != 0:
                logger.error(f"README generator failed for {repo_name}: {result.stderr}")
                return False
        except subprocess.TimeoutExpired:
            logger.error(f"README generator timed out for {repo_name}")
            return False
        
        logger.info(f"Successfully processed repository: {repo_name}")
        return True
    
    except Exception as e:
        logger.error(f"Error processing repository {repo_url}: {e}")
        return False

def clean_failed_repos(output_dir: str, repo_name: str) -> None:
    """
    Clean up repository directories that failed to process.
    
    Args:
        output_dir: Base output directory
        repo_name: Name of the repository to clean
    """
    # Clean up clone directory
    repo_clone_dir = os.path.join(output_dir, "cloned_repos", repo_name)
    if os.path.exists(repo_clone_dir):
        try:
            shutil.rmtree(repo_clone_dir)
            logger.info(f"Cleaned up cloned repository directory: {repo_clone_dir}")
        except Exception as e:
            logger.error(f"Error cleaning up repository directory {repo_clone_dir}: {e}")
    
def process_repositories_batch(repos_file: str, output_dir: str, max_workers: int = 4, 
                              skip_repos: Set[str] = None) -> None:
    """
    Process multiple repositories sequentially or in parallel.
    
    Args:
        repos_file: File containing repository URLs
        output_dir: Output directory for results
        max_workers: Maximum number of parallel workers (use 1 for sequential processing)
        skip_repos: Set of repository names to skip
    """
    try:
        # Read the list of repositories
        with open(repos_file, 'r') as f:
            repos = [line.strip() for line in f if line.strip() and not line.strip().startswith('#')]
        
        logger.info(f"Found {len(repos)} repositories to process")
        
        # Create output directory
        os.makedirs(output_dir, exist_ok=True)
        
        # Filter out repositories to skip
        if skip_repos:
            filtered_repos = []
            for repo in repos:
                repo_name = repo.split('/')[-1]
                if repo_name.endswith('.git'):
                    repo_name = repo_name[:-4]
                
                if repo_name not in skip_repos:
                    filtered_repos.append(repo)
                else:
                    logger.info(f"Skipping repository: {repo_name}")
            
            repos = filtered_repos
            
        # Process repositories
        successful = 0
        failed = 0
        
        if max_workers > 1:
            # Parallel processing
            with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
                future_to_repo = {executor.submit(process_repository, repo, output_dir): repo for repo in repos}
                
                for future in concurrent.futures.as_completed(future_to_repo):
                    repo = future_to_repo[future]
                    repo_name = repo.split('/')[-1]
                    if repo_name.endswith('.git'):
                        repo_name = repo_name[:-4]
                    
                    try:
                        if future.result():
                            successful += 1
                        else:
                            failed += 1
                            # Clean up failed repository
                            clean_failed_repos(output_dir, repo_name)
                    except Exception as e:
                        logger.error(f"Exception processing {repo}: {e}")
                        failed += 1
                        # Clean up failed repository
                        clean_failed_repos(output_dir, repo_name)
        else:
            # Sequential processing (more stable)
            for repo in repos:
                repo_name = repo.split('/')[-1]
                if repo_name.endswith('.git'):
                    repo_name = repo_name[:-4]
                
                if process_repository(repo, output_dir):
                    successful += 1
                else:
                    failed += 1
                    # Clean up failed repository
                    clean_failed_repos(output_dir, repo_name)
        
        logger.info(f"Batch processing completed. Successful: {successful}, Failed: {failed}")
        
    except Exception as e:
        logger.error(f"Error in batch processing: {e}")
        raise

def parse_args():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(description='Batch Repository Analyzer')
    parser.add_argument('--repos-file', type=str, required=True, help='File containing list of repository URLs')
    parser.add_argument('--output-dir', type=str, default='./analysis_results', help='Output directory')
    parser.add_argument('--max-workers', type=int, default=4, help='Maximum number of parallel workers (use 1 for sequential processing)')
    parser.add_argument('--skip', type=str, help='Comma-separated list of repository names to skip')
    return parser.parse_args()

def main():
    """Main entry point."""
    args = parse_args()
    
    # Parse repositories to skip
    skip_repos = set()
    if args.skip:
        skip_repos = set(repo.strip() for repo in args.skip.split(','))
    
    process_repositories_batch(args.repos_file, args.output_dir, args.max_workers, skip_repos)

if __name__ == '__main__':
    main()