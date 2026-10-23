def kth(k: int, m: int) -> int:
    # ways[n][last][r]: digit strings of length n that may follow digit `last`
    # (10 = none yet) when the digit sum so far is r mod m, ending on a multiple of m
    ways = [[[int(r == 0) for r in range(m)] for _ in range(11)]]
    while True:
        prev = ways[-1]
        ways.append(
            [
                [
                    sum(prev[d][(r + d) % m] for d in range(10) if d != last)
                    for r in range(m)
                ]
                for last in range(11)
            ]
        )
        n = len(ways) - 1
        count = sum(ways[n - 1][d][d % m] for d in range(1, 10))
        if k <= count:
            break
        k -= count
    digits, last, r = [], 10, 0
    for left in range(n - 1, -1, -1):
        for d in range(1 if last == 10 else 0, 10):
            if d == last:
                continue
            here = ways[left][d][(r + d) % m]
            if k <= here:
                digits.append(d)
                last, r = d, (r + d) % m
                break
            k -= here
    return int("".join(map(str, digits)))
