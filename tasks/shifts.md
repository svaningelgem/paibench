A worker does `n` jobs in `n` days, exactly one job per day. Days and jobs are numbered from `0`. Job `j` may be done on any day from `lo[j]` to `hi[j]`, inclusive. Both `lo` and `hi` are non-decreasing, and `lo[j] <= j <= hi[j]`, so doing job `j` on day `j` is always allowed.

A *late* job done on day `d` costs `hi[j] - d`; an *early* job costs `d - lo[j]`. At first every job is late. Then the jobs become early one at a time, in the order given by `order` (a permutation of `0` to `n - 1`), and stay early.

Write a Python function `shifts(lo: list[int], hi: list[int], order: list[int]) -> list[int]` that returns `n + 1` numbers: the lowest possible total cost of a schedule before any job became early, and after each of the `n` changes.

For example, `shifts([0, 0, 1], [2, 2, 2], [1, 0, 2]) == [3, 1, 1, 2]`. When only job `1` is early, the best schedule does jobs `1`, `0`, `2` on days `0`, `1`, `2`, with costs `0 + 1 + 0`.

- `1 <= n <= 2 * 10**4`.
- Each call must return within a second or two, also for the largest inputs.

Use only the standard library. Reply with only the Python code.
