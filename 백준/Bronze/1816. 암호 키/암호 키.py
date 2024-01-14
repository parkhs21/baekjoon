N = int(input())

for _ in range(N):
    num = int(input())

    for i in range(2,1000000):
        if num%i == 0:
            break
    
    if i == 999999: print('YES')
    else: print("NO")