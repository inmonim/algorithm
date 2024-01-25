import sys

input = sys.stdin.readline

for _ in range(int(input())):
    
    tem = {}
    for _ in range(int(input())):
        n, c = input().split()
        tem[c] = tem[c]+1 if tem.get(c) else 2
    
    a = 1
    for i in tem.values():
        a = a * i
    a -= 1
    print(a)