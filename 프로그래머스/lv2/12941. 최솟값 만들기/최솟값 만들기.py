def solution(A,B):
    answer, A, B = 0, sorted(A), sorted(B, reverse=True)
    for i in range(len(A)):
        answer += A[i] * B[i]
    return answer