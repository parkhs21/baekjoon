from collections import deque

N,M = map(int, input().split())
graph = [list(map(int, input())) for _ in range(N)]

dx = [1,0,-1,0]
dy = [0,1,0,-1]
queue = deque()
queue.append((0,0))
graph[0][0] = 2

while queue:
    x,y = queue.popleft()

    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]

        if 0<=nx<N and 0<=ny<M and graph[nx][ny]==1:
            graph[nx][ny] = graph[x][y]+1
            queue.append((nx,ny))

print(graph[N-1][M-1]-1)