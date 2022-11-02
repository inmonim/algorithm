n = int(input())
arr = list(map(int, input().split()))
if 1 in arr:
    arr.remove(1)

maxn = max(arr)
cnt = 0
filt = []

for i in range(2, int(maxn**0.5)+1):
    for j in range(2, i):
        if i%j == 0:
            break
    else:
        filt.append(i)
for i in arr:
    for j in filt:
        if i==j:
            cnt+=1
            break
        if i%j == 0:
            break
    else:
        cnt += 1
print(cnt)