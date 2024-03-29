def solution(number, limit, power):
    
    ans = 0
    for i in range(1, number+1):
        ad = 0
        
        for j in range(1, int(i**0.5)+1):
            
            if not i%j:
                ad += 2
                
                if i//j == j:
                    ad -= 1
            
            if ad > limit:
                ad = power
                break
                
        ans += ad
                
    return ans