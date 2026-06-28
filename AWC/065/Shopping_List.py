import sys

n, x = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))

cur = 0
idx = -1
for i in range(n):
    cur += A[i]
    if cur >= x:
        idx = i+1
        break
print(idx)