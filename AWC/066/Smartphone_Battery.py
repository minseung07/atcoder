import sys, bisect

n, l, k, y = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))
A.sort()

idx = bisect.bisect_left(A, l+1)
if idx == n:
    print(0)
else:
    cnt = min(n - idx, k)
    idx += cnt
    for i in range(idx, n):
        if A[i] - y > l:
            cnt += 1
    print(cnt)


