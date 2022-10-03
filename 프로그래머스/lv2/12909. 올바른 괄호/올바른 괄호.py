def solution(s):
    s = list(s)
    stack = []
    while s:
        stack.append(s.pop())
        if len(stack) >= 2 and stack[-1] == '(' and stack[-2] == ')':
            stack.pop()
            stack.pop()
    return False if stack else True