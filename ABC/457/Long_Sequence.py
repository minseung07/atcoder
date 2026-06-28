import sys

n, k = map(int, sys.stdin.readline().split())
A = [None] * n
L = [0] * n
for i in range(n):
    Ai = list(map(int, sys.stdin.readline().split()))
    L[i] = Ai[0]
    A[i] = Ai[1:]
C = list(map(int, sys.stdin.readline().split()))

cnt = 0
for i in range(n):
    if cnt + C[i] * L[i] < k:
        cnt += C[i] * L[i]
    else:
        x = k - cnt
        x %= L[i]
        print(A[i][x-1])
        break