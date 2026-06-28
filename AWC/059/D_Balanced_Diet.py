import sys

n = int(sys.stdin.readline())
s = sys.stdin.readline().strip()

A = [0] * n
for i in range(n):
    char = s[i]
    if i > 0: A[i] = A[i-1]
    if char == "V":
        A[i] += 1
    elif char == "F":
        A[i] -= 1

check = {}
for i in range(n):
    if A[i] in check:
        check[A[i]] += 1
    else: check[A[i]] = 1

res = 0
for i, c in check.items():
    if i == 0: res += c * (c + 1) // 2
    else: res += c * (c - 1) // 2
print(res)
