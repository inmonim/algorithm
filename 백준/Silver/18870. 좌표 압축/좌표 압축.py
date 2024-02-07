N = int(input())
arr = list(map(int, input().split()))
s_l = sorted(list({i:0 for i in arr}.keys()))
i_d = {s_l[i]:i for i in range(len(s_l))}
ans = [i_d[i] for i in arr]

print(' '.join(map(str, ans)))