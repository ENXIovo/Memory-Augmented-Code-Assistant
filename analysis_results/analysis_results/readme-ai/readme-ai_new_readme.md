# readme-ai

readme-ai is a sophisticated command-line tool designed to automatically generate README.md files with structured content and templates, ensuring comprehensive documentation for your projects. Its primary goal is to streamline the documentation process by leveraging modern techniques in README generation, thus enabling developers to focus more on coding and less on documentation.

## Project Structure

```
├── readme-ai/                 # Main project directory
│   ├── readme-ai/            # Core package for the application
│   │   └── .dockerignore      # Docker ignore file
│   │   └── .gitignore         # Git ignore file
│   │   └── .pre-commit-config.yaml # Pre-commit configuration file
│   │   └── .ruff.toml         # Configuration for Ruff
│   │   └── CHANGELOG.md       # List of changes in the project
│   │   └── CODE_OF_CONDUCT.md # Community guidelines
│   │   └── CONTRIBUTING.md    # Contribution guidelines
│   │   └── Dockerfile         # Docker configuration file
│   │   └── LICENSE            # Project license
│   │   └── Makefile           # Makefile for project automation
│   │   └── noxfile.py         # Nox configuration for testing
│   │   └── poetry.lock        # Locked dependencies for Poetry
│   │   └── pyproject.toml     # Project configuration
│   │   └── README.md          # Project README file
│   ├── .git/                  # Git metadata
│   ├── .github/               # GitHub workflows and configurations
│   ├── docs/                  # Documentation files
│   ├── examples/              # Example README files for various languages
│   ├── readmeai/              # Main application package
│   ├── scripts/               # Utility scripts for project management
│   ├── setup/                 # Project setup configurations
│   ├── tests/                 # Unit tests for the application
```

## Installation

To set up the project on your local machine, follow these steps:

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/readme-ai.git
   cd readme-ai/readme-ai/
   ```

2. Install the dependencies using Poetry (make sure Poetry is installed):
   ```
   poetry install
   ```

3. (Optional) If you want to run tests, you can set up the testing requirements:
   ```
   cd tests
   pytest
   ```

4. To run the application, you can use the command line interface as described in the **Usage** section.

## Components

### Important Files

- **main.py**: Entry point for the command-line interface.
- **pipeline.py**: Orchestrates the README.md file generation process.
- **options.py**: Contains command-line options for configuring the application.
- **builder.py**: Responsible for generating content for README sections.
- **settings.py**: Contains configuration handling modules.
- **test_errors.py**: Unit tests for error handling classes.

## Usage

To generate a README.md file, run the following command in your terminal:

```bash
python -m readmeai.cli.main -r <repository_url> -o <output_file_path>
```

### Example:

```bash
python -m readmeai.cli.main -r "https://github.com/yourusername/yourproject" -o "README.md"
```

This command initiates the README generation process and saves the output to `README.md`.

## API Overview

The following key functions, classes, and modules are integral to the readme-ai application:

- **main()** (in `main.py`): The main entry point for the CLI.
- **readme_agent()** (in `pipeline.py`): Manages the asynchronous README generation process with error handling.
- **MarkdownBuilder** (in `builder.py`): Generates sections of the README.md document.
- **ConfigLoader** (in `settings.py`): Loads configuration settings and resources for the application.
- **LLMProviders** (in `enums.py`): Enum class defining supported Large Language Model (LLM) services.

Explore the comprehensive functionality of readme-ai for enhancing your documentation workflow efficiently and effectively!