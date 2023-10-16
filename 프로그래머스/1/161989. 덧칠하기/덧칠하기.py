def solution(n, m, section):
    ans = 0
    now = 0
    for t in section:
        if t > now:
            now = t+m-1
            ans += 1
    return ans