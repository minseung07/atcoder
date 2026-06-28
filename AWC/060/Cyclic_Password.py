import sys

n, q, m = map(int, sys.stdin.readline().split())

ten = [0] * 60
ten[0] = 10 % m
for i in range(1, 60):
    ten[i] = (ten[i-1] * ten[i-1]) % m

next_pos = [[0] * (n+1) for _ in range(60)]
value = [[0] * (n+1) for _ in range(60)]
for i in range(1, n+1):
    value[0][i], next_pos[0][i] = map(int, sys.stdin.readline().split())

for p in range(1, 60):
    for i in range(1, n+1):
        next_pos[p][i] = next_pos[p-1][next_pos[p-1][i]]
        value[p][i] = (value[p-1][i] * ten[p-1] + value[p-1][next_pos[p-1][i]]) % m

for _ in range(q):
    s, k = map(int, sys.stdin.readline().split())
    curr = s
    total_v = 0
    for p in range(59, -1, -1):
        if k & (1 << p):
            total_v = (total_v * ten[p] + value[p][curr]) % m
            curr = next_pos[p][curr]
    print(total_v)