from collections import deque

N = int(input())
graph = [list(input()) for _ in range(N)]

dx = [1,0,-1,0]
dy = [0,1,0,-1]

def bfs(x,y):
    q = deque()
    q.append((x,y))
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<N and 0<=ny<N and graph[ny][nx]==graph[y][x] and visited[ny][nx]==1:
                q.append((nx,ny))
                visited[ny][nx] = 0


visited = [[1]*N for _ in range(N)]
people_cnt = 0
for i in range(N):
    for j in range(N):
        if visited[i][j]:
            bfs(j,i)
            people_cnt += 1

for i in range(N):
    for j in range(N):
        if graph[i][j]=='R':
            graph[i][j] = 'G'

visited = [[1]*N for _ in range(N)]
cow_cnt = 0
for i in range(N):
    for j in range(N):
        if visited[i][j]:
            bfs(j,i)
            cow_cnt += 1

print(people_cnt, cow_cnt)