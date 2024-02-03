X,N = map(int, input().split())
nums = [0] + list(map(int, input().split()))

count = 0
maximum = 0

temp = sum(nums[:N])
for i in range(N, X+1):
    temp = temp + nums[i] - nums[i-N]
    if temp > maximum:
        maximum = temp
        count = 1
    elif temp == maximum:
        count += 1

if not maximum:
    print("SAD")
else:
    print(maximum)
    print(count)