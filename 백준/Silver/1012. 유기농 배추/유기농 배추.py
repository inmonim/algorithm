for T in range(int(input())):
    M,N,K = map(int, input().split())
    A = 0
    arr = [[0]*M for _ in range(N)]
    for i in range(K):
        x,y = map(int, input().split())
        arr[y][x] = 1
        
    for y in range(N):
        for x in range(M):
            stack = []
            if arr[y][x] == 1:
                stack = [(y,x)]
                A += 1
            while stack:
                sy, sx = stack.pop()
                arr[y][x] = 0
                for dy,dx in [(-1,0),(0,1),(1,0),(0,-1)]:
                    ny, nx = dy+sy, dx+sx
                    if 0 <= ny < N and 0<= nx < M:
                        if arr[ny][nx] == 1:
                            arr[ny][nx] = 0
                            stack.append((ny,nx))
                            
    print(A)