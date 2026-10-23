Write a Python function `count(n: int, forbidden: list[str]) -> int` that returns how many strings of length `n` over the letters `a`, `b` and `c` contain none of the strings in `forbidden` as a substring, modulo `1_000_000_007`.

- `0 <= n <= 10**18`.
- `forbidden` holds 1 to 3 strings of 1 to 7 letters from `abc`. They may overlap or contain one another.
- Each call must return in well under a second, also for the largest `n`.

Use only the standard library. Reply with only the Python code.
