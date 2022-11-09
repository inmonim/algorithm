import sys

dq = []
for i in range(int(input())):
    s = sys.stdin.readline().split()
    if len(s) >= 2:
        if s[0] == 'push_back':
            dq.append(s[1])
        else:
            dq.insert(0, s[1])
    else:
        s = s[0]
        if s == 'pop_front':
            if dq:
                print(dq.pop(0))
            else:
                print(-1)
        elif s == 'pop_back':
            if dq:
                print(dq.pop())
            else:
                print(-1)
        elif s == 'size':
            print(len(dq))
        elif s == 'empty':
            if dq:
                print(0)
            else:
                print(1)
        elif s == 'front':
            if dq:
                print(dq[0])
            else:
                print(-1)
        elif s == 'back':
            if dq:
                print(dq[-1])
            else:
                print(-1)