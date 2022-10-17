N = int(input())
T = 1
while N:
    student = [input() for _ in range(N)]
    sin = sorted([int(input().split()[0]) for _ in range(N*2-1)]+[100])
    for i in range(N):
        if sin[i*2] != sin[i*2+1]:
            print(f'{T} {student[i]}')
            T += 1
            break
    N = int(input())