def solution(elements):
    
    s = set()
    for i in range(1, len(elements)+1):
        for ii in range(len(elements)):
            a = sum(elements[ii:ii+i])
            if ii+i >= len(elements):
                a += sum(elements[0 : ii+i-len(elements)])
            s.add(a)
    
    return len(s)