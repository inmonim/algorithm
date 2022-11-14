import sys

N = int(sys.stdin.readline())
arr = []
for i in range(N):
    arr.append(list(map(int, sys.stdin.readline().split())))

dic = {}
for a in arr:
    if dic.get(a[1]) == None:
        dic[a[1]] = [a[0]]
    else:
        dic[a[1]] += [a[0]]

R = []
for i in sorted(dic.keys()):
    for j in sorted(dic[i]):
        R.append([j, i])

for i in R:
    print(*i)