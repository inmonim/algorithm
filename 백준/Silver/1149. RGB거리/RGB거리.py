import sys

input = sys.stdin.readline

N = int(input())
rgb = [list(map(int, input().split())) for _ in range(N)]
order1 = ((0,2,0),(0,1,0),(1,2,0),(2,1,0))
order2 = ((1,2,1),(1,0,1),(0,2,1),(2,0,1))
order3 = ((0,1,2),(1,0,2),(2,0,2),(2,1,2))

f, s, t = rgb[0]
n = 3
for x in range(1, N//2+1):
    if x == N//2 and not N%2:
        n = 2
    arr = [[f,s,t]] + rgb[x*2-1:x*2+1]
    f_l, s_l, t_l = [], [], []
    for i in range(4):
        f, s, t = 0, 0, 0
        for j in range(n):
            f += arr[j][order1[i][j]]
            s += arr[j][order2[i][j]]
            t += arr[j][order3[i][j]]
        f_l.append(f)
        s_l.append(s)
        t_l.append(t)
    f, s, t = min(f_l), min(s_l), min(t_l)  

print(min([f,s,t]))