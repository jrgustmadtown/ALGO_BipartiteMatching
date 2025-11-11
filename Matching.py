import sys

inputy = list(map(int, sys.stdin.buffer.read().split()))
t = inputy[0]
idx = 1


def dfs(u, t, flow, adj, capacity, flow_map, visited):
    if u == t:
        return flow
    visited[u] = True
    for v in adj[u]:
        residual = capacity.get((u, v), 0) - flow_map.get((u, v), 0)
        if residual > 0 and not visited[v]:
            pushed = dfs(v, t, min(flow, residual), adj, capacity, flow_map, visited)
            if pushed > 0:
                flow_map[(u, v)] = flow_map.get((u, v), 0) + pushed
                flow_map[(v, u)] = flow_map.get((v, u), 0) - pushed
                return pushed
    return 0


def ford_fulkerson(s, t, adj, capacity):
    flow_map = {}
    maxflow = 0
    while True:
        visited = [False] * (t + 1)
        pushed = dfs(s, t, float('inf'), adj, capacity, flow_map, visited)
        if pushed == 0:
            break
        maxflow += pushed
    return maxflow


for _ in range(t):
    m = inputy[idx]; idx += 1
    n = inputy[idx]; idx += 1
    q = inputy[idx]; idx += 1

    s = 0
    offset = m
    sink = m + n + 1

    adj = {i: [] for i in range(sink + 1)}
    capacity = {}

    # source to A
    for i in range(1, m + 1):
        adj[s].append(i)
        adj[i].append(s)
        capacity[(s, i)] = 1

    # B to sink
    for j in range(1, n + 1):
        bj = offset + j
        adj[bj].append(sink)
        adj[sink].append(bj)
        capacity[(bj, sink)] = 1

    # (A→B)
    for _ in range(q):
        u = inputy[idx]; v = inputy[idx + 1]; idx += 2
        v += offset  # shift B nodes
        adj[u].append(v)
        adj[v].append(u)
        capacity[(u, v)] = 1

    sol = ford_fulkerson(s, sink, adj, capacity)
    print(str(sol) + " " + ("Y" if sol == m else "N"))
