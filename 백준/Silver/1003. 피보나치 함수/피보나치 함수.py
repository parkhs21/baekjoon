T = int(input())
dp = [1] + [0]*45
cur = 2

for _ in range(T):
    N = int(input())
    if cur<N+2:
        for i in range(cur,N+2):
            dp[i] = dp[i-1]+dp[i-2]
        cur = N+1
    print(dp[N], dp[N+1])