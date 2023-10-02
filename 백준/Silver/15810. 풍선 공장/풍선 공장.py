N,M = map(int, input().split())
A = list(map(int, input().split()))

left,right = 1,max(A)*M
while left <= right:
    mid = (left+right)//2
    temp = sum(map(lambda x: mid//x, A))

    if temp<M: left = mid+1
    else: right = mid-1

print(left)