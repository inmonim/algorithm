n = int(input())
num = list(map(int, input().split()))
a = float('inf')
for i in range(n):
    y = max(num) * num[i]
    if not sum(y % num[j] for j in range(n)):
        a = min(a, y)
print(a)