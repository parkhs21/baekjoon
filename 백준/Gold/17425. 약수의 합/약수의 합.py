MAX = 1000001
f = [0] * MAX
dp = [0] * MAX

for i in range(1, MAX):
    for j in range(i, MAX, i):
        f[j] += i
    dp[i] = dp[i-1] + f[i]

T = int(input())
results = [dp[int(input())] for _ in range(T)]
for i in range(T):
    print(results[i])