N,S,R = map(int, input().split())
brokens = sorted(map(int, input().split()))
mores = sorted(map(int, input().split()))

result = S

for b in brokens:
    for m in mores:
        if b==m:
            brokens.remove(m)
            mores.remove(m)
            result -= 1
            break

for b in brokens:
    for m in mores:
        if b>=m-1 and b<=m+1:
            mores.remove(m)
            result -= 1
            break

print(result)