from collections import deque

def solution(maps):
    w, h = len(maps[0]), len(maps)
    y, x = 0, 0
    q = deque([(y, x, 1)])
    visits = [[0]*w for _ in range(h)]
    visits[0][0] = 1
    al = []
    
    while q:
        y, x, a = q.popleft()
        for dy, dx in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            ny, nx = y+dy, x+dx
            if ny >= 0 and ny < h and nx >= 0 and nx < w and maps[ny][nx] == 1 and visits[ny][nx] == 0:
                if ny == h-1 and nx == w-1:
                    al.append(a+1)
                q.append((ny, nx, a+1))
                visits[ny][nx] = 1
    return min(al) if al else -1