n, m = map(int, input().split())
tree = [{} for _ in range(n+1)]

def bfs(s, e, tree):
    q = [(s, 0)]
    visited = set([s])
    while q:
        ci, cs = q.pop()
        for k, v in tree[ci].items():
            if k == e:
                return cs + v
            if k not in visited:
                visited.add(k)
                q.append((k, cs + v))

for _ in range(n-1):
    s, e, r = map(int, input().split())
    tree[s][e] = r
    tree[e][s] = r

for _ in range(m):
    s, e = map(int, input().split())
    print(bfs(s, e, tree))