MOD = 998244353


def _conv(f, g):
    # one big-integer product does the polynomial product: each coefficient gets its own byte slot
    width = (len(f) * (MOD - 1) ** 2).bit_length() // 8 + 1
    pack = lambda p: int.from_bytes(
        b"".join(x.to_bytes(width, "little") for x in p), "little"
    )
    raw = (pack(f) * pack(g)).to_bytes(width * (len(f) + len(g)), "little")
    return [
        int.from_bytes(raw[i : i + width], "little") % MOD
        for i in range(0, width * (len(f) + len(g) - 1), width)
    ]


def halves(a: list[int], b: list[int]) -> int:
    n = len(a)
    fact = [1] * (n + 1)
    for i in range(1, n + 1):
        fact[i] = fact[i - 1] * i % MOD
    inv = [1] * (n + 1)
    inv[n] = pow(fact[n], MOD - 2, MOD)
    for i in range(n, 0, -1):
        inv[i - 1] = inv[i] * i % MOD

    def choose(x, y):
        return 0 if y < 0 or x < y else fact[x] * inv[y] % MOD * inv[x - y] % MOD

    per_level = [0] * 31
    for x in b:
        per_level[x] += 1
    a = sorted(a)
    low = -(1 << 40)
    f = [1]
    for level in range(31):
        k = per_level[level]
        if k >= len(a):
            break
        top = (a[k] + 1) // 2 * 2
        c0 = sum(x == top - 1 for x in a)
        c1 = sum(x == top for x in a)
        c2 = sum(x in (top - 1, top) for x in a[:k])
        c3 = c0 + c1 - c2
        g = [0] * (c3 + 1)
        if low < top - 1:
            s = sum(f) % MOD
            for j in range(c3 + 1):
                g[j] = s * choose(c0, j) % MOD * choose(c1, c3 - j) % MOD
        elif low == top - 1:
            f = _conv(
                [v * fact[c0 - j] % MOD if j <= c0 else 0 for j, v in enumerate(f)],
                inv[: c0 + 1],
            )
            for j in range(max(0, c3 - c1), min(c3, c0) + 1):
                g[j] = (
                    f[c0 - j]
                    * fact[c1]
                    % MOD
                    * inv[c1 - c3 + j]
                    % MOD
                    * inv[j]
                    % MOD
                    * inv[c3 - j]
                    % MOD
                )
        elif low == top:
            tmp = [
                inv[c0 - j] * inv[c1 - c3 + j] % MOD if j >= c3 - c1 else 0
                for j in range(-c1, c0 + 1)
            ]
            f = _conv(
                [
                    v * fact[c0 + j] % MOD * fact[c1 - j] % MOD if j <= c1 else 0
                    for j, v in enumerate(f)
                ],
                tmp,
            )
            for j in range(c3 + 1):
                if j + c1 < len(f):
                    g[j] = f[c1 + j] * inv[j] % MOD * inv[c3 - j] % MOD
        else:
            g = [f[0] * choose(c1, c2) % MOD]
        f = g[sum(x == top - 1 for x in a[k:]) :]
        low = top >> 1
        a = [x >> 1 for x in a[k:]]
    ans = sum(f) % MOD
    for c in per_level:
        ans = ans * fact[c] % MOD
    return ans
