N,M = map(int, input().split())

listen = set([input() for _ in range(N)])
see = set([input() for _ in range(M)])

answer = list(listen&see)
answer.sort()

print(len(answer))
for a in answer: print(a)