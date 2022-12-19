import sys
input = sys.stdin.readline

N, M = map(int, input().split())
dic = {}
ans = []

for i in range(N):
    dic[input().strip()] = 1

for i in range(M):
    if dic.get(x := input().strip()):
        ans.append(x)
print(len(ans))
print(*sorted(ans), sep='\n')