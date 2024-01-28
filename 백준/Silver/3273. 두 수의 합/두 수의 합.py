n = int(input())
nums = list(map(int, input().split()))
x = int(input())

nums.sort()
result = 0
left, right = 0, n-1

while left < right:
    temp = nums[left] + nums[right]
    if temp == x:
        result += 1
        left += 1
    elif temp < x:
        left += 1
    else:
        right -= 1

print(result)