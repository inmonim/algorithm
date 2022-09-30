def solution(s):
    return True if s.upper().count('P')-s.upper().count('Y') == 0 else False