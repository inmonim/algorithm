N = int(input())
arr = list(map(int, input().split()))
B, C = map(int, input().split())

result = 0
for i in range(N):
    n = arr[i] - B
    result += 1
    if n <= 0:
        continue
    result = result + n//C if n % C == 0 else result + n//C +1

print(result)