A shop has `n` items; item `j` costs `prices[j]`. It also has `n` coupons; coupon `i` halves a price `cuts[i]` times, rounding down each time, so a price `p` becomes `p // 2**cuts[i]`. Every item gets exactly one coupon, and every coupon goes to exactly one item.

Write a Python function `halves(prices: list[int], cuts: list[int]) -> int` that returns the number of ways to hand out the coupons that give the lowest possible total price, modulo `998244353`. Two ways differ when some coupon goes to a different item. Items and coupons count as different even when their numbers are equal.

For example, `halves([3, 4, 10], [0, 1, 2]) == 2`: the lowest total is `7`, reached as `3 + 4 // 2 + 10 // 4` and as `4 + 3 // 2 + 10 // 4`.

- `1 <= n == len(prices) == len(cuts) <= 5 * 10**4`.
- `1 <= prices[j] <= 10**9` and `0 <= cuts[i] <= 30`.
- Each call must return within a second or two, also for the largest inputs.

Use only the standard library. Reply with only the Python code.
