dic = {}

for i in input():
    i = i.upper()
    if dic.get(i):
        dic[i] += 1
    else:
        dic[i] = 1

M = max(dic.values())

R = []
for k,v in dic.items():
    if v == M:
        R.append(k)

if len(R) > 1:
    print('?')
else:
    print(R[0])