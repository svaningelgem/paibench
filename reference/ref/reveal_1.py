def solve(inp: str) -> str:
    data = inp.split()
    idx = 0
    T = int(data[idx])
    idx += 1
    out = []
    for _ in range(T):
        N = int(data[idx])
        M = int(data[idx + 1])
        idx += 2
        xs = data[idx : idx + 2 * M]
        idx += 2 * M
        P = data[idx : idx + N]
        idx += N
        P = [0] + [int(p) for p in P]
        in_adj = [[] for _ in range(N + 1)]
        for i in range(M):
            a = P[int(xs[2 * i])]
            b = P[int(xs[2 * i + 1])]
            in_adj[b].append(a)
        revealed = [False] * (N + 1)
        isopen = [False] * (N + 1)
        A = [0] * (N + 1)
        stack = []
        ans = 0
        for w in range(1, N + 1):
            while stack and not isopen[stack[-1]]:
                stack.pop()
            ok = stack[-1] if stack else 0
            aw = 0
            hasedge = False
            for z in in_adj[w]:
                if revealed[z]:
                    aw = max(aw, z)
                else:
                    aw = max(aw, A[z])
                if z == ok:
                    hasedge = True
            A[w] = aw
            if ok == 0 or aw > ok or hasedge:
                isopen[w] = True
                stack.append(w)
            else:
                revealed[w] = True
                ans += 1
                st = [z for z in in_adj[w] if isopen[z]]
                for z in st:
                    isopen[z] = False
                while st:
                    z = st.pop()
                    for y in in_adj[z]:
                        if isopen[y]:
                            isopen[y] = False
                            st.append(y)
        out.append(str(ans))
    return "\n".join(out)


def fewest(n: int, ahead: list[tuple[int, int]], place: list[int]) -> int:
    edges = "".join(f"{x + 1} {y + 1}\n" for x, y in ahead)
    return int(solve(f"1\n{n} {len(ahead)}\n{edges}{' '.join(map(str, place))}\n"))
