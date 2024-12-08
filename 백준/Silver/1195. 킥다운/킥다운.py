a, b = list(map(int, list(input().strip()))), list(map(int, list(input().strip())))

answer = len(a) + len(b)

for i in range(-len(b), len(a)-1, 1):
    
    for ii in range(len(b)):
        
        if (len(a) > i+ii >= 0) and (a[i+ii] + b[ii] > 3):
            break
    else:
        tmp = 0
        if i < 0:
            tmp = max(len(a), i + len(b)) - i
        else:
            tmp = max(len(a), i + len(b))
        answer = min(answer, tmp)

print(answer)