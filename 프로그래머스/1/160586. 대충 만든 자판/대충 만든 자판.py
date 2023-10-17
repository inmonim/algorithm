def solution(keymap, targets):
    key_map = {}
    for km in keymap:
        for i in range(len(km)):
            if key_map.get(km[i]):
                if key_map[km[i]] > i+1: key_map[km[i]] = i+1
            else:
                key_map[km[i]] = i+1
    
    answer = []
    
    for t in targets:
        try:
            answer.append(sum([key_map[i] for i in t]))
        except:
            answer.append(-1)
    return answer