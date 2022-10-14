N = int(input())

for T in range(N):
    r, n = map(int, input().split())
    
    r1, n1, x = 1, 1, 1
    for i in range(1, n+1):
        n1 = n1*i
        if i <= r:
            r1 = r1*i
        if i <= n-r:
            x = x*i
    result = n1 // (r1*x)
    print(result)