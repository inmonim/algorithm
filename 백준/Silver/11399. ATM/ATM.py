import sys
input = sys.stdin.readline

N, arr = int(input()), sorted(list(map(int, input().split())))
print(sum([sum(arr[0:i+1]) for i in range(N)]))