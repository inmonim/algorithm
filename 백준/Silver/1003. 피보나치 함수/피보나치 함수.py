t=input
for _ in range(int(t())):
    x=int(t())
    Z,O=[1,0,1],[0,1,1]
    for i in range(3, x+1):
        Z.append(Z[i-2]+Z[i-1])
        O.append(O[i-2]+O[i-1])
    print(f'{Z[x]} {O[x]}')