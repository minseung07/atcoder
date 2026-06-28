import sys

n = int(sys.stdin.readline())
A, B = [0] * n, [0] * n
for i in range(n):
    A[i], B[i] = map(int, sys.stdin.readline().split())
m = int(sys.stdin.readline())
S = [sys.stdin.readline().strip() for _ in range(m)]

check = [[[False] * 26 for _ in range(11)] for __ in range(11)]
for s in S:
    for i in range(len(s)):
        check[len(s)][i][ord(s[i])-97] = True

for s in S:
    flag = False
    if len(s) == n:
        for i in range(n):
            if not check[A[i]][B[i]-1][ord(s[i])-97]:
                flag = True
    else: flag = True
    
    if flag: print("No")
    else: print("Yes")