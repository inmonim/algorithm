for _ in range(int(input())):
    n, s = input().split()
    r = []
    for x in s:
        r.append(x*int(n))
    print(''.join(r))