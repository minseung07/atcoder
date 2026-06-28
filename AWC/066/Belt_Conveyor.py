import sys

n, q = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))
for _ in range(q):
    b = int(sys.stdin.readline())
    b -= 1
    if b+1 < n:
        A[b+1] += A[b]
        A[b] = 0
    else:
        A[b] = 0
print(*A)