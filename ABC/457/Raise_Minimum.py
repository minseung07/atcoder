import sys

def solve(mid):
    cnt = 0
    for i in range(n):
        if mid > A[i]:
            cnt += (mid - A[i] + i) // (i+1)
    return cnt

n, k = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))

low = min(A)
high = 10**36
ans = 0
while low <= high:
    mid = (low + high) // 2
    x = solve(mid)
    if x > k:
        high = mid - 1
    else:
        low = mid + 1
        ans = mid

print(ans)