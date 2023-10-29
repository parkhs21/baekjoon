N,P = map(int,input().split())
W,L,G = map(int,input().split())
player = {}

for _ in range(P):
    name, result = input().split()
    if result == 'W':
        player[name] = result

score = 0
flag = False
for _ in range(N):
    name = input()
    score += W if name in player else -L
    if score < 0: score = 0
    elif score >= G: flag = True

if flag: print('I AM NOT IRONMAN!!')
else: print('I AM IRONMAN!!')