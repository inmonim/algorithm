for T in range(int(input())):
    ps = list(input())
    stack = []
    while ps:
        if ps[-1] == ')':
            stack.append(ps.pop())
        elif ps[-1] == '(' and stack and stack[-1] == ')':
            ps.pop()
            stack.pop()
        else:
            print('NO')
            break
    else:
        if stack:
            print('NO')
        else:
            print('YES')