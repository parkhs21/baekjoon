from heapq import heappush,heappop

N = int(input())
M = int(input())

graph = [[] for _ in range(N+1)]
distance = [2e9]*(N+1)
info = [[] for _ in range(N+1)]
src = dst = 0

for _ in range(M):
    a,b,c = map(int, input().split())
    graph[a].append((c,b))
src,dst = map(int, input().split())

def dijkstra(start, distance, info):
    q = []
    heappush(q, (0,start))
    distance[start] = 0

    while q:
        cost,now = heappop(q)
        if distance[now] < cost:
            continue

        for now_cost,now_dst in graph[now]:
            temp_cost = cost+now_cost
            if temp_cost < distance[now_dst]:
                distance[now_dst] = temp_cost
                info[now_dst] = info[now] + [now]
                heappush(q, (temp_cost, now_dst))

    return distance, info

dijkstra(src, distance, info)

print(distance[dst])
print(len(info[dst])+1)
print(*(info[dst]+[dst]))
