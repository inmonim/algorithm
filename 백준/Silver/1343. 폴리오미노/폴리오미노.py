arr = list(input()) + ['.']

stack = []
cnt = 0
result = ''
while arr:
    if arr[0] == 'X':
        cnt += 1
        arr.pop(0)
    else:
        if cnt % 2 == 1:
            result = -1
            break
        for i in range(cnt//4):
            result += 'AAAA'
        if cnt % 4 == 2:
            result += 'BB'
        cnt = 0
        result += arr.pop(0)
if result != -1:
    result = result[:-1]

print(result)