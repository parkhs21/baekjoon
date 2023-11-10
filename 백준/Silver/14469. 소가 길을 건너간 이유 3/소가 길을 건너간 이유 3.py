N = int(input())
cows = [list(map(int, input().split())) for _ in range(N)]
cows.sort()

result = 0

for a,t in cows:
    if result >= a:
        result += t
    else:
        result = a+t

print(result)