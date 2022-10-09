def solution(s):
    s = list(s)
    dic = {'[':']','(':')','{':'}'}
    S, E = map(list, [dic.keys(), dic.values()])
    L = len(s)
    result = 0

    for spin in range(L):
        s.append(s.pop(0))
        if s[-1] in S:
            continue
        s2 = s[:]
        stack = [s2.pop()]

        for i in range(L-2, -1,-1):
            if s2[i] in E:
                stack.append(s2.pop())
            else:
                if not stack:
                    break
                elif stack[-1] == dic[s2[i]]:
                    stack.pop()
                    s2.pop()
                else:
                    break
        else:
            if not stack:
                result += 1
    
    return result