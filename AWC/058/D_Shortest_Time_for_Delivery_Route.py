import sys, heapq

def dijkstra(graph, start):
    distances = [float('inf')] * (n+1)
    distances[start] = 0
    queue = []
    heapq.heappush(queue, [distances[start], start])

    while queue:
        cur_dist, cur_dest = heapq.heappop(queue)
        if distances[cur_dest] < cur_dist:
            continue
        for new_dest, weight in graph[cur_dest]:
            dist = cur_dist + weight
            if dist < distances[new_dest]:
                distances[new_dest] = dist
                heapq.heappush(queue, [dist, new_dest])
    return distances

n, m, k = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    u, v, c = map(int, sys.stdin.readline().split())
    graph[u].append((v, c))
    graph[v].append((u, c))

dist_k = dijkstra(graph, k)
res = dist_k[1] + dist_k[n]
if res == float('inf'):
    print(-1)
else: print(res)