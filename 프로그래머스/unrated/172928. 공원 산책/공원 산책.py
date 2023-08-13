def solution(park, routes):
    w, h = len(park[0]), len(park)
    
    for y in range(h):
        for x in range(w):
            if park[y][x] == 'S':
                now = [y, x]
                break
    
    for r in routes:
        op, n = r.split()
        n = int(n)
        if op == 'E':
            if now[1] + n >= w:
                continue
                
            for i in range(1, n+1):
                if park[now[0]][now[1] + i] == 'X':
                    break
            else:
                now = [now[0], now[1]+n]
        elif op == 'W':
            if now[1] - n < 0:
                continue
            
            for i in range(1, n+1):
                if park[now[0]][now[1] - i] == 'X':
                    break
            else:
                now = [now[0], now[1]-n]
        elif op == 'S':
            if now[0] + n >= h:
                continue
            for i in range(1, n+1):
                if park[now[0]+i][now[1]] == 'X':
                    break
            else:
                now = [now[0]+n, now[1]]
        elif op == 'N':
            if now[0] -n < 0:
                continue
            for i in range(1, n+1):
                if park[now[0]-i][now[1]] == 'X':
                    break
            else:
                now = [now[0]-n, now[1]]
                
    answer = now
    return answer