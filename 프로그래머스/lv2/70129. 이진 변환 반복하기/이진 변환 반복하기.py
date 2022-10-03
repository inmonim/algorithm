def solution(s):
    cnt = 0
    answer = [0,0]
    while len(s) > 1:
        a = s.count('1')
        b = len(s) - a
        s = bin(a)[2:]
        cnt += 1
        answer = [cnt, answer[1]+b]
    return answer