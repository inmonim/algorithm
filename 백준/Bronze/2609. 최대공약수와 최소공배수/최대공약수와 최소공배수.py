A,B=map(int, input().split())
m,M = min(A,B), max(A,B)
gcd, gcf = 0, 0
for i in range(m, 0, -1):
    if m%i == 0 and M%i == 0:
        gcd = i
        break
for i in range(1, M+1):
    if (m*i)% M == 0:
        gcf = (m*i)
        break
print(f'{gcd}\n{gcf}')