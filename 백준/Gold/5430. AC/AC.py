import sys

input = sys.stdin.readline

for t in range(int(input())):
    func = input()
    l = int(input())
    arr = []
    string = ''
    for s in input().strip()[1:]:
        if s.isdigit():
            string += s
        else:
            if string != '':
                arr.append(string)
            string = ''
    
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
            del arr[p]
    else:
        if p == -1:
            arr = arr[::-1]
        print(f"[{','.join(arr)}]")