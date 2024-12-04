def solution(n, stations, w):
    answer = 0
    
    nn = []
    
    if 1 < (stations[0] - w):
        nn.append((1, stations[0] - w-1))
    
    for i in range(len(stations)-1):
        
        a, b = stations[i], stations[i+1]
        
        if a + w < b - w:
            nn.append((a+w+1, b-w-1))
            
    if stations[-1] + w < n:
        nn.append((stations[-1]+w+1, n))
    
    for x in nn:
        print(x)
        answer += (((x[1] - x[0]) + 1) // (w*2+1))
        answer += 1 if (((x[1] - x[0]) + 1) % (w*2+1)) else 0
    
    return answer