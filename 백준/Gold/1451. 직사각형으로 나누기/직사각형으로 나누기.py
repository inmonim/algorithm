import sys

input = sys.stdin.readline

def sol():
    n, m = map(int, input().split())
    mat = [list(map(int, list(input().strip()))) for _ in range(n)]
    
    mx = 0
    if m >= 3:
        for i in range(m-2):
            for ii in range(i+1, m-1):
                for iii in range(ii+1, m):
                    a = b = c = 0
                    for y in range(n):
                        a += sum(mat[y][i:ii])
                        b += sum(mat[y][ii:iii])
                        c += sum(mat[y][iii:])
                    mx = max(mx, a * b * c)
    
    if n >= 3:
        for i in range(n-2):
            for ii in range(i+1, n-1):
                for iii in range(ii+1, n):
                    a = b = c = 0
                    a += sum([sum(mat[x]) for x in range(i, ii)])
                    b += sum([sum(mat[x]) for x in range(ii, iii)])
                    c += sum([sum(mat[x]) for x in range(iii, n)])
                    mx = max(mx, a * b * c)
    
    if n >= 2 and m >= 2:
        for y in range(1, n):
            for x in range(1, m):
                a = sum([sum(mat_y[:x]) for mat_y in mat[:y]])
                b = sum([sum(mat_y[x:]) for mat_y in mat[:y]])
                c = sum([sum(mat_y[:x]) for mat_y in mat[y:]])
                d = sum([sum(mat_y[x:]) for mat_y in mat[y:]])
                mx = max(mx, max([(a+b) * c * d, (a+c) * b * d, a * b * (c+d), a * c * (b+d)]))
    
    print(mx)

sol()