N = int(input())

a = 1
for i in range(1, N+1):
    a = a * i
a = str(a)[::-1]

for i in range(len(a)):
    if a[i] != '0':
        break

print(i)