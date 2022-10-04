def solution(s):
    if len(s)%2 == 1:
        return 0
    
    stack = [s[0]]
    for i in s[1:]:
        stack.append(i)
        while len(stack) >= 2 and stack[-2] == stack[-1]:
            stack.pop()
            stack.pop()
    
    return 0 if stack else 1