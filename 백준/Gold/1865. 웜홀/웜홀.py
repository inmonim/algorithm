import sys

input = sys.stdin.readline

TC = int(input())

for _ in range(TC):
    N, M, W = map(int, input().split())
    
    node = [[] for _ in range(N+1)]
    
    for i in range(M+W):
        S, E, T = map(int, input().split())
        if i >= M:
            T = -T
        else:
            node[E].append((T, S))
        node[S].append((T, E))
        
    dist = [M*T*2] * (N+1)
    
    p = 'NO'
    for i in range(N):
        
        for j in range(1, N+1):
            
            for n_node in node[j]:
                nv, ni = n_node
                rv = nv + dist[j]
                if dist[ni] > rv:
                    dist[ni] = rv
                    if i == N-1:
                        p = 'YES'

    print(p)