import sys

input = sys.stdin.readline

n = input()
arr = sorted(list(map(int, input().split(" "))))
top = arr[0]
if top != 1:
    print(1)
else:
    for i in arr[1:]:
        if top+1 < i:
            print(top+1)
            break
        top += i
    else:
        print(top+1)