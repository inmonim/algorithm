import sys
from array import array
input = sys.stdin.readline

n, m = map(int, input().split())

arr = array('i', map(int, input().split()))

time_dict = {}

for i in arr:
    if i not in time_dict:
        time_dict[i] = 1
    else:
        time_dict[i] += 1

mm = m * min(time_dict.keys())
t, b = mm, 1

while b <= t:
    c = (b + t)//2
    cur = sum([(c//k)*v for k,v in time_dict.items()])
    
    if cur >= m:
        t = c - 1
    else:
        b = c + 1

print(b)