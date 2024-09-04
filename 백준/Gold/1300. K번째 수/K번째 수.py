N, K = int(input()), int(input())

s, e = 1, K
a = 0

while s <= e:
    
    m = (s + e) // 2
    cnt = 0
    for i in range(1, N+1):
        cnt += min(m//i, N)
    
    if cnt >= K:
        a = m
        e = m-1
    else:
        s = m+1

print(a)