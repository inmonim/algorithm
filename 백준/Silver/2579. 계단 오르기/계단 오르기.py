N = int(input())

arr = [int(input()) for _ in range(N)]

if N <= 2:
    print(sum(arr))

else:
    sum_max = [arr[0], arr[0]+arr[1], max(arr[0]+arr[2], arr[1]+arr[2])]

    for i in range(3, N):
        sum_max.append(max(sum_max[i-3] + arr[i-1] + arr[i], sum_max[i-2] + arr[i]))
    print(sum_max[-1])