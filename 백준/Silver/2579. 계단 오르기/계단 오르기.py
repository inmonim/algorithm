n=int(input())
arr=[0]
for _ in range(n):
  arr.append(int(input()))

d=[0]*301
if n==1:
  d[n] = arr[1]
elif n==2:
  d[n] = arr[1]+arr[2]
else:
  d[1]=arr[1]
  d[2]=arr[1]+arr[2]
  d[3]=max(arr[1]+arr[3],arr[2]+arr[3])
  for i in range(4,n+1):
    d[i]=max(d[i-3]+arr[i-1]+arr[i], d[i-2]+arr[i])

print(d[n])