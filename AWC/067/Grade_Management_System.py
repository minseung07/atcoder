import sys

n, q = map(int, sys.stdin.readline().split())
A = [0] * n
for _ in range(q):
    c, l, r, v = map(int, sys.stdin.readline().split())
    if c == 1:
        l, r = l - 1, r - 1
        A[l] -= v
        A[r] += v
    if c == 2:
        l, r, x = r, v, l
        l, r, x = l - 1, r - 1, x - 1
        cnt = 0
        for i in range(l, r+1):
            if A[i] > A[x]:
                cnt += 1
        print(cnt)
    if c == 3:
        l, r = l - 1, r - 1
        for i in range(l, r+1):
            A[i] += v
