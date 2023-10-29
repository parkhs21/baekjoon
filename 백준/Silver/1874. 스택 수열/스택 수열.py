n = int(input())
li = []     
ans = []    
cnt = 0
flag = True
for _ in range(n):
    val = int(input())

    while cnt < val:
        cnt += 1
        li.append(cnt)
        ans.append('+')
    if li[-1] == val:
        li.pop()
        ans.append('-')
    else:
        flag = False
        break

if flag == True:
    print('\n'.join(ans))
else:
    print('NO')