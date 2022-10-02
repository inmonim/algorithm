def solution(nums):
    result = 0
    nums.sort()
    for i in range(len(nums)):
        F = nums[i]
        for j in range(len(nums))[i+1:]:
            S = nums[j]
            for k in range(len(nums))[j+1:]:
                T = nums[k]
                NC = 0
                for N in range(2, F+S+T):
                    if (F+S+T)%N == 0:
                        break
                else:
                    result +=1
    return result