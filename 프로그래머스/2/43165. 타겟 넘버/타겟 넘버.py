def solution(ns, target):
    answer = 0
    q = [(-ns[0], ns[0], 1)]
    while q:
        a, b, c = q.pop()
        if c < len(ns):
            a1, a2, b1, b2 = a+ns[c], a-ns[c], b+ns[c], b-ns[c]
            q.append((a1, a2, c+1))
            q.append((b1, b2, c+1))
            continue
        answer += [a,b].count(target)
        
    return answer