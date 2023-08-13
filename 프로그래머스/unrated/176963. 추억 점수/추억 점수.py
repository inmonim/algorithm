def solution(name, yearning, photo):
    mem = {n:y for n,y in zip(name, yearning)}
    answer = []
    
    for i in range(len(photo)):
        score = 0
        for n in photo[i]:
            score += mem.get(n) if mem.get(n) else 0
        answer.append(score)
    
    return answer