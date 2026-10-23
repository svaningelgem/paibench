from bisect import bisect_left, bisect_right

LIMIT = 400


def _insert(boffs, bqs, mins, o, q):
    if not boffs:
        boffs.append([o])
        bqs.append([q])
        mins.append(o)
        return
    bi = bisect_right(mins, o) - 1
    bi = max(bi, 0)
    lst = boffs[bi]
    j = bisect_left(lst, o)
    lst.insert(j, o)
    bqs[bi].insert(j, q)
    if j == 0:
        mins[bi] = o
    if len(lst) > LIMIT:
        h = len(lst) >> 1
        boffs.insert(bi + 1, lst[h:])
        bqs.insert(bi + 1, bqs[bi][h:])
        mins.insert(bi + 1, lst[h])
        del lst[h:]
        del bqs[bi][h:]


def _delete_range(boffs, bqs, mins, bi, j, r):
    last = None
    while bi < len(boffs):
        lst = boffs[bi]
        n = len(lst)
        if j >= n:
            bi += 1
            j = 0
            continue
        if lst[j] > r:
            break
        k = bisect_right(lst, r)
        ql = bqs[bi]
        last = (lst[k - 1], ql[k - 1])
        if j == 0 and k == n:
            del boffs[bi]
            del bqs[bi]
            del mins[bi]
        else:
            del lst[j:k]
            del ql[j:k]
            if j == 0:
                mins[bi] = lst[0]
            if k < n:
                break
            bi += 1
            j = 0
    return last


def solve_case(N, P, X, Y, A, C):
    Xm1 = X - 1
    Xm2 = X - 2
    YX = Y - X + 1
    Ym1 = Y - 1
    blk = {}
    for a, c in zip(A, C):
        b, p = divmod(a, Y)
        lo = p - Xm1
        lo = max(lo, 0)
        w = (lo, p, c)
        if b in blk:
            blk[b].append(w)
        else:
            blk[b] = [w]
        if p <= Xm2:
            w2 = (p + YX, Ym1, c)
            if b - 1 in blk:
                blk[b - 1].append(w2)
            else:
                blk[b - 1] = [w2]
    bs = sorted(blk)
    cur = 0
    i = 0
    nb = len(bs)
    while i < nb:
        j = i
        while j + 1 < nb and bs[j + 1] == bs[j] + 1:
            j += 1
        run = bs[i : j + 1]
        i = j + 1
        cs = {0}
        evs = []
        for b in run:
            ev = {}
            for lo, hi, c in blk[b]:
                ev[lo] = ev.get(lo, 0) + c
                cs.add(lo)
                if hi < Ym1:
                    ev[hi + 1] = ev.get(hi + 1, 0) - c
                    cs.add(hi + 1)
            evs.append(ev)
        coords = sorted(cs)
        idx = {c: k + 1 for k, c in enumerate(coords)}
        m = len(coords)
        tree = [0] * (m + 1)
        pc = 0
        boffs = [[0]]
        bqs = [[cur]]
        mins = [0]
        for ev in evs:
            keys = sorted(ev)
            segs = []
            start = 0
            v = -P
            for k in keys:
                if k > start:
                    if v > 0:
                        segs.append((start, k - 1, v))
                    elif segs and segs[-1][2] == 0:
                        segs[-1] = (segs[-1][0], k - 1, 0)
                    else:
                        segs.append((start, k - 1, 0))
                v += ev[k]
                start = k
            if v > 0:
                segs.append((start, Ym1, v))
            elif segs and segs[-1][2] == 0:
                segs[-1] = (segs[-1][0], Ym1, 0)
            else:
                segs.append((start, Ym1, 0))
            v0 = -P + ev.get(0, 0)
            cur0 = cur
            o_last = 0
            q_last = bqs[0][0]
            for l, r, v in segs:
                bi = bisect_right(mins, l) - 1
                if bi < 0:
                    bi = 0
                    jj = 0
                else:
                    lst = boffs[bi]
                    jj = bisect_left(lst, l)
                    if jj == len(lst):
                        bi += 1
                        jj = 0
                if bi < len(boffs):
                    o_i = boffs[bi][jj]
                else:
                    o_i = r + 1
                if v == 0:
                    if o_i <= r:
                        o_last, q_last = _delete_range(boffs, bqs, mins, bi, jj, r)
                    continue
                if o_i > l:
                    t = idx[o_last]
                    s = 0
                    while t:
                        s += tree[t]
                        t -= t & -t
                    wl = q_last + s - pc
                    if v + wl > cur:
                        t = idx[l]
                        s = 0
                        while t:
                            s += tree[t]
                            t -= t & -t
                        _insert(boffs, bqs, mins, l, wl - s + pc)
                        if o_i > r:
                            cur = v + wl
                        else:
                            b2 = bisect_right(mins, r) - 1
                            lst = boffs[b2]
                            k = bisect_right(lst, r) - 1
                            o_last = lst[k]
                            q_last = bqs[b2][k]
                            t = idx[o_last]
                            s = 0
                            while t:
                                s += tree[t]
                                t -= t & -t
                            cur = v + q_last + s - pc
                        continue
                    if o_i > r:
                        continue
                found = False
                sbi = bi
                sjj = jj
                nbk = len(boffs)
                while bi < nbk:
                    lst = boffs[bi]
                    ql = bqs[bi]
                    n = len(lst)
                    while jj < n:
                        o = lst[jj]
                        if o > r:
                            break
                        q = ql[jj]
                        o_last = o
                        q_last = q
                        t = idx[o]
                        s = 0
                        while t:
                            s += tree[t]
                            t -= t & -t
                        if v + q + s - pc > cur:
                            found = True
                            break
                        jj += 1
                    if found or jj < n:
                        break
                    bi += 1
                    jj = 0
                if found:
                    _delete_range(boffs, bqs, mins, sbi, sjj, o_last - 1)
                    b2 = bisect_right(mins, r) - 1
                    lst = boffs[b2]
                    k = bisect_right(lst, r) - 1
                    o2 = lst[k]
                    if o2 != o_last:
                        o_last = o2
                        q_last = bqs[b2][k]
                        t = idx[o_last]
                        s = 0
                        while t:
                            s += tree[t]
                            t -= t & -t
                    cur = v + q_last + s - pc
                else:
                    _delete_range(boffs, bqs, mins, sbi, sjj, r)
            if not boffs or mins[0] != 0:
                _insert(boffs, bqs, mins, 0, cur0 - (tree[1] - pc) - v0)
            for k, d in ev.items():
                t = idx[k]
                while t <= m:
                    tree[t] += d
                    t += t & -t
            pc += P
    return cur


def solve(inp: str) -> str:
    data = inp.split()
    T = int(data[0])
    pos = 1
    out = []
    for _ in range(T):
        N = int(data[pos])
        P = int(data[pos + 1])
        X = int(data[pos + 2])
        Y = int(data[pos + 3])
        pos += 4
        A = data[pos : pos + N]
        pos += N
        C = data[pos : pos + N]
        pos += N
        if N == 1:
            c = int(C[0]) - P
            out.append(max(0, c))
            continue
        if N == 2:
            a1 = int(A[0])
            a2 = int(A[1])
            c1 = int(C[0])
            c2 = int(C[1])
            if a1 > a2:
                a1, a2 = a2, a1
                c1, c2 = c2, c1
            if a2 - a1 <= X - 1:
                r = c1 + c2 - P
            else:
                r = max(c1 - P, c2 - P)
                if a2 - a1 + X - 1 >= Y:
                    r = max(r, c1 + c2 - 2 * P)
            out.append(max(0, r))
            continue
        out.append(solve_case(N, P, X, Y, list(map(int, A)), list(map(int, C))))
    return "\n".join(map(str, out))


def profit(fee: int, open_for: int, gap: int, customers: list[tuple[int, int]]) -> int:
    a = " ".join(str(t) for t, _ in customers)
    c = " ".join(str(v) for _, v in customers)
    return int(solve(f"1\n{len(customers)} {fee} {open_for} {gap}\n{a}\n{c}\n"))
