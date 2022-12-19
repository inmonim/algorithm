def check(n):
    if n < 0 or n > 100000:
        return
    if vis.get(n) == None:
        next_li.append(n)
        vis[n] = 1

N,M = map(int, input().split())

vis = {}
cnt = 0
Q = [N]
next_li = []

while Q:
    n = Q.pop(0)
    check(n*2)
    check(n+1)
    check(n-1)
    if n == M or M in next_li:
        if n == M:
            print(0)
        else:
            cnt += 1
            print(cnt)
        break
    if not Q:
        cnt += 1
        Q.extend(next_li)
        next_li = []
        