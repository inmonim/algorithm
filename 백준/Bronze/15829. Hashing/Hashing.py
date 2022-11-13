L=int(input())
R = 0
r = 1
txt = input()
for i in range(L):
    if i == 0:
        R += ord(txt[i])-96
    else:
        R += (ord(txt[i])-96)*((r:=r*31))

print(R%1234567891)