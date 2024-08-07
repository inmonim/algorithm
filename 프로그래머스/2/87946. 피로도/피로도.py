from itertools import permutations

def solution(k, dungeons):
    l = list(range(len(dungeons)))
    permu = set(permutations(l))
    
    answer = 0
    for p in permu:
        x = k
        cnt = 0
        for i in p:
            if x >= dungeons[i][0]:
                x -= dungeons[i][1]
                cnt += 1
            else:
                break
        answer = max([answer, cnt])
    
    return answer