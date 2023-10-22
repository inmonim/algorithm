def solution(food):
    s = ''
    for i in range(1, len(food)):
        m = food[i]//2
        s += str(i) * m
    
    s2 = s[::-1]
    a = s + '0' + s2
           
    return a