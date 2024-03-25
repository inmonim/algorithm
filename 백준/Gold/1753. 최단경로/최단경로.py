import heapq
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
start = int(input())
reach = [M*20 for _ in range(N+1)]
reach[start] = 0

node = [{} for _ in range(N+1)]
for _ in range(M):
    s, e, v = map(int, input().split())
    if e in node[s]:
        if node[s][e] > v:
            node[s][e] = v
    else:
        node[s][e] = v

Q = []
for k in node[start].keys():
    Q.append((node[start][k], k))
    reach[k] = node[start][k]

while Q:
    v, k = Q.pop(0)
    for nk in node[k].keys():
        nv = v + node[k][nk]
        if reach[nk] > nv:
            reach[nk] = nv
            heapq.heappush(Q, (nv, nk))

for i in reach[1:]:
    if i == M*20:
        print('INF')
    else:
        print(i)