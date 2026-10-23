A ring of `n` lamps is numbered `0` to `n - 1`, and `state` gives their values as a string of `0`s and `1`s. In one step every lamp changes at once: its new value is the XOR of the old values of the lamps at the given offsets from it, `new[i] = XOR of old[(i + o) % n] for o in offsets`.

Write a Python function `after(state: str, offsets: list[int], t: int) -> str` that returns the state after `t` steps.

- `1 <= n <= 5000`, `1 <= len(offsets) <= 5`, every offset is in `-n < o < n`, and `0 <= t <= 10**18`.
- Each call must return in well under a second, also for the largest inputs.

Use only the standard library. Reply with only the Python code.
