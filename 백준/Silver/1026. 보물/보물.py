N = int(input())
A = sorted(list(map(int, input().split())))
B = list(map(int, input().split()))
result = 0
for i in range(N):
    mb = max(B)
    result += mb * A[i]
    B.pop(B.index(mb))
print(result)