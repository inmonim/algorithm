def solution(X, Y):
    answer = []

    R = {str(i):0 for i in range(10)}
    R2 = {str(i):0 for i in range(10)}
    for i in X:
        R[i] += 1
    for i in Y:
        R2[i] += 1
    for i in range(9,-1,-1):
        i = str(i)
        m = min([R[i], R2[i]])
        if i == '0' and not answer and m > 0:
            answer = ['0']
            break
        if m > 0:
            answer.append(i * m)

    if not answer:
        answer = ['-1']

    return ''.join(answer)