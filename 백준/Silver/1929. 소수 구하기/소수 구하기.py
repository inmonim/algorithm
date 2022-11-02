s,e = map(int, input().split())

if s < 2:
    s = 2

filt = []

for i in range(2, int(e**0.5)+1):
    for j in range(2, i):
        if i%j == 0:
            break
    else:
        filt.append(i)

for i in filt:
    if i >= s:
        print(i)

for i in range(s, e+1):
    for j in filt:
        if i % j == 0:
            break
    else:
        print(i)