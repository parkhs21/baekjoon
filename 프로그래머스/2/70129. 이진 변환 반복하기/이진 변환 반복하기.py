def solution(s):
    answer = [0,0]
    
    while s!='1':
        answer[0] += 1
        answer[1] += s.count('0')
        
        remain = len(s) - s.count('0')
        s = bin(remain)[2:]
        
    return answer