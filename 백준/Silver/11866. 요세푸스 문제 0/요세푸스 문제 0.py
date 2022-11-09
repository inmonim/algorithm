n,k = map(int, input().split())
R = []
arr = [i for i in range(1, n+1)]
s = k-1
while arr:
    if s >= len(arr):
        s = s%len(arr)
    else:
        R.append(str(arr.pop(s)))
        s += k-1
        
print(f"<{', '.join(R)}>")