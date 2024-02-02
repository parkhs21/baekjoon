import bisect

N = int(input())
nums = list(map(int, input().split()))
M = int(input())

nums.sort()
left,right = 0,nums[-1]

while left <= right:
    mid = (left+right)//2

    temp = 0
    for i in range(len(nums)):
        if nums[i] < mid:
            temp += nums[i]
        else:
            temp += mid*(N-i)
            break

    if temp <= M: left = mid+1
    else: right = mid-1

print(right)