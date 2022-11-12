import sys

n,m = map(int, sys.stdin.readline().split())

arr = list(map(int, sys.stdin.readline().split()))
dic = {}

for i in arr:
    if i not in dic:
        dic[i] = 1
    else:
        dic[i] += 1
        
T = sorted(dic.keys())[::-1]
R = 0
mul = 0
for i in range(1, len(T)+1):
    if i < len(T):
        mul += dic[T[i-1]]
        R += (T[i-1] - T[i]) * mul
        if R >= m:
            print(T[i] + (R-m)//mul)
            break
    else:
        mul += dic[T[i-1]]
        R += (T[i-1]) * mul
        print((R-m)//mul)