def solution(arr):
    n = arr.pop()
    n2 = n
    while True:
        for i in arr:
            if n2 % i != 0:
                n2 += n
                break
        else:
            return n2