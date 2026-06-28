import sys, heapq

def dijkstra(graph, inter, start):
    distances = [float('inf')] * (n+1)
    distances[start] = 0
    queue = []
    heapq.heappush(queue, [distances[start], start])
    
    while queue:
        current_distance, current_destination = heapq.heappop(queue)
        if distances[current_destination] < current_distance:
            continue
        for new_destination in graph[current_destination]:
            distance = current_distance + 1
            if inter[new_destination]: distance += 1
            if distance < distances[new_destination]:
                distances[new_destination] = distance
                heapq.heappush(queue, [distance, new_destination])
    return distances

n, m, k = map(int, sys.stdin.readline().split())
road = [[] for _ in range(n+1)]
for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    road[u].append(v)
    road[v].append(u)

inter = [0] * (n+1)
for i in range(1, n+1):
    if len(road[i]) >= k:
        inter[i] = 1

distance = dijkstra(road, inter, 1)[n]
if distance == float('inf'):
    print(-1)
else:
    print(distance - inter[n])
