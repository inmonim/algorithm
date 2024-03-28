import sys
S = sys.stdin.readline()

stack = []
result = ''

for i in S:
    if i.isalpha():
        result += i
    else:
        if not stack:
            stack.append(i)
        elif i == '(':
            stack.append(i)
        elif i in '/*':
            while stack and stack[-1] in '/*':
                result += stack.pop()
            stack.append(i)
        elif i in '+-':
            while stack and stack[-1] != '(':
                result += stack.pop()
            stack.append(i)
        elif i == ')':
            while stack and stack[-1] != '(':
                result += stack.pop()
            stack.pop()

while stack:
    result += stack.pop()

print(result)