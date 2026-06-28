import sys

n, m = map(int, sys.stdin.readline().split())
batch = 1000

A = [[0] * 2001 for _ in range(2001)]
for _ in range(n):
    x, y, c = map(int, sys.stdin.readline().split())
    x1 = x + y
    y1 = x - y + batch
    A[x1][y1] += c
sA = [[0] * 2002 for _ in range(2002)]
for i in range(1, 2002):
    for j in range(1, 2002):
        sA[i][j] = sA[i-1][j] + sA[i][j-1] - sA[i-1][j-1] + A[i-1][j-1]
for _ in range(m):
    p, q, k = map(int, sys.stdin.readline().split())
    p1 = p + q
    q1 = p - q + batch
    res = sA[min(2001, p1+k+1)][min(2001, q1+k+1)] - sA[min(2001, p1+k+1)][max(0, q1-k)] - sA[max(0, p1-k)][min(2001, q1+k+1)] + sA[max(0, p1-k)][max(0, q1-k)]
    print(res)
    