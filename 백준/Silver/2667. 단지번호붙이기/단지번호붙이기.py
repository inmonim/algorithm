import sys

input = sys.stdin.readline

N = int(input())

jido = [list(map(int, input().strip())) for _ in range(N)]

visited = jido.copy()

houses = []

def bfs(Q : list):
    house = 0
    while Q:
        y, x = Q.pop(0)
        house += 1
        for dy, dx in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
            ny, nx = y+dy, x+dx
            if ny >= 0 and N > ny and nx >= 0 and N > nx:
                if jido[ny][nx] and visited[ny][nx]:
                    visited[ny][nx] = 0
                    Q.append((ny, nx))
    return house

cnt = 0
for y in range(N):
    for x in range(N):
        if jido[y][x] and visited[y][x]:
            visited[y][x] = 0
            cnt += 1
            
            Q = [(y, x)]
            house = bfs(Q)
            houses.append(house)

print(cnt, *sorted(houses), sep='\n')