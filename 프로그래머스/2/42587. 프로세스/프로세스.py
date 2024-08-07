def solution(p, l):
    
    cnt = 1
    while p:
        x = p.pop(0)
        if p and x >= max(p):
            if not l:
                return cnt
            cnt += 1
        elif not p:
            return cnt
        else:
            p.append(x)
        l -= 1
        if l == -1:
            l = len(p)-1