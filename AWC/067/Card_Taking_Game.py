import sys

n, k = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))

xor_sum = 0
for a in A:
    xor_sum ^= (a % (k+1))

if xor_sum == 0:
    print("Aoki")
else: print("Takahashi")