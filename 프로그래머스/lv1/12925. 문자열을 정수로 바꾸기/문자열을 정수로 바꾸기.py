def solution(s):
    return int(s) if s[0].isdigit() else (int(s[1:]) if s[0] == '+' else -int(s[1:]))