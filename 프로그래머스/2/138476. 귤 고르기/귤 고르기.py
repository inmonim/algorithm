def solution(k, tangerine):
    w = {}
    for t in tangerine:
        if w.get(t):
            w[t] += 1
        else:
            w[t] = 1
    cnt = 0
    for x in sorted(w.values(), reverse=True):
        k -= x
        cnt += 1
        if k <= 0:
            return cnt
    return cnt