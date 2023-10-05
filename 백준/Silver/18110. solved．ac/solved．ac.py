N = int(input())
difficulty = [int(input()) for i in range(N)]
difficulty.sort()

my_round = lambda x: int(x)+1 if x-int(x)>=0.5 else int(x)
cut = my_round(N*0.15)

if not N: print(0)
else:
    cut_diff = difficulty[cut:N-cut]
    print(my_round(sum(cut_diff)/len(cut_diff)))