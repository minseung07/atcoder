import sys

n, m = map(int, sys.stdin.readline().split())
C = [0] * (m + 1)
for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    C[a] -= 1
    C[b] += 1
for i in range(1, m+1):
    print(C[i])