from collections import deque

N = int(input())
graph = [list(map(int, input())) for _ in range(N)]
dx = [1,0,-1,0]
dy = [0,1,0,-1]

answer = []
for i in range(N*N):
    if graph[i//N][i%N]:
        q = deque([(i//N, i%N)])
        house = 0
        while q:
            x,y = q.popleft()
            if graph[x][y]:
                house += 1
                graph[x][y] = 0
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if 0<=nx<N and 0<=ny<N:
                        q.append((nx,ny))
        answer.append(house)
            
answer.sort()
print(len(answer))
for a in answer: print(a)