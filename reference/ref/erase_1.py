import math

FAR = 1 << 30


def erase(s: str, queries: list[tuple[int, int]]) -> list[int]:
    # height walk: b goes up, a goes down; erasing "ba" removes a peak
    v = [0]
    for c in s:
        v.append(v[-1] + (1 if c == "b" else -1))
    n = len(s)
    lo = min(v)
    size = 2 * max(v) - 2 * lo + 1
    v = [h - lo for h in v]

    table = [v]
    k = 1
    while (1 << k) <= n + 1:
        prev, half = table[-1], 1 << (k - 1)
        table.append([min(prev[i], prev[i + half]) for i in range(n + 2 - (1 << k))])
        k += 1

    def low(l, r):
        p = (r - l).bit_length() - 1
        return min(table[p][l], table[p][r - (1 << p)])

    pre, nxt, last = [-1] * (n + 1), [FAR] * (n + 1), [-1] * size
    for i, h in enumerate(v):
        pre[i] = last[h]
        if last[h] != -1:
            nxt[last[h]] = i
        last[h] = i

    front, back = [FAR] * size, [-FAR] * size

    def walk(x, y, L, R, fi, la):
        if not (L <= x <= R and L <= y <= R):
            return FAR
        ret = 0
        while True:
            if x < y:
                mi = low(y, R + 1)
                if mi == v[y] == la:
                    return ret
                val = front[fi + la - mi]
                if x < val or not L <= val <= R:
                    return FAR
                nx, ny = back[mi], front[fi + la - mi]
            else:
                mi = low(L, y + 1)
                if mi == v[y] == fi:
                    return ret
                val = back[fi + la - mi]
                if x > val or not L <= val <= R:
                    return FAR
                nx, ny = front[mi], back[fi + la - mi]
            ret += 2 * abs(v[y] - v[nx])
            x, y = nx, ny

    q = len(queries)
    width = max(1, int((n + 1) / max(1.0, math.sqrt(q * 2.0 / 3.0))))
    order = sorted(
        range(q),
        key=lambda i: (
            queries[i][0] // width,
            queries[i][1] if queries[i][0] // width % 2 == 0 else -queries[i][1],
        ),
    )
    ans = [0] * q
    l = r = 0
    for i in order:
        L, R = queries[i]
        while L < l:
            l -= 1
            front[v[l]] = l
            if back[v[l]] == -FAR:
                back[v[l]] = l
        while r < R + 1:
            back[v[r]] = r
            if front[v[r]] == FAR:
                front[v[r]] = r
            r += 1
        while l < L:
            front[v[l]] = nxt[l]
            if back[v[l]] == l:
                back[v[l]] = -FAR
            l += 1
        while r > R + 1:
            r -= 1
            back[v[r]] = pre[r]
            if front[v[r]] == r:
                front[v[r]] = FAR
        fi, la = v[L], v[R]
        mini = low(L, R + 1)
        res = min(
            walk(front[mini], back[fi + la - mini], L, R, fi, la),
            walk(back[mini], front[fi + la - mini], L, R, fi, la),
        )
        res += abs(fi + la - 2 * mini)
        ans[i] = -1 if res >= FAR else res
    return ans
