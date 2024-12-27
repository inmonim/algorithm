n = int(input())
x = list(map(int, input().split()))
arr = [0] * (max(x))

for i in x:
    arr[i-1] += 1

lc, rc = 0, sum(arr[1:])
ls, rs = 0, sum([abs(0 - i) * arr[0] for i in range(len(arr))])

ms = ls+rs
answer = 0
for i in range(1, len(arr)):
    if arr[i-1]:
        lc += arr[i-1]
    if arr[i]:
        rc -= arr[i]
    ls += lc
    rs -= (arr[i] + rc)
    if ms > ls+rs:
        ms = ls+rs
        answer = i

print(answer+1)