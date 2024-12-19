import math

def integer_sqrt(n):
    # 이분 탐색으로 제곱근 찾기
    low, high = 0, n
    while low <= high:
        mid = (low + high) // 2
        if mid * mid <= n < (mid + 1) * (mid + 1):
            return mid
        elif mid * mid < n:
            low = mid + 1
        else:
            high = mid - 1

# 입력 받기
n = int(input().strip())  # 최대 800자리 수
print(integer_sqrt(n))