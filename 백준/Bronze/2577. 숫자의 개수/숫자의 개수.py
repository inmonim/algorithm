a = 1
for i in range(3):
    n = int(input())
    a = a * n
a = str(a)
for i in range(10):
    print(a.count(str(i)))