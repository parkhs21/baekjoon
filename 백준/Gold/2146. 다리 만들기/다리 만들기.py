from collections import deque

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
dx = [1,0,-1,0]
dy = [0,1,0,-1]

visited = [[0]*N for _ in range(N)]
def check_land(a,b,land_no):
    q = deque()
    q.append((a,b))
    while q:
        x,y = q.popleft()
        graph[y][x] = land_no
        for d in range(4):
            nx,ny = x+dx[d],y+dy[d]
            if 0<=nx<N and 0<=ny<N and not visited[ny][nx] and graph[ny][nx]:
                q.append((nx,ny))
                visited[ny][nx] = 1

land_flag = 2
for i in range(N):
    for j in range(N):
        if not visited[i][j] and graph[i][j]:
            check_land(j,i,land_flag)
            land_flag += 1

answer = N*N

def find_bridge(q,flag):
    visited = [[0]*N for _  in range(N)]
    while q:
        x,y,c = q.popleft()
        for d in range(4):
            nx,ny = x+dx[d],y+dy[d]
            if 0<=nx<N and 0<=ny<N and not visited[ny][nx]:
                if graph[ny][nx]==flag: continue
                elif graph[ny][nx]: return c+1
                q.append((nx,ny,c+1))
                visited[ny][nx] = 1
    return N*N

for i in range(N):
    for j in range(N):
        if graph[i][j]:
            q = []
            for d in range(4):
                nx,ny = j+dx[d],i+dy[d]
                if 0<=nx<N and 0<=ny<N:
                    q.append((nx,ny,0))
            if q:
                answer = min(find_bridge(deque(q), graph[i][j]), answer)

print(answer)