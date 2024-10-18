def solution(wallet, bill):
    answer = 0
    x, y = bill
    while True:
        
        if wallet[0] < x or wallet[1] < y:
            if wallet[0] < y or wallet[1] < x:
                answer += 1
                if x > y:
                    x = x//2
                else:
                    y = y//2
            else:
                 break   
        else:
            break
    return answer