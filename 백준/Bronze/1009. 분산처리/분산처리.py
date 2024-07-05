for _ in range(int(input())):
    a,b = map(int, input().split())
    a %= 10
    if not a:
        print(10)
    else:
        if b%4: b %= 4
        print(a**b%10)