A food stall can open at the start of any whole minute `t`, including negative ones. It then stays open for `open_for` minutes and serves every customer who arrives at minute `t`, `t + 1`, ..., `t + open_for - 1`. Each opening costs `fee`. After opening at minute `t`, the stall can open again at minute `t + gap` at the earliest.

Customer `i` arrives at minute `customers[i][0]` and spends `customers[i][1]` if the stall is open at that minute.

Write a Python function `profit(fee: int, open_for: int, gap: int, customers: list[tuple[int, int]]) -> int` that returns the largest possible total spent by customers minus the total of the fees.

For example, `profit(4, 5, 12, [(3, 6), (5, 2), (11, 9)]) == 7`: open at minute `-1` to serve the first customer, and at minute `11` to serve the third.

- `1 <= len(customers) <= 2 * 10**5` and `1 <= fee <= 10**9`.
- `1 <= open_for <= gap <= 10**9`.
- Every arrival minute is between `1` and `10**18`, and every amount between `1` and `10**9`.
- Each call must return within a second or two, also for the largest inputs.

Use only the standard library. Reply with only the Python code.
