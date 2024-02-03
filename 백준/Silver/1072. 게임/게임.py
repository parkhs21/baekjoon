X,Y = map(int, input().split())

check = lambda x,y: int((100*y)/x)
Z = check(X,Y)

if Z>=99:
    print(-1)
else:
    left,right = 0,X
    while left<=right:
        mid = (left+right) // 2

        if check(X+mid, Y+mid) > Z:
            right = mid - 1
        else:
            left = mid + 1

    print(right+1)