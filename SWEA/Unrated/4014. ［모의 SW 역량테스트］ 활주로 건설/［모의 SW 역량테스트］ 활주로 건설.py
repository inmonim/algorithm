for TC in range(1, int(input())+1):
    N, X = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    arr2 = arr[:]
    arr2 = list(map(list, zip(*arr2)))
    for i in arr2:
        arr.append(i)
    
    result = 0

    for y in range(N*2):
        pre = arr[y][0]
        used = [0]*N
        for i in range(1,N):
            if pre == arr[y][i]:
                pre = arr[y][i]

            elif pre+1 == arr[y][i]:
                if i < X:
                    break
                elif sum(used[i-X:i])==0 and sum(arr[y][i-X:i])+(X*1) == arr[y][i]*X:
                    for j in range(i-X, i):
                        used[j] = 1
                    pre = arr[y][i]
                else:
                    break

            elif pre-1 == arr[y][i]:
                if i+X > N:
                    break
                elif sum(used[i:i+X])==0 and sum([1 for j in range(1, X) if arr[y][i+j] == arr[y][i]]) == X-1:
                    for j in range(i, i+X):
                        used[j] = 1
                    pre = arr[y][i]
                else:
                    break
            else:
                break
        else:
            result += 1
    
    print(f'#{TC} {result}')