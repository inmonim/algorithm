def solution(s):
    n = 0
    x = ''
    ans = 0
    for i in range(len(s)):
        if not n:
            x = s[i]
            n += 1
        elif s[i] == x:
            n += 1
        else:
            n -= 1
        
        if not n:
            ans += 1
    if n:
        ans += 1
        
    return ans