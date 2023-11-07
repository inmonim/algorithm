def solution(board):
    O = 0
    X = 0
    o_ver = [0,0,0]
    x_ver = [0,0,0]
    x_w = 0
    o_w = 0
    for y in range(3):
        x_hor = 0
        o_hor = 0
        for x in range(3):
            if board[y][x] == 'O':
                o_ver[x] += 1
                o_hor += 1
                O += 1
            elif board[y][x] == 'X':
                x_ver[x] += 1
                x_hor += 1
                X += 1
                
        if x_hor == 3:
            x_w += 1
        elif o_hor == 3:
            o_w += 1

    o_l_dia = [0,0,0]
    o_r_dia = [0,0,0]
    x_l_dia = [0,0,0]
    x_r_dia = [0,0,0]
    for y in range(3):
        for x in range(3):
            if y == x:
                if board[y][x] == 'O':
                    o_l_dia[x] = 1
                elif board[y][x] == 'X':
                    x_l_dia[x] = 1
            if y+x == 2:
                if board[y][x] == 'O':
                    o_r_dia[x] = 1
                elif board[y][x] == 'X':
                    x_r_dia[x] = 1

    for i in range(3):
        if o_ver[i] == 3:
            o_w += 1
        if x_ver[i] == 3:
            x_w += 1
                    
    if sum(o_l_dia) == 3:
        o_w += 1
    elif sum(x_l_dia) == 3:
        x_w += 1
    if sum(o_r_dia) == 3:
        o_w += 1
    elif sum(x_r_dia) == 3:
        x_w += 1
    
    ans = 1
    if X > O or O > X+1 or X > 4 or O > 5:
        ans = 0
    elif (x_w and o_w) or (o_w and X >= O) or (x_w and O > X):
        ans = 0
    
    
                
    return ans