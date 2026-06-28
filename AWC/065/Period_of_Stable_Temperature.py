import sys
from collections import deque

n, k, d = map(int, sys.stdin.readline().split())
H = list(map(int, sys.stdin.readline().split()))

mx = deque()
mn = deque()

res = 0
left = 0
for right in range(n):
    while mx and H[mx[-1]] <= H[right]:
        mx.pop()
    while mn and H[mn[-1]] >= H[right]:
        mn.pop()
    mx.append(right)
    mn.append(right)

    while H[mx[0]] - H[mn[0]] > d:
        left += 1
        if mx[0] < left: mx.popleft()
        if mn[0] < left: mn.popleft()

    cur = right - left + 1
    res = max(res, cur)

if res >= k:
    print(res)
else: print(-1)


