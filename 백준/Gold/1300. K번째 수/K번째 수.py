N = int(input())
k = int(input())

left,right = 1,N*N

while left<=right:
    mid = (left+right)//2

    temp = sum(map(lambda x: min(mid//x, N), range(1,N+1)))

    if temp >= k: right = mid-1
    else: left = mid+1

print(left)