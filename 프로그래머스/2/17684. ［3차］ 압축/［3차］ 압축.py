def solution(msg):
    alphabet_dict = { chr(65+i) : i+1 for i in range(26)}
    d_i = 27
    last_idx = 0
    answer = []
    i = 0
    while i < len(msg):
        tmp = 0
        for j in range(i+1, len(msg)+1):
            if alphabet_dict.get(msg[i:j]):
                last_idx = alphabet_dict[msg[i:j]]
                tmp += 1
            else:
                alphabet_dict[msg[i:j]] = d_i
                d_i += 1
                answer.append(last_idx)
                i += tmp
                break
        else:
            answer.append(last_idx)
            break
    
    return answer