from collections import deque

N,M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(M)]

dx = [1,0,-1,0]
dy = [0,1,0,-1]
queue = deque()

for i in range(M):
    for j in range(N):
        if graph[i][j]==1:
            queue.append((i,j))
        elif graph[i][j]==-1:
            graph[i][j] = 0
        else:
            graph[i][j] = -1

while queue:
    x,y = queue.popleft()

    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]

        if 0<=nx<M and 0<=ny<N and graph[nx][ny]==-1:
            graph[nx][ny] = graph[x][y]+1
            queue.append((nx,ny))

graph_1d = sum(graph, [])
if min(graph_1d) == -1: print(-1)
else: print(max(graph_1d)-1)