# scikit-learn

## Project Overview

This repository contains a Unknown, Python, JavaScript project.

## Installation

Clone the repository:

```bash
git clone https://github.com/scikit-learn/scikit-learn
cd scikit-learn
```

## Project Structure

### Project Summary

- **Total Files**: 971
- **Languages**: Unknown, Python, JavaScript, C, C++
- **Language Distribution**:
  - Python: 971 files (65.9%)
  - Unknown: 483 files (32.8%)
  - C/C++ Header: 7 files (0.5%)
  - JavaScript: 5 files (0.3%)
  - C++: 5 files (0.3%)

### Directory Structure

```
scikit-learn/
├── asv_benchmarks/
│   ├── benchmarks/
│   │   ├── __init__.py
│   │   ├── cluster.py
│   │   ├── common.py
│   │   ├── config.json
│   │   ├── datasets.py
│   │   ├── decomposition.py
│   │   ├── ensemble.py
│   │   ├── linear_model.py
│   │   ├── manifold.py
│   │   ├── ... (5 more items)
│   └── asv.conf.json
├── benchmarks/
│   ├── bench_20newsgroups.py
│   ├── bench_covertype.py
│   ├── bench_feature_expansions.py
│   ├── bench_glm.py
│   ├── bench_glmnet.py
│   ├── bench_hist_gradient_boosting.py
│   ├── bench_hist_gradient_boosting_adult.py
│   ├── bench_hist_gradient_boosting_categorical_only.py
│   ├── bench_hist_gradient_boosting_higgsboson.py
│   ├── ... (34 more items)
├── build_tools/
│   ├── azure/
│   │   ├── combine_coverage_reports.sh
│   │   ├── debian_32bit_lock.txt
│   │   ├── debian_32bit_requirements.txt
│   │   ├── get_commit_message.py
│   │   ├── get_selected_tests.py
│   │   ├── install.sh
│   │   ├── install_setup_conda.sh
│   │   ├── posix-all-parallel.yml
│   │   ├── posix-docker.yml
│   │   ├── ... (26 more items)
│   ├── circle/
│   │   ├── build_doc.sh
│   │   ├── checkout_merge_commit.sh
│   │   ├── doc_environment.yml
│   │   ├── doc_linux-64_conda.lock
│   │   ├── doc_min_dependencies_environment.yml
│   │   ├── doc_min_dependencies_linux-64_conda.lock
│   │   ├── download_documentation.sh
│   │   ├── list_versions.py
│   │   └── push_doc.sh
│   ├── github/
│   │   ├── build_minimal_windows_image.sh
│   │   ├── build_source.sh
│   │   ├── build_test_arm.sh
│   │   ├── check_build_trigger.sh
│   │   ├── check_wheels.py
│   │   ├── create_gpu_environment.sh
│   │   ├── pylatest_conda_forge_cuda_array-api_linux-64_conda.lock
│   │   ├── pylatest_conda_forge_cuda_array-api_linux-64_environment.yml
│   │   ├── pymin_conda_forge_arm_environment.yml
│   │   ├── ... (6 more items)
│   ├── wheels/
│   │   ├── LICENSE_linux.txt
│   │   ├── LICENSE_macos.txt
│   │   ├── LICENSE_windows.txt
│   │   ├── build_wheels.sh
│   │   ├── check_license.py
│   │   ├── cibw_before_build.sh
│   │   └── test_wheels.sh
│   ├── Makefile
│   ├── check-meson-openmp-dependencies.py
│   ├── codespell_ignore_words.txt
│   ├── generate_authors_table.py
│   ├── get_comment.py
│   ├── ... (3 more items)
├── doc/
│   ├── api/
│   │   ├── deprecated.rst.template
│   │   ├── index.rst.template
│   │   └── module.rst.template
│   ├── binder/
│   │   └── requirements.txt
│   ├── computing/
│   │   ├── computational_performance.rst
│   │   ├── parallelism.rst
│   │   └── scaling_strategies.rst
│   ├── css/
│   ├── datasets/
│   │   ├── loading_other_datasets.rst
│   │   ├── real_world.rst
│   │   ├── sample_generators.rst
│   │   └── toy_dataset.rst
│   ├── developers/
│   │   ├── advanced_installation.rst
│   │   ├── bug_triaging.rst
│   │   ├── contributing.rst
│   │   ├── cython.rst
│   │   ├── develop.rst
│   │   ├── index.rst
│   │   ├── maintainer.rst.template
│   │   ├── minimal_reproducer.rst
│   │   ├── performance.rst
│   │   ├── ... (3 more items)
│   ├── images/
│   │   ├── Tidelift-logo-on-light.svg
│   │   ├── axa-small.png
│   │   ├── axa.png
│   │   ├── bcg.png
│   │   ├── beta_divergence.png
│   │   ├── bnp-small.png
│   │   ├── bnp.png
│   │   ├── cds-logo.png
│   │   ├── chanel-small.png
│   │   ├── ... (58 more items)
│   ├── js/
│   │   └── scripts/
│   │       ├── vendor/
│   │       │   └── ...
│   │       ├── api-search.js
│   │       ├── dropdown.js
│   │       ├── sg_plotly_resize.js
│   │       └── version-switcher.js
│   ├── logos/
│   │   ├── brand_colors/
│   │   │   ├── colorswatch_29ABE2_cyan.png
│   │   │   ├── colorswatch_9B4600_brown.png
│   │   │   └── colorswatch_F7931E_orange.png
│   │   ├── brand_guidelines/
│   │   │   └── scikitlearn_logo_clearspace_updated.png
│   │   ├── 1280px-scikit-learn-logo.png
│   │   ├── README.md
│   │   ├── favicon.ico
│   │   ├── identity.pdf
│   │   ├── scikit-learn-logo-notext.png
│   │   ├── scikit-learn-logo-small.png
│   │   ├── scikit-learn-logo-thumb.png
│   │   ├── ... (4 more items)
│   ├── ... (50 more items)
├── examples/
│   ├── applications/
│   │   ├── README.txt
│   │   ├── plot_cyclical_feature_engineering.py
│   │   ├── plot_digits_denoising.py
│   │   ├── plot_face_recognition.py
│   │   ├── plot_model_complexity_influence.py
│   │   ├── plot_out_of_core_classification.py
│   │   ├── plot_outlier_detection_wine.py
│   │   ├── plot_prediction_latency.py
│   │   ├── plot_species_distribution_modeling.py
│   │   ├── ... (5 more items)
│   ├── bicluster/
│   │   ├── README.txt
│   │   ├── plot_bicluster_newsgroups.py
│   │   ├── plot_spectral_biclustering.py
│   │   └── plot_spectral_coclustering.py
│   ├── calibration/
│   │   ├── README.txt
│   │   ├── plot_calibration.py
│   │   ├── plot_calibration_curve.py
│   │   ├── plot_calibration_multiclass.py
│   │   └── plot_compare_calibration.py
│   ├── classification/
│   │   ├── README.txt
│   │   ├── plot_classification_probability.py
│   │   ├── plot_classifier_comparison.py
│   │   ├── plot_digits_classification.py
│   │   ├── plot_lda.py
│   │   └── plot_lda_qda.py
│   ├── cluster/
│   │   ├── README.txt
│   │   ├── plot_adjusted_for_chance_measures.py
│   │   ├── plot_affinity_propagation.py
│   │   ├── plot_agglomerative_clustering.py
│   │   ├── plot_agglomerative_clustering_metrics.py
│   │   ├── plot_agglomerative_dendrogram.py
│   │   ├── plot_birch_vs_minibatchkmeans.py
│   │   ├── plot_bisect_kmeans.py
│   │   ├── plot_cluster_comparison.py
│   │   ├── ... (21 more items)
│   ├── compose/
│   │   ├── README.txt
│   │   ├── plot_column_transformer.py
│   │   ├── plot_column_transformer_mixed_types.py
│   │   ├── plot_compare_reduction.py
│   │   ├── plot_digits_pipe.py
│   │   ├── plot_feature_union.py
│   │   └── plot_transformed_target.py
│   ├── covariance/
│   │   ├── README.txt
│   │   ├── plot_covariance_estimation.py
│   │   ├── plot_lw_vs_oas.py
│   │   ├── plot_mahalanobis_distances.py
│   │   ├── plot_robust_vs_empirical_covariance.py
│   │   └── plot_sparse_cov.py
│   ├── cross_decomposition/
│   │   ├── README.txt
│   │   ├── plot_compare_cross_decomposition.py
│   │   └── plot_pcr_vs_pls.py
│   ├── datasets/
│   │   ├── README.txt
│   │   └── plot_random_multilabel_dataset.py
│   ├── ... (25 more items)
├── maint_tools/
│   ├── bump-dependencies-versions.py
│   ├── check_xfailed_checks.py
│   ├── sort_whats_new.py
│   ├── update_tracking_issue.py
│   ├── vendor_array_api_compat.sh
│   ├── vendor_array_api_extra.sh
│   └── whats_missing.sh
├── sklearn/
│   ├── __check_build/
│   │   ├── __init__.py
│   │   ├── _check_build.pyx
│   │   └── meson.build
│   ├── _build_utils/
│   │   ├── __init__.py
│   │   ├── tempita.py
│   │   └── version.py
│   ├── _loss/
│   │   ├── tests/
│   │   │   ├── __init__.py
│   │   │   ├── test_link.py
│   │   │   └── test_loss.py
│   │   ├── __init__.py
│   │   ├── _loss.pxd
│   │   ├── _loss.pyx.tp
│   │   ├── link.py
│   │   ├── loss.py
│   │   └── meson.build
│   ├── cluster/
│   │   ├── _hdbscan/
│   │   │   ├── tests/
│   │   │   │   └── ...
│   │   │   ├── __init__.py
│   │   │   ├── _linkage.pyx
│   │   │   ├── _reachability.pyx
│   │   │   ├── _tree.pxd
│   │   │   ├── _tree.pyx
│   │   │   ├── hdbscan.py
│   │   │   └── meson.build
│   │   ├── tests/
│   │   │   ├── __init__.py
│   │   │   ├── common.py
│   │   │   ├── test_affinity_propagation.py
│   │   │   ├── test_bicluster.py
│   │   │   ├── test_birch.py
│   │   │   ├── test_bisect_k_means.py
│   │   │   ├── test_dbscan.py
│   │   │   ├── test_feature_agglomeration.py
│   │   │   ├── test_hdbscan.py
│   │   │   ├── ... (5 more items)
│   │   ├── __init__.py
│   │   ├── _affinity_propagation.py
│   │   ├── _agglomerative.py
│   │   ├── _bicluster.py
│   │   ├── _birch.py
│   │   ├── _bisect_k_means.py
│   │   ├── _dbscan.py
│   │   ├── ... (14 more items)
│   ├── compose/
│   │   ├── tests/
│   │   │   ├── __init__.py
│   │   │   ├── test_column_transformer.py
│   │   │   └── test_target.py
│   │   ├── __init__.py
│   │   ├── _column_transformer.py
│   │   └── _target.py
│   ├── covariance/
│   │   ├── tests/
│   │   │   ├── __init__.py
│   │   │   ├── test_covariance.py
│   │   │   ├── test_elliptic_envelope.py
│   │   │   ├── test_graphical_lasso.py
│   │   │   └── test_robust_covariance.py
│   │   ├── __init__.py
│   │   ├── _elliptic_envelope.py
│   │   ├── _empirical_covariance.py
│   │   ├── _graph_lasso.py
│   │   ├── _robust_covariance.py
│   │   └── _shrunk_covariance.py
│   ├── cross_decomposition/
│   │   ├── tests/
│   │   │   ├── __init__.py
│   │   │   └── test_pls.py
│   │   ├── __init__.py
│   │   └── _pls.py
│   ├── datasets/
│   │   ├── data/
│   │   │   ├── __init__.py
│   │   │   ├── boston_house_prices.csv
│   │   │   ├── breast_cancer.csv
│   │   │   ├── diabetes_data_raw.csv.gz
│   │   │   ├── diabetes_target.csv.gz
│   │   │   ├── digits.csv.gz
│   │   │   ├── iris.csv
│   │   │   ├── linnerud_exercise.csv
│   │   │   ├── linnerud_physiological.csv
│   │   │   └── wine_data.csv
│   │   ├── descr/
│   │   │   ├── __init__.py
│   │   │   ├── breast_cancer.rst
│   │   │   ├── california_housing.rst
│   │   │   ├── covtype.rst
│   │   │   ├── diabetes.rst
│   │   │   ├── digits.rst
│   │   │   ├── iris.rst
│   │   │   ├── kddcup99.rst
│   │   │   ├── lfw.rst
│   │   │   ├── ... (6 more items)
│   │   ├── images/
│   │   │   ├── README.txt
│   │   │   ├── __init__.py
│   │   │   ├── china.jpg
│   │   │   └── flower.jpg
│   │   ├── tests/
│   │   │   ├── data/
│   │   │   │   └── ...
│   │   │   ├── __init__.py
│   │   │   ├── test_20news.py
│   │   │   ├── test_arff_parser.py
│   │   │   ├── test_base.py
│   │   │   ├── test_california_housing.py
│   │   │   ├── test_common.py
│   │   │   ├── test_covtype.py
│   │   │   ├── test_kddcup99.py
│   │   │   ├── ... (6 more items)
│   │   ├── __init__.py
│   │   ├── _arff_parser.py
│   │   ├── _base.py
│   │   ├── _california_housing.py
│   │   ├── _covtype.py
│   │   ├── ... (11 more items)
│   ├── decomposition/
│   │   ├── tests/
│   │   │   ├── __init__.py
│   │   │   ├── test_dict_learning.py
│   │   │   ├── test_factor_analysis.py
│   │   │   ├── test_fastica.py
│   │   │   ├── test_incremental_pca.py
│   │   │   ├── test_kernel_pca.py
│   │   │   ├── test_nmf.py
│   │   │   ├── test_online_lda.py
│   │   │   ├── test_pca.py
│   │   │   ├── ... (2 more items)
│   │   ├── __init__.py
│   │   ├── _base.py
│   │   ├── _cdnmf_fast.pyx
│   │   ├── _dict_learning.py
│   │   ├── _factor_analysis.py
│   │   ├── _fastica.py
│   │   ├── _incremental_pca.py
│   │   ├── _kernel_pca.py
│   │   ├── ... (7 more items)
│   ├── ... (42 more items)
├── CITATION.cff
├── CODE_OF_CONDUCT.md
├── ... (8 more items)
```

## Key Files

### Python Core Files

### estimator_checks.py

**Path**: sklearn\utils\estimator_checks.py
**Language**: Python
**Lines of Code**: 4089
**Description**: Various utilities to check the compatibility of estimators with scikit-learn API.
**Dependencies**: __future__.annotations, pickle, re, textwrap, warnings and 100 more
**Classes**: 1
**Functions**: 141

### _classification.py

**Path**: sklearn\metrics\_classification.py
**Language**: Python
**Lines of Code**: 3067
**Description**: Metrics to assess performance on classification task given class prediction. Functions named as ``*_score`` return a scalar value to maximize: the higher the better. Function named as ``*_error`` or...
**Dependencies**: warnings, numbers.Integral, numbers.Real, numpy, scipy.sparse.coo_matrix and 36 more
**Functions**: 27

### _data.py

**Path**: sklearn\preprocessing\_data.py
**Language**: Python
**Lines of Code**: 2928
**Dependencies**: warnings, numbers.Integral, numbers.Real, numpy, scipy.optimize and 36 more
**Classes**: 9
**Functions**: 11

### _coordinate_descent.py

**Path**: sklearn\linear_model\_coordinate_descent.py
**Language**: Python
**Lines of Code**: 2644
**Dependencies**: numbers, sys, warnings, abc.ABC, abc.abstractmethod and 38 more
**Classes**: 9
**Functions**: 5

### test_classification.py

**Path**: sklearn\metrics\tests\test_classification.py
**Language**: Python
**Lines of Code**: 2596
**Dependencies**: re, warnings, functools.partial, itertools.chain, itertools.permutations and 49 more
**Functions**: 113

### _forest.py

**Path**: sklearn\ensemble\_forest.py
**Language**: Python
**Lines of Code**: 2435
**Description**: Forest of trees-based ensemble methods. Those methods include random forests and extremely randomized trees. The module structure is the following: - The ``BaseForest`` base class implements a comm...
**Dependencies**: threading, abc.ABCMeta, abc.abstractmethod, numbers.Integral, numbers.Real and 40 more
**Classes**: 8
**Functions**: 5

## Usage

Please refer to the file summaries for usage examples and API documentation.

## License

This project is licensed under the terms specified in the repository.
