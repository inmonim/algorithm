def solution(s):
    d = {}
    a = []
    for i in range(len(s)):
        if s[i] in d:
            a.append(i - d[s[i]])
            d[s[i]] = i
        else:
            a.append(-1)
            d[s[i]] = i
    return a