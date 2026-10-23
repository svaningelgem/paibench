def shifts(lo: list[int], hi: list[int], order: list[int]) -> list[int]:
    n = len(lo)

    def claim(link, start):
        # union-find over free slots: the first free slot reached from `start`
        path = []
        while link[start] != start:
            path.append(start)
            start = link[start]
        for p in path:
            link[p] = start
        return start

    # day each job takes when it turns early (scanning from the left in switch order)
    nxt = list(range(n + 1))
    early = []
    for j in order:
        d = claim(nxt, lo[j])
        nxt[d] = d + 1
        early.append(d)
    # day each job gives up as a late job (scanning from the right in reverse switch order)
    prv = list(range(n + 1))
    late = [0] * n
    for i in range(n - 1, -1, -1):
        d = claim(prv, hi[order[i]] + 1)
        prv[d] = d - 1
        late[i] = d - 1

    # balance of the n - 1 gaps between days: range add, leftmost position breaking a bound
    size = 1
    while size < max(1, n - 1):
        size *= 2
    lg = size.bit_length() - 1
    mn = [0] * (2 * size)
    mx = [0] * (2 * size)
    lz = [0] * size
    for i in range(n - 1, size):
        mn[size + i], mx[size + i] = 1 << 60, -(1 << 60)
    for i in range(size - 1, 0, -1):
        mn[i], mx[i] = min(mn[2 * i], mn[2 * i + 1]), max(mx[2 * i], mx[2 * i + 1])

    def put(k, f):
        mn[k] += f
        mx[k] += f
        if k < size:
            lz[k] += f

    def push(k):
        if lz[k]:
            put(2 * k, lz[k])
            put(2 * k + 1, lz[k])
            lz[k] = 0

    def pull(k):
        mn[k] = min(mn[2 * k], mn[2 * k + 1])
        mx[k] = max(mx[2 * k], mx[2 * k + 1])

    def add(l, r, f):
        if l == r:
            return
        l += size
        r += size
        for i in range(lg, 0, -1):
            if ((l >> i) << i) != l:
                push(l >> i)
            if ((r >> i) << i) != r:
                push((r - 1) >> i)
        l2, r2 = l, r
        while l2 < r2:
            if l2 & 1:
                put(l2, f)
                l2 += 1
            if r2 & 1:
                r2 -= 1
                put(r2, f)
            l2 >>= 1
            r2 >>= 1
        for i in range(1, lg + 1):
            if ((l >> i) << i) != l:
                pull(l >> i)
            if ((r >> i) << i) != r:
                pull((r - 1) >> i)

    def run(l, ok):
        # largest r with ok(node) for every position in [l, r)
        if l >= n - 1:
            return n - 1
        l += size
        for i in range(lg, 0, -1):
            push(l >> i)
        while True:
            while l % 2 == 0:
                l >>= 1
            if not ok(l):
                while l < size:
                    push(l)
                    l *= 2
                    if ok(l):
                        l += 1
                return l - size
            l += 1
            if l & -l == l:
                return n - 1

    # per direction: gaps a move may cross for free, then gaps it pays for
    free = {1: lambda k: mn[k] >= 0, -1: lambda k: mn[k] >= 1}
    paid = {1: lambda k: mx[k] <= -1, -1: lambda k: mx[k] <= 0}
    total = sum(hi) - n * (n - 1) // 2
    out = [total]
    for i in range(n):
        l, r, sign = early[i], late[i], 1
        if l > r:
            l, r, sign = r, l, -1
        total += l + r - lo[order[i]] - hi[order[i]]
        m = l
        while m < r:
            nm = min(r, run(m, free[sign]))
            total += (nm - m) * sign
            m = nm
            nm = min(r, run(m, paid[sign]))
            total -= (nm - m) * sign
            m = nm
        add(l, r, sign)
        out.append(total)
    return out
