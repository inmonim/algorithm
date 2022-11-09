for _ in range(int(input())):
    s = input()
    x = 0
    R = 0
    for i in s:
        if i == 'O':
            x += 1
            R += x
        else:
            x = 0
    print(R)