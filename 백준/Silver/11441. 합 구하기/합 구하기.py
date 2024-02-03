N = int(input())
A = [0] + list(map(int, input().split()))
M = int(input())
sections = [list(map(int, input().split())) for _ in range(M)]

psum = [0]*(N+1)
for i in range(1,N+1):
    psum[i] = psum[i-1]+A[i]

for l,r in sections:
    print(psum[r]-psum[l-1])