N,M = map(int, input().split())
_, *known = map(int, input().split())
party = [list(map(int, input().split())) for _ in range(M)]

parent = [i for i in range(N+1)]
truth = [False] * (N+1)

def find(x):
    if parent[x] != x:
        return find(parent[x])
    return x

def union(target,b):
    b = find(b)
    if target<b: parent[b] = target
    else: parent[target] = b

for _, *people in party:
    target = find(people[0])
    for p in people[1:]:
        union(target, p)
        

for k in known:
    knwon_parent = find(k)
    truth[knwon_parent] = True
    truth[k] = True
for i in range(1,N+1):
    if not truth[i]:
        p = find(parent[i])
        if truth[p]:
            truth[i] = True


cnt = 0
for _, *people in party:
    if not truth[people[0]]:
        cnt += 1
print(cnt)