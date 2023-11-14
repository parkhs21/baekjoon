import math

N = int(input())

log_N = int(math.log2(N))
if N == 2**log_N:
  print(N, 0)
else:
  remain = bin(2**(log_N + 1)-N)[2:][::-1]
  for i in range(len(remain)):
    if remain[i] == '1': break
  print(2**(log_N+1), log_N-i+1)