for _ in range(int(input())):
    
    n = int(input())
    a = [0, 1, 2, 4]
    while len(a) <= n:
        a.append(a[-3] + a[-2] + a[-1])
    
    print(a[n])