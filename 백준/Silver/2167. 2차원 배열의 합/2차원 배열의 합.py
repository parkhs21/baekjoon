N,M = map(int, input().split())
nums = [list(map(int, input().split())) for _ in range(N)]

dp = [[0]*(M+1) for _ in range(N+1)]
for i in range(N):
    for j in range(M):
        dp[i+1][j+1] = dp[i][j+1] + dp[i+1][j] - dp[i][j] + nums[i][j]

K = int(input())
for _ in range(K):
    i,j,x,y = map(int, input().split())
    print(dp[x][y] - dp[x][j-1] - dp[i-1][y] + dp[i-1][j-1])