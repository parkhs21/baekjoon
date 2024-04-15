R,C,T = map(int, input().split())

dx = [0,1,0,-1]
dy = [1,0,-1,0]

graph = []
air = 0
for i in range(R):
    cur = list(map(int, input().split()))
    graph.append(cur)
    if cur[0] == -1: air = i-1

def diffusion():
    for i in range(R):
        for j in range(C):
            if graph[i][j]==-1: room[i][j] = -1
            if graph[i][j]<=0: continue
            
            dir_cnt = 0
            for d in range(4):
                nx = j+dx[d]
                ny = i+dy[d]
                
                if 0<=nx<C and 0<=ny<R and graph[ny][nx]>=0:
                    dir_cnt += 1
                    room[ny][nx] += graph[i][j]//5
                    
            room[i][j] += graph[i][j] - (graph[i][j]//5) * dir_cnt
            
    
def circulation_upper():
    i,j = 0,0
    d = 0
    temp = room[i][j]
    room[i][j] = room[0][1]
    while True:
        nx = j+dx[d]
        ny = i+dy[d]
        
        if nx==0 and ny==0:
            break
        elif not (0<=nx<C and 0<=ny<=air):
            d += 1
            continue
        
        i,j = ny,nx
        temp,room[i][j] = room[i][j],temp
        
    room[air][0] = -1
    room[air][1] = 0
    
def circulation_lower():
    i,j = R-1,C-1
    d = 3
    temp = room[i][j]
    room[i][j] = room[-2][-1]
    while True:
        nx = j+dx[d]
        ny = i+dy[d]
        
        if nx==C-1 and ny==R-1:
            break
        elif not (0<=nx<C and air<ny<R):
            d -= 1
            continue
        
        i,j = ny,nx
        temp,room[i][j] = room[i][j],temp
        
    room[air+1][0] = -1
    room[air+1][1] = 0




for _ in range(T):
    room = [[0]*C for _ in range(R)]
    
    diffusion()
    circulation_upper()
    circulation_lower()
    
    graph = room



dust = sum(sum(r) for r in graph)
print(dust+2)