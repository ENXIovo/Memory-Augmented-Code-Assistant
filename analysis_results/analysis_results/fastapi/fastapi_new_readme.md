# FastAPI
FastAPI is a modern, high-performance web framework for building APIs with Python 3.6+ based on standard Python-type hints. It is designed to be easy to learn, quick to code, and ready for production.

## Installation
To install FastAPI, use pip:

```bash
pip install fastapi[standard]
```

This installation includes all necessary dependencies.

## Components
The FastAPI repository contains the following key files and modules:

- `fastapi/__init__.py`: The main module of the FastAPI framework, providing high-performance capabilities and easy integration.
- `fastapi/applications.py`: Contains the `FastAPI` application class, which is the main entry point to create FastAPI applications.
- `fastapi/cli.py`: Command line interface for FastAPI applications, allowing easy execution of commands.
- `fastapi/security/api_key.py`: Implements security features such as API key retrieval using headers, cookies, and query parameters.
- `fastapi/openapi/__init__.py`: Manages OpenAPI schema generation for FastAPI.

### Documentation Examples
- `docs_src/first_steps/tutorial001.py`: Example tutorial for beginners.
- `docs_src/first_steps/tutorial002.py`: Continuation of beginner tutorials.
- `docs_src/static_files/tutorial001.py`: Demonstrates static file handling.

## Usage
Here’s a simple example of how to create a FastAPI application:

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}
```

To run the application, save it as `main.py` and execute:

```bash
uvicorn main:app --reload
```

This will start a server at `http://127.0.0.1:8000`, where you can access the endpoint.

## API Overview
Below are key functions and classes available within FastAPI:

### `FastAPI`
The main class used to create FastAPI applications. It is designed for high performance and ease of use.

### `main()`
This function in `fastapi/cli.py` provides command-line utilities for running FastAPI applications. It shows warning messages if FastAPI dependencies are not properly installed.

### `create_app()`
Used to create a FastAPI instance for testing purposes, including various route examples and body examples using Pydantic models.

### Security Classes
- **`APIKeyBase`**, **`APIKeyQuery`**, **`APIKeyHeader`**, **`APIKeyCookie`**: Classes that facilitate API key management through different methods.

For more detailed documentation, tutorials, and guidance, please refer to the official FastAPI documentation at [FastAPI Docs](https://fastapi.tiangolo.com/).