def solution(n):
    arr = [1, 1]
    for i in range(1, n):
        arr.append(arr[-2] + arr[-1])
    return arr[-1]%1234567