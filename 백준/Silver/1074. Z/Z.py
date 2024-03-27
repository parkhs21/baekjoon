N,r,c = map(int, input().split())
answer = 0

N = 2**(N-1)
while N>0:
    if r<N and c<N:
        answer += 0
    elif r<N and c>=N:
        answer += N**2
        c -= N
    elif r>=N and c<N:
        answer += 2*N**2
        r -= N
    else:
        answer += 3*N**2
        c -= N
        r -= N
    
    N = N//2
    
    
print(answer)