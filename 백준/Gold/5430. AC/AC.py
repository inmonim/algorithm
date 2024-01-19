import sys


def Sol():
    input = sys.stdin.readline

    T = int(input())

    for _ in range(T):
        commands = [*map(len, input().rstrip().replace("RR", "").split("R"))]
        is_flip = (len(commands) + 1) % 2

        n = int(input())
        if n == 0:
            input()
            arr = []
        else:
            arr = input().strip("[]\n").split(",")

        front = sum(commands[0::2])
        try:
            back = sum(commands[1::2])
        except:
            back = 0


        if front + back > n:
            print("error")
            continue
        else:
            arr = arr[front:(n-back)]

        print(f'[{",".join(reversed(arr) if is_flip else arr)}]')

Sol()