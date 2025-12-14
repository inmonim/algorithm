import heapq as hq

def solution(s, K):
    hq.heapify(s)
    answer = 0
    while len(s) >= 2 and s[0] < K:
        a, b = hq.heappop(s), hq.heappop(s)
        nc = a + b*2
        hq.heappush(s, nc)
        answer += 1
    if (len(s) == 1 and s[0] < K):
        answer = -1
    return answer