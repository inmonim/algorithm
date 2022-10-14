grade = ['A+','A0','A-','B+','B0','B-','C+','C0','C-','D0']
for T in range(1, int(input())+1):
    N, M = map(int, input().split())
    scores = [list(map(int, input().split())) for _ in range(N)]
    score_list = []

    for i, S in enumerate(scores):
        f,s,t = S
        score_list.append([i+1, round(f*0.35+s*0.45+t*0.2, 2)])
    score_list.sort(key=lambda x:x[1], reverse=True)

    for i in range(10):
        for j in range(N//10):
            score_list[i*(N//10) + j][1] = grade[i]
    
    for i in score_list:
        if i[0] == M:
            print(f'#{T} {i[1]}')