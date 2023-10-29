from collections import deque

N,M = map(int, input().split())
nums = list(map(int, input().split()))

deq = deque([i for i in range(1,N+1)])
count = 0

for num in nums:
    while (deq[0] != num):
        if deq.index(num) > len(deq)//2:
            deq.rotate(1)
        else:
            deq.rotate(-1)
        count += 1
    deq.popleft()
print(count)