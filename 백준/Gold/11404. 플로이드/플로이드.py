N = int(input())
M = int(input())

graph = [[1e9]*N for _ in range(N)]
for i in range(N): graph[i][i] = 0

for _ in range(M):
    a,b,c = map(int, input().split())
    graph[a-1][b-1] = min(c, graph[a-1][b-1])

for k in range(N):
    for a in range(N):
        for b in range(N):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

for a in range(N):
    for b in range(N):
        cur = graph[a][b]
        print(cur if cur<1e9 else 0, end=' ')
    print()