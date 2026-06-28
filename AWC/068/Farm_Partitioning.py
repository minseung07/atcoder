import sys

n, m = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))
sA = [0] * (n+1)
for i in range(n):
    sA[i+1] = sA[i] + A[i]

mx = 0
mn = sA[n]
for _ in range(m):
    l, r = map(int, sys.stdin.readline().split())
    x = sA[r] - sA[l-1]
    mn = min(mn, x)
    mx = max(mx, x)
print(mx - mn)
