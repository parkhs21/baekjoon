N = int(input())
nums = list(map(int, input().split()))
dp = [0] * (N)
dp[0] = nums[0]

result = dp[0]
for i in range(1, N):
    dp[i] = nums[i] + max(0, dp[i-1])
    result = max(result, dp[i])

print(result)