import sys

n, m, k = map(int, sys.stdin.readline().split())
H = list(map(int, sys.stdin.readline().split()))

for i in range(n):
    if H[i] < k:
        H[i] = 0

mx = sum(H[:m])
cur = mx
for i in range(m, n):
    cur = cur + H[i] - H[i-m]
    mx = max(cur, mx)
print(mx)