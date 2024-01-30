import sys
input = sys.stdin.readline

N, arr = int(input()), sorted(list(map(int, input().split())))
a = 0
for i in range(N):
    a += sum(arr[0:i+1])
print(a)