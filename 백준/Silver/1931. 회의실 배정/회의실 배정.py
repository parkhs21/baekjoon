N = int(input())
I = [list(map(int, input().split())) for _ in range(N)]
I.sort(key=(lambda x: (x[1],x[0])))

cur = 0
answer = 0
for i in range(N):
    if cur<=I[i][0]:
        cur = I[i][1]
        answer += 1

print(answer)