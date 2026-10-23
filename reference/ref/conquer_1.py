def _solve(N, M, K, C, Edge):
    C = [(C[i] - C[0]) % (2 * K + 1) for i in range(N)]

    blue_vertex = [v for v in range(N) if K + 1 <= C[v]]
    blue_vertex.sort(key=lambda v: C[v])

    edge = [[] for v in range(N)]
    for eid, (u, v) in enumerate(Edge):
        if u == 0 or v == 0:
            continue
        edge[u].append((v, eid))
        edge[v].append((u, eid))

    done = [False] * N
    parent = [(-1, -1)] * N
    v_ord = [-1] * N
    lowlink = [-1] * N
    nxt_ord = 0

    eid_to_c = [-1] * M

    sub_blue_cnt = [0] * N
    sub_zero_cnt = [0] * N
    sub_minimum_blue = [2 * K + 1] * N

    for root in blue_vertex:
        if done[root]:
            continue

        st = [(root, -1, -1)]
        done[root] = True

        all_blue_cnt = 0
        all_zero_cnt = 0
        topo = []
        while st:
            v, pv, pid = st.pop()
            if v < 0:
                v = ~v
                topo.append(v)
                if C[v] == 0:
                    all_zero_cnt += 1
                if K + 1 <= C[v]:
                    all_blue_cnt += 1
                lowlink[v] = v_ord[v]
                for nv, eid in edge[v]:
                    if nv == parent[v]:
                        continue
                    if v_ord[nv] > v_ord[v]:
                        lowlink[v] = min(lowlink[v], lowlink[nv])
                    else:
                        lowlink[v] = min(lowlink[v], v_ord[nv])
                continue

            if v_ord[v] != -1:
                continue

            parent[v] = (pv, pid)
            v_ord[v] = nxt_ord
            nxt_ord += 1
            st.append((~v, -1, -1))
            for nv, eid in edge[v]:
                if v_ord[nv] == -1:
                    done[nv] = True
                    st.append((nv, v, eid))

        stack = [(root, -1, -1)]
        nxt_c = 0

        while stack:
            v, pv, pid = stack.pop()

            for nv, eid in edge[v]:
                if v_ord[v] < v_ord[nv] and parent[nv][1] != eid:
                    continue

                if v_ord[v] < v_ord[nv]:
                    stack.append((nv, v, eid))
                    if lowlink[nv] < v_ord[v]:
                        eid_to_c[eid] = eid_to_c[pid]
                    else:
                        eid_to_c[eid] = nxt_c
                        nxt_c += 1
                else:
                    eid_to_c[eid] = eid_to_c[pid]

        st = [(root, -1, -1)]
        check_flg = False
        while st:
            v, pv, pid = st.pop()

            if v < 0:
                v = ~v

                for nv, eid in edge[v]:
                    if v_ord[v] < v_ord[nv] and parent[nv][1] != eid:
                        continue
                    if v_ord[v] < v_ord[nv]:
                        sub_blue_cnt[v] += sub_blue_cnt[nv]
                        sub_zero_cnt[v] += sub_zero_cnt[nv]
                        sub_minimum_blue[v] = min(
                            sub_minimum_blue[v], sub_minimum_blue[nv]
                        )

                if C[v] == 0:
                    sub_zero_cnt[v] += 1
                if K + 1 <= C[v]:
                    sub_blue_cnt[v] += 1
                    sub_minimum_blue[v] = min(sub_minimum_blue[v], C[v])

                if 1 <= C[v] <= K:
                    if C[v] < C[root] - K:
                        continue

                    root_blue = all_blue_cnt
                    root_zero = all_zero_cnt
                    pid = parent[v][1]
                    pid_color = eid_to_c[pid]
                    flg = True

                    child = []

                    for nv, eid in edge[v]:
                        if v_ord[v] < v_ord[nv] and parent[nv][1] != eid:
                            continue
                        if v_ord[v] < v_ord[nv] and eid_to_c[eid] != pid_color:
                            child.append(nv)
                            root_blue -= sub_blue_cnt[nv]
                            root_zero -= sub_zero_cnt[nv]

                            if sub_zero_cnt[nv] > 0 and sub_blue_cnt[nv] == 0:
                                flg = False
                            if (
                                sub_minimum_blue[nv] - K > C[v]
                                and sub_blue_cnt[nv] != 0
                            ):
                                flg = False

                    if root_zero > 0 and root_blue == 0:
                        flg = False

                    if flg:
                        check_flg = True

                continue

            st.append((~v, -1, -1))
            for nv, eid in edge[v]:
                if v_ord[v] < v_ord[nv] and parent[nv][1] != eid:
                    continue
                if v_ord[v] < v_ord[nv]:
                    st.append((nv, v, eid))

        if not check_flg:
            return False

    for v in range(1, N):
        if not done[v] and C[v] == 0:
            return False

    return True


def conquer(k: int, banner: list[int], roads: list[tuple[int, int]]) -> bool:
    return _solve(len(banner), len(roads), k, banner, roads)
