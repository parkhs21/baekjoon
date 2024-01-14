import sys

array = []

for _ in range(9):
    array.append(int(sys.stdin.readline()))

array.sort()
sum_array = sum(array)

for i in range(8, 0, -1):
    for j in range(i-1, -1, -1):
        if sum_array-array[i]-array[j]==100:
            one,two = array[i], array[j]

array.remove(one)
array.remove(two)

for i in range(7):
    sys.stdout.write(str(array[i])+'\n')