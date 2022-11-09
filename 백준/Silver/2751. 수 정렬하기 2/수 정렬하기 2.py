import sys
N = int(sys.stdin.readline())
arr = [int(sys.stdin.readline().strip()) for _ in range(N)]

m,M = min(arr),max(arr)

dic = {i:0 for i in range(int(m),int(M)+1)}

for i in arr:
    dic[i] = 1
R = []
for k,v in dic.items():
    if v == 1:
        R.append(k)

print(*R, sep='\n')