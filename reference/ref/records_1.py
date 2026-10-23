def records(n: int, log: str) -> int:
    total = n * (n - 1) // 2
    # fewest people whose groups give exactly i linked pairs (sum of c * (c - 1) / 2)
    fewest = [0] + [1 << 60] * total
    for i in range(1, total + 1):
        best, j = fewest[i], 2
        while j * (j - 1) // 2 <= i:
            best = min(best, fewest[i - j * (j - 1) // 2] + j)
            j += 1
        fewest[i] = best
    # distance from the end of each 0, nearest first (1-based)
    gaps = [0] + [total - i for i in range(total - 1, -1, -1) if log[i] == "0"]
    m = len(gaps) - 1
    if not m:
        return 0
    start = [-1] * (n + 1)
    for i in range(2, n + 1):
        k = i // 2
        for j in range(max(i * (n - i), m - (i // 2) * ((i + 1) // 2)), m):
            while j + (k - 1) * (i - k + 1) >= m:
                k -= 1
            x, y = n - i, j - i * (n - i)
            if x * (x - 1) // 2 >= y and fewest[x * (x - 1) // 2 - y] <= x:
                start[j + k * (i - k) - m] = max(start[j + k * (i - k) - m], j)
    return min(
        sum(max(0, j + i - gaps[j]) for j in range(start[i] + 1, m + 1))
        for i in range(n)
        if start[i] != -1
    )
