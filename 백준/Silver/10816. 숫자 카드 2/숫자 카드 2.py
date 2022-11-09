import sys

n = int(input())
arr = list(sys.stdin.readline().split())
m = int(input())
tar = list(sys.stdin.readline().split())
dic = {}

for i in arr:
    if dic.get(i) == None:
        dic[i] = 1
    else:
        dic[i] += 1

R = []
for i in tar:
    if dic.get(i) == None:
        R.append(0)
    else:
        R.append(dic.get(i))

print(*R, sep=' ')