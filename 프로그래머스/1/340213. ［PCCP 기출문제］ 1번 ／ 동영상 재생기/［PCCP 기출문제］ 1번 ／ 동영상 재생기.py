def solution(video_len, pos, op_start, op_end, commands):
    답 = ''
    def 초변환(문자):
        분, 초 = map(int, 문자.split(':'))
        return 분*60 + 초
    
    끝시간 = 초변환(video_len)
    시간 = 초변환(pos)
    시작시작시간 = 초변환(op_start)
    시작끝시간 = 초변환(op_end)
    
    def 시작확인(시간):
        if 시작시작시간 <= 시간 and 시간 <= 시작끝시간:
            return 시작끝시간
        return 시간
        
    def 임계확인(시간):
        if 0 > 시간:
            return 0
        elif 끝시간 < 시간:
            return 끝시간
        return 시간
    
    def 행동(시간, 행위):
        if 행위 == "next":
            시간 += 10
        elif 행위 == "prev":
            시간 -= 10
        시간 = 임계확인(시간)
        시간 = 시작확인(시간)
        return 시간
    
    시간 = 임계확인(시간)
    시간 = 시작확인(시간)
    for 행위 in commands:
        시간 = 행동(시간, 행위)
    
    답 = f"{str(시간//60).rjust(2, '0')}:{str(시간%60).rjust(2, '0')}"
    
    return 답