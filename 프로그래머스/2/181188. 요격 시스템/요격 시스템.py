def solution(targets):
    answer = 0
    d = {}
    for t in targets:
        if t[0] in d:
            if d[t[0]] > t[1]:
                d[t[0]] = t[1]
        else:
             d[t[0]] = t[1]

    d_list = sorted(d.keys())
    ml = d[d_list[-1]]
    i = d_list[0]
    last = d[i]
    flag = 0
    
    # [시작 : 최소끝] 쌍의 시작으로 순회
    for i in d_list:
        
        # 시작 값이 이전 최소끝보다 길 경우 요격, 최소끝을 초기화
        if i >= last:
            answer += 1
            last = ml
        
        # 이번 최소끝이 이전 최소끝보다 짧을 경우 새롭게 배정
        if d[i] < last:
            last = d[i]
    
    return answer+1