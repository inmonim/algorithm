import sys
stack = []
for _ in range(int(sys.stdin.readline())):
    if (i := sys.stdin.readline().strip()) == '0':
        stack.pop()
    else:
        stack.append(int(i))
print(sum(stack))