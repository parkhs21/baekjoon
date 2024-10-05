from heapq import heappop, heappush

def solution(n, s, a, b, fares):
    INF = 1e8
    graph = [[] for _ in range(n+1)]
    for c,d,f in fares:
        graph[c].append([d,f])
        graph[d].append([c,f])
        
    def dijkstra(s):
        distance = [INF]*(n+1)
        distance[s] = 0
        q = [[0,s]]
        while q:
            dist,cur = heappop(q)
            if distance[cur] < dist: continue
            for ncur,ndist in graph[cur]:
                cost = dist+ndist
                if distance[ncur] > cost:
                    distance[ncur] = cost
                    heappush(q, (cost, ncur))
        return distance
    
    sdist = dijkstra(s)
    adist = dijkstra(a)
    bdist = dijkstra(b)
    answer = INF
    for i in range(1,n+1):
        answer = min(answer, sdist[i]+adist[i]+bdist[i])
    
    return answer