import sys

n, q = map(int, sys.stdin.readline().split())
W = list(map(int, sys.stdin.readline().split()))

A = [0] * n
for _ in range(q):
    l, r, d = map(int, sys.stdin.readline().split())
    if l > 0: A[l-1] += d
    if r < n: A[r] -= d

B = [0] * n
B[0] = A[0]
for i in range(1, n):
    B[i] = B[i-1] + A[i]

cnt = 0
for i in range(n):
    if B[i] >= W[i]:
        cnt += 1
print(cnt)