def solution(k, score):
    ans = []
    l = []
    for s in score:
        l.append(s)
        
        for i in range(len(l)-2, -1, -1):
            if l[i] < l[i+1]:
                l[i], l[i+1] = l[i+1], l[i]
        
        if len(l) > k:
            l.pop()
        
        ans.append(l[-1])

    return ans