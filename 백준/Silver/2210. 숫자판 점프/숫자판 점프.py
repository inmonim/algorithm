mat = [input().strip().split() for _ in range(5)]

num_set = set()

for y in range(5):
    for x in range(5):
        q = [(mat[y][x], y, x)]
        while q:
            cur, py, px = q.pop()
            for dy, dx in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                ny, nx = py+dy, px+dx
                
                if 0 <= ny < 5 and 0 <= nx < 5:
                    if len(cur) == 5:
                        num_set.add(cur + mat[ny][nx])
                    else:
                        q.append((cur + mat[ny][nx], ny, nx))

print(len(num_set))