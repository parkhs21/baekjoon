def solution(priorities, location):
    answer = 0
    length = len(priorities)
    
    i = 0
    target = 1
    while target>0:
        target = max(priorities)
        if priorities[i] == target:
            if i == location:
                return answer+1
            answer += 1
            priorities[i] = 0
        i = (i+1)%length
    
    
    return answer
