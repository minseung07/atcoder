import sys

n, m, k = map(int, sys.stdin.readline().split())
T = list(map(int, sys.stdin.readline().split()))
S = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

qualified = []
for i in range(n):
    check = True
    for j in range(m):
        if S[i][j] < T[j]: check = False
    if check: qualified.append((sum(S[i]), i))

if len(qualified) <= k:
    for score, idx in qualified:
        print(idx+1)
    sys.exit()

qualified.sort(reverse=True)
mini_score = qualified[k-1][0]
res = []
for score, idx in qualified:
    if score >= mini_score:
        res.append(idx)
    else: break
res.sort()
for idx in res:
    print(idx+1)