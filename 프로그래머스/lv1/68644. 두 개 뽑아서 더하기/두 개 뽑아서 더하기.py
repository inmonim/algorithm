def solution(num):
    result = set()
    for i in range(len(num)-1):
        for j in range(i+1, len(num)):
            result.add(num[i]+num[j])
    return sorted(list(result))