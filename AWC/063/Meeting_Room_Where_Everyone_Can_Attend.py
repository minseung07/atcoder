import sys
import math

n, m = map(int, sys.stdin.readline().split())
P = list(map(int, sys.stdin.readline().split()))

if n == 1:
    if P[0] <= m:
        print("Yes")
    else: print("No")
    sys.exit()

l = math.lcm(P[0], P[1])
for i in range(1, n):
    l = math.lcm(l, P[i])
    if l > m: break
if l <= m:
    print("Yes")
else: print("No")