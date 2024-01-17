import sys

p=sys.stdin.readline

N=int(p())

a=[int(p()) for _ in range(N)]

if N<=2:
    print(sum(a))

else:
    s=[a[0], a[0]+a[1], max(a[0]+a[2], a[1]+a[2])]

    for i in range(3, N):
        s.append(max(s[i-3] + a[i-1] + a[i], s[i-2] + a[i]))
    print(s[-1])