def min_k_dp(A):
    N = len(A)
    dp = [float('inf')] * N
    dp[0] = 0

    for i in range(1, N):
        for j in range(i):
            cost = (i - j) * (1 + abs(A[i] - A[j]))
            dp[i] = min(dp[i], max(dp[j], cost))

    return dp[N - 1]

# 입력 처리
N = int(input())
A = list(map(int, input().split()))
print(min_k_dp(A))  # 출력: 2 (예제와 동일)