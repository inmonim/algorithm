def solution(n):
    answer = [-1]
    stack = [n[-1]]
    for i in range(len(n)-2, -1, -1):
        while True:
            if n[i] < stack[-1]:
                answer.append(stack[-1])
                stack.append(n[i])
                break
            else:
                stack.pop()
                if not stack:
                    answer.append(-1)
                    stack.append(n[i])
                    break
    return answer[::-1]