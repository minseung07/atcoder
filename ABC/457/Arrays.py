import sys

n = int(sys.stdin.readline())
A = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
x, y = map(int, sys.stdin.readline().split())
print(A[x-1][y])