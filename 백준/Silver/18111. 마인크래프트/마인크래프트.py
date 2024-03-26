N,M,B = map(int, input().split())
ground = []
for _ in range(N):
    ground.extend(map(int, input().split()))

time = 100000000
high = 0

for h in range(min(ground), max(ground)+1):
    cur_time = 0
    cur_B = B
    
    for g in ground:
        if g>h:
            cur_time += (g-h)*2
            cur_B += g-h
        else:
            cur_time += h-g
            cur_B -= h-g
            
    if cur_B>=0 and time>=cur_time:
        time = cur_time
        high = h
        
print(time, high)