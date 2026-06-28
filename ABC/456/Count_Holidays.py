import sys

mod = 998244353

### Bostan-Mori Algorithm (NTT version, friendly mod = 998244353)

CUT = 32

_rev_cache = {}
_w_cache = {}

def _get_rev(n):
    rev = _rev_cache.get(n)
    if rev is not None:
        return rev
    rev = [0] * n
    half = n >> 1
    for i in range(1, n):
        rev[i] = (rev[i >> 1] >> 1) | ((i & 1) * half)
    _rev_cache[n] = rev
    return rev

def _get_wl(mod, g, inv, l):
    key = (mod, g, inv, l)
    wl = _w_cache.get(key)
    if wl is None:
        root = pow(g, mod - 2, mod) if inv else g
        wl = pow(root, (mod - 1) // l, mod)
        _w_cache[key] = wl
    return wl

def ntt(a, mod=998244353, g=3, inv=False):
    n = len(a)
    rev = _get_rev(n)
    for i in range(n):
        j = rev[i]
        if i < j:
            a[i], a[j] = a[j], a[i]

    l = 2
    while l <= n:
        h = l >> 1
        wl = _get_wl(mod, g, inv, l)
        for i in range(0, n, l):
            w = 1
            e = i + h
            for j in range(i, e):
                u = a[j]
                v = a[j + h] * w % mod
                x = u + v
                if x >= mod:
                    x -= mod
                a[j] = x
                y = u - v
                if y < 0:
                    y += mod
                a[j + h] = y
                w = w * wl % mod
        l <<= 1

    if inv:
        ninv = pow(n, mod - 2, mod)
        for i in range(n):
            a[i] = a[i] * ninv % mod

def multiply(a, b, mod=998244353, g=3, cut=CUT):
    if not a or not b:
        return []

    n1 = len(a)
    n2 = len(b)
    sz = n1 + n2 - 1

    a = [x % mod for x in a]
    b = [x % mod for x in b]

    if min(n1, n2) <= cut:
        r = [0] * sz
        for i, ai in enumerate(a):
            if ai == 0:
                continue
            for j, bj in enumerate(b):
                r[i + j] += ai * bj
        for i in range(sz):
            r[i] %= mod
        return r

    n = 1
    while n < sz:
        n <<= 1

    a += [0] * (n - n1)
    b += [0] * (n - n2)

    ntt(a, mod, g, False)
    ntt(b, mod, g, False)

    for i in range(n):
        a[i] = a[i] * b[i] % mod

    ntt(a, mod, g, True)
    return a[:sz]

"""
선형 점화식의 n번째 항을 O(K log K log N)에 계산합니다.
a_n = c[0]*a_{n-1} + c[1]*a_{n-2} + ... + c[k-1]*a_{n-k}
"""
def bostan_mori(c, a, n, mod=998244353, g=3):
    k = len(c)
    if n < k:
        return a[n] % mod

    Q = [0] * (k + 1)
    Q[0] = 1
    for i in range(k):
        Q[i+1] = -c[i] % mod
        
    P = multiply(a[:k], Q, mod, g)[:k]
    while n > 0:
        Q1 = [val if i % 2 == 0 else (-val % mod) for i, val in enumerate(Q)]

        U = multiply(P, Q1, mod, g)
        V = multiply(Q, Q1, mod, g)

        P = U[n % 2 :: 2]
        Q = V[0 :: 2]
        
        n //= 2
    
    return (P[0] * pow(Q[0], mod - 2, mod)) % mod

def solve(n, k):
    if k == 0: return 1
    c = [2] + [0] * (k-1) + [-1]
    a = [0] + [pow(2, i, mod) for i in range(1, k+1)] + [(pow(2, k, mod) - 2) %]
    return bostan_mori(c, a, n)

n = int(sys.stdin.readline())
s = sys.stdin.readline().strip()
A = [len(t) for t in s.split('x') if len(t) > 0]

record = [1] * (n+1)
for i in range(1, n+1):
    for a in A:
        record[i] *= solve(a, i)
        record[i] %= mod

for k in range(1, n+1):
    print((record[k] - record[k-1]) % mod)