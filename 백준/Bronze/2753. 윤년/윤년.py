x=int(input())
if not x%4 and (x%100 or x%400==0):
    print(1) 
else:
    print(0)