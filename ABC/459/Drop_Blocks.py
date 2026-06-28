import sys

n, q = map(int, sys.stdin.readline().split())

tree = [0] * (2 * n)
minu = 0

size = 3 * 10**5 + 1
count_tree = [0] * (2 * size)
count_tree[size] = n
for i in range(size - 1, 0, -1):
    count_tree[i] = count_tree[i>>1] + count_tree[i>>1|1]

def update(n, tree, i, val):
    i += n
    tree[i] += val
    while i > 1:
        i //= 2
        tree[i] = min(tree[i*2], tree[i*2+1])

def query(n, tree, l, r):
    l, r = l + n, r + n
    res = 0
    while l < r:
        if l & 1:
            res += tree[l]
            l += 1
        if r & 1:
            r -= 1
            res -= tree[r]
        l //= 2
        r //= 2
    return res

for _ in range(q):
    c, a = map(int, sys.stdin.readline().split())
    if c == 1:
        update(size, count_tree, tree[i], -1)
        update(size, count_tree, tree[i]+1, 1)
        update(n, tree, a-1, 1)
        if tree[1] >= minu + 1:
            minu += 1
    else:
        print(n - query(size, count_tree, 0, a + minu))

print(count_tree)