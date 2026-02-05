from math import comb
n = int(input())
answer = 0
for i in range(n):
    k = (n-i)
    if (i + k*5) % 3 == 0:
        answer += comb(n-1, i)

print(answer % 1_000_000_007)