N = int(input())

min_a,min_b = 1e7,1e7
max_a,max_b = -1e7,-1e7
for _ in range(N):
    a,b = map(int, input().split())
    min_a = min(min_a, a)
    min_b = min(min_b, b)
    max_a = max(max_a, a)
    max_b = max(max_b, b)

print((max_a - min_a) * (max_b - min_b))
