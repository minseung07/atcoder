import sys

n, d = map(int, sys.stdin.readline().split())
C = [0] * n
F = [0] * n
for i in range(n):
    C[i], F[i] = map(int, sys.stdin.readline().split())

dp = [float('inf')] * (d+1)
dp[0] = 0
for i in range(n):
    for j in range(1, d+1):
        prev = max(0, j - F[i])
        if dp[prev] + C[i] < dp[j]:
            dp[j] = dp[prev] + C[i]
print(dp[d])