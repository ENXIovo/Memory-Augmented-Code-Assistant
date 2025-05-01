# Scikit-Learn Benchmarking and Examples

Scikit-Learn Benchmarking and Examples is a comprehensive library designed to facilitate performance evaluation and provide illustrative examples for machine learning tasks using the Scikit-Learn framework. This project aims at enhancing your experience with Scikit-Learn through benchmarking various algorithms and offering a variety of practical coding examples.

## Installation

To set up this project, you will need Python and Git installed. Below are the steps to install the project:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/scikit-learn/scikit-learn.git
   cd scikit-learn
   ```

2. **Create and activate a virtual environment (optional but recommended):**
   ```bash
   python -m venv myenv
   source myenv/bin/activate  # On Windows use `myenv\Scripts\activate`
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Build the project:**
   ```bash
   ./build_tools/build_wheels.sh
   ```

## Components

The project’s directory structure is organized as follows:

- `asv_benchmarks/` - Contains benchmarking scripts and configurations for ASV (A/B testing).
- `benchmarks/` - Python scripts for various dataset benchmarks.
- `build_tools/` - Scripts for managing builds, dependency checks, and testing.
- `doc/` - Documentation related files, including guides and API references.
- `examples/` - Practical examples and use cases for Scikit-Learn.
- `maint_tools/` - Maintenance tools for developers.
- `sklearn/` - The core library code for Scikit-Learn.

## Usage

Here are some typical workflows for utilizing this library:

### Running Benchmarks

You can run the benchmark scripts found in the `benchmarks/` directory. 

For example, to benchmark the Hist Gradient Boosting algorithm, use:

```bash
python benchmarks/bench_hist_gradient_boosting.py
```

### Example Workflows

Explore the `examples/` directory for a variety of scripts that demonstrate different features and applications of Scikit-Learn:

- **Release Highlights:**
  Each release has corresponding highlight scripts such as:
  - `examples/release_highlights/plot_release_highlights_1_0_0.py`
  - `examples/release_highlights/plot_release_highlights_1_2_0.py`

- **Model Selection:**
  You could view how different models perform regarding classification via:
  ```bash
  python examples/model_selection/plot_likelihood_ratios.py
  ```

- **Feature Selection:**
  A practical example of model-based feature selection can be explored with:
  ```bash
  python examples/feature_selection/plot_select_from_model_diabetes.py
  ```

## API Overview

The library provides several key functions and modules:

- **set_config**:
  ```python
  from sklearn import set_config
  set_config(display='diagram')
  ```
  Set global configurations for Scikit-Learn, affecting how outputs are displayed.

- **one_run** (in benchmarks):
  A function to perform a benchmarking run against different algorithms like LightGBM, XGBoost, and CatBoost, while recording metrics.

- **all_functions**:
  Returns a list of all available functions in the Scikit-Learn module including their names and callable references.

  ```python
  from sklearn.utils.discovery import all_functions
  functions = all_functions()
  ```

For further insights and detailed documentation, kindly explore the `doc/` directory. The extensive set of examples means you'll find code snippets appropriate for learning best practices and efficient usage of Scikit-Learn.

--- 

Feel free to contribute to this project by submitting pull requests, or by reporting issues. Happy exploring!