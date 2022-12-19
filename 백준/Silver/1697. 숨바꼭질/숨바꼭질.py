from collections import deque

def check(n):
    if n < 0 or n > 100000:
        return
    if vis.get(n) == None:
        next_li.append(n)
        vis[n] = 1

N,M = map(int, input().split())

vis = {}
cnt = 0
next_li = [N]


while next_li:
    Q = deque(next_li)
    next_li = []
    cnt += 1
    while Q:
        n = Q.popleft()
        check(n*2)
        check(n+1)
        check(n-1)
        if n == M or M in next_li:
            if n == M:
                print(0)
            else:
                print(cnt)
            next_li = []
            break