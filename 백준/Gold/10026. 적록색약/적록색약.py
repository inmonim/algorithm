import sys

input = sys.stdin.readline

N = int(input())

no_arr = [input().strip() for _ in range(N)]
rg_arr = [i.replace('G','R') for i in no_arr]

no_visited = [[0]*N for _ in range(N)]
rg_visited = [[0]*N for _ in range(N)]

def bfs(Q, arr, visited):
    
    y, x = Q[0]
    if visited[y][x] == 1:
        return 0
    color = arr[y][x]
    
    while Q:
        y,x = Q.pop()
        for dy, dx in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            ny, nx = dy+y, dx+x
            if 0 <= ny < N and 0 <= nx < N:
                if visited[ny][nx] == 0 and arr[ny][nx] == color:
                    Q.append((ny, nx))
                    visited[ny][nx] = 1
    return 1

no_cnt, rg_cnt = 0, 0
for y in range(N):
    for x in range(N):
        no_cnt += bfs([[y, x]], no_arr, no_visited)
        rg_cnt += bfs([[y, x]], rg_arr, rg_visited)

print(no_cnt, rg_cnt)