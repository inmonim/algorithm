for t in range(1, int(input())+1):
    N = int(input())
    arr = [[0] * N for i in range(N)]
    x, y = 0,0
    cnt = 1
    while cnt < N*N+1:
        while cnt < N*N+1:
            if x == N-1:
                arr[y][x] = str(cnt)
                y += 1
                cnt+=1
                break
            elif arr[y][x+1] == 0:
                arr[y][x] = str(cnt)
                x += 1
                cnt += 1
            else:
                arr[y][x] = str(cnt)
                y += 1
                cnt += 1
                break

        while cnt < N*N+1:
            if y == N-1:
                arr[y][x] = str(cnt)
                cnt += 1
                x -= 1
                break
            elif arr[y+1][x] == 0:
                arr[y][x] = str(cnt)
                y += 1
                cnt += 1
            else:
                arr[y][x] = str(cnt)
                x -= 1
                cnt += 1
                break
        while cnt < N*N+1:
            if x == 0:
                arr[y][x] = str(cnt)
                cnt += 1
                y -= 1
                break
            elif arr[y][x-1] == 0:
                arr[y][x] = str(cnt)
                x -= 1
                cnt += 1
            else:
                arr[y][x] = str(cnt)
                y -= 1
                cnt += 1
                break
        while cnt < N*N+1:
            if arr[y-1][x] == 0:
                arr[y][x] = str(cnt)
                y -= 1
                cnt += 1
            else:
                arr[y][x] = str(cnt)
                x += 1
                cnt += 1
                break
    print(f'#{t}')
    for i in range(N):
        print(' '.join(arr[i]))