import sys

input = sys.stdin.readline

for t in range(int(input())):
    func = input()
    l = int(input())
    arr = []
    arr_string = input().strip()
    string = ''
    if l:
        arr = arr_string[1:-1].split(',')
    
    p = 0
    for f in func:
        if f == 'R':
            if p == 0:
                p = -1
            elif p == -1:
                p = 0
        elif f == 'D':
            if not arr:
                print('error')
                break
            arr.pop(p)
    else:
        if p == -1:
            arr.reverse()
        print(f"[{','.join(arr)}]")