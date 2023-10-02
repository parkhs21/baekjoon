N,K,D = map(int, input().split())
graph = []

for _ in range(N):
    student = list(map(int, input().split()))
    student.append(list(map(int, input().split())))
    graph.append(student)
graph.sort(key=lambda x: (x[1], x[0]))

start,end = 0,0
E = 0
all_know,group_know = 0,0
algorithm = [0]*(K+1)

while end<N:
    if graph[end][1]-graph[start][1] <= D:
        all_know = 0
        for a in graph[end][2]:
            algorithm[a] += 1
            if algorithm[a]==1: group_know += 1
            if algorithm[a]==end-start+1: all_know += 1

        E = max(E, (group_know-all_know)*(end-start+1))
        end += 1

    else:
        for a in graph[start][2]:
            algorithm[a] -= 1
            if not algorithm[a]: group_know -= 1

        start += 1

print(E)