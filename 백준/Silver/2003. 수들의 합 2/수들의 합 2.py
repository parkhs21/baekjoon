N,M = map(int, input().split())
nums = list(map(int, input().split()))

left,right = 0,1
result = 0

while right <= N and left <= right:
    temp = sum(nums[left:right])

    if temp == M:
        result += 1
        right += 1
    elif temp < M:
        right += 1
    else:
        left += 1

print(result)