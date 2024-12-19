t = int(input())

def bs(x):
    b, t = 1, x-1
    
    while b <= t:
        m = (b + t) // 2
        if m**2 < x:
            b = m + 1
        else:
            t = m - 1
    return b

print(bs(t))