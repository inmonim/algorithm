N, M = map(int, input().split())
arr = [[0]*100 for _ in range(100)]

for T in range(N):
    x1,y1,x2,y2 = map(int, input().split())
    for y in range(y1-1, y2):
        for x in range(x1-1, x2):
            arr[y][x] += 1

result = 0
for i in arr:
    for j in i:
        if j > M:
            result += 1

print(result)