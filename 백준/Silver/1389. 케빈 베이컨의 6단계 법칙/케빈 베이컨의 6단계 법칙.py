import sys

N, T = map(int, input().split())
node = [[] for _ in range(N+1)]
bacon = [0] * (N+1)

for i in range(T):
    a, b = map(int, sys.stdin.readline().split())
    node[a].append(b)
    node[b].append(a)


for i in range(1, N+1):
    i_bacon = [0] * (N+1)
    check = 0
    cnt = 1
    Q = node[i].copy()
    next_li = []
    while Q:
        next_n = Q.pop(0)
        if i_bacon[next_n] == 0:
            i_bacon[next_n] = cnt
            check += 1
        next_li.extend(node[next_n])
        
        if check == N:
            break
        
        if not Q:
            Q.extend(next_li)
            next_li = []
            cnt += 1
    bacon[i] = sum(i_bacon)

mb = min(bacon[1:])
print(bacon.index(mb))