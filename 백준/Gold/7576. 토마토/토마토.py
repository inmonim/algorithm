import sys

input = sys.stdin.readline

X, Y = map(int, input().split())

now, arr, t, cnt = [], [], 0, 0

for y in range(Y):
    arr.append(input().split())
    for x in range(X):
        if arr[y][x] == '0':
            t += 1
        if arr[y][x] == '1':
            now.append((y, x))

while now:
    tom = []
    
    for y, x in now:
        
        for dy, dx in ((0, 1), (1, 0), (-1, 0), (0, -1)):
            ny, nx = y + dy, x + dx
            if 0 <= ny < Y and 0 <= nx < X:
                if arr[ny][nx] == '0':
                    tom.append((ny, nx))
                    arr[ny][nx] = 'x'
                    t -= 1
    
    if tom:
        cnt += 1
    now = tom

cnt = -1 if t else cnt

print(cnt)