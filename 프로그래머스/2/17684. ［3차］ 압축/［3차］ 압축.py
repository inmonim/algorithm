def solution(msg):
    alphabet_dict = { chr(65+i) : i+1 for i in range(26)}
    d_i = 27
    last_idx = 0
    answer = []
    i = 0
    while i < len(msg):
        tmp = 0
        for j in range(i+1, len(msg)+1):
            # 있으면 last_idx에 대입, 임시 시작 인덱스 값 +1
            if alphabet_dict.get(msg[i:j]):
                last_idx = alphabet_dict[msg[i:j]]
                tmp += 1
            # 없으면 last_idx를 answer에 삽입, dictionary_index 값 1 상승
            # 시작 인덱스 값 +
            else:
                alphabet_dict[msg[i:j]] = d_i
                d_i += 1
                answer.append(last_idx)
                i += tmp
                break
        # 루프가 break없이 종료되었다는 것은 마지막 글자임을 의미, last_idx 삽입하고 알고리즘 종료
        else:
            answer.append(last_idx)
            break
    
    return answer