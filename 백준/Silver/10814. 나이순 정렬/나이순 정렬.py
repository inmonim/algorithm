import sys
arr = []
for _ in range(int(input())):
    arr.append(list(sys.stdin.readline().split()))
arr.sort(key=lambda x:int(x[0]))
for i in arr:
    print(' '.join(i))