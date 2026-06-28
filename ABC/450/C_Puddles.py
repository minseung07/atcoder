import sys

h, w = map(int, sys.stdin.readline().split())
S = [sys.stdin.readline().strip() for _ in range(h)]
C = [[0] * w for _ in range(h)]

cnt = 1
for i in range(h):
    for j in range(w):
        if S[i][j] == "." and C[i][j] == 0:
            C[i][j] = cnt
            cur = [(i, j)]
            while cur:
                p, q = cur.pop()
                for dp, dq in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                    x, y = p+dp, q+dq
                    if 0 <= x < h and 0 <= y < w and S[x][y] == "." and C[x][y] == 0:
                        C[x][y] = cnt
                        cur.append((x, y))
            cnt += 1

check = [1] * cnt
check[0] = 0
for i in [0, h-1]:
    for j in range(w):
        check[C[i][j]] = 0
for i in range(h):
    for j in [0, w-1]:
        check[C[i][j]] = 0
print(sum(check))