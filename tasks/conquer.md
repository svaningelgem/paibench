There are `n` towns, numbered `0` to `n - 1`, joined by two-way roads so that every town can reach every other one. Town `v` flies a banner with a number `banner[v]` between `0` and `2 * k`.

A town `u` can capture a town `v` that it has a road to, when `(banner[v] - banner[u]) % (2 * k + 1)` is between `1` and `k`. Town `v` then disappears, and every road that led to `v` now leads to `u` instead: a road between `u` and itself is dropped, and two roads between the same two towns count as one. The banner of `u` does not change.

Write a Python function `conquer(k: int, banner: list[int], roads: list[tuple[int, int]]) -> bool` that returns whether some order of captures leaves town `0` as the only town.

For example, `conquer(1, [0, 2, 1], [(0, 1), (1, 2)])` is `True`: town `2` captures town `1`, which gives a road between towns `0` and `2`, and then town `0` captures town `2`. `conquer(1, [0, 0], [(0, 1)])` is `False`.

- `2 <= n == len(banner) <= 10**5` and `1 <= k <= n`.
- `n - 1 <= len(roads) <= 10**5`. Each road `(a, b)` has `a != b`, and no two roads join the same two towns.
- Each call must return within a second or two, also for the largest inputs.

Use only the standard library. Reply with only the Python code.
