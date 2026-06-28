import sys

def solve(A, x):
    cnt = 1
    cur = 0
    for i in range(n):
        if cur + A[i] > x:
            cnt += 1
            cur = 0
        cur += A[i]
    return cnt

n, k = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))

low = max(A)
high = sum(A)
ans = 0
while low <= high:
    mid = (low + high) // 2
    cur = solve(A, mid)
    if cur > k:
        low = mid + 1
    else:
        high = mid - 1
        ans = mid
print(ans)