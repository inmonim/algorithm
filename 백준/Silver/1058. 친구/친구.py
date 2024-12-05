N = int(input())

tmp = [input().strip() for _ in range(N)]

arr = [0] * N
for i in range(N):
    cur_arr = []
    for j in range(N):
        if i == j:
            continue
        
        if tmp[i][j] == "Y":
            cur_arr.append(j)

    arr[i] = cur_arr

answer = []
for i in range(N):
    friends = set()
    
    for ii in arr[i]:
        if ii != i:
            friends.add(ii)
            for iii in arr[ii]:
                if iii != i:
                    friends.add(iii)
    
    answer.append(len(friends))
    
print(max(answer))