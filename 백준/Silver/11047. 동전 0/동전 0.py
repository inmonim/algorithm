N, t = map(int, input().split())
worth = [int(input()) for _ in range(N)]
worth.reverse()

i = 0
cnt = 0
while t:
    n = worth[i]
    if t//n:
       cnt += t//n
       t %= n
    i += 1
print(cnt)