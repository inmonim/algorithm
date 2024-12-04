def solution(n, stations, w):
    answer = 0
    nn = []
    
    # 시작점부터 첫 기지국까지 빈 공간이 있는지
    if 1 < (stations[0] - w):
        nn.append((1, stations[0]-w-1))
    
    # 첫 기지국 부터 마지막 기지국 사이의 빈공간 찾기
    for i in range(len(stations)-1):
        a, b = stations[i], stations[i+1]
        
        if a + w + 1 < b - w:
            nn.append((a+w+1, b-w-1))
    
    # 마지막 기지국 부터 끝까지 빈공간 있는지
    if stations[-1] + w < n:
        nn.append((stations[-1]+w+1, n))
    
    # 전파 도달 거리
    length = w*2 + 1
    
    # 조각난 빈공간들을 순회
    for x in nn:

        lose_range = (x[1] - x[0]) + 1
        
        # 최소한의 기지국 수
        answer += lose_range // length
        # 닿지 않는 남은 거리가 있는 경우 +1
        answer += 1 if lose_range % length else 0
    
    return answer