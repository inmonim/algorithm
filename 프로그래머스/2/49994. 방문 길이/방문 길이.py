d = {
    'U': (-1, 0),
    'L': (0, -1),
    'R': (0, 1),
    'D': (1, 0)
}

def solution(dirs):
    xv, yv = dict(), dict()
    y, x = 0, 0
    a = 0
    ds = list(dirs)[::-1]
    while ds:
        o = ds.pop()
        dy, dx, = d[o]
        ny, nx = y-dy, x-dx
        if -5 <= ny and ny <= 5 and -5 <= nx and nx <= 5:
            if o in ['D', 'U']:
                g = f"{min([ny, y])}{max([ny, y])}{x}"
                if not yv.get(g):
                    yv[g] = 1
                    a += 1
            else:
                g = f"{min([nx, x])}{max([nx, x])}{y}"
                if not xv.get(g):
                    xv[g] = 1
                    a += 1
            y, x = ny, nx

    return a