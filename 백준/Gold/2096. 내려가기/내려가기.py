import sys

input = sys.stdin.readline

n = int(input())

n_l = list(map(int, input().split()))
dp_min = n_l
dp_max = n_l
for _ in range(n-1):
    n_l = list(map(int, input().split()))
    dp_min = [min(dp_min[0], dp_min[1]) + n_l[0],
                min(dp_min) + n_l[1],
                min(dp_min[1], dp_min[2]) + n_l[2]]
    dp_max = [max(dp_max[0], dp_max[1]) + n_l[0],
                max(dp_max) + n_l[1],
                max(dp_max[1], dp_max[2]) + n_l[2]]
print(max(dp_max), min(dp_min))