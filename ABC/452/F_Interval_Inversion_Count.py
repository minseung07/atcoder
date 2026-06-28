import sys

n, k = map(int, sys.stdin.readline().split())
P = list(map(int, sys.stdin.readline().split()))

def update(n, tree, i, delta):
    while i <= n:
        tree[i] += delta
        i += i & (-i)

def query(n, tree, i):
    res = 0
    while i > 0:
        res += tree[i]
        i -= i & (-i)
    return res

def count(n, k):
    if k < 0: return 0
    res = 0
    cur_inv = 0
    r = 0
    tree = [0] * (n+1)
    for l in range(n):
        while r < n:
            add_inv = (r - l) - query(n, tree, P[r])
            if cur_inv + add_inv <= k:
                cur_inv += add_inv
                update(n, tree, P[r], 1)
                r += 1
            else: break
        res += r - l
        cur_inv -= query(n, tree, P[l]-1)
        update(n, tree, P[l], -1)
    return res

print(count(n, k) - count(n, k-1))
