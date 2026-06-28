import sys

s = sys.stdin.readline().strip()
t = sys.stdin.readline().strip()

# dp[j]: T의 j번째 문자열까지 완성
dp = [0] * (len(t) + 1)

ans = 0
for i in range(len(s)):
    dp[0] += 1
    for j in range(len(t) - 1, -1, -1):
        if s[i] == t[j]:
            dp[j+1] += dp[j]
            dp[j] = 0
    ans += sum(dp[:-1])
print(ans)