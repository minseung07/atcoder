import sys

sys.setrecursionlimit(10**6)
def count_alphabet(p, c):
    if p < fibo[3]:
        if p < fibo[2]:
            return y[:p].count(c)
        return count[2][ord(c)-97] + x[:p-fibo[2]].count(c)
    for i in range(99, 0, -1):
        if p >= fibo[i]:
            return count[i][ord(c)-97] + count_alphabet(p-fibo[i], c)

x = sys.stdin.readline().strip()
y = sys.stdin.readline().strip()

lx, ly = len(x), len(y)
fibo = [0] * 100
fibo[1], fibo[2] = lx, ly
for i in range(3, 100):
    fibo[i] = fibo[i-1] + fibo[i-2]

count = [[0] * 26 for _ in range(100)]
for i in range(26):
    count[1][i] = x.count(chr(97+i))
    count[2][i] = y.count(chr(97+i))
for i in range(3, 100):
    for j in range(26):
        count[i][j] = count[i-1][j] + count[i-2][j]

for _ in range(int(sys.stdin.readline())):
    l, r, c = sys.stdin.readline().strip().split()
    l, r = int(l) - 1, int(r)
    print(count_alphabet(r, c) - count_alphabet(l, c))
