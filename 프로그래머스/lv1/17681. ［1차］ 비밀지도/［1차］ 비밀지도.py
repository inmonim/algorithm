def solution(n, arr1, arr2):
    M = ['' for _ in range(n)]
    for i in range(n):
        b_a1 = bin(arr1[i])[2:].rjust(n,'0')
        b_a2 = bin(arr2[i])[2:].rjust(n,'0')
        for j in range(n):
            if b_a1[j] == '1' or b_a2[j] == '1':
                M[i] += '#'
            else:
                M[i] += ' '
    return M