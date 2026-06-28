import sys

n, k = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))
B = [A[i] % k for i in range(n)]
B.sort()

res = B[-1] - B[0]
for i in range(n-1):
    res = min(res, B[i] + k - B[i+1])
print(res)