N, T = map(int, input().split())
arr = sorted([int(input()) for _ in range(N)])

end = max(arr)
start = 1

while start <= end:
    R = 0
    mid = (start+end)//2
    for i in range(N):
        R += arr[i]//mid
    if R >= T:
        start = mid + 1
    elif R < T:
        end = mid -1
print(end)