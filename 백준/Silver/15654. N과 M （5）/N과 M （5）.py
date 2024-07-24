N,M = map(int, input().split())
data = list(map(int , input().split()))
data.sort()
visited = [False] * N
out = []

def dfs():
    if len(out) == M:
        print(' '.join(map(str, out)))
        return
    
    for i in range(N):
        if not visited[i]:
            out.append(data[i])
            visited[i] = True
            dfs()
            visited[i] = False
            out.pop()

dfs()