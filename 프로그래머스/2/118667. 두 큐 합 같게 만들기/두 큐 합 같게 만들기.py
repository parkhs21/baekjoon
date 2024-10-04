def solution(q1, q2):
    flag = sum(q1) + sum(q2)
    flag //= 2
    
    arr = [*q1,*q2,*q1]
    s,e = 0,len(q1)
    check = sum(q1)
    answer = 0
    
    while flag!=check:
        if s>=len(arr)-len(q1) or e>=len(arr):
            return -1
        
        if check < flag:
            check += arr[e]
            e += 1
        else:
            check -= arr[s]
            s += 1
        answer += 1
    
    return answer