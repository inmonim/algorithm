for T in range(int(input())):
    N, S = map(int, input().split())
    arr = list(map(int, input().split()))
    tar = arr[S]
    idx = S
    cnt = 0
    
    while arr:
        if arr[0] < max(arr):
            arr.append(arr.pop(0))
            if idx:
                idx-=1
            else:
                idx += N-1
        elif arr[0] == max(arr):
            cnt += 1
            if arr.pop(0) == tar and idx == 0:
                break
            N -= 1
            idx -= 1
            
    print(cnt)