node = [[] for _ in range(int(input())+1)]
q = []
for c in range(int(input())):
    
    a, b = map(int, input().split())
    node[a].append(b)
    node[b].append(a)

visit = {i:0 for i in range(len(node))}
q.extend(node[1])
visit[1] = 1
node[1] = []
cnt = 0
while q:
    next_c = q.pop(0)
    if visit.get(next_c) == 0:
        visit[next_c] = 1
        q.extend(node[next_c])
        node[next_c] = []
        cnt +=1

print(cnt)