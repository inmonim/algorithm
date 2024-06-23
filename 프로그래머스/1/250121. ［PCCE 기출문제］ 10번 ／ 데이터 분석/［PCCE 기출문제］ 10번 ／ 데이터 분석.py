def solution(data, ext, val_ext, sort_by):
    from datetime import datetime
    def change_date_type(string):
        return datetime.strptime(string, '%Y%m%d')
    
    c = {'code' : 0, 'date':1, 'maximum':2, 'remain':3}
    answer = []
    
    if ext == 'date':
        val_ext = change_date_type(str(val_ext))
        for d in data:
            x = d[1]
            x = change_date_type(str(x))
            if x < val_ext:
                answer.append(d)
    else:
        for d in data:
            if d[c[ext]] < val_ext:
                answer.append(d)
    
    answer.sort(key=lambda x: x[c[sort_by]])
    return answer