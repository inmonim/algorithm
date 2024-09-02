import sys

input = sys.stdin.readline
N, C = map(int, input().split())

arr = sorted([int(input()) for _ in range(N)])

min_range = 1
max_range = arr[-1] - arr[0]

result = 0

while min_range <= max_range:
    threshold = (min_range + max_range)//2
    emplace = 1
    
    now = arr[0]
    
    for i in range(1, len(arr)):
        if arr[i] >= threshold + now:
            emplace += 1
            now = arr[i]
            if emplace >= C:
                min_range = threshold + 1
                result = threshold
                break
    else:
        if emplace < C:
            max_range = threshold - 1

print(result)