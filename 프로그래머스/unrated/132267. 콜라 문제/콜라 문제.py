def solution(a, b, n):
    result = 0
    stack = n
    while stack:
        stack -= a
        stack += b
        result += b
        if stack < a:
            break
    return result