N, T = map(int, input().split())
arr = sorted([int(input()) for _ in range(N)])

start = 0
idx = 0
while True:
    R = 0
    for a in arr:
        R += a//arr[idx]
    if R <= T:
        break
    arr.pop(0)
    idx += 1
end = arr[idx]
start = 1

while start <= end:
    R = 0
    mid = (start+end)//2
    for i in range(N-idx):
        R += arr[i]//mid
    if R >= T:
        start = mid + 1
    elif R < T:
        end = mid -1
print(end)