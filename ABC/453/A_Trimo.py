import sys

n = int(sys.stdin.readline())
s = sys.stdin.readline().strip()
idx = 0
for char in s:
    if char == "o":
        idx += 1
    else: break
print(s[idx:])