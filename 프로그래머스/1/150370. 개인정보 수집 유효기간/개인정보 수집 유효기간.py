def solution(today, terms, privacies):
    terms = {k.split(' ')[0]:int(k.split(' ')[1]) for k in terms}
    ty, tm, td = map(int, today.split('.'))
    cnt = 1
    answer = []
    for privacy in privacies:
        begin, term = privacy.split(' ')
        
        by, bm, bd = map(int, begin.split('.'))

        term = terms[term]
        d = term * 28 - 1
        nd = (bd + d) % 28 if (bd + d) % 28 else 28
        nm = (((bd + d) // 28 ) + bm) % 12 if (((bd + d) // 28 ) + bm) % 12 else 12
        ny = ((((bd + d) // 28 ) + bm) // 12) + by
        if nm == 12: ny -= 1
        if nd == 28: nm -= 1
        
        
        print(ny, nm, nd)
        
        if ty - ny > 0:
            answer.append(cnt)
            cnt +=1
            continue
        
        if ty - ny == 0:
            if tm - nm > 0:
                answer.append(cnt)
                cnt +=1
                continue
            elif tm - nm == 0:
                if td - nd > 0:
                    answer.append(cnt)
                    cnt += 1
                    continue
        cnt += 1

    return answer