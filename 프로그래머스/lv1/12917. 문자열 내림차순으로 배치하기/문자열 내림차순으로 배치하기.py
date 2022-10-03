def solution(s):
    s = sorted(list(s), reverse=True)
    A, B = [],[]
    for i in range(len(s)):
        B.append(s[i]) if s[i].isupper() else A.append(s[i])
    A = ''.join(A+B)
    return A