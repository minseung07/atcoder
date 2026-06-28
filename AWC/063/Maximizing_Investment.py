import sys

n, k = map(int, sys.stdin.readline().split())
S = list(map(int, sys.stdin.readline().split()))

res = sum(S) - max(S) + max(S) * pow(2, k, 10**9+7)
res %= 10**9 + 7
print(res)