def solution(a, b):
    arr = list(zip(a,b))
    result = []

    while arr:
        next = []
        comp_job = 0
        for i in range(len(arr)):
            x = arr.pop(0)
            x2 = x[0] + x[1]
            if (i == 0 or not next) and x2 >= 100:
                comp_job +=1 
            else:
                next.append((x2, x[1]))
        arr = next
        if comp_job:
            result.append(comp_job)
    
    return result