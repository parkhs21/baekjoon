from heapq import heappush, heappop
import sys
input = sys.stdin.readline

heap = []
for _ in range(int(input())):
    x = int(input())
    if x!=0: heappush(heap, x)
    elif len(heap)==0: print(0)
    else: print(heappop(heap))