def solution(survey, choices):
    mbti = ["RT", "CF", "JM", "AN"]
    score = {}
    for i in range(4):
        score[mbti[i]] = [0,0]
    
    for i in range(len(survey)):
        if choices[i]==4:
            continue

        choice = choices[i]
        surv = survey[i]
            
        if surv[0] > surv[1]:
            surv = surv[::-1]
            choice = 8-choice
        
        if choice < 4:
            score[surv][0] += 4-choice
        else:
            score[surv][1] += choice-4
    
    answer = ''
    
    for m in mbti:
        s = score[m]
        if s[0] >= s[1]:
            answer += m[0]
        else:
            answer += m[1]
    
    return answer