import math

N = int(input())
answer = 0
for i in range(N, -1, -2):
    temp = (N-i)//2
    answer += 2**temp * math.factorial(i+temp)//(math.factorial(i)*math.factorial(temp))

print(answer%10007)