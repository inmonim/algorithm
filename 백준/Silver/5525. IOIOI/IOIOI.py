import sys, re

input = sys.stdin.readline

ioi = 'I'

N = int(input())
ioi += 'OI'*(N)
L = int(input())
S = input().strip()

dos = re.sub('O{2,}', '', S)
dis = re.sub('I{3,}', 'II', dos)

ans = 0
l = len(ioi)
flag = 0

i = 0
while i < len(dis):
    if flag:
        if dis[i:i+2] == 'OI':
            ans += 1
            i += 1
        else:
            flag = 0
    if not flag and dis[i] == 'I':
        if dis[i:i+l] == ioi:
            ans += 1
            i += l-1
            flag = 1
    i += 1

print(ans)