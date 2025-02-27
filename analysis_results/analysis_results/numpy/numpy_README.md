# numpy

## Project Overview

<h1 align="center"> <img src="https://raw.githubusercontent.com/numpy/numpy/main/branding/logo/primary/numpylogo.svg" width="300"> </h1><br>

## Installation

Clone the repository:

```bash
git clone https://github.com/numpy/numpy
cd numpy
```

## Project Structure

### Project Summary

- **Total Files**: 578
- **Languages**: Unknown, Python, C/C++ Header, C, C++
- **Language Distribution**:
  - Unknown: 1143 files (53.2%)
  - Python: 578 files (26.9%)
  - C/C++ Header: 228 files (10.6%)
  - C: 174 files (8.1%)
  - C++: 27 files (1.3%)

### Directory Structure

```
numpy/
├── benchmarks/
│   ├── benchmarks/
│   │   ├── __init__.py
│   │   ├── bench_app.py
│   │   ├── bench_array_coercion.py
│   │   ├── bench_clip.py
│   │   ├── bench_core.py
│   │   ├── bench_creation.py
│   │   ├── bench_function_base.py
│   │   ├── bench_import.py
│   │   ├── bench_indexing.py
│   │   ├── ... (18 more items)
│   ├── README.rst
│   ├── asv.conf.json
│   ├── asv_compare.conf.json.tpl
│   └── asv_pip_nopep517.py
├── branding/
│   └── logo/
│       ├── logomark/
│       │   ├── numpylogoicon.png
│       │   ├── numpylogoicon.svg
│       │   ├── numpylogoicondark.png
│       │   └── numpylogoiconlight.png
│       ├── primary/
│       │   ├── numpylogo.png
│       │   ├── numpylogo.svg
│       │   ├── numpylogodark.png
│       │   └── numpylogolight.png
│       ├── secondary/
│       │   ├── numpylogo2.png
│       │   ├── numpylogo2.svg
│       │   ├── numpylogo2dark.png
│       │   └── numpylogo2light.png
│       └── logoguidelines.md
├── doc/
│   ├── changelog/
│   │   ├── 1.12.0-changelog.rst
│   │   ├── 1.12.1-changelog.rst
│   │   ├── 1.13.0-changelog.rst
│   │   ├── 1.13.1-changelog.rst
│   │   ├── 1.13.2-changelog.rst
│   │   ├── 1.13.3-changelog.rst
│   │   ├── 1.14.0-changelog.rst
│   │   ├── 1.14.1-changelog.rst
│   │   ├── 1.14.2-changelog.rst
│   │   ├── ... (80 more items)
│   ├── neps/
│   │   ├── _static/
│   │   │   ├── casting_flow.svg
│   │   │   ├── dtype_hierarchy.svg
│   │   │   ├── nep-0000.png
│   │   │   ├── nep-0040_dtype-hierarchy.png
│   │   │   ├── nep-0041-mindmap.svg
│   │   │   ├── nep-0041-type-sketch-no-fonts.svg
│   │   │   ├── nep-0041-type-sketch.svg
│   │   │   ├── nep-0047-casting-rules-lattice.png
│   │   │   ├── nep-0047-library-dependencies.png
│   │   │   ├── ... (11 more items)
│   │   ├── tools/
│   │   │   └── build_index.py
│   │   ├── Makefile
│   │   ├── accepted.rst.tmpl
│   │   ├── conf.py
│   │   ├── content.rst
│   │   ├── deferred.rst.tmpl
│   │   ├── finished.rst.tmpl
│   │   ├── index.rst
│   │   ├── ... (63 more items)
│   ├── release/
│   │   └── upcoming_changes/
│   │       ├── 26018.change.rst
│   │       ├── 26018.performance.rst
│   │       ├── 26745.highlight.rst
│   │       ├── 27288.improvement.rst
│   │       ├── 27789.new_function.rst
│   │       ├── 27883.c_api.rst
│   │       ├── 27883.change.rst
│   │       ├── 27998.c_api.rst
│   │       ├── 28080.c_api.rst
│   │       ├── ... (8 more items)
│   ├── source/
│   │   ├── _static/
│   │   │   ├── favicon/
│   │   │   │   └── ...
│   │   │   ├── index-images/
│   │   │   │   └── ...
│   │   │   ├── scipy-mathjax/
│   │   │   │   └── ...
│   │   │   ├── numpy.css
│   │   │   ├── numpylogo.svg
│   │   │   └── numpylogo_dark.svg
│   │   ├── _templates/
│   │   │   ├── autosummary/
│   │   │   │   └── ...
│   │   │   └── searchbox.html
│   │   ├── building/
│   │   │   ├── blas_lapack.rst
│   │   │   ├── compilers_and_options.rst
│   │   │   ├── cross_compilation.rst
│   │   │   ├── distutils_equivalents.rst
│   │   │   ├── index.rst
│   │   │   ├── introspecting_a_build.rst
│   │   │   ├── redistributable_binaries.rst
│   │   │   └── understanding_meson.rst
│   │   ├── dev/
│   │   │   ├── examples/
│   │   │   │   └── ...
│   │   │   ├── governance/
│   │   │   │   └── ...
│   │   │   ├── alignment.rst
│   │   │   ├── depending_on_numpy.rst
│   │   │   ├── development_advanced_debugging.rst
│   │   │   ├── development_environment.rst
│   │   │   ├── development_workflow.rst
│   │   │   ├── howto-docs.rst
│   │   │   ├── howto_build_docs.rst
│   │   │   ├── ... (7 more items)
│   │   ├── f2py/
│   │   │   ├── advanced/
│   │   │   │   └── ...
│   │   │   ├── buildtools/
│   │   │   │   └── ...
│   │   │   ├── code/
│   │   │   │   └── ...
│   │   │   ├── windows/
│   │   │   │   └── ...
│   │   │   ├── f2py-examples.rst
│   │   │   ├── f2py-reference.rst
│   │   │   ├── f2py-testing.rst
│   │   │   ├── f2py-user.rst
│   │   │   ├── f2py.getting-started.rst
│   │   │   ├── ... (4 more items)
│   │   ├── reference/
│   │   │   ├── c-api/
│   │   │   │   └── ...
│   │   │   ├── distutils/
│   │   │   │   └── ...
│   │   │   ├── figures/
│   │   │   │   └── ...
│   │   │   ├── random/
│   │   │   │   └── ...
│   │   │   ├── simd/
│   │   │   │   └── ...
│   │   │   ├── alignment.rst
│   │   │   ├── array_api.rst
│   │   │   ├── arrays.classes.rst
│   │   │   ├── arrays.datetime.rst
│   │   │   ├── ... (70 more items)
│   │   ├── release/
│   │   │   ├── 1.10.0-notes.rst
│   │   │   ├── 1.10.1-notes.rst
│   │   │   ├── 1.10.2-notes.rst
│   │   │   ├── 1.10.3-notes.rst
│   │   │   ├── 1.10.4-notes.rst
│   │   │   ├── 1.11.0-notes.rst
│   │   │   ├── 1.11.1-notes.rst
│   │   │   ├── 1.11.2-notes.rst
│   │   │   ├── 1.11.3-notes.rst
│   │   │   ├── ... (106 more items)
│   │   ├── user/
│   │   │   ├── images/
│   │   │   │   └── ...
│   │   │   ├── plots/
│   │   │   │   └── ...
│   │   │   ├── absolute_beginners.rst
│   │   │   ├── basics.broadcasting.rst
│   │   │   ├── basics.copies.rst
│   │   │   ├── basics.creation.rst
│   │   │   ├── basics.dispatch.rst
│   │   │   ├── basics.indexing.rst
│   │   │   ├── basics.interoperability.rst
│   │   │   ├── ... (39 more items)
│   │   ├── benchmarking.rst
│   │   ├── ... (10 more items)
│   ├── BRANCH_WALKTHROUGH.rst
│   ├── C_STYLE_GUIDE.rst
│   ├── DISTUTILS.rst
│   ├── EXAMPLE_DOCSTRING.rst
│   ├── HOWTO_DOCUMENT.rst
│   ├── ... (10 more items)
├── meson_cpu/
│   ├── arm/
│   │   └── meson.build
│   ├── loongarch64/
│   │   └── meson.build
│   ├── ppc64/
│   │   └── meson.build
│   ├── riscv64/
│   │   └── meson.build
│   ├── s390x/
│   │   └── meson.build
│   ├── x86/
│   │   └── meson.build
│   ├── main_config.h.in
│   └── meson.build
├── numpy/
│   ├── _build_utils/
│   │   ├── tempita/
│   │   │   ├── LICENSE.txt
│   │   │   ├── __init__.py
│   │   │   ├── _looper.py
│   │   │   └── _tempita.py
│   │   ├── __init__.py
│   │   ├── gcc_build_bitness.py
│   │   ├── gitversion.py
│   │   ├── process_src_template.py
│   │   └── tempita.py
│   ├── _core/
│   │   ├── code_generators/
│   │   │   ├── __init__.py
│   │   │   ├── cversions.txt
│   │   │   ├── genapi.py
│   │   │   ├── generate_numpy_api.py
│   │   │   ├── generate_ufunc_api.py
│   │   │   ├── generate_umath.py
│   │   │   ├── generate_umath_doc.py
│   │   │   ├── numpy_api.py
│   │   │   ├── ufunc_docstrings.py
│   │   │   └── verify_c_api_version.py
│   │   ├── include/
│   │   │   ├── numpy/
│   │   │   │   └── ...
│   │   │   └── meson.build
│   │   ├── src/
│   │   │   ├── _simd/
│   │   │   │   └── ...
│   │   │   ├── common/
│   │   │   │   └── ...
│   │   │   ├── highway/
│   │   │   │   └── ...
│   │   │   ├── multiarray/
│   │   │   │   └── ...
│   │   │   ├── npymath/
│   │   │   │   └── ...
│   │   │   ├── npysort/
│   │   │   │   └── ...
│   │   │   ├── umath/
│   │   │   │   └── ...
│   │   │   └── dummymodule.c
│   │   ├── tests/
│   │   │   ├── data/
│   │   │   │   └── ...
│   │   │   ├── examples/
│   │   │   │   └── ...
│   │   │   ├── _locales.py
│   │   │   ├── _natype.py
│   │   │   ├── test__exceptions.py
│   │   │   ├── test_abc.py
│   │   │   ├── test_api.py
│   │   │   ├── test_argparse.py
│   │   │   ├── test_array_api_info.py
│   │   │   ├── ... (60 more items)
│   │   ├── __init__.py
│   │   ├── __init__.pyi
│   │   ├── _add_newdocs.py
│   │   ├── _add_newdocs_scalars.py
│   │   ├── _asarray.py
│   │   ├── ... (51 more items)
│   ├── _pyinstaller/
│   │   ├── tests/
│   │   │   ├── __init__.py
│   │   │   ├── pyinstaller-smoke.py
│   │   │   └── test_pyinstaller.py
│   │   ├── __init__.py
│   │   └── hook-numpy.py
│   ├── _typing/
│   │   ├── __init__.py
│   │   ├── _add_docstring.py
│   │   ├── _array_like.py
│   │   ├── _callable.pyi
│   │   ├── _char_codes.py
│   │   ├── _dtype_like.py
│   │   ├── _extended_precision.py
│   │   ├── _nbit.py
│   │   ├── _nbit_base.py
│   │   ├── ... (5 more items)
│   ├── _utils/
│   │   ├── __init__.py
│   │   ├── _convertions.py
│   │   ├── _inspect.py
│   │   └── _pep440.py
│   ├── char/
│   │   ├── __init__.py
│   │   └── __init__.pyi
│   ├── compat/
│   │   ├── tests/
│   │   │   └── __init__.py
│   │   ├── __init__.py
│   │   └── py3k.py
│   ├── core/
│   │   ├── __init__.py
│   │   ├── __init__.pyi
│   │   ├── _dtype.py
│   │   ├── _dtype_ctypes.py
│   │   ├── _internal.py
│   │   ├── _multiarray_umath.py
│   │   ├── _utils.py
│   │   ├── arrayprint.py
│   │   ├── defchararray.py
│   │   ├── ... (11 more items)
│   ├── ctypeslib/
│   │   ├── __init__.py
│   │   ├── __init__.pyi
│   │   ├── _ctypeslib.py
│   │   └── _ctypeslib.pyi
│   ├── ... (43 more items)
├── requirements/
│   ├── all_requirements.txt
│   ├── build_requirements.txt
│   ├── ci32_requirements.txt
│   ├── ci_requirements.txt
│   ├── doc_requirements.txt
│   ├── emscripten_test_requirements.txt
│   ├── linter_requirements.txt
│   ├── release_requirements.txt
│   ├── setuptools_requirement.txt
│   └── test_requirements.txt
├── tools/
│   ├── c_coverage/
│   │   ├── HOWTO_C_COVERAGE.txt
│   │   ├── c_coverage_collect.sh
│   │   └── c_coverage_report.py
│   ├── ci/
│   │   ├── emscripten/
│   │   │   └── emscripten.meson.cross
│   │   ├── _blis_debian.pc
│   │   ├── array-api-xfails.txt
│   │   ├── cirrus_arm.yml
│   │   ├── cirrus_wheels.yml
│   │   ├── push_docs_to_repo.py
│   │   ├── run_32_bit_linux_docker.sh
│   │   ├── test_all_newsfragments_used.py
│   │   └── tsan_suppressions.txt
│   ├── swig/
│   │   ├── test/
│   │   │   ├── Array.i
│   │   │   ├── Array1.cxx
│   │   │   ├── Array1.h
│   │   │   ├── Array2.cxx
│   │   │   ├── Array2.h
│   │   │   ├── ArrayZ.cxx
│   │   │   ├── ArrayZ.h
│   │   │   ├── Farray.cxx
│   │   │   ├── Farray.h
│   │   │   ├── ... (29 more items)
│   │   ├── Makefile
│   │   ├── README
│   │   ├── numpy.i
│   │   └── pyfragments.swg
│   ├── wheels/
│   │   ├── LICENSE_linux.txt
│   │   ├── LICENSE_osx.txt
│   │   ├── LICENSE_win32.txt
│   │   ├── check_license.py
│   │   ├── cibw_before_build.sh
│   │   ├── cibw_test_command.sh
│   │   ├── gfortran_utils.sh
│   │   ├── repair_windows.sh
│   │   └── upload_wheels.sh
│   ├── changelog.py
│   ├── check_installed_files.py
│   ├── check_openblas_version.py
│   ├── commitstats.py
│   ├── download-wheels.py
│   ├── ... (8 more items)
├── vendored-meson/
│   └── meson/
├── CITATION.bib
├── ... (16 more items)
```

## Key Files

### Configuration Files

### setup.py

**Path**: tools\swig\test\setup.py
**Language**: Python
**Lines of Code**: 48
**Dependencies**: distutils.core.Extension, distutils.core.setup, numpy

### setup.py

**Path**: numpy\_core\tests\examples\cython\setup.py
**Language**: Python
**Lines of Code**: 30
**Description**: Provide python-space access to the functions exposed in numpy/__init__.pxd for testing.
**Dependencies**: Cython, numpy, numpy._utils._pep440, distutils.core.setup, Cython.Build.cythonize and 2 more

### setup.py

**Path**: numpy\_core\tests\examples\limited_api\setup.py
**Language**: Python
**Lines of Code**: 17
**Description**: Build an example package using the limited Python C API.
**Dependencies**: numpy, setuptools.setup, setuptools.Extension, os

### Python Files

### test_multiarray.py

**Path**: numpy\_core\tests\test_multiarray.py
**Language**: Python
**Lines of Code**: 7923
**Dependencies**: __future__.annotations, collections.abc, tempfile, sys, warnings and 72 more
**Classes**: 143
**Functions**: 40

### core.py

**Path**: numpy\ma\core.py
**Language**: Python
**Lines of Code**: 7018
**Description**: numpy.ma : a package to handle missing or invalid values. This package was initially written for numarray by Paul F. Dubois at Lawrence Livermore National Laboratory. In 2006, the package was complet...
**Dependencies**: builtins, functools, inspect, operator, warnings and 23 more
**Classes**: 20
**Functions**: 98

### _add_newdocs.py

**Path**: numpy\_core\_add_newdocs.py
**Language**: Python
**Lines of Code**: 5268
**Description**: This is only meant to add docs to objects defined in C-extension modules. The purpose is to allow easier editing of the docstrings without requiring a re-compile. NOTE: Many of the methods of ndarray...
**Dependencies**: numpy._core.function_base.add_newdoc, numpy._core.overrides.get_array_function_like_doc
**Functions**: 1

## Usage

Please refer to the file summaries for usage examples and API documentation.

## License

This project is licensed under the terms specified in the repository.
