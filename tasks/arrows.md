You are given `n` arrows in the plane; arrow `i` points from the origin to `points[i] = (x, y)`. Choose any subset of the arrows, possibly empty. Let `(X, Y)` be the sum of the chosen arrows and `S` the sum of `x**2 + y**2` over the chosen arrows. The score of the subset is `X**2 + Y**2 - 3 * S`.

Write a Python function `arrows(points: list[tuple[int, int]]) -> int` that returns the largest possible score.

For example, `arrows([(4, 1), (5, -1), (3, 2), (-6, 0), (1, 1)]) == 4`: all arrows except `(-6, 0)` add up to `(13, 3)`, so the score is `169 + 9 - 3 * (17 + 26 + 13 + 2)`.

- `1 <= len(points) <= 2 * 10**4`.
- The absolute values of all `x` add up to at most `10**9`, and likewise for all `y`.
- Each call must return within a second or two, also for the largest inputs.

Use only the standard library. Reply with only the Python code.
