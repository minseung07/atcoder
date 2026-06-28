import sys

class segment:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (n+1)
    def update(self, i, val):
        delta = val - self.tree[i]
        while i <= self.n:
            self.tree[i] += delta
            i += (i & -i)
    def query(self, i):
        res = 0
        while i > 0:
            res += self.tree[i]
            i -= (i & -i)
        return res
    def sm(self, l, r):
        return self.query(r) - self.query(l)

n, m, q = map(int, sys.stdin.readline().split())
trees = [segment(m) for _ in range(n)]
for _ in range(q):
    command = list(map(int, sys.stdin.readline().split()))
    c = command[0]
    if c == 1:
        x, y = command[1:]
        trees[x-1].tree[:] = trees[y-1].tree
    if c == 2:
        x, y, z = command[1:]
        trees[x-1].update(y, z)
    if c == 3:
        x, l, r = command[1:]
        print(trees[x-1].sm(l, r))
