from collections import deque

N,M = map(int, input().split())
graph = [list(map(int, input())) for _ in range(N)]
visited = [[[0,0] for _ in range(M)] for _ in range(N)]
dx = [1,0,-1,0]
dy = [0,1,0,-1]

q = deque()
q.append((0,0,0))
visited[0][0] = [1,1]

def bfs():
    while q:
        x,y,b = q.popleft()
        
        if x==M-1 and y==N-1:
            return visited[y][x][b]
            
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if not (0<=nx<M and 0<=ny<N):
                continue
            elif graph[ny][nx] and not b:
                visited[ny][nx][1] = visited[y][x][0]+1
                q.append((nx,ny,b+1))
            elif not graph[ny][nx] and not visited[ny][nx][b]:
                visited[ny][nx][b] = visited[y][x][b]+1
                q.append((nx,ny,b))
    
    return -1
                        

print(bfs())