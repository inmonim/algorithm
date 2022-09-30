def solution(s):
    arr = sorted(map(int, s.split()))
    return str(arr[0])+' '+str(arr[-1])