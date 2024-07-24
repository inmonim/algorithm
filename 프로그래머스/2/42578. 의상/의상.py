def solution(clothes):
    wear_dict = {}
    for c in clothes:
        if wear_dict.get(c[1]):
            wear_dict[c[1]] += 1
        else:
            wear_dict[c[1]] = 1
    
    answer = 1
    for i in wear_dict.values():
        answer *= i+1
    return answer - 1