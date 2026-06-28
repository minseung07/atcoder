import sys

s = sys.stdin.readline().strip()

dp = [[0] * 3 for _ in range(len(s))]

if s[0] == "a": dp[0][0] = 1
if s[0] == "b": dp[0][1] = 1
if s[0] == "c": dp[0][2] = 1

mod = 998244353
for i in range(1, len(s)):
    if s[i] == "a":
        dp[i][0] = (dp[i-1][0] + dp[i-1][1] + dp[i-1][2] + 1) % mod
        dp[i][1] = dp[i-1][1]
        dp[i][2] = dp[i-1][2]
    if s[i] == "b":
        dp[i][0] = dp[i-1][0]
        dp[i][1] = (dp[i-1][0] + dp[i-1][1] + dp[i-1][2] + 1) % mod
        dp[i][2] = dp[i-1][2]
    if s[i] == "c":
        dp[i][0] = dp[i-1][0]
        dp[i][1] = dp[i-1][1]
        dp[i][2] = (dp[i-1][0] + dp[i-1][1] + dp[i-1][2] + 1) % mod

res = (dp[-1][0] + dp[-1][1] + dp[-1][2]) % mod
print(res)