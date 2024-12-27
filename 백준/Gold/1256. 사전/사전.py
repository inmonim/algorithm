from math import comb

def find_kth_string(N, M, K):
    # 전체 조합이 K보다 작다면 -1 반환
    total_combinations = comb(N + M, N)
    if K > total_combinations:
        return -1

    result = []
    while N > 0 and M > 0:
        # 'a'를 선택했을 때 가능한 조합의 수
        a_combinations = comb(N + M - 1, N - 1)
        if K <= a_combinations:
            # K가 'a'로 시작하는 범위에 속하면 'a'를 선택
            result.append('a')
            N -= 1
        else:
            # 그렇지 않으면 'z'를 선택하고 K값을 감소
            result.append('z')
            M -= 1
            K -= a_combinations

    # 남은 'a' 또는 'z'를 결과에 추가
    result.extend(['a'] * N)
    result.extend(['z'] * M)

    return ''.join(result)

# 입력 예제
N,M,K = map(int, input().split())
print(find_kth_string(N, M, K))