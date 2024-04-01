import sys

input = sys.stdin.readline

r, c = map(int, input().split())

visited = [0] * 26

alp_set = set()
map_ = []
for _ in range(r):
    alpabet = input().strip()
    for i in alpabet:
        alp_set.add(i)
    map_.append(alpabet)

max_c = len(alp_set)

visited[ord(map_[0][0]) - 65] = 1

def dfs(visited, y, x, res):
    ans = res
    for dy, dx in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
        ny, nx = dy+y, dx+x
        if 0 > ny or 0 > nx or ny >= r or nx >= c:
            continue
        
        alp = ord(map_[ny][nx]) - 65
        if visited[alp] == 0:
            visited[alp] = 1
            ans = max(ans, dfs(visited, ny, nx, res+1))
            if ans == max_c:
                return max_c
            visited[alp] = 0
    
    return ans

print(dfs(visited, 0, 0, 1))