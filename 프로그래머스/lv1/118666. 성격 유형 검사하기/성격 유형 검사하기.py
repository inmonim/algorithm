def solution(survey, choices):
    result = ''
    answer = {'R':0 ,'C':0 ,'J': 0,'A':0}
    
    for i in range(len(survey)):
        if survey[i][1] in list(answer.keys()):
            answer[survey[i][1]] += choices[i] - 4
        else:
            answer[survey[i][0]] -= choices[i] - 4
    
    idx, another = 0, ['T','F','M','N']
    for k, v in answer.items():
        if v >= 0:
            result += k
        else:
            result += another[idx]
        idx += 1
    
    return result