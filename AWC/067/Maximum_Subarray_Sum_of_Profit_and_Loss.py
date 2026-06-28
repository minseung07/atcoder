import sys

n = int(sys.stdin.readline())
B = list(map(int, sys.stdin.readline().split()))
res = [-float('inf')] * n
cur = [-float('inf')] * n

res[0] = B[0]
cur[0] = B[0]
print(res[0])
for i in range(1, n):
    if cur[i-1] + B[i] > B[i]:
        cur[i] = cur[i-1] + B[i]
    else: cur[i] = B[i]
    res[i] = max(res[i-1], cur[i])
    print(res[i])