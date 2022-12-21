d={}
for i in range(10):
    d[int(input())%42] = 1
print(len(d.keys()))