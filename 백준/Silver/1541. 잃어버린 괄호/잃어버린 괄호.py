import sys

txt = sys.stdin.readline().strip().split('-')

N = 0
for j in txt[0].split('+'):
    N += int(j)

for i in range(1, len(txt)):
    for j in txt[i].split('+'):
        N -= int(j)

print(N)