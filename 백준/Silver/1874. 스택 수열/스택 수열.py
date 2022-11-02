N = int(input())
result = []
stack = []
cnt = 1

for i in range(N):
    num = int(input())

    while cnt <= num:
        stack.append(cnt)
        result.append('+')
        cnt += 1
    
    if stack[-1] == num:
        stack.pop()
        result.append('-')
        
    else:
        result = ['NO']
        break
        
for i in result:
    print(i)