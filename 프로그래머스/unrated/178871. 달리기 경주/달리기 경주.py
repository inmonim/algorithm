def solution(players, callings):
    rank = {}
    for i in range(len(players)):
        rank[players[i]] = i
    
    for c in callings:
        over_rank = rank[c]
        players[over_rank-1], players[over_rank] = players[over_rank], players[over_rank-1]
        rank[c] -= 1
        rank[players[over_rank]] += 1
        
        
    return players