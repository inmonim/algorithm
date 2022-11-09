n,k = map(int, input().split())
if n == k:
    print(1)
elif k == 0:
    print(1)
else:
    n1, n2 = n, n-k
    for i in range(2, n1):
        n1 = n1*i
    for i in range(2, k):
        k = k*i
    for i in range(2, n2):
        n2 = n2*i
    print(n1//(k*n2))