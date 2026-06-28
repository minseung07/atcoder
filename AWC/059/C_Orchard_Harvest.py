import sys

n, m = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))
B = [0] * n
for _ in range(m):
    l, r = map(int, sys.stdin.readline().split())
    B[l-1] += 1
    if r < n: B[r] -= 1

cur = B[0]
P = [0] * n
P[0] = cur * A[0]
for i in range(1, n):
    cur += B[i]
    P[i] = A[i] * cur
print(*P)