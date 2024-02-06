n = int(input())

m = int(n ** 0.5)

cnt = 4
for i in range(m, 0, -1):
    n2 = n
    if i**2 <= n2:
        n2 -= i**2
        if n2:
            for i2 in range(i, 0, -1):
                n3 = n2
                if i2**2 <= n3:
                    n3 -= i2**2
                    if n3:
                        for i3 in range(i2, 0, -1):
                            n4 = n3
                            if i3**2 <= n4:
                                n4 -= i3**2
                                if n4:
                                    cnt = min(cnt, 4)
                                else:
                                    cnt = min(cnt, 3)
                    else:
                        cnt = min(cnt, 2)
        else:
            cnt = min(cnt, 1)

print(cnt)