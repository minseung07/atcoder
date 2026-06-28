import sys

n, x = map(int, sys.stdin.readline().split())
A =  list(map(int, sys.stdin.readline().split()))

res = 0
for a in A:
    if a > x:
        res += a - x
print(res)