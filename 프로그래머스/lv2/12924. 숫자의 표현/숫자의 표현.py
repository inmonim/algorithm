def solution(n):
    result = 1
    for i in range(1, n//2+1):
        tmp = 0
        while tmp <= n:
            if tmp == n:
                result += 1
            tmp += i
            i += 1
    return result