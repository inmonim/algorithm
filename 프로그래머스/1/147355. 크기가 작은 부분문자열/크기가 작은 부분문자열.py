def solution(t, p):
    L = len(p)
    p = int(p)
    ans = 0
    for i in range(len(t)-L+1):
        print(t[i:i+L])
        if int(t[i:i+L]) <= p:
            ans += 1 
    return ans