# Requests HTTP Library
A simple and user-friendly HTTP library for Python, designed to interact with web services and APIs effortlessly.

## Installation
To install the Requests HTTP Library, you can use pip:

```bash
pip install requests
```

## Components
Here are some of the key components in the project:

- **src/requests/__init__.py**: Initializes the Requests library, defining global functions such as `check_compatibility`.
- **src/requests/api.py**: Contains the core API functions for making HTTP requests (e.g., `get`, `post`, etc.).
- **src/requests/auth.py**: Manages authentication classes and methods, including `HTTPBasicAuth` and `HTTPDigestAuth`.
- **src/requests/models.py**: Provides classes for managing requests and responses.
- **src/requests/exceptions.py**: Defines various exceptions that can be raised by the library.
- **src/requests/hooks.py**: Contains functions for managing event hooks.
- **src/requests/structures.py**: Implements custom data structures like `CaseInsensitiveDict` and `LookupDict`.
- **tests/test_requests.py**: Contains unit tests for all major functionalities of the Requests library.

## Usage
Here's how to use the Requests library to make a simple GET request:

```python
import requests

response = requests.get('https://jsonplaceholder.typicode.com/posts/1')
if response.status_code == 200:
    print(response.json())
```

For making a POST request with JSON data, you can use:

```python
response = requests.post(
    'https://jsonplaceholder.typicode.com/posts',
    json={'title': 'foo', 'body': 'bar', 'userId': 1}
)
print(response.json())
```

### Session Management
You can create a session to persist settings across multiple requests:

```python
with requests.Session() as session:
    session.headers.update({'Authorization': 'Bearer your_token'})
    response = session.get('https://jsonplaceholder.typicode.com/posts/')
    print(response.json())
```

## API Overview
The following are key functions and classes available in the Requests library:

### Classes
- **Session**: Provides cookie persistence, connection pooling, and configuration for HTTP requests.
- **Request**: Represents an HTTP request. This class is used in conjunction with Sessions.

### Functions
- `requests.get(url, **kwargs)`: Sends a GET request to the specified URL.
- `requests.post(url, data=None, json=None, **kwargs)`: Sends a POST request to the specified URL.
- `requests.put(url, data=None, **kwargs)`: Sends a PUT request to the specified URL.
- `requests.delete(url, **kwargs)`: Sends a DELETE request to the specified URL.
- `requests.head(url, **kwargs)`: Sends a HEAD request to the specified URL.
- `requests.options(url, **kwargs)`: Sends an OPTIONS request to the specified URL.

### Exceptions
- `RequestException`: The base class for all exceptions raised by the Requests library.
- `HTTPError`: An error class for handling HTTP errors.

## Tests
To run the tests for the Requests library, you can execute the following command:

```bash
pytest tests/
```

This command will run all unit tests defined in the `tests/test_requests.py` and other test files.

---

For more details on advanced usage and additional topics, please refer to the official documentation or the provided code comments.