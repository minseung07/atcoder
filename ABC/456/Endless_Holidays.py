import sys

t = int(sys.stdin.readline())
for _ in range(t):
    n, m = map(int, sys.stdin.readline().split())
    graph = [[i] for i in range(n+1)]
    graph[0] = [i for i in range(1, n+1)]
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        graph[u].append(v)
        graph[v].append(u)
    w = int(sys.stdin.readline())
    s = [''] * (n+1)
    for i in range(1, n+1):
        s[i] = sys.stdin.readline().strip()

    d = 0
    stack = set([0])
    while stack and d < w+1:
        next_stack = set()
        for cur in stack:
            for next in graph[cur]:
                if s[next][d%w] == "o":
                    next_stack.add(next)
        stack = next_stack
        d += 1
    
    if stack:
        print("Yes")
    else: 
        print("No")