i=input
r=range
N=[1,1,1,2,2,3]
for _ in r(96):N+=[N[-1]+N[-5]]
for _ in r(int(i())):print(N[int(i())-1])