import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(n)]
answer = -1
cnt = 0
while answer == -1:
    visit = [[0]*m for _ in range(n)]
    q = deque()
    for y in range(n):
        if q:
            break
        for x in range(m):
            if mat[y][x] > 0:
                q.append((y, x))
                visit[y][x] = 1
                break
    else:
        answer = 0
        break
    while q:
        y, x = q.pop()
        for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ny, nx = y+dy, x+dx
            if 0 <= ny < n and 0 <= nx < m:
                if visit[ny][nx] == 0 and mat[ny][nx] > 0:
                    visit[ny][nx] = 1
                    q.append((ny, nx))
                elif mat[ny][nx] == -1:
                    mat[ny][nx] = 0
    for y in range(n):
        for x in range(m):
            if mat[y][x] <= 0:
                continue
            if visit[y][x] != 1:
                answer = cnt
                break
            for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                ny, nx = y+dy, x+dx
                if 0 <= ny < n and 0 <= nx < m:
                    if not mat[ny][nx]:
                        mat[y][x] -= 1
                        if not mat[y][x]:
                            mat[y][x] = -1
                            break

    cnt += 1
print(answer)