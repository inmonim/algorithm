def solution(participant, completion):
    complete = {i:0 for i in participant}

    for j in participant:
        complete[j] += 1

    for k in completion:
        complete[k] -= 1

    for v in participant:
        if complete[v] == 1:
            return v