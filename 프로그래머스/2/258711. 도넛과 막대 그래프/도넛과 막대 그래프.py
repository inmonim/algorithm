def solution(edges):
    arr = [[] for _ in range(len(edges)+2)]
    for e in edges:
        arr[e[0]].append(e[1])
    
    mxl = mxe = 0
    for i in range(len(arr)):
        if len(arr[i]) > mxl:
            mxl = len(arr[i])
            mxe = i
    
    # 8자 그래프 2개만 있는 경우, 정점 찾기가 곤란해짐.
    if mxl == 2:
        for i in range(len(arr)):
            a = arr[i]
            if len(a) == 2:
                if len(arr[a[0]]) == 2 and len(arr[a[1]]):
                    mxe = i
                    break
    answer = [mxe, 0, 0, 0]

    for a in arr[mxe]:
        x = a
        # 운 나쁘게 막대 그래프의 마지막 노드로 와서 다음 노드가 없으면
        if not arr[x]:
            answer[2] += 1
            continue
        while True:
            # 간선이 2개 이상인 정점은 8자의 중심 밖에 없음
            if len(arr[x]) == 2:
                answer[3] += 1
                break
            # 다음 노드로 계속 이동
            elif arr[x]:
                x = arr[x].pop()
            # 다음 노드가 없는 경우?
            else:
                # 지금 위치가 처음 위치인 경우 도넛
                if x == a:
                    answer[1] += 1
                    break
                # 아니면 막대
                else:
                    answer[2] += 1
                    break
    return answer