def solution(s):

    arr = s[2:-2].split('},{')

    arr2 = []

    for i in arr:
        arr2.append(i.split(','))
    arr2.sort(key=len)

    result = [int(arr2[0][0])]

    for i in range(len(arr2)-1):
        for j in arr2[i+1]:
            if j not in arr2[i]:
                result.append(int(j))
    
    return result