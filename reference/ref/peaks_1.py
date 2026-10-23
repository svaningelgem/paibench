from bisect import bisect_right


def _count(N, M, K):
    MOD = 998244353
    n = N - 2
    S = 0
    while (S + 1) * (S + 1) <= K - 1 and S + 1 <= M:
        S += 1
    if S == 0:
        return 0

    def dead(a, b):
        c = min(M, K - a * b)
        lo = max(b, (K + a - 1) // a - 1)
        return c - lo if c > lo else 0

    p_w = []
    p_par = []
    p_t2 = []
    p_dead = []
    p_size = []
    p_single = []
    row_starts = []
    row_first = []
    brk = bytearray(min(M, K - 1) + 3)
    for b in range(1, S + 1):
        A = min(M, (K - 1) // b)
        for a in range(b + 2, A + 1):
            if min(b, K - a * b) != min(b, K - (a - 1) * b):
                brk[a] = 1
        starts = [b]
        if A >= b + 1:
            starts.append(b + 1)
            for a in range(b + 2, A + 1):
                if brk[a]:
                    starts.append(a)
        row_starts.append(starts)
        first = len(p_w)
        row_first.append(first)
        for i, s in enumerate(starts):
            e = starts[i + 1] - 1 if i + 1 < len(starts) else A
            p_w.append(min(b, K - s * b))
            p_size.append(e - s + 1)
            p_single.append(1 if i == 0 else 0)
            if b >= 2:
                ps = row_starts[b - 2]
                p_par.append(row_first[b - 2] + bisect_right(ps, s) - 1)
            else:
                p_par.append(-1)
            p_t2.append(-1 if i == 0 else first)
            d = 0
            for a in range(s, e + 1):
                d += dead(a, b)
            p_dead.append(d % MOD)

    P = len(p_w)
    f = [1 if p_single[i] else 2 for i in range(P)]
    col = [0] * P
    D = 3 * S
    F = [sum(f[i] * p_size[i] for i in range(P)) % MOD]
    steps = min(n, D)
    for _ in range(steps):
        for i in range(P):
            p = p_par[i]
            col[i] = (col[p] + f[p]) % MOD if p >= 0 else 0
        newf = [0] * P
        for i in range(P):
            v = p_w[i] * f[i] + col[i]
            t = p_t2[i]
            if t >= 0:
                v += col[t] + f[t]
            newf[i] = v % MOD
        L = 0
        Dd = 0
        for i in range(P):
            L += newf[i] * p_size[i]
            Dd += f[i] * p_dead[i]
        F.append((L + Dd) % MOD)
        f = newf
    if n <= D:
        return F[n] % MOD

    def pmul(a, b):
        la, lb = len(a), len(b)
        if la == 0 or lb == 0:
            return []
        ba = b"".join(x.to_bytes(9, "little") for x in a)
        bb = b"".join(x.to_bytes(9, "little") for x in b)
        prod = int.from_bytes(ba, "little") * int.from_bytes(bb, "little")
        out_len = la + lb - 1
        pb = prod.to_bytes(9 * (la + lb), "little")
        return [
            int.from_bytes(pb[9 * i : 9 * i + 9], "little") % MOD
            for i in range(out_len)
        ]

    Q = [1]
    for s in range(1, S + 1):
        for _ in range(3):
            nq = [0] * (len(Q) + 1)
            for i, c in enumerate(Q):
                nq[i] = (nq[i] + c) % MOD
                nq[i + 1] = (nq[i + 1] - s * c) % MOD
            Q = nq
    Pn = pmul(F[: D + 1], Q)[: D + 1]
    while n > 0:
        Qn = [(-c if (i & 1) else c) % MOD for i, c in enumerate(Q)]
        U = pmul(Pn, Qn)
        V = pmul(Q, Qn)
        Pn = U[(n & 1) :: 2]
        Q = V[0::2]
        n >>= 1
    if not Pn:
        return 0
    return Pn[0] * pow(Q[0], MOD - 2, MOD) % MOD


def count(n: int, m: int, cap: int) -> int:
    # a[i] + a[j] * a[l] over i < j < l is the reverse of a[i] * a[j] + a[l]: same count
    return _count(n, m, cap)
