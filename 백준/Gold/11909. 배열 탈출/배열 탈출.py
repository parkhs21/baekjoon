N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
dp = [[0]*N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if i==0 and j==0:
            dp[i][j] = 0
        elif i==0:
            dp[i][j] = dp[0][j-1] + max(graph[0][j] - graph[0][j-1] + 1, 0)
        elif j==0:
            dp[i][j] = dp[i-1][0] + max(graph[i][0] - graph[i-1][0] + 1, 0)
        else:
            up = dp[i][j-1] + max(graph[i][j] - graph[i][j-1] + 1, 0)
            left = dp[i-1][j] + max(graph[i][j] - graph[i-1][j] + 1, 0)
            dp[i][j] = min(up, left)

print(dp[N-1][N-1])