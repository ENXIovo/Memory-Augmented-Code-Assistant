# pandas

## Project Overview

<picture align="center"> <source media="(prefers-color-scheme: dark)" srcset="https://pandas.pydata.org/static/img/pandas_white.svg"> <img alt="Pandas Logo" src="https://pandas.pydata.org/static/img/pandas.svg"> </picture>

## Installation

Clone the repository:

```bash
git clone https://github.com/pandas-dev/pandas
cd pandas
```

## Project Structure

### Project Summary

- **Total Files**: 1500
- **Languages**: Unknown, Python, C/C++ Header, C
- **Language Distribution**:
  - Python: 1500 files (69.2%)
  - Unknown: 643 files (29.7%)
  - C/C++ Header: 12 files (0.6%)
  - C: 12 files (0.6%)

### Directory Structure

```
pandas/
├── LICENSES/
│   ├── BOTTLENECK_LICENCE
│   ├── DATEUTIL_LICENSE
│   ├── HAVEN_LICENSE
│   ├── HAVEN_MIT
│   ├── KLIB_LICENSE
│   ├── MUSL_LICENSE
│   ├── NUMPY_LICENSE
│   ├── PACKAGING_LICENSE
│   ├── PSF_LICENSE
│   ├── ... (4 more items)
├── asv_bench/
│   ├── benchmarks/
│   │   ├── algos/
│   │   │   ├── __init__.py
│   │   │   └── isin.py
│   │   ├── io/
│   │   │   ├── __init__.py
│   │   │   ├── csv.py
│   │   │   ├── excel.py
│   │   │   ├── hdf.py
│   │   │   ├── json.py
│   │   │   ├── parsers.py
│   │   │   ├── pickle.py
│   │   │   ├── sas.py
│   │   │   ├── sql.py
│   │   │   ├── ... (2 more items)
│   │   ├── tslibs/
│   │   │   ├── __init__.py
│   │   │   ├── fields.py
│   │   │   ├── normalize.py
│   │   │   ├── offsets.py
│   │   │   ├── period.py
│   │   │   ├── resolution.py
│   │   │   ├── timedelta.py
│   │   │   ├── timestamp.py
│   │   │   ├── tslib.py
│   │   │   └── tz_convert.py
│   │   ├── __init__.py
│   │   ├── algorithms.py
│   │   ├── arithmetic.py
│   │   ├── array.py
│   │   ├── attrs_caching.py
│   │   ├── boolean.py
│   │   ├── ... (33 more items)
│   └── asv.conf.json
├── ci/
│   ├── deps/
│   │   ├── actions-310-minimum_versions.yaml
│   │   ├── actions-310.yaml
│   │   ├── actions-311-downstream_compat.yaml
│   │   ├── actions-311-numpydev.yaml
│   │   ├── actions-311-pyarrownightly.yaml
│   │   ├── actions-311.yaml
│   │   ├── actions-312.yaml
│   │   └── actions-pypy-39.yaml
│   ├── code_checks.sh
│   ├── meta.yaml
│   ├── run_tests.sh
│   └── upload_wheels.sh
├── doc/
│   ├── _templates/
│   │   ├── autosummary/
│   │   │   ├── accessor.rst
│   │   │   ├── accessor_attribute.rst
│   │   │   ├── accessor_callable.rst
│   │   │   ├── accessor_method.rst
│   │   │   ├── class.rst
│   │   │   └── class_without_autosummary.rst
│   │   ├── api_redirect.html
│   │   ├── pandas_footer.html
│   │   └── sidebar-nav-bs.html
│   ├── cheatsheet/
│   │   ├── Pandas_Cheat_Sheet.pdf
│   │   ├── Pandas_Cheat_Sheet.pptx
│   │   ├── Pandas_Cheat_Sheet_FA.pdf
│   │   ├── Pandas_Cheat_Sheet_FA.pptx
│   │   ├── Pandas_Cheat_Sheet_JA.pdf
│   │   ├── Pandas_Cheat_Sheet_JA.pptx
│   │   └── README.md
│   ├── data/
│   │   ├── air_quality_long.csv
│   │   ├── air_quality_no2.csv
│   │   ├── air_quality_no2_long.csv
│   │   ├── air_quality_parameters.csv
│   │   ├── air_quality_pm25_long.csv
│   │   ├── air_quality_stations.csv
│   │   ├── baseball.csv
│   │   ├── iris.data
│   │   └── titanic.csv
│   ├── scripts/
│   │   └── eval_performance.py
│   ├── source/
│   │   ├── _static/
│   │   │   ├── css/
│   │   │   │   └── ...
│   │   │   ├── schemas/
│   │   │   │   └── ...
│   │   │   ├── spreadsheets/
│   │   │   │   └── ...
│   │   │   ├── style/
│   │   │   │   └── ...
│   │   │   ├── ci.png
│   │   │   ├── df_repr_truncated.png
│   │   │   ├── eval-perf.png
│   │   │   ├── index_api.svg
│   │   │   ├── index_contribute.svg
│   │   │   ├── ... (24 more items)
│   │   ├── development/
│   │   │   ├── gitpod-imgs/
│   │   │   │   └── ...
│   │   │   ├── community.rst
│   │   │   ├── contributing.rst
│   │   │   ├── contributing_codebase.rst
│   │   │   ├── contributing_docstring.rst
│   │   │   ├── contributing_documentation.rst
│   │   │   ├── contributing_environment.rst
│   │   │   ├── contributing_gitpod.rst
│   │   │   ├── copy_on_write.rst
│   │   │   ├── ... (7 more items)
│   │   ├── getting_started/
│   │   │   ├── comparison/
│   │   │   │   └── ...
│   │   │   ├── intro_tutorials/
│   │   │   │   └── ...
│   │   │   ├── index.rst
│   │   │   ├── install.rst
│   │   │   ├── overview.rst
│   │   │   └── tutorials.rst
│   │   ├── reference/
│   │   │   ├── arrays.rst
│   │   │   ├── extensions.rst
│   │   │   ├── frame.rst
│   │   │   ├── general_functions.rst
│   │   │   ├── groupby.rst
│   │   │   ├── index.rst
│   │   │   ├── indexing.rst
│   │   │   ├── io.rst
│   │   │   ├── missing_value.rst
│   │   │   ├── ... (8 more items)
│   │   ├── user_guide/
│   │   │   ├── templates/
│   │   │   │   └── ...
│   │   │   ├── 10min.rst
│   │   │   ├── advanced.rst
│   │   │   ├── basics.rst
│   │   │   ├── boolean.rst
│   │   │   ├── categorical.rst
│   │   │   ├── cookbook.rst
│   │   │   ├── copy_on_write.rst
│   │   │   ├── dsintro.rst
│   │   │   ├── ... (21 more items)
│   │   ├── whatsnew/
│   │   │   ├── index.rst
│   │   │   ├── v0.10.0.rst
│   │   │   ├── v0.10.1.rst
│   │   │   ├── v0.11.0.rst
│   │   │   ├── v0.12.0.rst
│   │   │   ├── v0.13.0.rst
│   │   │   ├── v0.13.1.rst
│   │   │   ├── v0.14.0.rst
│   │   │   ├── v0.14.1.rst
│   │   │   ├── ... (92 more items)
│   │   ├── conf.py
│   │   └── index.rst.template
│   ├── sphinxext/
│   │   ├── README.rst
│   │   ├── announce.py
│   │   └── contributors.py
│   ├── make.py
│   └── redirects.csv
├── gitpod/
│   ├── Dockerfile
│   ├── gitpod.Dockerfile
│   ├── settings.json
│   └── workspace_config
├── pandas/
│   ├── _config/
│   │   ├── __init__.py
│   │   ├── config.py
│   │   ├── dates.py
│   │   ├── display.py
│   │   └── localization.py
│   ├── _libs/
│   │   ├── include/
│   │   │   └── pandas/
│   │   │       └── ...
│   │   ├── src/
│   │   │   ├── datetime/
│   │   │   │   └── ...
│   │   │   ├── parser/
│   │   │   │   └── ...
│   │   │   └── vendored/
│   │   │       └── ...
│   │   ├── tslibs/
│   │   │   ├── __init__.py
│   │   │   ├── base.pxd
│   │   │   ├── base.pyx
│   │   │   ├── ccalendar.pxd
│   │   │   ├── ccalendar.pyi
│   │   │   ├── ccalendar.pyx
│   │   │   ├── conversion.pxd
│   │   │   ├── conversion.pyi
│   │   │   ├── conversion.pyx
│   │   │   ├── ... (39 more items)
│   │   ├── window/
│   │   │   ├── __init__.py
│   │   │   ├── aggregations.pyi
│   │   │   ├── aggregations.pyx
│   │   │   ├── indexers.pyi
│   │   │   ├── indexers.pyx
│   │   │   └── meson.build
│   │   ├── __init__.py
│   │   ├── algos.pxd
│   │   ├── algos.pyi
│   │   ├── algos.pyx
│   │   ├── algos_common_helper.pxi.in
│   │   ├── ... (61 more items)
│   ├── _testing/
│   │   ├── __init__.py
│   │   ├── _hypothesis.py
│   │   ├── _io.py
│   │   ├── _warnings.py
│   │   ├── asserters.py
│   │   ├── compat.py
│   │   └── contexts.py
│   ├── api/
│   │   ├── extensions/
│   │   │   └── __init__.py
│   │   ├── indexers/
│   │   │   └── __init__.py
│   │   ├── interchange/
│   │   │   └── __init__.py
│   │   ├── types/
│   │   │   └── __init__.py
│   │   ├── typing/
│   │   │   └── __init__.py
│   │   ├── __init__.py
│   │   └── internals.py
│   ├── arrays/
│   │   └── __init__.py
│   ├── compat/
│   │   ├── numpy/
│   │   │   ├── __init__.py
│   │   │   └── function.py
│   │   ├── __init__.py
│   │   ├── _constants.py
│   │   ├── _optional.py
│   │   ├── pickle_compat.py
│   │   └── pyarrow.py
│   ├── core/
│   │   ├── _numba/
│   │   │   ├── kernels/
│   │   │   │   └── ...
│   │   │   ├── __init__.py
│   │   │   ├── executor.py
│   │   │   └── extensions.py
│   │   ├── array_algos/
│   │   │   ├── __init__.py
│   │   │   ├── datetimelike_accumulations.py
│   │   │   ├── masked_accumulations.py
│   │   │   ├── masked_reductions.py
│   │   │   ├── putmask.py
│   │   │   ├── quantile.py
│   │   │   ├── replace.py
│   │   │   ├── take.py
│   │   │   └── transforms.py
│   │   ├── arrays/
│   │   │   ├── arrow/
│   │   │   │   └── ...
│   │   │   ├── sparse/
│   │   │   │   └── ...
│   │   │   ├── __init__.py
│   │   │   ├── _arrow_string_mixins.py
│   │   │   ├── _mixins.py
│   │   │   ├── _ranges.py
│   │   │   ├── _utils.py
│   │   │   ├── base.py
│   │   │   ├── boolean.py
│   │   │   ├── ... (13 more items)
│   │   ├── computation/
│   │   │   ├── __init__.py
│   │   │   ├── align.py
│   │   │   ├── api.py
│   │   │   ├── check.py
│   │   │   ├── common.py
│   │   │   ├── engines.py
│   │   │   ├── eval.py
│   │   │   ├── expr.py
│   │   │   ├── expressions.py
│   │   │   ├── ... (4 more items)
│   │   ├── dtypes/
│   │   │   ├── __init__.py
│   │   │   ├── api.py
│   │   │   ├── astype.py
│   │   │   ├── base.py
│   │   │   ├── cast.py
│   │   │   ├── common.py
│   │   │   ├── concat.py
│   │   │   ├── dtypes.py
│   │   │   ├── generic.py
│   │   │   ├── ... (2 more items)
│   │   ├── groupby/
│   │   │   ├── __init__.py
│   │   │   ├── base.py
│   │   │   ├── categorical.py
│   │   │   ├── generic.py
│   │   │   ├── groupby.py
│   │   │   ├── grouper.py
│   │   │   ├── indexing.py
│   │   │   ├── numba_.py
│   │   │   └── ops.py
│   │   ├── indexers/
│   │   │   ├── __init__.py
│   │   │   ├── objects.py
│   │   │   └── utils.py
│   │   ├── indexes/
│   │   │   ├── __init__.py
│   │   │   ├── accessors.py
│   │   │   ├── api.py
│   │   │   ├── base.py
│   │   │   ├── category.py
│   │   │   ├── datetimelike.py
│   │   │   ├── datetimes.py
│   │   │   ├── extension.py
│   │   │   ├── frozen.py
│   │   │   ├── ... (5 more items)
│   │   ├── interchange/
│   │   │   ├── __init__.py
│   │   │   ├── buffer.py
│   │   │   ├── column.py
│   │   │   ├── dataframe.py
│   │   │   ├── dataframe_protocol.py
│   │   │   ├── from_dataframe.py
│   │   │   └── utils.py
│   │   ├── ... (31 more items)
│   ├── errors/
│   │   ├── __init__.py
│   │   └── cow.py
│   ├── io/
│   │   ├── clipboard/
│   │   │   └── __init__.py
│   │   ├── excel/
│   │   │   ├── __init__.py
│   │   │   ├── _base.py
│   │   │   ├── _calamine.py
│   │   │   ├── _odfreader.py
│   │   │   ├── _odswriter.py
│   │   │   ├── _openpyxl.py
│   │   │   ├── _pyxlsb.py
│   │   │   ├── _util.py
│   │   │   ├── _xlrd.py
│   │   │   └── _xlsxwriter.py
│   │   ├── formats/
│   │   │   ├── templates/
│   │   │   │   └── ...
│   │   │   ├── __init__.py
│   │   │   ├── _color_data.py
│   │   │   ├── console.py
│   │   │   ├── css.py
│   │   │   ├── csvs.py
│   │   │   ├── excel.py
│   │   │   ├── format.py
│   │   │   ├── html.py
│   │   │   ├── ... (6 more items)
│   │   ├── json/
│   │   │   ├── __init__.py
│   │   │   ├── _json.py
│   │   │   ├── _normalize.py
│   │   │   └── _table_schema.py
│   │   ├── parsers/
│   │   │   ├── __init__.py
│   │   │   ├── arrow_parser_wrapper.py
│   │   │   ├── base_parser.py
│   │   │   ├── c_parser_wrapper.py
│   │   │   ├── python_parser.py
│   │   │   └── readers.py
│   │   ├── sas/
│   │   │   ├── __init__.py
│   │   │   ├── sas7bdat.py
│   │   │   ├── sas_constants.py
│   │   │   ├── sas_xport.py
│   │   │   └── sasreader.py
│   │   ├── __init__.py
│   │   ├── _util.py
│   │   ├── api.py
│   │   ├── ... (12 more items)
│   ├── ... (10 more items)
├── scripts/
│   ├── tests/
│   │   ├── data/
│   │   │   ├── deps_expected_duplicate_package.yaml
│   │   │   ├── deps_expected_no_version.yaml
│   │   │   ├── deps_expected_random.yaml
│   │   │   ├── deps_expected_range.yaml
│   │   │   ├── deps_expected_same_version.yaml
│   │   │   ├── deps_minimum.toml
│   │   │   ├── deps_unmodified_duplicate_package.yaml
│   │   │   ├── deps_unmodified_no_version.yaml
│   │   │   ├── deps_unmodified_random.yaml
│   │   │   ├── ... (2 more items)
│   │   ├── __init__.py
│   │   ├── conftest.py
│   │   ├── test_check_test_naming.py
│   │   ├── test_inconsistent_namespace_check.py
│   │   ├── test_sort_whatsnew_note.py
│   │   ├── test_validate_docstrings.py
│   │   ├── test_validate_exception_location.py
│   │   ├── test_validate_min_versions_in_sync.py
│   │   └── test_validate_unwanted_patterns.py
│   ├── __init__.py
│   ├── check_for_inconsistent_pandas_namespace.py
│   ├── check_test_naming.py
│   ├── cibw_before_build.sh
│   ├── cibw_before_build_windows.sh
│   ├── cibw_before_test_windows.sh
│   ├── download_wheels.sh
│   ├── generate_pip_deps_from_conda.py
│   ├── ... (9 more items)
├── tooling/
│   └── debug/
│       ├── Dockerfile.pandas-debug
│       └── README
├── typings/
│   └── numba.pyi
├── ... (16 more items)
```

## Key Files

### Python Core Files

### frame.py

**Path**: pandas\core\frame.py
**Language**: Python
**Lines of Code**: 11458
**Description**: DataFrame --------- An efficient 2D container for potentially mixed-type time series or other labeled data series. Similar to its R counterpart, data.frame, except providing automatic data alignment ...
**Dependencies**: __future__.annotations, collections, collections.abc, collections.abc.Callable, collections.abc.Hashable and 219 more
**Classes**: 1
**Functions**: 2

### generic.py

**Path**: pandas\core\generic.py
**Language**: Python
**Lines of Code**: 10826
**Dependencies**: __future__.annotations, collections, copy.deepcopy, datetime, functools.partial and 168 more
**Classes**: 1
**Functions**: 1

### series.py

**Path**: pandas\core\series.py
**Language**: Python
**Lines of Code**: 6043
**Description**: Data structure for 1-dimensional cross-sectional and time series data
**Dependencies**: __future__.annotations, collections.abc.Callable, collections.abc.Hashable, collections.abc.Iterable, collections.abc.Mapping and 145 more
**Classes**: 1

### base.py

**Path**: pandas\core\indexes\base.py
**Language**: Python
**Lines of Code**: 6006
**Dependencies**: __future__.annotations, collections.abc, datetime.datetime, functools, itertools.zip_longest and 174 more
**Classes**: 1
**Functions**: 13

### groupby.py

**Path**: pandas\core\groupby\groupby.py
**Language**: Python
**Lines of Code**: 4704
**Description**: Provide the groupby split-apply-combine paradigm. Define the GroupBy class providing the base-class of operations. The SeriesGroupBy and DataFrameGroupBy sub-class (defined in pandas.core.groupby.gen...
**Dependencies**: __future__.annotations, collections.abc.Callable, collections.abc.Hashable, collections.abc.Iterable, collections.abc.Iterator and 110 more
**Classes**: 3
**Functions**: 2

### pytables.py

**Path**: pandas\io\pytables.py
**Language**: Python
**Lines of Code**: 4338
**Description**: High level interface to PyTables for reading and writing pandas data structures to disk
**Dependencies**: __future__.annotations, contextlib.suppress, copy, datetime.date, datetime.tzinfo and 83 more
**Classes**: 21
**Functions**: 21

### Configuration Files

### setup.py

**Path**: setup.py
**Language**: Python
**Lines of Code**: 528
**Description**: Parts of this file were taken from the pyzmq project (https://github.com/zeromq/pyzmq) which have been permitted for use under the BSD license. Parts are from lxml (https://github.com/lxml/lxml)
**Dependencies**: argparse, multiprocessing, os, os.path.join, platform and 13 more
**Classes**: 6
**Functions**: 4

## Usage

Please refer to the file summaries for usage examples and API documentation.

## License

This project is licensed under the terms specified in the repository.
