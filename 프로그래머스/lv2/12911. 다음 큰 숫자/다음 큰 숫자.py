def solution(n):
    result = 0
    target = bin(n).count('1')
    n2 = n
    while not result:
        n2 += 1
        if bin(n2).count('1') == target:
            result = n2
    return result