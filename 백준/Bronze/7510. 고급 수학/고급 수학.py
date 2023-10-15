N = int(input())

for i in range(N):
    nums = list(map(int, input().split()))
    nums.sort()

    print(f"Scenario #{i+1}:")
    if nums[0]**2 + nums[1]**2 == nums[2]**2:
        print("yes")
    else:
        print("no")
    print()
