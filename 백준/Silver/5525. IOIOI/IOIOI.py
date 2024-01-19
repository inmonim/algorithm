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

i = 0
while i < len(dis):
    if dis[i] == 'I':
        if dis[i:i+l] == ioi:
            ans += 1
            i += 1
    i += 1

print(ans)