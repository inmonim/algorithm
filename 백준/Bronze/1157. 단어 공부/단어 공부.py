l = list(input())

D = {i.upper():0 for i in l}

for i in l:
    D[i.upper()] += 1
m = max(D.values())
R = []

for k,v in D.items():
    if v == m:
        R.append(k)

if len(set(R)) == 1:
    print(R[0])
else:
    print('?')