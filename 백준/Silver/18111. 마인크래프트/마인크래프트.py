N,M,B = map(int, input().split())
A = [0,0]
Map = []
for i in range(N):
    Map.append(list(map(int, input().split())))
D = {}
for i in Map:
    for j in i:
        if D.get(int(j)):
            D[int(j)] += 1
        else:
            D[int(j)] = 1
t = max(D.keys())
A[1] = t
while len(D) != 1:
    b = min(D.keys())
    b_v = D[b]
    t = max(D.keys())
    t_v = D[t] * 2
    if b_v <= t_v and D[b] <= B:
        A[0] += b_v
        if D.get(b+1):
            D[b+1] += D[b]
        else:
            D[b+1] = D[b]
        B -= D[b]
        del D[b]
    else:
        A[0] += t_v
        if D.get(t-1):
            D[t-1] += D[t]
        else:
            D[t-1] = D[t]
        B += D[t]
        del D[t]
        A[1] = max(D.keys())
print(*A)