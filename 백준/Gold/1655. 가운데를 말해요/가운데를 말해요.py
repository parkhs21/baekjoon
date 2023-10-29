import heapq
import sys
input = sys.stdin.readline

N = int(input())

left = []
right = []
for _ in range(N):
    num = int(input())
    if len(left) == len(right):
        heapq.heappush(left, -num)
    else:
        heapq.heappush(right, num)

    if right and -left[0] > right[0]:
        heapq.heappush(left, -heapq.heappop(right))
        heapq.heappush(right, -heapq.heappop(left))

    print(-left[0])