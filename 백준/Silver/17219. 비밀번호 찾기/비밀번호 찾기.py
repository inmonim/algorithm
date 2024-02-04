import sys

input = sys.stdin.readline

N, M = map(int, input().split())

d = {}
for _ in range(N):
    u, p = input().split()
    d[u] = p

for _ in range(M):
    print(d[input().strip()])