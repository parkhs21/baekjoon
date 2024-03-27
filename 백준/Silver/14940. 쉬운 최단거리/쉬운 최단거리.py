from collections import deque

N,M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
depth = [[-1]*M for _ in range(N)]
dx = [1,0,-1,0]
dy = [0,1,0,-1]

def bfs(a,b):
    q = deque([(a,b)])
    depth[a][b] = 0
    while q:
        x,y = q.popleft()
        cur = depth[x][y]
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<N and 0<=ny<M and depth[nx][ny]<0:
                if graph[nx][ny] == 0:
                    depth[nx][ny] = 0
                else:
                    depth[nx][ny] = cur+1
                    q.append((nx,ny))

for i in range(N):
    if 2 in graph[i]:
        bfs(i, graph[i].index(2))
        break
    
for i in range(N):
    for j in range(M):
        print(depth[i][j] if graph[i][j] else 0, end=' ')
    print()