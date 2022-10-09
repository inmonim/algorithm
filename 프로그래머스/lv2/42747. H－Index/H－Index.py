def solution(citations):
    citations.sort()
    L = len(citations)
    for i in range(len(citations), 0, -1):
        if citations[i-1] <= L - i:
            break
    else:
        return L
    return L-i