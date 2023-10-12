N = int(input())
points = [list(map(int, input().split())) for _ in range(N)]
points.append(points[0])
answer = 0

for i in range(N):
    answer -= points[i][1]*points[i+1][0]
    answer += points[i][0]*points[i+1][1]

print(round(abs(answer)/2,1))