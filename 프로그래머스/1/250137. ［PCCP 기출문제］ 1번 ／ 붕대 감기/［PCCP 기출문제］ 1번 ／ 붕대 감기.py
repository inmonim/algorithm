def solution(엄, 준, 식):
    
    어, 떻, 게 = 엄
    
    ㅋ = 준
    
    이 = 식[-1][0]
    름 = 0
    냐 = 0
    
    사, 람 = 식.pop(0)
    while 이 > 름:
        
        름 += 1
        
        if 름 == 사:
            
            준 -= 람
            냐 = 0
            if 준 <= 0:
                준 = -1
                break
            if 식:
                사, 람 = 식.pop(0)
        
        else:
            
            냐 += 1
        
            if 냐 == 어:
                if ㅋ > 준:
                    준 += 게
                    if ㅋ < 준:
                        준 = ㅋ
                냐 = 0

            if ㅋ > 준:
                준 += 떻
                if ㅋ < 준:
                    준 = ㅋ
    
    return 준