Write a Python function `compare(a: str, b: str) -> int` that compares two version strings by Semantic Versioning 2.0.0 precedence. Return `-1` if `a` has lower precedence, `0` if equal, `1` if higher. Build metadata (`+...`) is ignored for precedence.

Raise `ValueError` if either string is not a valid SemVer 2.0.0 version (no `v` prefix, no surrounding whitespace). Use only the standard library.

Reply with only the Python code.
