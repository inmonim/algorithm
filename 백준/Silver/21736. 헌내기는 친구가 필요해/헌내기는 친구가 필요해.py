import sys
from collections import deque

input = sys.stdin.readline

Y, X = map(int, input().split())

mat = []
p = 0

for y in range(Y):
    arr = input().strip()
    if not p and 'I' in arr:
        now = [y, arr.index('I')]
        p = 1
    mat.append(arr)

visited = [[0]*X for _ in range(Y)]

cnt = 0
Q = deque()
Q.append(now)
while Q:
    y, x = Q.popleft()
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