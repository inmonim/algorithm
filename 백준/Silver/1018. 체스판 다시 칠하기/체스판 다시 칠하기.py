Y, X = map(int, input().split())

arr = [input() for _ in range(Y)]

TF = 0
result = 64

for sy in range(Y-7):
    for sx in range(X-7):
        for i in range(2):
            if i == 0:
                check = 'W'
            else:
                check = 'B'
            tmp = 0
            for y in range(8):
                if y > 0:
                    if check == 'W':
                        check = 'B'
                    else:
                        check = 'W'
                for x in range(8):
                    if check == arr[sy+y][sx+x]:
                        tmp += 1
                        
                    if check == 'W':
                        check = 'B'
                    else:
                        check = 'W'
                    if result < tmp:
                        TF = 1
                        break
                if TF == 1:
                    TF = 0
                    break
            else:
                result = tmp

print(result)