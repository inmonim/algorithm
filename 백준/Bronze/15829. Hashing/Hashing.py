input()
R = 0
r = 1
cnt = 0
for i in input():
    if cnt == 0:
        R += ord(i)-96
        cnt+=1
    else:
        R += (ord(i)-96)*(r:=r*31)

print(R%1234567891)