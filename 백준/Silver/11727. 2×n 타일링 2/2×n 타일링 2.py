n = int(input())
a = [0, 1]
for i in range(1, n):
    if i%2 == 1:
        a.append(a[i]*2 +1)
    else:
        a.append(a[i]*2 -1)
print(a.pop()%10007)