import sys

check = [set() for _ in range(10)]
for i in range(30):
    x = str(2**i)
    check[len(x)].add(x)

for i in range(2, 10):
    for j in range(1, i):
        for n1 in check[j]:
            for n2 in check[i-j]:
                check[i].add(n1+n2)

n = int(sys.stdin.readline())
i = 1
while n > len(check[i]):
    n -= len(check[i])
    i += 1
check[i] = list(map(int, check[i]))
check[i].sort()
print(check[i][n-1])