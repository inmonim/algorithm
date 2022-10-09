def solution(citations):
    citations.sort(reverse=True)
    L = len(citations)
    for i in range(L):
        if citations[i] <= i+1:
            break
    else:
        return L
    return i