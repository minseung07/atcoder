import sys

h, w = map(int, sys.stdin.readline().split())
print("#" * w)
for i in range(h-2):
    print("#" + "." * (w-2) + "#")
print("#" * w)