for _ in range(int(input())):
    N = int(input())
    Z = [1,0]
    O = [0,1]
    for i in range(1, N):
        Z.append(Z[-2] + Z[-1])
        O.append(O[-2] + O[-1])
    if N == 0:
        print('1 0')
    elif N == 1:
        print('0 1')
    else:
        print(f'{Z[-1]} {O[-1]}')