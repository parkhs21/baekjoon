T = int(input())
for _ in range(T):
    N = int(input())
    nums = list(map(int, input().split()))

    maximum = -10000
    temp = 0
    for num in nums:
        temp = max(num, temp+num)
        maximum = max(temp, maximum)

    print(maximum)