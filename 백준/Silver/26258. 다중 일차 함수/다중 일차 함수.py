import sys

input = sys.stdin.readline

n = int(input())

xys = [list(map(int, input().split())) for _ in range(n)]

qs = [float(input().strip()) for _ in range(int(input()))]

def bs(lst, tar):
    b, t = 0, len(lst) - 1
    while b <= t:
        m = (b + t) // 2
        if lst[m] < tar:
            b = m + 1
        else:
            t = m - 1
    return b

slop = { }

for i in range(1, n):
    px, py = xys[i-1]
    x, y = xys[i]
    
    if py < y:
        slop[x] = 1
    elif py > y:
        slop[x] = -1
    else:
        slop[x] = 0

xs = sorted(list(slop.keys()))

for q in qs:
    x = bs(xs, q)
    print(slop[xs[x]])