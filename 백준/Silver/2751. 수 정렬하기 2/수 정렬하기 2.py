import sys
N = int(input())
arr = [int(sys.stdin.readline().strip()) for _ in range(N)]
dic = {i:0 for i in range(min(arr),max(arr)+1)}
for i in arr:
    dic[i] = 1
R = []
for k,v in dic.items():
    if v == 1:
        R.append(k)
print(*R, sep='\n')