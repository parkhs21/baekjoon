T = int(input())
dp = [0,1,2,4] + [0]*8
cur = 3

for _ in range(T):
    N = int(input())
    if cur<N:
        for i in range(cur+1, N+1):
            dp[i] = dp[i-1]+dp[i-2]+dp[i-3]
        cur = N
    print(dp[N])