Write a Python function `calc(expr: str) -> float` that evaluates an arithmetic expression. Do not use `eval`, `exec` or the `ast` module.

- Numbers: digits with an optional fractional part, e.g. `3`, `0.5`, `.5`.
- Binary operators `+ - * /` and `^` (power). `^` binds tightest, then `* /`, then `+ -`. `^` is right-associative; the others are left-associative.
- Unary `+` and `-`, e.g. `-3`, `--3`, `2*-3`. Unary minus binds looser than `^`: `-2^2` is `-4`, while `2^-1` is `0.5`.
- Parentheses. Whitespace between tokens is ignored.
- Raise `ValueError` for malformed input (e.g. `""`, `"1+"`, `"(1"`, `"1 2"`, `"2**3"`) and `ZeroDivisionError` for division by zero.

Reply with only the Python code.
