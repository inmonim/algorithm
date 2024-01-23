import sys

input = sys.stdin.readline

for t in range(int(input())):
    
    M, N, x, y = map(int, input().split())
        
    n = x
    while n <= M*N:
        if n%N == y or (N == y and n%N == 0):
            print(n)
            break
        n += M
        
    else:
        print(-1)