import heapq

INF = int(1e9)
N,M = map(int, input().split())
graph = [[] * (N+1) for _ in range(N+1)]
without_graph = [[] * (N+1) for _ in range(N+1)]

for _ in range(M):
  a,b,c = map(int, input().split())
  graph[a].append((b,c))

X,Y,Z = map(int, input().split())

for i in range(len(graph)):
  if i==Y: continue
  for v,w in graph[i]:
    if v==Y: continue
    without_graph[i].append((v,w))

def dijkstra(start, graph):
  distance = [INF] * (N+1)
  q = []
  heapq.heappush(q, (0,start))
  distance[start] = 0

  while q:
    dist, now = heapq.heappop(q)
    if distance[now] < dist:
      continue
    for i in graph[now]:
      cost = dist + i[1]
      if cost < distance[i[0]]:
        distance[i[0]] = cost
        heapq.heappush(q, (cost, i[0]))

  return distance

start_X = dijkstra(X, graph)
start_Y = dijkstra(Y, graph)
without_Y = dijkstra(X, without_graph)

result_1 = -1 if start_X[Y]==INF or start_Y[Z]==INF else start_X[Y]+start_Y[Z]
result_2 = -1 if without_Y[Z]==INF else without_Y[Z]
print(result_1, result_2)