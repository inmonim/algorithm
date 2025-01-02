def sol():
    from collections import deque, defaultdict
    import sys
    input = sys.stdin.read().split('\n')
    n, m = map(int, input[0].split())

    graph = defaultdict(list)
    for i in range(1, m+1):
        a, b = map(int, input[i].split())
        graph[b].append(a)

    # BFS로 특정 노드에서 연결된 모든 노드 수 계산
    def bfs(start):
        visited = [False] * (n + 1)
        queue = deque([start])
        visited[start] = True
        count = 1  # 시작 노드 포함
        while queue:
            node = queue.popleft()
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)
                    count += 1
        return count

    # 모든 노드에 대해 BFS 수행
    max_hack = 0
    result = []
    for i in range(1, n + 1):
        hacked = bfs(i)
        if hacked > max_hack:
            max_hack = hacked
            result = [i]
        elif hacked == max_hack:
            result.append(i)

    # 결과 출력
    print(*sorted(result))

sol()