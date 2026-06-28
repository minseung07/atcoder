import sys, random

n = int(sys.stdin.readline())
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
hash = [random.getrandbits(64) for _ in range(25)]

A = [0] * n
for i in range(n):
    p, q = map(int, sys.stdin.readline().split())
    for j in range(25):
        cnt = 0
        while p % primes[j] == 0:
            p //= primes[j]
            cnt += 1
        while q % primes[j] == 0:
            q //= primes[j]
            cnt -= 1
        A[i] += hash[j] * cnt

n1 = n // 2
n2 = n - n1

left = {}
right = {}
res = n + 1

for i in range(1, 1 << n1):
    s_hash = 0
    cnt = 0
    for j in range(n1):
        if i & (1 << j):
            s_hash += A[j]
            cnt += 1
    if s_hash == 0 and cnt >= 2:
        res = min(res, cnt)
    if not s_hash in left or left[s_hash] > cnt:
        left[s_hash] = cnt
    
for i in range(1, 1 << n2):
    s_hash = 0
    cnt = 0
    for j in range(n2):
        if i & (1 << j):
            s_hash += A[n1 + j]
            cnt += 1
    if s_hash == 0 and cnt >= 2:
        res = min(res, cnt)
    if not s_hash in right or right[s_hash] > cnt:
        right[s_hash] = cnt

for s_hash, cnt1 in left.items():
    if -s_hash in right:
        cnt2 = right[-s_hash]
        cnt = cnt1 + cnt2
        if cnt >= 2 and cnt < res:
            res = cnt
if res == n+1:
    print(-1)
else: print(res)