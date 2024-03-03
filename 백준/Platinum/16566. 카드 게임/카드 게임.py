from bisect import bisect_right

N,M,K = map(int, input().split())
cards = sorted(list(map(int, input().split())))
nums = list(map(int, input().split()))
visited = [False]*(M+1)

for n in nums:
    idx = bisect_right(cards, n)
    while visited[idx]: idx += 1
    visited[idx] = True
    print(cards[idx])