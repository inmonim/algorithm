def solution(m, n, startX, startY, balls):
    answer = []
    for ball in balls:
        endX, endY = ball
        distance = []
        if startX - m != endX - m:
            dis1 = ((n - endY) + (n - startY)) ** 2 + abs(startX - endX) ** 2
            dis2 = (endY + startY) ** 2 + abs(startX - endX) ** 2
            distance.extend([dis1, dis2])
        elif startY > endY:
            dis = ((n - startY) + (n - endY))**2
            distance.append(dis)
        elif startY < endY:
            dis = (startY + endY) ** 2
            distance.append(dis)
            
        if startY - n != endY - n:
            dis1 = ((m - endX) + (m - startX)) ** 2 + abs(startY - endY) ** 2
            dis2 = (endX + startX) ** 2 + abs(startY - endY) ** 2
            distance.extend([dis1, dis2])
        elif startX < endX:
            dis = (startX + endX) ** 2
            distance.append(dis)
        elif startX > endX:
            dis = ((m - startX) + (m - endX)) ** 2
            distance.append(dis)
        
        answer.append(min(distance))
    
    return answer