def solution(k, m, score):
    score.sort(reverse=True)
    answer = 0
    for i in range(1, len(score)//m+1):
        i = i*m
        answer += score[i-1] * m
    return answer