n, m = map(int, input().split())
c = list(map(int, input().split()))

R = 0
for i1 in range(n-2):
    for i2 in range(i1+1,n-1):
        for i3 in range(i2+1,n):
            if m >= c[i1]+c[i2]+c[i3] > R:
                R = c[i1]+c[i2]+c[i3]
print(R)