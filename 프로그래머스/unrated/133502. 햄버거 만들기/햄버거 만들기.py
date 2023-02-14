def solution(ingredient):
    cnt = 0
    stack = []
    for i in range(len(ingredient)):
        stack.append(ingredient[i])
        if len(stack) < 4:
            continue
        if stack[-4] == 1 and stack[-3] == 2 and stack[-2] == 3 and stack[-1] == 1:
            for i in range(4):
                stack.pop()
            cnt += 1
    return cnt
