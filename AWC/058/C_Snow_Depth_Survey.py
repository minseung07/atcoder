import sys

n, m, k = map(int, sys.stdin.readline().split())
A = [0] * n
for _ in range(m):
    l, r = map(int, sys.stdin.readline().split())
    if l >= 1: A[l-1] += 1
    if r < n: A[r] -= 1

cur = 0
cnt = 0
for i in range(n):
    cur += A[i]
    if cur >= k: cnt += 1
print(cnt)