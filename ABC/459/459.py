import sys

n = int(sys.stdin.readline())
S = list(sys.stdin.readline().strip().split())

c = ''
for s in S:
    x = ord(s[0]) - 97
    if 0 <= x <= 2: c += '2'
    if 3 <= x <= 5: c += '3'
    if 6 <= x <= 8: c += '4'
    if 9 <= x <= 11: c += '5'
    if 12 <= x <= 14: c += '6'
    if 15 <= x <= 18: c += '7'
    if 19 <= x <= 21: c += '8'
    if 22 <= x <= 25: c += '9'
print(c)