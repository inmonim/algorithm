def solution(babbling):
    cnt = 0
    for i in babbling:
        idx = 0
        P = 5
        while idx < len(i):
            if P != 0 and i[idx:idx+2] == "ye":
                idx += 2
                P = 0
            elif P != 1 and i[idx:idx+2] == "ma": 
                idx += 2
                P = 1
            elif P != 2 and i[idx:idx+3] == "woo":
                idx += 3
                P = 2
            elif P != 3 and i[idx:idx+3] == "aya":
                idx += 3
                P = 3
            else:
                break

            if idx == len(i):
                cnt += 1
    return cnt