def solution(n, left, right):
    a = []
    
    rl, rr = left % n, right % n
    s, e = left // n+1, right // n+1
    
    for i in range(s, e+1):
        arr = [i]*(i-1) + [ii for ii in range(i, n+1)]
        a.extend(arr)
    answer = a[rl:((e-s)*n)+rr+1]
            
    return answer