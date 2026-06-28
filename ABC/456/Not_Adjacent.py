import sys

s = sys.stdin.readline().strip()
dp = [[0] * 3 for _ in range(len(s)+1)]

if s[0] == "a": dp[1][0] = 1
if s[0] == "b": dp[1][1] = 1
if s[0] == "c": dp[1][2] = 1

mod = 998244353

for i in range(2, len(s) + 1):
    if s[i-1] == "a":
        dp[i][0] = (dp[i-1][1] + dp[i-1][2] + 1) % mod
    if s[i-1] == "b":
        dp[i][1] = (dp[i-1][0] + dp[i-1][2] + 1) % mod
    if s[i-1] == "c":
        dp[i][2] = (dp[i-1][0] + dp[i-1][1] + 1) % mod

res = 0
for i in range(1, len(s) + 1):
    res += sum(dp[i])
    res %= mod
print(res)