q = []
R = []
for _ in range(int(input())):
    i = input().split()
    if len(i) == 2:
        q.append(i[1])
    else:
        i = i[0]
        if i == 'pop':
            if q:
                R.append(q[0])
                q=q[1:]
            else:
                R.append(-1)
        elif i == 'front':
            if q:
                R.append(q[0])
            else:
                R.append(-1)
        elif i == 'back':
            if q:
                R.append(q[-1])
            else:
                R.append(-1)
        elif i == 'size':
            R.append(len(q))
        elif i == 'empty':
            if q:
                R.append(0)
            else:
                R.append(1)
print(*R, sep='\n')