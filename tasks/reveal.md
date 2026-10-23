In a race, runners `0` to `n - 1` finished in the places given by `place`: runner `v` came in at place `place[v]`, where place `1` is the winner and no two runners share a place. The audience only saw some of the duels. Each pair `(x, y)` in `ahead` tells them that runner `x` finished before runner `y`. They know these pairs, but not `place`.

You may announce the place of some runners. Write a Python function `fewest(n: int, ahead: list[tuple[int, int]], place: list[int]) -> int` that returns the smallest number of runners whose place you must announce so that the audience can work out every runner's place.

For example, `fewest(3, [(0, 1)], [1, 2, 3]) == 1`. Announcing that runner `2` came third settles it, but no announcement at all leaves `[1, 2, 3]`, `[1, 3, 2]` and `[2, 3, 1]` open.

- `1 <= n <= 2 * 10**5` and `0 <= len(ahead) <= 2 * 10**5`.
- The pairs are distinct and agree with `place`.
- Each call must return within a second or two, also for the largest inputs.

Use only the standard library. Reply with only the Python code.
