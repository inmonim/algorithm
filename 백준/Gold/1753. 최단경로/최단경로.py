import heapq
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
start = int(input())
reach = [M*20 for _ in range(N+1)]
reach[start] = 0

node = [[] for _ in range(N+1)]
for _ in range(M):
    s, e, v = map(int, input().split())
    node[s].append((v, e))

Q = []
heapq.heappush(Q, (0, start))

while Q:
    v, i = heapq.heappop(Q)
    if reach[i] < v:
        continue
    
    for n_node in node[i]:
        nv, ni = n_node
        rv = v + nv
        if reach[ni] > rv:
            reach[ni] = rv
            heapq.heappush(Q, (rv, ni))

for i in reach[1:]:
    if i == M*20:
        print('INF')
    else:
        print(i)