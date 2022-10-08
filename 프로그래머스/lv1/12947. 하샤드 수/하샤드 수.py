def solution(x):
    a = 0
    for i in list(str(x)):
        a += int(i)
    return x % a == 0