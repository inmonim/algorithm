def solution(people, limit):
    people.sort()
    result = 0
    s = 0
    e = len(people)-1

    while e >= s:
        if people[e] + people[s] <= limit:
            result += 1
            e, s = e-1, s+1
        else:
            result, e = result+1, e-1

    return result