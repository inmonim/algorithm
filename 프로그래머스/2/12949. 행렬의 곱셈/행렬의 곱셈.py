def solution(arr1, arr2):
    arr = [[0] * len(arr2[0]) for _ in range(len(arr1))]

    for i in range(len(arr1)):
        for j in range(len(arr2[0])):
            x = 0
            for k in range(len(arr1[0])):
                x += arr1[i][k] * arr2[k][j]
            arr[i][j] = x

    return arr