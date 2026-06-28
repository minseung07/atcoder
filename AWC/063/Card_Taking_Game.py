import sys

n = int(sys.stdin.readline())
V = list(map(int, sys.stdin.readline().split()))

# dp[i][j]: 구간 [i, j]가 남아있을 때 점수 차
dp = [[0] * n for _ in range(n)]
for i in range(n):
    dp[i][i] = V[i]

for i in range(1, n):
    for j in range(i-1, -1, -1):
        dp[j][i] = max(V[j] - dp[j+1][i], V[i] - dp[j][i-1])

print(dp[0][n-1])