idx, n = 0,0
for i in range(9):
    x = int(input())
    if x > n:
        idx = i+1
        n = x
print(n)
print(idx)