N = int(input())
dp = [[0]] + [[0]+list(map(int, input().split()))+[0] for _ in range(N)]

for i in range(2,N+1):
    for j in range(1,i+1):
        dp[i][j] = max(dp[i-1][j-1], dp[i-1][j])+dp[i][j]

print(max(dp[-1]))