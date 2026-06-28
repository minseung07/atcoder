import sys

n, l, r = map(int, sys.stdin.readline().split())
cnt = 0
for _ in range(n):
    t = int(sys.stdin.readline())
    if l <= t <= r: cnt += 1
print(cnt)