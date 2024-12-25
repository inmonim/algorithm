arr = list(map(int, input().split()))
mat = [{} for _ in range(8)]
first = {i : 0 for i in range(8)}
second, third = first.copy(), first.copy()
s = 0
for i in range(8):
    for ii in range(i, 7):
        mat[i][ii+1] = arr[s + (ii-i)]/100
    
    ts = 0
    for ij in range(i):
        mat[i][ij] = (100 - arr[ts+(i-(ij+1))])/100
        ts = ts + (7-ij)
    s = s + (7-i)

for i in range(4):
    first[2*i] = mat[2*i][2*i+1]
    first[2*i+1] = mat[2*i+1][2*i]

for i in range(4):
    if i in [0, 2]:
        second[2*i] = first[2*i] * (first[2*(i+1)] * mat[2*i][2*(i+1)] + first[2*(i+1)+1] * mat[2*i][2*(i+1)+1])
        second[2*i+1] = first[2*i+1] * (first[2*(i+1)] * mat[2*i+1][2*(i+1)] + first[2*(i+1)+1] * mat[2*i+1][2*(i+1)+1])
    else:
        second[2*i] = first[2*i] * (first[2*(i-1)] * mat[2*i][2*(i-1)] + first[2*(i-1)+1] * mat[2*i][2*(i-1)+1])
        second[2*i+1] = first[2*i+1] * (first[2*(i-1)] * mat[2*i+1][2*(i-1)] + first[2*(i-1)+1] * mat[2*i+1][2*(i-1)+1])

for i in range(8):
    se = [4, 8] if i < 4 else [0, 4]
    
    for ii in range(se[0], se[1]):
        third[i] += second[i] * second[ii] * mat[i][ii]
    third[i] = round(third[i], 9)

print(*third.values())