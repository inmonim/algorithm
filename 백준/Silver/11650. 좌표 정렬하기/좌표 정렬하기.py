import sys

N = int(sys.stdin.readline())
arr = []
for i in range(N):
    arr.append(list(map(int, sys.stdin.readline().split())))

arr.sort(key=lambda x:x[1])
arr.sort(key=lambda x:x[0])

for i in arr:
    print(*i, sep=' ')