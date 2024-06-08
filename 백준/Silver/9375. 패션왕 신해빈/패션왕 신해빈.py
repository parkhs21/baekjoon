T = int(input())

for _ in range(T):
    clothes = {}

    n = int(input())
    for _ in range(n):
        name, catg = input().split()
        if catg in clothes:
            clothes[catg].append(name)
        else:
            clothes[catg] = [name]
    
    count = 1
    for catg in clothes:
        count *= len(clothes[catg])+1
    print(count-1)