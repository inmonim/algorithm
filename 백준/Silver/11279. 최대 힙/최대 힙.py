import sys, heapq

input = sys.stdin.readline

oper = [int(input()) for _ in range(int(input()))]

Q = []

for o in oper:
    if not o:
        if Q:
            print(-heapq.heappop(Q))
        else:
            print(0)
    else:
        heapq.heappush(Q, -o)