import sys

n = int(sys.stdin.readline())
L = list(map(int, sys.stdin.readline().split()))

cur = [[0.5, 0]]
for l in L:
    next = []
    for c, res in cur:
        if c * (c + l) < 0:
            next.append([c+l, res+1])
        else: next.append([c+l, res])
        if c * (c - l) < 0:
            next.append([c-l, res+1])
        else: next.append([c-l, res])
    cur = next

mx = 0
for c, res in cur:
    mx = max(mx, res)
print(mx)