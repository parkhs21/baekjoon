K,N = map(int, input().split())
lans = [int(input()) for _ in range(K)]

left,right = 1,max(lans)

while left<=right:
    mid = (left+right)//2
    lines = sum(map(lambda x: x//mid, lans))

    if lines >= N: left = mid+1
    else: right = mid-1

print(right)
