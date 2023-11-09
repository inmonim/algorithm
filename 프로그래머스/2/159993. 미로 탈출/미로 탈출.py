def bfs(maps, next_step, target, visit, cnt):
    max_y, max_x = len(maps), len(maps[0])
    next_step = [next_step]
    while next_step:
        starts = next_step
        next_step = []
        for yx in starts:
            y, x = yx
            for dy, dx in ((0, 1), (1, 0), (-1, 0), (0,-1)):
                ny, nx = y+dy, x+dx
                if (ny >= 0 and ny < max_y and nx >= 0 and nx < max_x and maps[ny][nx] != "X"):
                    
                    if visit[ny][nx] != '-':
                        next_step.append([ny,nx])
                        visit[ny][nx] = '-'

                    if maps[ny][nx] == target and maps[ny][nx] == 'L':
                        visit = [[0] * len(maps[0]) for _ in range(len(maps))]
                        return bfs(maps, [ny, nx], 'E', visit, cnt + 1)
                    
                    elif maps[ny][nx] == target and maps[ny][nx] == 'E':
                        return cnt + 1
        cnt += 1
    else:
        return -1

def solution(maps):
    for y in range(len(maps)):
        for x in range(len(maps[0])):
            if maps[y][x] == "S":
                start = [y, x]
    
    visited = [[0] * len(maps[0]) for _ in range(len(maps))]
    answer = bfs(maps, start, 'L', visited, 0)

    return answer