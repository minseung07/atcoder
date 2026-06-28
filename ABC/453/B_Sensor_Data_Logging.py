import sys

t, x = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))

cur = A[0]
print(0, cur)
for i in range(1, t+1):
    if abs(A[i] - cur) >= x:
        cur = A[i]
        print(i, cur)