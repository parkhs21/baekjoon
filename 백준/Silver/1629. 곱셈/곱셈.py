A,B,C = map(int, input().split())
result = 1
bin_reverse = bin(B)[2:][::-1]

for i in bin_reverse:
    if i == '1': result = (result*A)%C
    A = (A*A)%C

print(result)