import sys
N = int(sys.stdin.readline())
arr = sorted([int(sys.stdin.readline().strip()) for _ in range(N)])
print(*arr, sep='\n')