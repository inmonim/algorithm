import sys

for T in range(int(input())):
    k, n = int(sys.stdin.readline()), int(sys.stdin.readline())
    arr = [[0] * n for _ in range(k)]
    arr[0] = [i for i in range(1, n+1)]
    for y in range(1, k):
        for x in range(1, n+1):
            arr[y][x-1] = sum(arr[y-1][0:x])
    print(sum(arr[-1]))