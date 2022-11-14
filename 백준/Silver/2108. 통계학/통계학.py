import sys
D = {}
for _ in range(N:=int(sys.stdin.readline())):
    if D.get(i:=int(sys.stdin.readline().strip()))==None:
        D[i]=1
    else:
        D[i]+=1

arr=[]
vm=max(D.values())
many=[]
for i in (Dk:=sorted(D.keys())):
    if D[i] == vm: many.append(i)
    arr.extend(D[i]*[i])
    
print(int(round(sum(arr)/N,0)))
print(arr[N//2])
print(many[1] if len(many) >=2 else many[0])
print(Dk[-1]-Dk[0])