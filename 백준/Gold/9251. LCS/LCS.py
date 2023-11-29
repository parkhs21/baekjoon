A = input()
B = input()

len_A, len_B = len(A), len(B)
lcs = [[0] * (len_B+1) for _ in range(len_A+1)]

for i in range(1, len_A+1):
    for j in range(1, len_B+1):
        if A[i-1] == B[j-1]: lcs[i][j] = lcs[i-1][j-1] + 1
        else: lcs[i][j] = max(lcs[i][j-1], lcs[i-1][j])

print(lcs[-1][-1])