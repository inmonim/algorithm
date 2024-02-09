import sys

input = sys.stdin.readline

def sol():
    N, M = map(int, input().split())
    trues = list(map(int, input().split()))
    true_p = []
    if trues[0] >= 1:
        true_p = trues[1:]
    else:
        print(M)
        return
    
    partys = [list(map(int, input().split()))[1:] for _ in range(M)]
    
    insfested = [0]*(N+1)
    for p in true_p:
        insfested[p] = 1
    
    Q = true_p
    while Q:
        p = Q.pop(0)
        
        for party in partys:
            if p in party:
                for i in party:
                    if not insfested[i]:
                        Q.append(i)
                        insfested[i] = 1
    cnt = 0
    for party in partys:
        for p in party:
            if insfested[p]:
                break
        else:
            cnt += 1
            
    print(cnt)

sol()