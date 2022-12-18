btn = [i for i in range(0,10)]

N = int(input())

for i in range(int(input())):
    if i == 0:
        broken = list(map(int, input().split()))
    btn.remove(broken[i])
ans = abs(N - 100)

TF = 0
for i1 in [0]+btn:
    n = 0
    n += i1*100000
    for i2 in [0]+btn if n == 0 else btn:
        n2 = n + i2*10000
        for i3 in [0]+btn if n2 == 0 else btn:
            n3 = n2 + i3*1000
            for i4 in [0]+btn if n3 == 0 else btn:
                n4 = n3 + i4*100
                for i5 in [0]+btn if n4 == 0 else btn:
                    n5 = n4 + i5*10
                    for i6 in btn:
                        n6 = n5 + i6
                        if ans > (i := abs(N - n6)+len(str(n6))):
                            ans = i
print(ans)