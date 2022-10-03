def solution(board, moves):
    buket = []
    result = 0
    for i in moves:
        for j in board:
            if j[i-1] != 0:
                buket.append(j[i-1])
                j[i-1] = 0
                break
        if len(buket) >=2:
            if buket[-2] == buket[-1]:
                buket = buket[:-2]
                result += 2
    return result