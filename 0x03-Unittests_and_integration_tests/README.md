# GithubOrgClient Unit and Integration Tests

This repository contains unit and integration tests for the `GithubOrgClient` class located in the `client.py` module.

## Overview

The tests cover the following:

- **Unit Tests**: 
  - `org` property to verify correct API URL usage and returned data.
  - `_public_repos_url` property to ensure correct repos URL extraction.
  - `public_repos()` method to test proper fetching and filtering of repositories.
  - `has_license()` method for license checking logic.

- **Integration Tests**:
  - Testing `public_repos()` method behavior using real fixture data while mocking only the HTTP requests to avoid actual external calls.
  
## Testing Frameworks and Tools

- Python `unittest` framework
- `unittest.mock` for patching and mocking external calls and properties
- `parameterized` for running parameterized tests
- Fixtures are used to simulate API payloads without making real HTTP requests

## How to Run Tests

```bash
python3 -m unittest discover -s tests -p "test_client.py"
````

or simply:

```bash
python3 test_client.py
```

Make sure the `fixtures.py` file is available in the same directory as `test_client.py`.


## Notes

* No real HTTP requests are made during the tests — all external interactions are mocked.
* Ensure all dependencies (`parameterized`) are installed before running tests:

```bash
pip install parameterized
```

---

Happy Testing! 🚀

