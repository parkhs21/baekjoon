N = int(input())
lifeguard = []
times = [0]*1001

for _ in range(N):
    start, end = map(int, input().split())
    lifeguard.append([start, end])
    for i in range(start, end):
        times[i] += 1

total_time = 0
max_time = 0

for i in range(1001):
    if times[i] > 0:
        total_time += 1

for guard in lifeguard:
    start, end = guard
    temp_time = total_time

    for i in range(start, end):
        if times[i] == 1:
            temp_time -= 1

    max_time = max(max_time, temp_time)

print(max_time)