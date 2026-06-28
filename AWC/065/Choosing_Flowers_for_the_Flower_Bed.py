import sys

n = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))

# dp1[i]: i번째까지 하고, i번째 화단에 심음
# dp2[i]: i번째까지 하고, i번째 화단에 심지 않음

dp1 = [0] * n
dp2 = [0] * n

if n == 1:
    print(A[0])
elif n == 2:
    print(max(A[0], A[1]))
else:
    dp1[0] = A[0]
    dp1[1] = A[1]
    dp2[1] = A[0]
    for i in range(2, n):
        dp1[i] = max(dp1[i-2], dp2[i-1]) + A[i]
        dp2[i] = max(dp1[i-1], dp2[i-1])
    print(max(dp1[-1], dp2[-1]))