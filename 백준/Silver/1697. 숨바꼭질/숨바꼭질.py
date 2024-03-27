from collections import deque

N,X = map(int, input().split())
visited = [0] * 100001

def bfs(cur):
    q = deque([cur])
    while q:
        cur = q.popleft()
        if cur==X:
            return visited[cur]
        for next in (cur-1, cur+1, 2*cur):
            if 0 <= next <= 100000 and not visited[next]:
                visited[next] = visited[cur]+1                
                q.append(next)

print(bfs(N))