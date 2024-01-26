import sys
from collections import deque

input = sys.stdin.readline

for _ in range(int(input())):
    
    n, T = map(int, input().split())
    
    check = set([n])
    Q = deque()
    
    Q.append(('', n))
    while Q:
        
        h, n = Q.popleft()
        
        if n == T:
            print(h)

        n1 = (n*2) % 10000
        if n1 not in check:
            h1 = h+'D'
            check.add(n1)
            Q.append((h1, n1))
            
        n2 = (n-1) % 10000
        if n2 not in check:
            h2 = h+'S'
            check.add(n2)
            Q.append((h2, n2))
            
        n3 = ((n%1000)*10+(n//1000))
        if n3 not in check:
            h3 = h+'L'
            check.add(n3)
            Q.append((h3, n3))

        n4 = ((n%10)*1000)+(n//10)
        if n4 not in check:
            h4 = h+'R'
            check.add(n4)
            Q.append((h4, n4))

