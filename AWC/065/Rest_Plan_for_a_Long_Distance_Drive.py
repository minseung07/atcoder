import sys

n, k = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))

time = 0
for i in range(n):
    time += A[i]
    if (i + 1) < n and (i + 1) % k == 0:
        time += 1
print(time)