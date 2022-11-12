N = int(input())

R = N
for i in range(N,0,-1):
    x = i + sum([int(j) for j in list(str(i))])
    if x == N and R > i:
        R = i
else:
    if R == N:
        R = 0
print(R)