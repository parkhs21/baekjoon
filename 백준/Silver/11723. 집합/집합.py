import sys
input = sys.stdin.readline

M = int(input())
bit = 0

for _ in range(M):
    oper = input().split()
    op = oper[0]

    if op=='all': bit = 2**20-1
    elif op=='empty': bit = 0
    else:
        num = int(oper[1])-1
        if op=='add': bit |= 1<<num
        elif op=='remove': bit &= ~(1<<num)
        elif op=='check': print(1 if (bit>>num)%2 else 0)
        elif op=='toggle': bit ^= 1<<num
