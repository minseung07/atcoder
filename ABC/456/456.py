import sys

A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))
C = list(map(int, sys.stdin.readline().split()))

p1 = A.count(4)
p2 = A.count(5)
p3 = A.count(6)
q1 = B.count(4)
q2 = B.count(5)
q3 = B.count(6)
r1 = C.count(4)
r2 = C.count(5)
r3 = C.count(6)

res = p1 * q2 * r3 + p1 * q3 * r2 + p2 * q1 * r3 + p2 * q3 * r1 + p3 * q1 * r2 + p3 * q2 * r1
print(res / 216)