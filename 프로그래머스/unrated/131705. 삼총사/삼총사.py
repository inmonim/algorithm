def solution(number):
    n = len(number)
    result = 0
    for i1 in range(n-2):
        for i2 in range(i1+1, n-1):
            for i3 in range(i2+1, n):
                if number[i1]+number[i2]+number[i3] == 0:
                    result += 1
    return result