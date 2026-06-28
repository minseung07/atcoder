import sys

n, q = map(int, sys.stdin.readline().split())
P = [0] + [1] + list(map(int, sys.stdin.readline().split()))

parent = [[0] * (n + 1) for _ in range(20)]
depth = [0] * (n + 1)

for i in range(1, n+1):
    parent[0][i] = P[i]
    depth[i] = depth[P[i]] + 1
for k in range(1, 20):
    for i in range(1, n+1):
        if parent[k-1][i] != 0:
            parent[k][i] = parent[k-1][parent[k-1][i]]

def get_lca(u, v):
    if depth[u] > depth[v]:
        u, v = v, u
    
    diff = depth[v] - depth[u]
    for k in range(20):
        if (diff >> k) & 1:
            v = parent[k][v]
    if u == v: return u

    for k in range(19, -1, -1):
        if parent[k][u] != parent[k][v]:
            u = parent[k][u]
            v = parent[k][v]

    return parent[0][u]

for _ in range(q):
    x, y = map(int, sys.stdin.readline().split())
    print(get_lca(x, y))