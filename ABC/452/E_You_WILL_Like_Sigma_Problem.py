import sys

n, m = map(int, sys.stdin.readline().split())
A = [0] + list(map(int, sys.stdin.readline().split()))
B = [0] + list(map(int, sys.stdin.readline().split()))
mod = 998244353

sigmaA = [0] * (n+1)
constant = 0
for i in range(1, n+1):
    sigmaA[i] = sigmaA[i-1] + A[i]
    sigmaA[i] %= mod
    constant += i * A[i]
    constant %= mod

res = 0
for j in range(1, m+1):
    minus = 0
    for k in range(n // j + 1):
        mx_idx = min(n, j * (k+1) - 1)
        mn_idx = max(0, j * k - 1)
        minus += j * k * (sigmaA[mx_idx] - sigmaA[mn_idx])
        minus %= mod
    res += B[j] * (constant - minus)
    res %= mod
print(res)