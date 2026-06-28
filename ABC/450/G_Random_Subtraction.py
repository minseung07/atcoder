import sys

n = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
mod = 998244353

if n == 1:
    res = A[0] ** 2
    res %= mod
    print(res)
    sys.exit()
if n == 2:
    res = (A[0] - A[1]) ** 2
    res %= mod
    print(res)
    sys.exit()

sigmaA = sum(A) % mod
sigmaAA = sum(a**2 for a in A) % mod

numer = 3 * (n-1) * sigmaAA - 2 * (sigmaA**2 - sigmaAA)
denom = 3 * (n-1)
numer %= mod
denom %= mod

res = numer * pow(denom, mod-2, mod) % mod
print(res)