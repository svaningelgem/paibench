At a party, `n` guests numbered `0` to `n - 1` start as strangers. For every pair of guests, two events happen during the party, each exactly once: the two are *introduced*, and the two are *checked*. A check gives `1` if the two guests are linked by a chain of introductions made before it, and `0` otherwise. All `n * (n - 1)` events happen one after another, in any order. The check results in time order form the party's *record*, a string of `n * (n - 1) // 2` characters.

Write a Python function `records(n: int, log: str) -> int`. `log` has the length of a record and holds only `0`s and `1`s. Return the fewest swaps of two neighbouring characters that turn `log` into a record some party could produce. This is always possible.

For example, `records(4, "110110") == 1`, because `110101` is a possible record and `110110` is not. Also, `records(5, "1111111110") == 3`.

- `2 <= n <= 150`.
- Each call must return within a second or two, also for the largest inputs.

Use only the standard library. Reply with only the Python code.
