import sys

n = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))

for i in range(n-1):
    if A[i] > A[i+1]:
        A[i] = A[i] + A[i+1] // 2
        A[i+1] = 0
    elif A[i] < A[i+1]:
        A[i+1] = A[i] // 2 + A[i+1]
        A[i] = 0

cnt = 0
for i in range(n):
    if A[i] > 0: cnt += 1
print(cnt)