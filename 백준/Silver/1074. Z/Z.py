N, y, x = map(int, input().split(' '))

L = 2**N
l = L//2

answer = 0

while l != 0:
    N -= 1
    score = 4**(N)
    
    if l <= y:
        if l <= x:
            answer += score * 3
            x = x - l
        elif l > x:
            answer += score * 2
        y = y - l
        
    elif l > y:
        if l <= x:
            answer += score
            x = x - l
    
    l = l//2

print(answer)