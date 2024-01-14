N = int(input())
paper = [[0]*101 for _ in range(101)]

for _ in range(N):
    x,y = map(int, input().split())
    for i in range(x, x+10):
        for j in range(y, y+10):
            paper[j][i] = 1

result = 0
for i in range(101):
    result += sum(paper[i])
print(result)