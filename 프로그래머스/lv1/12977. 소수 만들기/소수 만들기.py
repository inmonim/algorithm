def solution(nums):
    N, tmp, result = len(nums), set(), 0
    for i1 in range(N-2):
        for i2 in range(i1+1, N-1):
            for i3 in range(i2+1, N):
                num = (nums[i1] + nums[i2] + nums[i3])
                for i in range(2, num):
                    if num%i == 0:
                        break
                else:
                    result += 1
    return result