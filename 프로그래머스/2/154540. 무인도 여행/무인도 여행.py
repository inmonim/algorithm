def solution(maps):
    islands = []
    visited = {}
    Y, X = len(maps), len(maps[0])
    
    def bfs(y, x):
        days = 0
        Q = [(y, x)]
        visited[(y, x)] = 1
        while Q:
            y, x = Q.pop(0)
            days += int(maps[y][x])
            for dy, dx in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
                ny, nx = y + dy, x + dx
                if ny >= Y or ny < 0 or nx >= X or nx < 0:
                    continue
                if maps[ny][nx].isdigit() and not visited.get((ny, nx)):
                    Q.append((ny, nx))
                    visited[(ny, nx)] = 1
        return days

    for y in range(Y):
        for x in range(X):
            if maps[y][x].isdigit() and not visited.get((y, x)):
                islands.append(bfs(y, x))
                
    if not islands:
        islands = [-1]
    islands.sort()
        
    return islands