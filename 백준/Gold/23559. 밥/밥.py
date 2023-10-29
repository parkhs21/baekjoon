N,X = map(int, input().split())

menu = [list(map(int, input().split())) for _ in range(N)]
menu.sort(key=lambda x: x[1]-x[0])


temp = (X-1000*N)//4000

score = 0
for i in range(N):
    if temp and menu[i][0] > menu[i][1]:
        temp -= 1
        score += menu[i][0]
    else:
        score += menu[i][1]

print(score)