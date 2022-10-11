def solution(s):
    s = s[1:-1]

    arr = []

    for i in s:
        if i == '{':
            tmp = []
            tmp2 = ''
        elif i == ',':
            tmp.append(int(tmp2))
            tmp2 = ''
        elif i == '}':
            tmp.append(int(tmp2))
            arr.append(tmp)
            tmp = []
        else:
            tmp2 += i

    arr.sort(key=lambda x:len(x))

    result = [arr[0][0]]

    for i in range(len(arr)-1):
        for j in arr[i+1]:
            if j not in arr[i]:
                result.append(j)
    
    return result