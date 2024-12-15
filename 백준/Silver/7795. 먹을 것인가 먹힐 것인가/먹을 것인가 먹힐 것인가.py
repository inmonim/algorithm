import sys

input = sys.stdin.readline

T = int(input())

def f(d, l, n):
    keys = []
    for i in range(n):
        if l[i] in d:
            d[l[i]] += 1
        else:
            d[l[i]] = 1
            keys.append(l[i])
    return d, sorted(keys)

def bs(bdl, tar):
    b, t = 0, len(bdl) - 1
    while b <= t:
        m = (b + t) // 2
        if bdl[m] < tar:
            b = m + 1
        else:
            t = m - 1
    return b
    
def sol_func():
    n, m = map(int, input().split())
    a, b = list(map(int, input().split())), list(map(int, input().split()))

    ad, adl = f({}, a, n)
    bd, bdl = f({}, b, m)

    ac = 0
    for k in bdl:
        ac += bd[k]
        bd[k] = ac

    answer = 0
    for x in adl:
        if x > bdl[-1]:
            answer += ad[x] * bd[bdl[-1]]
        elif x > bdl[0]:
            y = bs(bdl, x)
            if y > 0:
                answer += ad[x] * bd[bdl[y-1]]

    print(answer)

for _ in range(T):
    sol_func()