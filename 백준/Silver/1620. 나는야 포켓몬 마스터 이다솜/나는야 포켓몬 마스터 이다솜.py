import sys

input = sys.stdin.readline

N,M = map(int, input().split())

n_d = {}
for i in range(N):
    n_d[input().strip()] = i+1
n_l = [0]+list(n_d.keys())

for i in range(M):
    a = input().strip()
    if a.isdigit():
        print(n_l[int(a)])
    else:
        print(n_d[a])