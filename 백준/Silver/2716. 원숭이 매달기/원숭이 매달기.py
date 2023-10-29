T = int(input())

for _ in range(T):
    tree = input()
    count = 0
    max_count = 0
    for c in tree:
        count += 1 if c == '[' else -1
        max_count = max(max_count, count)
    print(2 ** max_count)

