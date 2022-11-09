for _ in range(int(input())):
    R = ''
    y,x,t = map(int,input().split())
    
    A = y if t%y == 0 else t%y
    B = t//y if t%y == 0 else t//y+1
    if B < 10:
        B = '0'+str(B)
    R = str(A)+str(B)
    
    print(R)