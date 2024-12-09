n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())))

def bs(b, t, target):
    while b <= t:
        mid = (b+t) // 2
        if arr[mid] > target:
            t = mid - 1
        elif arr[mid] < target:
            b = mid + 1
        else:
            return 1
    return 0

i, j = 0, n-1

def two_point(i, j):
    while i < j:
        a, c = arr[i], arr[j]
        if a + c == m:
            return 1
        elif a + c > m:
            j -= 1
        else:
            b = m - (a + c)
            if b not in [a, c] and bs(i, j, b):
                return 1
            i += 1
            
    return 0

if m in arr:
    print(1)
else:
    print(two_point(i, j))