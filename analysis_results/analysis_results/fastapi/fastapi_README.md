# fastapi

## Project Overview

<p align="center"> <a href="https://fastapi.tiangolo.com"><img src="https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png" alt="FastAPI"></a> </p> <p align="center"> <em>FastAPI framework, high performance, easy to learn, fast to code, ready for production</em> </p>

## Installation

Clone the repository:

```bash
git clone https://github.com/tiangolo/fastapi
cd fastapi
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Project Structure

### Project Summary

- **Total Files**: 1130
- **Languages**: Unknown, Python, JavaScript
- **Language Distribution**:
  - Unknown: 1141 files (50.2%)
  - Python: 1130 files (49.7%)
  - JavaScript: 3 files (0.1%)

### Directory Structure

```
fastapi/
├── docs/
│   ├── az/
│   │   ├── docs/
│   │   │   ├── learn/
│   │   │   │   └── ...
│   │   │   └── index.md
│   │   └── mkdocs.yml
│   ├── bn/
│   │   ├── docs/
│   │   │   ├── learn/
│   │   │   │   └── ...
│   │   │   ├── index.md
│   │   │   └── python-types.md
│   │   └── mkdocs.yml
│   ├── de/
│   │   ├── docs/
│   │   │   ├── about/
│   │   │   │   └── ...
│   │   │   ├── advanced/
│   │   │   │   └── ...
│   │   │   ├── deployment/
│   │   │   │   └── ...
│   │   │   ├── how-to/
│   │   │   │   └── ...
│   │   │   ├── learn/
│   │   │   │   └── ...
│   │   │   ├── resources/
│   │   │   │   └── ...
│   │   │   ├── tutorial/
│   │   │   │   └── ...
│   │   │   ├── alternatives.md
│   │   │   ├── async.md
│   │   │   ├── ... (7 more items)
│   │   └── mkdocs.yml
│   ├── em/
│   │   ├── docs/
│   │   │   ├── advanced/
│   │   │   │   └── ...
│   │   │   ├── deployment/
│   │   │   │   └── ...
│   │   │   ├── how-to/
│   │   │   │   └── ...
│   │   │   ├── tutorial/
│   │   │   │   └── ...
│   │   │   ├── alternatives.md
│   │   │   ├── async.md
│   │   │   ├── benchmarks.md
│   │   │   ├── features.md
│   │   │   ├── help-fastapi.md
│   │   │   ├── ... (4 more items)
│   │   └── mkdocs.yml
│   ├── en/
│   │   ├── data/
│   │   │   ├── contributors.yml
│   │   │   ├── external_links.yml
│   │   │   ├── github_sponsors.yml
│   │   │   ├── members.yml
│   │   │   ├── people.yml
│   │   │   ├── skip_users.yml
│   │   │   ├── sponsors.yml
│   │   │   ├── sponsors_badge.yml
│   │   │   ├── topic_repos.yml
│   │   │   ├── ... (2 more items)
│   │   ├── docs/
│   │   │   ├── about/
│   │   │   │   └── ...
│   │   │   ├── advanced/
│   │   │   │   └── ...
│   │   │   ├── css/
│   │   │   │   └── ...
│   │   │   ├── deployment/
│   │   │   │   └── ...
│   │   │   ├── how-to/
│   │   │   │   └── ...
│   │   │   ├── img/
│   │   │   │   └── ...
│   │   │   ├── js/
│   │   │   │   └── ...
│   │   │   ├── learn/
│   │   │   │   └── ...
│   │   │   ├── reference/
│   │   │   │   └── ...
│   │   │   ├── ... (21 more items)
│   │   ├── overrides/
│   │   │   ├── partials/
│   │   │   │   └── ...
│   │   │   └── main.html
│   │   ├── mkdocs.insiders.yml
│   │   ├── mkdocs.maybe-insiders.yml
│   │   ├── mkdocs.no-insiders.yml
│   │   └── mkdocs.yml
│   ├── es/
│   │   ├── docs/
│   │   │   ├── about/
│   │   │   │   └── ...
│   │   │   ├── advanced/
│   │   │   │   └── ...
│   │   │   ├── deployment/
│   │   │   │   └── ...
│   │   │   ├── how-to/
│   │   │   │   └── ...
│   │   │   ├── learn/
│   │   │   │   └── ...
│   │   │   ├── resources/
│   │   │   │   └── ...
│   │   │   ├── tutorial/
│   │   │   │   └── ...
│   │   │   ├── alternatives.md
│   │   │   ├── async.md
│   │   │   ├── ... (10 more items)
│   │   ├── llm-prompt.md
│   │   └── mkdocs.yml
│   ├── fa/
│   │   ├── docs/
│   │   │   ├── advanced/
│   │   │   │   └── ...
│   │   │   ├── tutorial/
│   │   │   │   └── ...
│   │   │   ├── features.md
│   │   │   └── index.md
│   │   └── mkdocs.yml
│   ├── fr/
│   │   ├── docs/
│   │   │   ├── advanced/
│   │   │   │   └── ...
│   │   │   ├── deployment/
│   │   │   │   └── ...
│   │   │   ├── learn/
│   │   │   │   └── ...
│   │   │   ├── tutorial/
│   │   │   │   └── ...
│   │   │   ├── alternatives.md
│   │   │   ├── async.md
│   │   │   ├── benchmarks.md
│   │   │   ├── features.md
│   │   │   ├── help-fastapi.md
│   │   │   ├── ... (4 more items)
│   │   └── mkdocs.yml
│   ├── he/
│   │   ├── docs/
│   │   │   └── index.md
│   │   └── mkdocs.yml
│   ├── ... (18 more items)
├── docs_src/
│   ├── additional_responses/
│   │   ├── tutorial001.py
│   │   ├── tutorial002.py
│   │   ├── tutorial003.py
│   │   └── tutorial004.py
│   ├── additional_status_codes/
│   │   ├── tutorial001.py
│   │   ├── tutorial001_an.py
│   │   ├── tutorial001_an_py310.py
│   │   ├── tutorial001_an_py39.py
│   │   └── tutorial001_py310.py
│   ├── advanced_middleware/
│   │   ├── tutorial001.py
│   │   ├── tutorial002.py
│   │   └── tutorial003.py
│   ├── app_testing/
│   │   ├── app_b/
│   │   │   ├── __init__.py
│   │   │   ├── main.py
│   │   │   └── test_main.py
│   │   ├── app_b_an/
│   │   │   ├── __init__.py
│   │   │   ├── main.py
│   │   │   └── test_main.py
│   │   ├── app_b_an_py310/
│   │   │   ├── __init__.py
│   │   │   ├── main.py
│   │   │   └── test_main.py
│   │   ├── app_b_an_py39/
│   │   │   ├── __init__.py
│   │   │   ├── main.py
│   │   │   └── test_main.py
│   │   ├── app_b_py310/
│   │   │   ├── __init__.py
│   │   │   ├── main.py
│   │   │   └── test_main.py
│   │   ├── __init__.py
│   │   ├── main.py
│   │   ├── test_main.py
│   │   ├── tutorial001.py
│   │   ├── ... (2 more items)
│   ├── async_tests/
│   │   ├── __init__.py
│   │   ├── main.py
│   │   └── test_main.py
│   ├── background_tasks/
│   │   ├── tutorial001.py
│   │   ├── tutorial002.py
│   │   ├── tutorial002_an.py
│   │   ├── tutorial002_an_py310.py
│   │   ├── tutorial002_an_py39.py
│   │   └── tutorial002_py310.py
│   ├── behind_a_proxy/
│   │   ├── tutorial001.py
│   │   ├── tutorial002.py
│   │   ├── tutorial003.py
│   │   └── tutorial004.py
│   ├── bigger_applications/
│   │   ├── app/
│   │   │   ├── internal/
│   │   │   │   └── ...
│   │   │   ├── routers/
│   │   │   │   └── ...
│   │   │   ├── __init__.py
│   │   │   ├── dependencies.py
│   │   │   └── main.py
│   │   ├── app_an/
│   │   │   ├── internal/
│   │   │   │   └── ...
│   │   │   ├── routers/
│   │   │   │   └── ...
│   │   │   ├── __init__.py
│   │   │   ├── dependencies.py
│   │   │   └── main.py
│   │   ├── app_an_py39/
│   │   │   ├── internal/
│   │   │   │   └── ...
│   │   │   ├── routers/
│   │   │   │   └── ...
│   │   │   ├── __init__.py
│   │   │   ├── dependencies.py
│   │   │   └── main.py
│   │   └── __init__.py
│   ├── body/
│   │   ├── tutorial001.py
│   │   ├── tutorial001_py310.py
│   │   ├── tutorial002.py
│   │   ├── tutorial002_py310.py
│   │   ├── tutorial003.py
│   │   ├── tutorial003_py310.py
│   │   ├── tutorial004.py
│   │   └── tutorial004_py310.py
│   ├── ... (60 more items)
├── fastapi/
│   ├── dependencies/
│   │   ├── __init__.py
│   │   ├── models.py
│   │   └── utils.py
│   ├── middleware/
│   │   ├── __init__.py
│   │   ├── cors.py
│   │   ├── gzip.py
│   │   ├── httpsredirect.py
│   │   ├── trustedhost.py
│   │   └── wsgi.py
│   ├── openapi/
│   │   ├── __init__.py
│   │   ├── constants.py
│   │   ├── docs.py
│   │   ├── models.py
│   │   └── utils.py
│   ├── security/
│   │   ├── __init__.py
│   │   ├── api_key.py
│   │   ├── base.py
│   │   ├── http.py
│   │   ├── oauth2.py
│   │   ├── open_id_connect_url.py
│   │   └── utils.py
│   ├── __init__.py
│   ├── __main__.py
│   ├── _compat.py
│   ├── applications.py
│   ├── background.py
│   ├── ... (19 more items)
├── scripts/
│   ├── playwright/
│   │   ├── cookie_param_models/
│   │   │   └── image01.py
│   │   ├── header_param_models/
│   │   │   └── image01.py
│   │   ├── query_param_models/
│   │   │   └── image01.py
│   │   ├── request_form_models/
│   │   │   └── image01.py
│   │   ├── separate_openapi_schemas/
│   │   │   ├── image01.py
│   │   │   ├── image02.py
│   │   │   ├── image03.py
│   │   │   ├── image04.py
│   │   │   └── image05.py
│   │   └── sql_databases/
│   │       ├── image01.py
│   │       └── image02.py
│   ├── contributors.py
│   ├── deploy_docs_status.py
│   ├── docs.py
│   ├── format.sh
│   ├── label_approved.py
│   ├── lint.sh
│   ├── mkdocs_hooks.py
│   ├── notify_translations.py
│   ├── ... (6 more items)
├── tests/
│   ├── test_filter_pydantic_sub_model/
│   │   ├── __init__.py
│   │   ├── app_pv1.py
│   │   └── test_filter_pydantic_sub_model_pv1.py
│   ├── test_modules_same_name_body/
│   │   ├── app/
│   │   │   ├── __init__.py
│   │   │   ├── a.py
│   │   │   ├── b.py
│   │   │   └── main.py
│   │   ├── __init__.py
│   │   └── test_main.py
│   ├── test_tutorial/
│   │   ├── test_additional_responses/
│   │   │   ├── __init__.py
│   │   │   ├── test_tutorial001.py
│   │   │   ├── test_tutorial002.py
│   │   │   ├── test_tutorial003.py
│   │   │   └── test_tutorial004.py
│   │   ├── test_additional_status_codes/
│   │   │   ├── __init__.py
│   │   │   └── test_tutorial001.py
│   │   ├── test_advanced_middleware/
│   │   │   ├── __init__.py
│   │   │   ├── test_tutorial001.py
│   │   │   ├── test_tutorial002.py
│   │   │   └── test_tutorial003.py
│   │   ├── test_async_tests/
│   │   │   ├── __init__.py
│   │   │   └── test_main.py
│   │   ├── test_background_tasks/
│   │   │   ├── __init__.py
│   │   │   ├── test_tutorial001.py
│   │   │   └── test_tutorial002.py
│   │   ├── test_behind_a_proxy/
│   │   │   ├── __init__.py
│   │   │   ├── test_tutorial001.py
│   │   │   ├── test_tutorial002.py
│   │   │   ├── test_tutorial003.py
│   │   │   └── test_tutorial004.py
│   │   ├── test_bigger_applications/
│   │   │   ├── __init__.py
│   │   │   └── test_main.py
│   │   ├── test_body/
│   │   │   ├── __init__.py
│   │   │   └── test_tutorial001.py
│   │   ├── test_body_fields/
│   │   │   ├── __init__.py
│   │   │   └── test_tutorial001.py
│   │   ├── ... (51 more items)
│   ├── test_validate_response_recursive/
│   │   ├── __init__.py
│   │   ├── app_pv1.py
│   │   ├── app_pv2.py
│   │   ├── test_validate_response_recursive_pv1.py
│   │   └── test_validate_response_recursive_pv2.py
│   ├── __init__.py
│   ├── main.py
│   ├── test_additional_properties.py
│   ├── test_additional_properties_bool.py
│   ├── test_additional_response_extra.py
│   ├── ... (143 more items)
├── CITATION.cff
├── CONTRIBUTING.md
├── LICENSE
├── README.md
├── ... (10 more items)
```

## Key Files

### Python Files

### test_include_router_defaults_overrides.py

**Path**: tests\test_include_router_defaults_overrides.py
**Language**: Python
**Lines of Code**: 7200
**Dependencies**: warnings, pytest, fastapi.APIRouter, fastapi.Depends, fastapi.FastAPI and 3 more
**Classes**: 6
**Functions**: 5

### applications.py

**Path**: fastapi\applications.py
**Language**: Python
**Lines of Code**: 3930
**Dependencies**: enum.Enum, typing.Any, typing.Awaitable, typing.Callable, typing.Coroutine and 42 more
**Classes**: 1

### routing.py

**Path**: fastapi\routing.py
**Language**: Python
**Lines of Code**: 3902
**Dependencies**: asyncio, dataclasses, email.message, inspect, json and 68 more
**Classes**: 3
**Functions**: 4

## Usage

Please refer to the file summaries for usage examples and API documentation.

## License

This project is licensed under the terms specified in the repository.
