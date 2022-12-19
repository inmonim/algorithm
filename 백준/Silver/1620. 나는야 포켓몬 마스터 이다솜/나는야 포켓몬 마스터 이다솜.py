import sys

input = sys.stdin.readline

N,M = map(int, input().split())

idx = {}
name = {}

for i in range(N):
    idx[1+i] = input().strip()
    name[idx[1+i]] = 1+i
    
for i in range(M):
    x = input().strip()
    if x.isdigit():
        print(idx[int(x)])
    else:
        print(name[x])