from collections import deque

N,M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

dx = [1,0,-1,0]
dy = [0,1,0,-1]

T = 0
while True:
    q = deque()
    check = [[0]*M for _ in range(N)]

    q.append((0,0))
    while q:
        x,y = q.popleft()
        
        if graph[y][x]==-1: continue
        graph[y][x] = -1
            
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            
            if 0<=nx<M and 0<=ny<N:
                if graph[ny][nx]==0:
                    q.append((nx,ny))
                elif graph[ny][nx]==1: 
                    check[ny][nx] += 1

    for i in range(N):
        for j in range(M):
            if graph[i][j]==-1 or check[i][j]>=2:
                graph[i][j] = 0

    if sum(sum(c) for c in check) == 0:
        break
    T += 1

print(T)
        