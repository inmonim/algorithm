def solution(n):
    n_r = n**0.5
    prime = []
    for i in range(2, int(n_r)+1):
        if n_r%i==0:
            break
        else:
            prime.append(i)
    tmp = set()    
    for pr in prime:
        x = 2
        while pr*x <= n:
            tmp.add(pr*x)
            x += 1
    return n - len(tmp) - 1