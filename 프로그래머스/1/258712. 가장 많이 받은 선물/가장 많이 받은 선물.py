def solution(friends, gifts):
    fd = {friend:{friend:0 for friend in friends} for friend in friends}
    gift_score = {friend:0 for friend in friends}
    answer = {friend:0 for friend in friends}
    for gift in gifts:
        s, d = gift.split(' ')
        fd[s][d] += 1
        gift_score[s] += 1
        gift_score[d] -= 1
    
    for f in friends:
        f_send_gift = fd[f]
        
        for k, v in f_send_gift.items():
            # 선물 횟수 비교
            # k가 f에게 보낸 선물 < f가 k에게 보낸 선물
            if fd[k][f] < v:
                answer[f] += 1
            # k가 f에게 보낸 선물 > f가 k에게 보낸 선물
            elif fd[k][f] > v:
                answer[k] += 1
            # k가 f에게 보낸 선물 = f가 k에게 보낸 선물
            else:
                # gift_score 비교
                if gift_score[k] > gift_score[f]:
                    answer[k] += 1
                elif gift_score[k] < gift_score[f]:
                    answer[f] += 1

    return max(answer.values())//2