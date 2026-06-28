import sys, math

n = int(sys.stdin.readline())
p, q= map(int, sys.stdin.readline().split())
for i in range(1, n):
    cp, cq = map(int, sys.stdin.readline().split())
    numer = math.lcm(p * cq, cp * q)
    denom = q * cq
    g = math.gcd(numer, denom)
    p = numer // g
    q = denom // g
print(p, q)