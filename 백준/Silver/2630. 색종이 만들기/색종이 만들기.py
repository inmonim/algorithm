import sys

input = sys.stdin.readline

N = int(input())

paper = [list(map(int, input().split())) for _ in range(N)]

b, w = 0, 0

def graph(n, m, paper):
    global b, w
    for dx, dy in [(0, 0), (0, n), (n, 0), (n, n)]:
        check = 0
        for y in range(dy, dy+n):
            check += sum(paper[y][dx : dx+n])
        if check == m:
            b += 1
        elif check == 0:
            w += 1
        else:
            graph(n//2, m//4, [paper[y][dx : dx+n] for y in range(dy, dy+n)])

n = N//2
m = N**2 // 4

f = sum([sum(p) for p in paper])

if f == N**2:
    print(f'{0}\n{1}')
elif not f:
    print(f'{1}\n{0}')
else:
    graph(n, m, paper)
    print(f'{w}\n{b}')