N = int(input())
arr = list(map(int, input().split()))

result = ['0'] * N

cnt = 0
while sum(arr) != 1001*N:
    M = min(arr)
    for i in range(len(arr)):
        if i == len(arr):
            break
        elif arr[i] == M:
            arr[i] = 1001
            result[i] = str(cnt)
            cnt += 1

print(' '.join(result))