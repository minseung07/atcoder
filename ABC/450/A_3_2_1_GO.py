import sys

n = int(sys.stdin.readline())
for i in range(n, 0, -1):
    if i < n: print(",", end="")
    print(str(i), end="")
