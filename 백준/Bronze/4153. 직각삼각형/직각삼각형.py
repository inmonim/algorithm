a,b,x = sorted(list(map(int, input().split())))
while a+b+x:
    print('right' if a**2 + b**2 == x**2 else 'wrong')
    a,b,x = sorted(list(map(int, input().split())))