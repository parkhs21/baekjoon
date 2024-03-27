N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]
paper_sum = [[0]*(N+1) for _ in range(N+1)]
white = 0
blue = 0

for i in range(1,N+1):
    for j in range(1,N+1):
        paper_sum[i][j] = paper_sum[i-1][j] + paper_sum[i][j-1] - paper_sum[i-1][j-1] + paper[i-1][j-1]

def find(r,c,p):
    global white, blue
    if p==1:
        if paper[c][r]: blue += 1
        else: white += 1
    else:
        temp = paper_sum[c+p][r+p] - paper_sum[c][r+p] - paper_sum[c+p][r] + paper_sum[c][r]
        if temp == 0:
            white += 1
        elif temp == p**2:
            blue += 1
        else:
            new_p = p//2
            find(r, c, new_p)
            find(r+new_p, c, new_p)
            find(r, c+new_p, new_p)
            find(r+new_p, c+new_p, new_p)
            
find(0,0,N)

print(white)
print(blue)