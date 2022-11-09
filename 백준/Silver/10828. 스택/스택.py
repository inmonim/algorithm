import sys

stack = []
for i in range(int(input())):
    s = sys.stdin.readline().split()
    if len(s) >= 2:
        stack.append(s[1])
    else:
        s = s[0]
        if s == 'top':
            if stack:
                print(stack[-1])
            else:
                print(-1)
        elif s == 'size':
            print(len(stack))
        elif s == 'empty':
            if stack:
                print(0)
            else:
                print(1)
        elif s == 'pop':
            if stack:
                print(stack.pop())
            else:
                print(-1)