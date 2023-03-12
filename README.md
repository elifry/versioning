# Versioning

This is a Python module that provides tools for formatting version numbers, building strings for various uses, and classes for versioning schemes.

## Installation

To install this module, run the following command:

```bash
pip install elifry_versioning
```

## Usage
To use this module, import it in your Python code and call the functions or classes that you need. For example:

```python
import elifry_versioning as ev

# Format a version number as a string
version = ev.Version(1, 2, 3, 4)
print(version.format()) # 1.2.3.4

# Build a string for a GitHub release
print(version.build_github_release("elifry", "elifry_versioning")) # https://github.com/elifry/elifry_versioning/releases/tag/1.2.3.4

# Create a versioning scheme object
scheme = ev.SemanticVersioning()
print(scheme.name) # Semantic Versioning
print(scheme.validate(version)) # True
```

## License
This project is licensed under the BSD 2-clause License. See the LICENSE file for more details.
