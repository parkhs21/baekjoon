L,R = input().split()
result = 0

if len(L)==len(R):
  for i in range(len(L)):
    if L[i]==R[i]:
      if L[i]=='8': result += 1
    else: break

print(result)