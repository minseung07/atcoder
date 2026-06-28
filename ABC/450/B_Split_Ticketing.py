import sys

n = int(sys.stdin.readline())
C = [None] * (n-1)
for i in range(n-1):
    C[i] = [0] * (i+1) + list(map(int, sys.stdin.readline().split()))

for a in range(n):
    for b in range(a+1, n):
        for c in range(b+1, n):
            if C[a][b] + C[b][c] < C[a][c]:
                print("Yes")
                sys.exit()
print("No")