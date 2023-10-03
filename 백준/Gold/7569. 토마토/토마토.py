from collections import deque

N,M,H = map(int, input().split())
graph = [[list(map(int, input().split())) for _ in range(M)] for _ in range(H)]

dx = [1,0,-1,0,0,0]
dy = [0,1,0,-1,0,0]
dz = [0,0,0,0,1,-1]
queue = deque()

for i in range(H):
    for j in range(M):
        for k in range(N):
            if graph[i][j][k]==1:
                queue.append((i,j,k))
            elif graph[i][j][k]==-1:
                graph[i][j][k] = 0
            else:
                graph[i][j][k] = -1

while queue:
    x,y,z = queue.popleft()

    for i in range(6):
        nx = x+dx[i]
        ny = y+dy[i]
        nz = z+dz[i]

        if 0<=nx<H and 0<=ny<M and 0<=nz<N and graph[nx][ny][nz]==-1:
            graph[nx][ny][nz] = graph[x][y][z]+1
            queue.append((nx,ny,nz))

graph_2d = sum(graph, [])
graph_1d = sum(graph_2d, [])
if min(graph_1d) == -1: print(-1)
else: print(max(graph_1d)-1)