def solution(brown, yellow):
    N = brown + yellow

    xy = [[N,1]]
    for i in range(int(N**0.5), N):
        if N%i == 0:
            xy.append([i, N//i])

    for wh in xy:
        if wh[0] < wh[1]:
            continue
        if (wh[0]-2) * (wh[1]-2) == yellow:
            return wh
    