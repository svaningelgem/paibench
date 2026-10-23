A sequence `a` of length `n` holds integers from `1` to `m`. Its peak is the largest value of `a[i] + a[j] * a[l]` over all index triples `i < j < l`.

Write a Python function `count(n: int, m: int, cap: int) -> int` that returns how many such sequences have a peak of at most `cap`, modulo `998244353`.

For example, `count(3, 5, 4) == 9`: the sequences are `(1, 1, 1)`, `(2, 1, 1)`, `(1, 2, 1)`, `(1, 1, 2)`, `(3, 1, 1)`, `(2, 2, 1)`, `(2, 1, 2)`, `(1, 3, 1)` and `(1, 1, 3)`.

- `3 <= n <= 10**9` and `1 <= m, cap <= 10**5`.
- Each call must return within a second or two, also for the largest inputs.

Use only the standard library. Reply with only the Python code.
