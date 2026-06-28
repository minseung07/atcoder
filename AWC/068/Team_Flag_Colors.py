import sys

def find_parent(parent, x):
    root = x
    while parent[root] != root:
        root = parent[root]
    curr = x
    while parent[curr] != root:
        parent[curr], curr = root, parent[curr]
    return root

def union_parents(parent, a, b, c):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    color[a] = c
    color[b] = c
    if a < b:
        parent[b] = a
    else: parent[a] = b

n, m = map(int, sys.stdin.readline().split())
cnt = 0
parent = [i for i in range(n+1)]
color = [0] * (n+1)
for _ in range(m):
    u, v, c = map(int, sys.stdin.readline().split())
    union_parents(parent, u, v, c)

find_colors = set()
for i in range(1, n+1):
    root = find_parent(parent, i)
    if color[root] != 0:
        find_colors.add(color[root])

print(len(find_colors))

