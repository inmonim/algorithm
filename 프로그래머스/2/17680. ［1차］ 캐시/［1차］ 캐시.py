def solution(n, arr):
    if n == 0:
        return len(arr)*5
    arr = [x.lower() for x in arr]
    cache = ['']*n
    answer = 0
    for x in arr:
        idx = -1
        for i in range(len(cache)):
            if x == cache[i]:
                idx = i
                break
        if idx == -1:
            answer += 5
            cache.pop()
        else:
            answer += 1
            cache.pop(idx)
        cache = [x]+cache
    
    return answer