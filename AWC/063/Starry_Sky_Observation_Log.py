import sys

h, w = map(int, sys.stdin.readline().split())
S = [sys.stdin.readline().strip() for _ in range(h)]

k = 0
res = []
for i in range(h):
    for j in range(w):
        if S[i][j] == "T":
            k += 1
            res.append((i+1, j+1))
print(k)
for i, j in res:
    print(i, j)