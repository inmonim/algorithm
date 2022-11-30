N,M,B = map(int, input().split())

answer = [0,0]

Map = []
for i in range(N):
    Map.append(list(map(int, input().split())))

dic = {}

for i in Map:
    for j in i:
        if dic.get(int(j)):
            dic[int(j)] += 1
        else:
            dic[int(j)] = 1

bottom = min(dic.keys())
bottom_val = dic[bottom]

top = max(dic.keys())
top_val = dic[top] * 2

answer[1] = top

while len(dic) != 1:
    bottom = min(dic.keys())
    bottom_val = dic[bottom]

    top = max(dic.keys())
    top_val = dic[top] * 2

    answer[1] = top

    if bottom_val <= top_val and dic[bottom] <= B:
        answer[0] += bottom_val
        if dic.get(bottom+1):
            dic[bottom+1] += dic[bottom]
        else:
            dic[bottom+1] = dic[bottom]
        B -= dic[bottom]
        del dic[bottom]
        
    else:
        answer[0] += top_val
        if dic.get(top-1):
            dic[top-1] += dic[top]
        else:
            dic[top-1] = dic[top]
        B += dic[top]
        del dic[top]
        answer[1] = max(dic.keys())

    if len(dic) == 1:
        break

print(*answer)