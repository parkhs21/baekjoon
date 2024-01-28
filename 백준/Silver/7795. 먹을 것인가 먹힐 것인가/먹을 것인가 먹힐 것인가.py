T = int(input())

for _ in range(T):
    N,M = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    B = sorted(list(map(int, input().split())))

    start = 0
    count = 0
    
    for i in range(N):
        while True:
            if start==M or A[i]<=B[start]:
                count += start
                break
            else:
                start += 1

    print(count)