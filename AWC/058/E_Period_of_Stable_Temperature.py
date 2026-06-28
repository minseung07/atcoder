import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))

max_dq = deque()
min_dq = deque()

ans = 0
l = 0
for r in range(n):
    while max_dq and A[max_dq[-1]] <= A[r]:
        max_dq.pop()
    max_dq.append(r)
    while min_dq and A[min_dq[-1]] >= A[r]:
        min_dq.pop()
    min_dq.append(r)

    while A[max_dq[0]] - A[min_dq[0]] > k:
        l += 1
        if max_dq[0] < l: max_dq.popleft()
        if min_dq[0] < l: min_dq.popleft()
    ans = max(ans, r-l+1)
print(ans)