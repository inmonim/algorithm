N = int(input())
n = 1
cnt = 0
while True:
    n += cnt*6
    if n >= N:
        print(cnt+1)
        break
    cnt += 1