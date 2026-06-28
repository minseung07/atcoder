import sys

n, m = map(int, sys.stdin.readline().split())
S = [0] + list(map(int, sys.stdin.readline().split()))
graph = [[float('inf')] * (n+1) for _ in range(n+1)]
for i in range(1, n+1):
    graph[i][i] = 0
for _ in range(m):
    u, v, w = map(int, sys.stdin.readline().split())
    graph[u][v] = w
    graph[v][u] = w

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

C = [0] * (n+1)
check = [[0] * (n+1) for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(1, n+1):
        if graph[i][j] <= S[i]:
            check[i][j] = 1
            C[i] += 1

cnt = 0
for i in range(1, n+1):
    for j in range(i+1, n+1):
        if C[i] == C[j] and check[i][j] and check[j][i]:
            cnt += 1
print(cnt)