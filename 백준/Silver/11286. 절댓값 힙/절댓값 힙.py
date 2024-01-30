import sys, heapq

input = sys.stdin.readline

N = int(input())
q = []
for _ in range(N):
    n = int(input())
    
    if not n and q:
        qn = heapq.heappop(q)
        if qn%1:
            qn = -(int(qn+0.5))
        print(qn)
    elif not n:
        print(0)
    else:
        if n < 0:
            n = -(n + 0.5)
        heapq.heappush(q, n)