N = int(input())
row = [0]*N

def check(x):
    for i in range(x):
        if row[x]==row[i] or abs(row[x]-row[i])==abs(x-i):
            return False
    return True

def nq(x):
    answer = 0
    if x==N: return 1
    for i in range(N):
        row[x] = i
        if check(x):
            answer += nq(x+1)
    return answer

print(nq(0))