N = int(input())
steps = [0] + [int(input()) for _ in range(N)]
dp = [0] * (N+1)

dp[1] = steps[1]
if N > 1:
    dp[2] = steps[1] + steps[2]
    for i in range(3, N+1):
        dp[i] = steps[i] + max(dp[i-3]+steps[i-1], dp[i-2])

print(dp[-1])