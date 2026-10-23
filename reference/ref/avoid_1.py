MOD = 1_000_000_007


def count(n: int, forbidden: list[str]) -> int:
    # Aho-Corasick automaton over the forbidden strings; states that end a match are dropped
    goto, fail, bad = [{}], [0], [False]
    for word in forbidden:
        node = 0
        for ch in word:
            if ch not in goto[node]:
                goto[node][ch] = len(goto)
                goto.append({})
                fail.append(0)
                bad.append(False)
            node = goto[node][ch]
        bad[node] = True
    queue = list(goto[0].values())
    for node in queue:
        bad[node] |= bad[fail[node]]
        for ch, child in goto[node].items():
            f = fail[node]
            while f and ch not in goto[f]:
                f = fail[f]
            fail[child] = goto[f][ch] if ch in goto[f] and goto[f][ch] != child else 0
            queue.append(child)

    def step(node: int, ch: str) -> int:
        while node and ch not in goto[node]:
            node = fail[node]
        return goto[node].get(ch, 0)

    good = [s for s in range(len(goto)) if not bad[s]]
    index = {s: i for i, s in enumerate(good)}
    size = len(good)
    matrix = [[0] * size for _ in range(size)]
    for s in good:
        for ch in "abc":
            if not bad[nxt := step(s, ch)]:
                matrix[index[s]][index[nxt]] += 1

    def mul(a: list[list[int]], b: list[list[int]]) -> list[list[int]]:
        cols = list(zip(*b))
        return [
            [sum(x * y for x, y in zip(row, col)) % MOD for col in cols] for row in a
        ]

    vector = [[int(s == 0) for s in good]]
    while n:
        if n & 1:
            vector = mul(vector, matrix)
        matrix = mul(matrix, matrix)
        n >>= 1
    return sum(vector[0]) % MOD
