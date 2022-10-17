result = 0
for _ in range(int(input())):
    T = input()
    check = set(T[0])
    stack = [T[0]]
    for i in range(1,len(T)):
        stack.append(T[i])
        if stack[-1] not in check:
            check.add(T[i])
        elif stack[-1] in check:
            if stack[-1] != stack[-2]:
                break
    else:
        result += 1
print(result)