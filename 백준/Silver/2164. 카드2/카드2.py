N=int(input())
i=int(bin(N<<1)[3:],2)
print(i if i else N)