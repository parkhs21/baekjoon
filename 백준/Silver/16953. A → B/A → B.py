from collections import deque

A,B = map(int, input().split())

graph = deque()
graph.append([2*A, 1])
graph.append([int(str(A)+'1'), 1])

while graph:
    num,depth = graph.popleft()
    if num<B:
        graph.append([2*num, depth+1])
        graph.append([int(str(num)+'1'), depth+1])
    elif num==B:
        graph.append([0,0])
        print(depth+1)
        break

if not graph: print(-1)