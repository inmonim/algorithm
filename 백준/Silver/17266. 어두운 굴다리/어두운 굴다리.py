import math
n, m = int(input()), int(input())
arr = list(map(int, input().split()))
ns = [math.ceil((arr[i] - arr[i-1]) / 2) for i in range(1, m)] + [0 + arr[0], n - arr[-1]]
print(max(ns))