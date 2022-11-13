L = int(input())
h= [list(map(int, input().split()))+[i] for i in range(L)]

R = [0]*L
for i in range(L):
    G = 1
    for j in range(L):
        if h[i][0] < h[j][0] and h[i][1] < h[j][1]:
            G += 1
    R[h[i][2]] = G

print(*R)