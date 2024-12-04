def solution(stones, k):
    answer = 0
    
    cnt_idxs = {}
    for i in range(len(stones)):
        if cnt_idxs.get(stones[i]):
            cnt_idxs[stones[i]].append(i)
        else:
            cnt_idxs[stones[i]] = [i]
    
    cnt_list = sorted(list(cnt_idxs.keys()))
    
    dead_set = set()
    for c in cnt_list:
        
        idxs = cnt_idxs[c]
        
        dead_set.update(idxs)
        
        if len(dead_set) < k:
            continue
        
        for i in idxs:
            i_p = i + 1
            i_m = i - 1
            tmp_cnt = 1
            while i_p in dead_set:
                tmp_cnt += 1
                i_p += 1
            while i_m in dead_set:
                tmp_cnt += 1
                i_m -= 1
            
            if tmp_cnt >= k:
                answer = c
                return answer
        
    return answer