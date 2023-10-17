def solution(s, skip, index):
    alp = 'abcdefghijklmnopqrstuvwxyz'
    for i in skip:
        alp = alp.replace(i,'')
    
    alp = alp*10
    
    ans = ''
    for i in s:
        ans += alp[alp.index(i) + index]
    
    return ans