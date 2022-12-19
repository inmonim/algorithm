import sys

def sol(arr, N):
    for i in range(N*N):
        check = arr[0][0]
        if N == 3:
            for i2 in range(9):
                if check != arr[i2//N][i2%N]:
                    for i2 in range(9):
                        dic[arr[i2//N][i2%N]] += 1
                    break
            else:
                dic[check] += 1
            return
        
        if arr[i//N][i%N] != check:
            next_arr = []
            for Y in range(3):
                w = Y*(N//3)
                for x in range(3):
                    tmp = []
                    for y in range(N//3):
                        tmp.append(arr[w+y][x*(N//3):(x+1)*(N//3)])
                    next_arr.append(tmp)
            
            for i in range(9):
                sol(next_arr[i], N//3)
            return
    else:
        dic[check] += 1
        return

N = int(input())

dic = {-1:0, 0:0, 1:0}
arr = [list(map(int, input().split())) for _ in range(N)]

sol(arr, N)

print(*dic.values(), sep='\n')