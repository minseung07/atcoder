import sys

n, m, s, t = map(int, sys.stdin.readline().split())
C = [int(sys.stdin.readline()) for _ in range(n)]
graph = [[] for _ in range(n)]
for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    u, v = u - 1, v - 1
    graph[u].append(v)
    graph[v].append(u)

start = s - 1
end = t - 1

count = [[0] * n for _ in range(1<<n)]
score = [[0] * n for _ in range(1<<n)]

count[1<<start][start] = 1
score[1<<start][start] = C[start]
for mask in range(1<<n):
    for curr in range(n):
        if not count[mask][curr]: continue
        if curr == end: continue
        for next in graph[curr]:
            if not (mask & (1 << next)):
                new = mask | (1 << next)
                count[new][next] += count[mask][curr]
                score[new][next] += score[mask][curr] + count[mask][curr] * C[next]

cnt = 0
total = 0
for mask in range(1<<n):
    cnt += count[mask][end]
    total += score[mask][end]
print(total / cnt)