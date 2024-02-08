import sys

input = sys.stdin.readline

Y, X = map(int, input().split())

mat = [input().strip() for _ in range(Y)]
visited = [[0]*X for _ in range(Y)]

now = []
for y in range(Y):
    for x in range(X):
        if mat[y][x] == 'I':
            now = [y, x]
            break

cnt = 0
Q = [now]
while Q:
    y, x = Q.pop(0)
    for dy, dx in ((0, 1), (1, 0), (-1, 0), (0, -1)):
        ny, nx = dy + y, dx + x
        if 0 <= ny < Y and 0 <= nx < X:
            t = mat[ny][nx]
            if visited[ny][nx]:
                continue
            if t == 'O':
                Q.append([ny,nx])
            elif t == 'P':
                Q.append([ny,nx])
                cnt += 1
            visited[ny][nx] = 1
cnt = cnt if cnt else 'TT'

print(cnt)