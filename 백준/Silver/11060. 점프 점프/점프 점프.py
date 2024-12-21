n = int(input())
arr = list(map(int, input().split()))
dp = [0] * n

def func():
    for i in range(n):
        for ii in range(i+1, i+1+arr[i]):
            if ii >= n:
                return max(dp)
            if not dp[ii] or dp[i] + 1 < dp[ii]:
                if i > 0 and dp[i] == 0:
                    return -1
                dp[ii] = dp[i] + 1

if n == 1:
    print(0)
else:
    print(func())