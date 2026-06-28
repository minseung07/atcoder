import sys
import heapq

q = int(sys.stdin.readline())
trees = []
cnt = 0
for _ in range(q):
    c, h = map(int, sys.stdin.readline().split())
    if c == 1:
        heapq.heappush(trees, h)
        cnt += 1
    else:
        while trees and trees[0] <= h:
            heapq.heappop(trees)
            cnt -= 1
    print(cnt)