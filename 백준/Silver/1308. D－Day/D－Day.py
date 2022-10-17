import datetime as dt
Y,M,D = map(int, input().split())
dY,dM,dD = map(int, input().split())

R = dt.datetime(dY,dM,dD) - dt.datetime(Y,M,D)
A = 1 if D > dD else 0
B = 1 if M > dM-A else 0
if dY-Y-B >= 1000:
    print('gg')
else:
    print(f'D-{R.days}')