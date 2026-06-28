import sys, bisect

n, m = map(int, sys.stdin.readline().split())
L = [[] for _ in range(n+1)]
R = [[] for _ in range(n+1)]
for _ in range(m):
    l, r = map(int, sys.stdin.readline().split())
    L[l].append(r)
    R[r].append(l)
for i in range(n+1):
    L[i].sort()
    R[i].sort()

first_min = [n+1] * (n+1)
second_min = [n+1] * (n+1)
for i in range(n, -1, -1):
    check = []
    if i < n:
        check.append(first_min[i+1])
        check.append(second_min[i+1])
    if len(L[i]) >= 1:
        check.append(L[i][0])
        if len(L[i]) >= 2:
            check.append(L[i][1])
    check.sort()
    if len(check) >= 1:
        first_min[i] = check[0]
        if len(check) >= 2:
            second_min[i] = check[1]

q = int(sys.stdin.readline())
for _ in range(q):
    s, t = map(int, sys.stdin.readline().split())
    i_check = bisect.bisect_left(L[s], t)
    if i_check < len(L[s]) and L[s][i_check] == t:
        if second_min[s] <= t:
            print("Yes")
        else: print("No")
        continue

    if len(L[s]) == 0 or len(R[t]) == 0:
        print("No")
        continue

    i1 = bisect.bisect_left(L[s], t) - 1
    if i1 < 0:
        print("No")
        continue
    i2 = bisect.bisect_left(R[t], s)
    if i2 == len(R[t]):
        print("No")
        continue
    
    lmax = L[s][i1]
    rmin = R[t][i2]
    if rmin <= lmax + 1:
        print("Yes")
    else: print("No")
