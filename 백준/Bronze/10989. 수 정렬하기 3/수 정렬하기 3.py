import sys

dic = {}
for i in range(int(sys.stdin.readline())):
    x = int(sys.stdin.readline())
    if dic.get(x) != None:
        dic[x] += 1
    else:
        dic[x] = 1

for i in sorted(dic.keys()):
    for j in range(dic[i]):
        print(i)