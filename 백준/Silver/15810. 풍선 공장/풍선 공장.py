import sys
from array import array
n, m = map(int, input().split())

arr = list(map(int, input().split()))
arr = array('I', arr)

mm = m * min(arr)
t, b = mm, 1

while b <= t:
    c = (b+t)//2
    cur = sum(c//i for i in arr)
    
    if cur >= m:
        t = c - 1
    else:
        b = c + 1

print(b)