E,S,B=map(int,input().split())
e=s=b=1
R=1
while 1:
    if e==E and s==S and b==B:break
    e+=1 if e<15 else -14
    s+=1 if s<28 else -27
    b+=1 if b<19 else -18
    R+=1
print(R)