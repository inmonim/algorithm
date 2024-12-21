n = int(input())
arr = list(map(int, input().split()))

stack = set()
stack.add((0, arr[0]))
answer = 0
f = 1 if len(arr) == 1 else 0
while stack and not f:
    answer += 1
    cur_stack = set()
    for start_idx, able_range in stack:
        for able_idx in range(1, able_range+1):
            target_idx = start_idx + able_idx
            if target_idx >= n-1:
                f = 1
                break
            cur_stack.add((target_idx, arr[target_idx]))
    stack = cur_stack
if f:
    print(answer)
else:
    print(-1)