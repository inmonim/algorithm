n = int(input())
ta = list(map(int, input().split(" ")))
t, p = list(map(int, input().split(" ")))

ty = 0
for tx in ta:
    if not tx:
        continue
    ty += (tx-1)//t + 1

print(ty)
print(f"{n//p} {n%p}")