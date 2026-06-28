import sys

n, q = map(int, sys.stdin.readline().split())
C = list(map(int, sys.stdin.readline().split()))
for _ in range(q):
    T = list(map(int, sys.stdin.readline().split()))
    command = T[0]
    