N = int(input())
nums = list(map(int, input().split()))
 
dp = [0]*(N+1)
for i in range(N-1):
    dp[i+1] = dp[i]+nums[i]
 
result = 0
for i in range(N-1, 0, -1):
    result += nums[i]*dp[i]
 
print(result)