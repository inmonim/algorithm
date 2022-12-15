import sys

N, M, V = map(int, input().split())

node = [[] for _ in range(N+1)]
for i in range(M):
    s,e = map(int, sys.stdin.readline().split())
    node[s].append(e)
    node[e].append(s)
    
for i in range(N+1):
    node[i] = sorted(node[i], reverse=True)

# dfs
stack = node[V].copy()
dfs_ans = str(V)
dfs_vis = {V:1}

while stack:
    next_node = stack.pop()
    if dfs_vis.get(next_node):
        continue
    else:
        dfs_ans += ' '+str(next_node)
        dfs_vis[next_node] = 1
        stack.extend(node[next_node])
print(dfs_ans)

for i in range(N+1):
    node[i] = node[i][::-1]

# bfs
Q = node[V].copy()
bfs_ans = str(V)
bfs_vis = {V:1}
while Q:
    next_node = Q.pop(0)
    if bfs_vis.get(next_node):
        continue
    else:
        bfs_ans += ' '+str(next_node)
        bfs_vis[next_node] = 1
        Q.extend(node[next_node])
print(bfs_ans)