def find_minimum_width(first_gear, second_gear):
    len_first = len(first_gear)
    len_second = len(second_gear)
    
    # 최소 너비를 현재 두 문자열 길이 합으로 초기화
    min_width = len_first + len_second

    # 첫 번째 기어를 왼쪽으로 이동하면서 체크
    for offset in range(-len_second + 1, len_first):
        valid = True
        for i in range(len_second):
            pos = offset + i
            if 0 <= pos < len_first:  # 겹치는 경우만 체크
                if first_gear[pos] == '2' and second_gear[i] == '2':
                    valid = False
                    break
        if valid:
            # 현재 너비 계산: 왼쪽 시작과 오른쪽 끝 간격
            left = min(0, offset)
            right = max(len_first, offset + len_second)
            min_width = min(min_width, right - left)

    return min_width

# 입력 처리
first_gear = input().strip()
second_gear = input().strip()

# 결과 출력
print(find_minimum_width(first_gear, second_gear))