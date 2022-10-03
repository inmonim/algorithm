def solution(s):
    answer = []
    for S in s.split(' '):
        if S == '':
            answer.append(S)
        elif S[0].isdigit():
            answer.append(S.lower())
        else:
            answer.append(S[0].upper()+S[1:].lower())
    return ' '.join(answer)