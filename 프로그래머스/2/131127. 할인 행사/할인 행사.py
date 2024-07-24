def solution(want, number, discount):
    want_dict_org = {want[i]:number[i] for i in range(len(want))}
    
    c = 0
    for j in range(len(discount) - 9):
        want_dict = want_dict_org.copy()
        
        for i in range(10):
            item = discount[j+i]
            if want_dict.get(item):
                want_dict[item] = want_dict[item] - 1
        swd = sum(want_dict.values())
        if not swd:
            c += 1

    return c