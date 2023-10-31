def solution(board):
    for y in range(len(board)):
        for x in range(len(board[0])):
            if board[y][x] == "R":
                now = [y,x]
    max_y, max_x = len(board), len(board[0])
    
    visit = [[0] * max_x for i in range(max_y)]
    
    cnt = 0
    goal = 0
    next_move = [now]
    
    while next_move:
        now_move = next_move
        print(now_move)
        next_move = []
        cnt += 1
        for now in now_move:
            for dy, dx in ((0, 1), (1, 0), (-1, 0), (0, -1)):
                y, x = now
                is_move = 0
                
                while True:
                    ny = y + dy
                    nx = x + dx
                    if ny >= max_y or ny < 0 or nx >= max_x or nx < 0:
                        break
                    elif board[ny][nx] == 'D':
                        break
                    else:
                        y = ny
                        x = nx
                        is_move = 1
                        
                if board[y][x] == 'G':
                    goal = 1
                    break
                    
                elif is_move:
                    if visit[y][x] == 0:
                        visit[y][x] = 1
                        next_move.append([y,x])
            if goal:
                break
        if goal:
            break
    if goal == 0:
        cnt = -1
    
    return cnt