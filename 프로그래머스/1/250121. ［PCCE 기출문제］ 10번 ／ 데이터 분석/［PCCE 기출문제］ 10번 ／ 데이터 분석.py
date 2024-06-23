def solution(data, ext, val_ext, sort_by):
    
    c = {'code' : 0, 'date':1, 'maximum':2, 'remain':3}
    answer = [d for d in data if d[c[ext]] < val_ext]
    
    answer.sort(key=lambda x: x[c[sort_by]])
    return answer