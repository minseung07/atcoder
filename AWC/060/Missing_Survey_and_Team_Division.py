import sys

n = int(sys.stdin.readline())
r = 0
w = 0
k = 0
for i in range(n):
    s = sys.stdin.readline().strip()
    if s == "R": r += 1
    if s == "W": w += 1
    if s == "?": k += 1

ans = abs(r - w)
if ans >= k:
    ans -= k
    print(ans)
else:
    k -= ans
    print(k % 2)