import sys

# 유클리드 호제법 활용한 최대 공약수
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


# 최소 공배수
def lcm(a, b):
    return (a * b) // gcd(a, b)


T = int(input())
for _ in range(T):
    M, N, x, y = map(int, input().split())
		# 두개를 계속 더해가는 것이 아니라 x가 3일때, y가 9인경우를 찾으면됨
    # 즉, 모든 경우가 아닌 연도가 3,13,23,33,43... (x + i*M) 일때 y가 9인 경우가 답
    # 최대범위 // M번만 순회하며 확인하면 됨
    # ny가 0인 경우는 없으므로 나머지가 0일때는 ny가 N이 되어야함
    max_year = lcm(M, N)
    for i in range(max_year // M):
        year = x + i * M
        ny = N if year % N == 0 else year % N
        if ny == y:
            print(year)
            break
    else:
        print(-1)