def solution(mats, park):
    mats = sorted(mats)[::-1]
    y_l, x_l = len(park), len(park[0])

    def check(y, x, m):
        for yy in range(y, y+m):
            for xx in range(x, x+m):
                if park[yy][xx] != "-1":
                    return 0
        return 1
    
    def mat(m):
        for y in range(y_l-m+1):
            for x in range(x_l-m+1):
                if park[y][x] == "-1":
                    res = check(y, x, m)
                    if res:
                        return m
    
    answer = 0
    for m in mats:
        answer = mat(m)
        if answer:
            return answer
    else:
        return -1