import sys

input = sys.stdin.readline

l = [(list(map(int, input().split()))) for i in range(int(input()))]

l.sort(key=lambda x:[x[1], x[0]])

ep = 0
a = 0

for s, e in l:
    if ep <= s:
        a += 1
        ep = e

print(a)