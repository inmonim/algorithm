N = int(input())

result,x=0,0
if N in [4,7]:
    result=-1
while result==0:
    if ((N%5)+x*5)%3==0:
        result=(N//5-x)+((N%5)+x*5)//3
    x += 1

print(result)