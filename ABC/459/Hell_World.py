import sys

n = int(sys.stdin.readline())
n -= 1
s = "HelloWorld"
print(s[:n] + s[n+1:])