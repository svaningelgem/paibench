Write a Python function `kth(k: int, m: int) -> int` that returns the `k`-th smallest positive integer whose decimal digits have no two equal neighbours and add up to a multiple of `m`.

For example, with `m = 3` the sequence starts `3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 36, 39, 42`: `33` is left out because of its equal neighbours, and `31` because its digit sum is not a multiple of 3.

- `1 <= m <= 9` and `1 <= k <= 10**18`.
- Each call must return in well under a second, also for the largest `k`.

Use only the standard library. Reply with only the Python code.
