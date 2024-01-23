import sys

input = sys.stdin.readline

X, Z, Y = map(int, input().split())

target = 0
day = []
mat = []
cnt = 0
for i in range(Y):
    arr = []
    for j in range(Z):
        arr.append(list(map(int, input().split())))
        for h in range(X):
            t = arr[-1][h]
            if t == 1:
                day.append([i, j, h])
            elif t == 0:
                target += 1
    mat.append(arr)
    
while day:
    tom = []
    
    for y, z, x in day:
        for dy, dz, dx in ([0,1,0], [0,-1,0], [0,0,1], [0,0,-1], [1, 0, 0], [-1, 0, 0]):
            ny, nz, nx = y+dy, z+dz, x+dx
            
            if 0 <= ny < Y and 0 <= nx < X and 0 <= nz < Z:
                if mat[ny][nz][nx] == 0:
                    mat[ny][nz][nx] = 1
                    tom.append([ny, nz, nx])
                    target -= 1
    if len(tom) >= 1:
        cnt += 1
    day = tom

cnt = -1 if target > 0 else cnt
print(cnt)