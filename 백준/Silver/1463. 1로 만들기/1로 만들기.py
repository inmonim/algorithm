import sys

Q = [int(sys.stdin.readline().strip())]

def sol(n):
    if check.get(n) == None:
        next_li.append(n)
        check[n] = 1

check= {}
TF = 1
cnt = 0
next_li = []
while TF:
    Q.extend(next_li)
    next_li = []
    cnt += 1
    while Q:
        n = Q.pop(0)
        if n%3 == 0:
            sol(n//3)
        if n%2 == 0:
            sol(n//2)
        sol(n-1)
        if n == 1:
            if cnt == 1:
                print(0)
            else:
                print(cnt-1)
            TF = 0
            break