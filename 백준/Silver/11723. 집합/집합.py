from array import array
import sys

input = sys.stdin.readline

from array import array

S = array('i', [0]*21)
S1 = [i for i in range(21)]

for _ in range(int(input())):
    op = input().split()
    if len(op) == 1:
        if op[0][0] == 'a':
            S = array('i', S1)
        else:
            S = [0]*21
        continue
    o, n = op
    n = int(n)
    if o[0] == 'a':
        S[n] = 1
    elif o[0] == 'r':
        S[n] = 0
    elif o[0] == 't':
        S[n] = 0 if S[n] else 1
    else:
        if S[n]:
            print(1)
        else:
            print(0)