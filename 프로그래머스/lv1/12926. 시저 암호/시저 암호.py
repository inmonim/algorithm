def solution(s, n):
    answer = ''
    for i in s:
        if i == ' ':
            answer += i
            continue
        if ord(i) < 97:
            answer += chr((ord(i)+n-ord('A'))%26 + ord('A'))
        else:
            answer += chr((ord(i)+n-ord('a'))%26 + ord('a'))
    return answer