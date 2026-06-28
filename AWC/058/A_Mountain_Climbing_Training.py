import sys

n, p, t, c = map(int, sys.stdin.readline().split())
if n == 1:
    if p >= t: print(0)
    else: print(-1)
    sys.exit()
S = list(map(int, sys.stdin.readline().split()))
if p >= t: print(0)
else:
    if max(S) >= p:
        print(c)
    else: print(-1)