N, y, x = map(int, input().split())

L = 2**N
l = L//2

answer = 0

while l != 0:
    if y >= l:
        if x >= l:
            answer += 3*(l**2)
            y -= l
            x -= l
        else:
            answer += 2*(l**2)
            y -= l
    else:
        if x >= l:
            answer += (l**2)
            x -= l
        else:
            answer += 0
    l = l//2

print(answer)